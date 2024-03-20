import uuid
from django.template.defaultfilters import slugify
from django.db import models
import environ

env = environ.Env()

def upload_airdrop_to(instance, filename):
    return f'Airdrop/{instance.name}/{filename}'

class Category(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(max_length=20, choices=[
        ["latest", "latest"],
        ["hottest", "hottest"],
        ["potential", "potential"]
    ], unique=True)

    def __str__(self):
        return self.name


class Airdrop(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    name = models.CharField(max_length=100)
    slug = models.SlugField(blank=True, max_length=255)
    logo = models.ImageField(blank=True, upload_to=upload_airdrop_to)
    description = models.TextField()
    platform = models.CharField(max_length=50, blank=True, default="N/A")
    total_value = models.CharField(max_length=50, blank=True, default="N/A")
    total_supply = models.CharField(max_length=50, blank=True, default="N/A")
    estimate_value = models.CharField(max_length=50, blank=True, default="N/A")
    tokens_per_claim = models.CharField(max_length=50, blank=True, default="N/A")
    value = models.CharField(max_length=50, blank=True, default="N/A")
    max_participants = models.CharField(max_length=50, blank=True, default="Unlimited")
    website = models.URLField(blank=True)
    ticker = models.CharField(max_length=50, blank=True)
    white_paper = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    telegram = models.URLField(blank=True)
    discord = models.URLField(blank=True)
    medium = models.URLField(blank=True)
    facebook = models.URLField(blank=True)
    github = models.URLField(blank=True)
    video = models.URLField(blank=True)
    coinmarketcap = models.URLField(blank=True)
    coingecko = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    isConfirmed = models.BooleanField(default=False)

    kyc_required = models.BooleanField(default=False)
    mail_required = models.BooleanField(default=False)
    phone_required = models.BooleanField(default=False)
    twitter_required = models.BooleanField(default=False)

    action = models.CharField(max_length=100, blank=True)
    # end_date = models.DateTimeField()
    date_added = models.DateTimeField(auto_now_add=True)

    categories = models.ManyToManyField(Category)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)

        super(Airdrop, self).save(*args, **kwargs)
