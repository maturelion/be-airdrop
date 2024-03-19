from django.contrib import admin
from .models import Airdrop, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name'
                    )


@admin.register(Airdrop)
class AirdropAdmin(admin.ModelAdmin):
    list_display = ('id',
                    'name',
                    'slug',
                    'platform',
                    'total_value',
                    'total_supply',
                    'estimate_value',
                    'tokens_per_claim',
                    'value',
                    'max_participants',
                    'website',
                    'ticker',
                    'white_paper',
                    'twitter',
                    'telegram',
                    'discord',
                    'medium',
                    'facebook',
                    'github',
                    'video',
                    'coinmarketcap',
                    'coingecko',
                    'featured',
                    'isConfirmed',
                    'kyc_required',
                    'mail_required',
                    'phone_required',
                    'twitter_required',
                    'action',
                    'date_added'
                    )
