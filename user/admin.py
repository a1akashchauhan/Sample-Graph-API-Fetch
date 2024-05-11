from django.contrib import admin

# Register your models here.

from .models import users, SocialMediaTokens, Analytics

admin.site.register(users)
admin.site.register(SocialMediaTokens)
admin.site.register(Analytics)

