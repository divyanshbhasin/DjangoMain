from django.db import models

class City(models.Model):
    name = models.CharField(max_length=25, null=True)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'cities'