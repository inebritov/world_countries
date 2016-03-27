from django.db import models


class Language(models.Model):
    alpha2 = models.CharField(max_length=2, unique=True)
    English = models.CharField(max_length=255)

    def __str__(self):
        return "{English}({alpha2})".format(**self.__dict__)

    def __unicode__(self):
        return self.__str__()
