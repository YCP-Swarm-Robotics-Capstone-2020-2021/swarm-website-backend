from rest_framework import serializers

# Model Imports
from core.models import User
from core.models import Sponsor
from core.models import Wiki


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'firstName', 'lastName')


# Sponsor serializer
class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('companyName', 'page')


# Wiki serializer
class WikiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wiki
        fields = ('title', 'entries', 'briefDescription')