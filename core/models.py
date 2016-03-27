from django.db import models


class Language(models.Model):
    alpha2 = models.CharField(max_length=2, unique=True)
    English = models.CharField(max_length=255)

    def __str__(self):
        return "{English}({alpha2})".format(**self.__dict__)

    def __unicode__(self):
        return self.__str__()


class Country(models.Model):
    name = models.CharField(max_length=255)
    population = models.IntegerField()
    alpha2 = models.CharField(max_length=2, unique=True)
    alpha3 = models.CharField(max_length=3, unique=True)
    languages = models.ManyToManyField(Language)
    neighbors = models.ManyToManyField('self')

    def __str__(self):
        return "{name}({alpha3})".format(**self.__dict__)

    def __unicode__(self):
        return self.__str__()

    class Meta:
        verbose_name_plural = 'Countries'
