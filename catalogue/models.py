from django.db import models


class KayakManager(models.Manager):
    catalogue = models.Manager()

    @property
    def riot_models(self):
        return self.filter(brand=Kayak.BrandChoices.RIOT)

    @property
    def azul_models(self):
        return self.filter(brand=Kayak.BrandChoices.AZUL)

    @property
    def boreal_models(self):
        return self.filter(brand=Kayak.BrandChoices.BOREAL)

    @property
    def riot_sup_models(self):
        return self.filter(brand=Kayak.BrandChoices.RIOT_SUP)

    @property
    def cobra_models(self):
        return self.filter(brand=Kayak.BrandChoices.COBRA)


class Kayak(models.Model):
    class BrandChoices(models.TextChoices):
        AZUL = "AZ", "Azul Kayaks"
        COBRA = "CB", "Cobra Kayaks"
        RIOT = "RT", "Riot Kayaks"
        RIOT_SUP = "Rs", "Riot SUP Kayaks"
        BOREAL = "BR", "Boreal Design"

    class PaddlingChoices(models.TextChoices):
        SOLO = "S", "Solo"
        TANDEM = "T", "Tandem"

    class SteeringChoices(models.TextChoices):
        RUDDER = "R", "Rudder"
        SKEG = "S", "Skeg"
    brand = models.CharField(verbose_name="Brand", max_length=20,
                             null=True,
                             blank=True, choices=BrandChoices.choices)
    model_name = models.CharField(verbose_name="Model", max_length=50)
    material = models.CharField(verbose_name="Material", max_length=50, null=True, blank=True)
    description = models.TextField(verbose_name="Description")
    key_features = models.TextField(null=True, blank=True)
    model_code = models.CharField(verbose_name="Code", max_length=20, null=True, blank=True)
    web_page = models.URLField(max_length=255,
                               null=True,
                               blank=True)
    youtube = models.URLField(verbose_name="Youtube", max_length=50, null=True, blank=True)

    steering = models.CharField(
        verbose_name="Steering",
        max_length=20,
        choices=SteeringChoices.choices, blank=True, null=True
    )
    paddling = models.CharField(
        verbose_name="Paddling",
        max_length=20,
        choices=PaddlingChoices.choices,
        null=True,
        blank=True,
    )

    # Dimensions
    length = models.CharField(max_length=20, verbose_name="Length", null=True, blank=True)
    width = models.CharField(max_length=20, verbose_name="Width", null=True, blank=True)
    height = models.CharField(max_length=20, verbose_name="Height", null=True, blank=True)
    weight = models.CharField(max_length=50, verbose_name="Weight", null=True, blank=True)
    load_capacity = models.CharField(max_length=50, verbose_name="Load Capacity", null=True, blank=True)
    outer_cockpit_dimensions = models.CharField(max_length=50,
                                                null=True,
                                                blank=True)
    ideal_paddler_size = models.CharField(max_length=20, verbose_name="Paddler Size", null=True, blank=True)
    beluga_skirt_size = models.CharField(max_length=20, verbose_name="Beluga Skirt", null=True, blank=True)
    impulse_drive = models.CharField(verbose_name="Impulse Drive", max_length=50, null=True, blank=True)

    is_new = models.BooleanField(verbose_name="New", default=False, null=True, blank=True)
    in_stock = models.BooleanField(verbose_name="In Stock", default=True, null=True, blank=True)

    kayaks = KayakManager()

    def __str__(self):
        return self.model_name


class Photo(models.Model):
    image = models.ImageField(upload_to="../static/boat_photos")
    Kayak = models.ForeignKey(Kayak,
                              on_delete=models.SET_NULL,
                              null=True,
                              blank=True)

    def __str__(self):
        return self.image.path.split("\\")[-1]
