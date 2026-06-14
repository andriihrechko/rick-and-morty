from django.db import models


class Character(models.Model):
    """Character model from Rick and Morty API."""

    class StatusChoices(models.TextChoices):
        ALIVE = "Alive"
        DEAD = "Dead"
        UNKNOWN = "Unknown"

    class GenderChoices(models.TextChoices):
        MALE = "Male"
        FEMALE = "Female"
        GENDERLESS = "Genderless"
        UNKNOWN = "Unknown"

    api_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=255)
    status = models.CharField(max_length=7, choices=StatusChoices.choices)
    species = models.CharField(max_length=255)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    image = models.URLField()

    def __str__(self):
        return self.name
