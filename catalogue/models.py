from django.db import models


class Feature(models.Model):
    text = models.CharField(max_length=200)


class Kayak(models.Model):
    class BRAND_CHOICES(models.TextChoices):
        AZUL = 'AZ', 'Axul Kayaks'
        COBRA = 'CB', 'Cobra Kayaks'
        RIOT = 'RT', 'Riot Kayaks'
        BOREAL = 'BR', 'Boreal Design'

    class PADDLING_CHOICES(models.TextChoices):
        SOLO = 'S', 'Solo'
        TANDEM = 'T', 'Tandem'

    class STEERING_CHOICES(models.TextChoices):
        SOLO = 'RUDDER', 'Rudder'
        TANDEM = 'SKEG', 'Skeg'

    brand = models.CharField(max_length=20)
    model_name = models.CharField(
        "Model", max_length=50, primary_key=True, choices=BRAND_CHOICES.choices)
    build = models.CharField(max_length=50)
    description = models.TextField()
    model_code = models.CharField("Code", max_length=20)
    web_page = models.URLField(max_length=255, unique=True)
    youtube = models.URLField(max_length=50)

    steering = models.CharField(
        "Steering", max_length=20, choices=STEERING_CHOICES.choices
    )  # Skeg / Rudder
    paddling = models.CharField(
        "Paddling", max_length=20, choices=PADDLING_CHOICES.choices
    )  # Solo / Tandem

    is_new = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)
    discontinued = models.BooleanField(default=True)

    # Dimensions
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    load_capacity = models.CharField(max_length=7)

    def __str__(self):
        return self.model_name
