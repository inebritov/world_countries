import json
from urllib.request import urlopen

from core.models import Language
from django.conf import settings
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Collects languages information'

    def handle(self, *args, **options):
        response = urlopen(settings.LANGUAGES_URL)
        data = json.loads(response.read().decode('utf-8'))

        added, updated = 0, 0

        for lang in data:
            try:
                language = Language.objects.get(alpha2=lang['alpha2'])
                Language.English = lang['English']
                language.save()
                updated += 1
                self.stdout.write("Updated language {}.".format(language))
            except Language.DoesNotExist:
                language = Language(**lang)
                language.save()
                added += 1
                self.stdout.write("Added language {}.".format(language))

        self.stdout.write('\n' + ('=' * 80))
        self.stdout.write(self.style.SUCCESS("Added: {}\nUpdated: {}".format(added, updated)))
