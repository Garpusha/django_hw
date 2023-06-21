from django.db import models


class Sensor(models.Model):
    name = models.CharField(max_length=20, verbose_name="Наименование датчика")
    description = models.CharField(
        max_length=50, blank=True, verbose_name="Описание датчика"
    )


class Measurement(models.Model):
    sensor = models.ForeignKey(
        Sensor,
        on_delete=models.CASCADE,
        related_name="measurements",
        verbose_name="ID датчика",
    )
    temperature = models.FloatField(verbose_name="Температура")
    created_at = models.DateTimeField(auto_now_add=True)
