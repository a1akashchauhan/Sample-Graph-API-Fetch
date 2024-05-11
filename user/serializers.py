from rest_framework import serializers

from . models import users, SocialMediaTokens, Analytics

class usersSerializer(serializers.ModelSerializer):
    class Meta:
        model= users
        fields= "__all__"

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = SocialMediaTokens
        fields= "__all__"

class AnalyticsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Analytics
        fields="__all__"

