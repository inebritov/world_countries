import json
from urllib.request import urlopen

from core.models import Country, Language
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Collects countries information'

    def handle(self, *args, **options):
        response = urlopen(settings.COUNTRIES_URL)
        data = json.loads(response.read().decode('utf-8'))
        data = {item['alpha3Code']: item for item in data}

        added, updated = [], []

        for alpha3, item in data.items():
            try:
                country = Country.objects.get(alpha3=alpha3)
                update_country(country, item)
                country.save()
                updated.append(country)
                self.stdout.write("Updated country {}.".format(alpha3))
            except Country.DoesNotExist:
                country = Country()
                update_country(country, item)
                country.save()
                added.append(country)
                self.stdout.write("Added country {}.".format(alpha3))

        for country in added + updated:

            # Update languages
            country_languages = country.languages.all()

            for language_alpha2 in data[country.alpha3]['languages']:
                language = Language.objects.get(alpha2=language_alpha2)
                if language not in country_languages:
                    country.languages.add(language)
                    country.save()
                    self.stdout.write("Language {} added to country {}.".format(language.alpha2,
                                                                                country.alpha3))

            for cl in country_languages:
                if cl.alpha2 not in data[country.alpha3]['languages']:
                    country.languages.remove(cl)
                    country.save()
                    self.stdout.write("Language {} removed from country {}.".format(cl.alpha2,
                                                                                    country.alpha3))

            # Update neighbors
            country_neighbors = country.neighbors.all()

            for neighbor_alpha3 in data[country.alpha3]['borders']:
                if neighbor_alpha3 not in data:
                    continue

                neighbor = Country.objects.get(alpha3=neighbor_alpha3)
                if neighbor not in country_neighbors:
                    country.neighbors.add(neighbor)
                    country.save()
                    self.stdout.write("Neighbouring Country {} added to country {}.".format(neighbor.alpha3,
                                                                                            country.alpha3))

            for cn in country_neighbors:
                if cn.alpha3 not in data[country.alpha3]['borders']:
                    country.neighbors.remove(cn)
                    country.save()
                    self.stdout.write("Neighbouring Country {} removed from country {}.".format(cn.alpha3,
                                                                                                country.alpha3))

        self.stdout.write('\n' + ('=' * 80))
        self.stdout.write(self.style.SUCCESS("Added: {}\nUpdated: {}".format(len(added), len(updated))))


def update_country(country, update_dict):
    country.name = update_dict['name']
    country.population = update_dict['population']
    country.alpha2 = update_dict['alpha2Code']
    country.alpha3 = update_dict['alpha3Code']
