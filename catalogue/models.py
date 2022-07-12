from django.db import models


class Kayak(models.Model):
    class BRAND_CHOICES(models.TextChoices):
        AZUL = "AZ", "Azul Kayaks"
        COBRA = "CB", "Cobra Kayaks"
        RIOT = "RT", "Riot Kayaks"
        BOREAL = "BR", "Boreal Design"

    class PADDLING_CHOICES(models.TextChoices):
        SOLO = "S", "Solo"
        TANDEM = "T", "Tandem"

    class STEERING_CHOICES(models.TextChoices):
        SOLO = "RUDDER", "Rudder"
        TANDEM = "SKEG", "Skeg"

    brand = models.CharField(max_length=20, choices=BRAND_CHOICES.choices)
    model_name = models.CharField("Model", max_length=50, primary_key=True)
    build = models.CharField(max_length=50)
    description = models.TextField()
    key_features = models.TextField(null=True, blank=True)
    model_code = models.CharField("Code", max_length=20)
    web_page = models.URLField(max_length=255, unique=True)
    youtube = models.URLField(max_length=50)

    steering = models.CharField(
        "Steering", max_length=20, choices=STEERING_CHOICES.choices
    )  # Skeg / Rudder
    paddling = models.CharField(
        "Paddling", max_length=20, choices=PADDLING_CHOICES.choices
    )  # Solo / Tandem

    # Dimensions
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    load_capacity = models.CharField(max_length=7)
    outer_cockpit_dimensions = models.CharField(
        max_length=50, null=True, blank=True)
    ideal_paddler_size = models.PositiveIntegerField(null=True, blank=True)
    beluga_skirt_size = models.CharField(max_length=10, null=True, blank=True)

    is_new = models.BooleanField(default=False)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return self.model_name


class Photo(models.Model):
    image = models.ImageField(upload_to="../static/boat_photos")
    Kayak = models.ForeignKey(Kayak, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.image.path.split('\\')[-1]
