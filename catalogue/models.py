from django.db import models
from django.urls import reverse

from django.utils.text import slugify


class KayakManager(models.Manager):
    catalogue = models.Manager()

    @property
    def riot(self):
        return self.filter(brand=Kayak.BrandChoices.RIOT)

    @property
    def azul(self):
        return self.filter(brand=Kayak.BrandChoices.AZUL)

    @property
    def boreal(self):
        return self.filter(brand=Kayak.BrandChoices.BOREAL)

    @property
    def riot_sup(self):
        return self.filter(brand=Kayak.BrandChoices.RIOT_SUP)

    @property
    def cobra(self):
        return self.filter(brand=Kayak.BrandChoices.COBRA)

    @property
    def thermoformed(self):
        return self.filter(material__icontains="thermoformed")

    @property
    def thermoformed_abs(self):
        return self.filter(material="Thermoformed ABS")

    @property
    def thermoformed_tx(self):
        return self.filter(material="Thermoformed TX")

    @property
    def blowmolded_plastic(self):
        return self.filter(material="Thermoformed Plastic")

    @property
    def rotomolded_hdpe(self):
        return self.filter(material="Rotomolded HDPE")

    @property
    def new(self):
        return self.filter(is_new=True)

    @property
    def new_riot(self):
        return self.filter(is_new=True).filter(brand=Kayak.BrandChoices.RIOT)

    @property
    def new_azul(self):
        return self.filter(is_new=True).filter(brand=Kayak.BrandChoices.AZUL)

    @property
    def new_boreal(self):
        return self.filter(is_new=True).filter(brand=Kayak.BrandChoices.BOREAL)

    @property
    def new_riot_sup(self):
        return self.filter(is_new=True).filter(brand=Kayak.BrandChoices.RIOT_SUP)


class Kayak(models.Model):
    class BrandChoices(models.TextChoices):
        AZUL = "AZUL KAYAKS", "Azul kayaks"
        COBRA = "COBRA KAYAKS", "Cobra kayaks"
        RIOT = "RIOT KAYAKS", "Riot Kayaks"
        RIOT_SUP = "RIOT SUP", "Riot SUP"
        BOREAL = "BOREAL DESIGN", "Boreal Design"

    class PaddlingChoices(models.TextChoices):
        SOLO = "SOLO", "Solo"
        TANDEM = "TANDEM", "Tandem"

    class SteeringChoices(models.TextChoices):
        RUDDER = "RUDDER", "Rudder"
        SKEG = "SKEG", "Skeg"

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
    slug = models.SlugField(blank=True, null=True)

    top_view = models.ImageField(null=True, blank=True)
    side_view = models.ImageField(null=True, blank=True)
    angle_view = models.ImageField(null=True, blank=True)
    action_shot = models.ImageField(null=True, blank=True)

    kayaks = KayakManager()

    def __str__(self):
        return self.model_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model_name)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("kayak-detail", kwargs={"slug": self.slug})

