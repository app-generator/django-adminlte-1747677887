# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Auftragsstatus(models.Model):

    #__Auftragsstatus_FIELDS__
    bezeichnung = models.CharField(max_length=255, null=True, blank=True)

    #__Auftragsstatus_FIELDS__END

    class Meta:
        verbose_name        = _("Auftragsstatus")
        verbose_name_plural = _("Auftragsstatus")


class Kontaktdatenbank(models.Model):

    #__Kontaktdatenbank_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)
    telefon = models.CharField(max_length=255, null=True, blank=True)
    adresse = models.CharField(max_length=255, null=True, blank=True)
    plz = models.CharField(max_length=255, null=True, blank=True)
    ort = models.CharField(max_length=255, null=True, blank=True)
    notizen = models.TextField(max_length=255, null=True, blank=True)
    log = models.TextField(max_length=255, null=True, blank=True)
    kontaktbezeichnung = models.CharField(max_length=255, null=True, blank=True)
    istmitarbeiter = models.BooleanField()

    #__Kontaktdatenbank_FIELDS__END

    class Meta:
        verbose_name        = _("Kontaktdatenbank")
        verbose_name_plural = _("Kontaktdatenbank")


class Auftragsdatenbank(models.Model):

    #__Auftragsdatenbank_FIELDS__
    nummer = models.IntegerField(null=True, blank=True)
    bezeichnung = models.CharField(max_length=255, null=True, blank=True)
    notizen = models.TextField(max_length=255, null=True, blank=True)
    log = models.TextField(max_length=255, null=True, blank=True)
    bearbeiter = models.ForeignKey(Kontaktdatenbank, on_delete=models.CASCADE)
    kunde = models.ForeignKey(Kontaktdatenbank, on_delete=models.CASCADE)
    planer = models.ForeignKey(Kontaktdatenbank, on_delete=models.CASCADE)
    bauleiter = models.ForeignKey(Kontaktdatenbank, on_delete=models.CASCADE)
    status = models.ForeignKey(Auftragsstatus, on_delete=models.CASCADE)
    eingangsdatum = models.DateTimeField(blank=True, null=True, default=timezone.now)
    geplantefertigstellung = models.DateTimeField(blank=True, null=True, default=timezone.now)
    fertigstellung = models.DateTimeField(blank=True, null=True, default=timezone.now)
    letzteaenderung = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Auftragsdatenbank_FIELDS__END

    class Meta:
        verbose_name        = _("Auftragsdatenbank")
        verbose_name_plural = _("Auftragsdatenbank")



#__MODELS__END
