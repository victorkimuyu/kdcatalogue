import os
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


def kayak_path(instance, filename):
    ext = filename[-4:]
    special_chars = ["”", "'", "'", '"', "′", "(", ")"]

    model_name = "".join(char for char in instance.model_name if char not in special_chars)

    os.path.join("kd", "public", instance.brand, model_name + ext)


class Kayak(models.Model):
    class BrandChoices(models.TextChoices):
        AZUL = "Azul Kayaks", "Azul kayaks"
        COBRA = "Cobra Kayaks", "Cobra kayaks"
        RIOT = "Riot Kayaks", "Riot Kayaks"
        RIOT_SUP = "Riot SUP", "Riot SUP"
        BOREAL = "Boreal Design", "Boreal Design"

    class PaddlingChoices(models.TextChoices):
        SOLO = "Solo", "Solo"
        TANDEM = "Tandem", "Tandem"

    class SteeringChoices(models.TextChoices):
        RUDDER = "Rudder", "Rudder"
        SKEG = "Skeg", "Skeg"
        BOTH = "Both", "Both"

    def upload_path(self, filename):
        ext = filename[-4:]
        special_chars = ["”", "'", "'", '"', "′", "(", ")"]
        name = "".join(char for char in self.model_name if char not in special_chars)
        return f"{self.brand}/{name}{ext}"

    brand = models.CharField(verbose_name="Brand", max_length=50, choices=BrandChoices.choices)
    model_name = models.CharField(verbose_name="Model", max_length=50)
    material = models.CharField(verbose_name="Material", max_length=50, null=True, blank=True)
    description = models.TextField(verbose_name="Description")
    key_features = models.TextField(null=True, blank=True)
    model_code = models.CharField(verbose_name="Code", max_length=50, null=True, blank=True)
    web_page = models.URLField(max_length=255,
                               null=True,
                               blank=True)
    youtube = models.URLField(verbose_name="Youtube", max_length=50, null=True, blank=True)

    steering = models.CharField(
        verbose_name="Steering",
        max_length=50,
        choices=SteeringChoices.choices, blank=True, null=True
    )
    paddling = models.CharField(
        verbose_name="Paddling",
        max_length=50,
        choices=PaddlingChoices.choices,
        null=True,
        blank=True,
    )

    # Dimensions
    length = models.CharField(max_length=50, verbose_name="Length", null=True, blank=True)
    width = models.CharField(max_length=50, verbose_name="Width", null=True, blank=True)
    height = models.CharField(max_length=50, verbose_name="Height", null=True, blank=True)
    weight = models.CharField(max_length=50, verbose_name="Weight", null=True, blank=True)
    load_capacity = models.CharField(max_length=50, verbose_name="Load Capacity", null=True, blank=True)
    outer_cockpit_dimensions = models.CharField(max_length=50,
                                                null=True,
                                                blank=True)
    ideal_paddler_size = models.CharField(max_length=50, verbose_name="Paddler Size", null=True, blank=True)
    beluga_skirt_size = models.CharField(max_length=50, verbose_name="Beluga Skirt", null=True, blank=True)
    impulse_drive = models.CharField(verbose_name="Impulse Drive", max_length=50, null=True, blank=True)

    is_new = models.BooleanField(verbose_name="New", default=False, null=True, blank=True)
    in_stock = models.BooleanField(verbose_name="In Stock", default=True, null=True, blank=True)
    slug = models.SlugField(blank=True, null=True)

    top_view = models.ImageField("Top View", upload_to=upload_path, null=True, blank=True)
    side_view = models.ImageField("Side View", upload_to=upload_path,  null=True, blank=True)
    angle_view = models.ImageField("Angle View", upload_to=upload_path, null=True, blank=True)
    action_shot_1 = models.ImageField("Action Shot 1", upload_to=upload_path, null=True, blank=True)
    action_shot_2 = models.ImageField("Action Shot 2", upload_to=upload_path, null=True, blank=True)

    kayaks = KayakManager()

    def __str__(self):
        return self.model_name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.model_name)
        if "boreal" in self.brand.lower():
            self.brand = "Boreal Design"
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("kayak-detail", kwargs={"slug": self.slug})

    def features_list(self):
        return self.key_features.split('\n')
