from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver

# Create your models here.
class PassPhrase(models.Model):
    keys = models.TextField(null=False, blank=False, max_length=500, unique=True)
    amount_of_pi = models.CharField(null=True, blank=True, max_length=100)
    unlock_date = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    look_up = models.CharField(null=False, blank=False, max_length=20)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Keys'
        verbose_name_plural = 'Keys'
        ordering = ['-date']


@receiver(pre_delete, sender=PassPhrase)
def prevent_delete(sender, instance, **kwargs):
    raise models.ProtectedError("You cannot delete anything", instance)


class Nel_PassPhrase(models.Model):
    keys = models.TextField(null=False, blank=False, max_length=500, unique=True)
    amount_of_pi = models.CharField(null=True, blank=True, max_length=100)
    unlock_date = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    look_up = models.CharField(null=False, blank=False, max_length=20)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Nel Keys'
        verbose_name_plural = 'Nel Keys'
        ordering = ['-date']


@receiver(pre_delete, sender=Nel_PassPhrase)
def prevent_delete(sender, instance, **kwargs):
    raise models.ProtectedError("You cannot delete anything", instance)


class Chi_PassPhrase(models.Model):
    keys = models.TextField(null=False, blank=False, max_length=500, unique=True)
    amount_of_pi = models.CharField(null=True, blank=True, max_length=100)
    unlock_date = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    look_up = models.CharField(null=False, blank=False, max_length=20)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Chi Keys'
        verbose_name_plural = 'Chi Keys'
        ordering = ['-date']


@receiver(pre_delete, sender=Chi_PassPhrase)
def prevent_delete(sender, instance, **kwargs):
    raise models.ProtectedError("You cannot delete anything", instance)

class Santus_PassPhrase(models.Model):
    keys = models.TextField(null=False, blank=False, max_length=500, unique=True)
    amount_of_pi = models.CharField(null=True, blank=True, max_length=100)
    unlock_date = models.DateTimeField(null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    look_up = models.CharField(null=False, blank=False, max_length=20)

    def __str__(self):
        return str(self.date)

    class Meta:
        verbose_name = 'Santus Keys'
        verbose_name_plural = 'Santus Keys'
        ordering = ['-date']