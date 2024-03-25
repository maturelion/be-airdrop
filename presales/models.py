import uuid
from django.template.defaultfilters import slugify
from django.db import models


def upload_presale_to(instance, filename):
    return f'Presale/{instance.name}/{filename}'


class Presale(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, max_length=255)
    logo = models.ImageField(blank=True, upload_to=upload_presale_to)
    chain = models.CharField(max_length=50)
    token = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.BigIntegerField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_added']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Presale, self).save(*args, **kwargs)
