from rest_framework import serializers

# Model Imports
from core.models import Admin
from core.models import Change
from core.models import Comment
from core.models import Contribution
from core.models import Developer
from core.models import DevPersonalPage
from core.models import Entry
from core.models import Heading
from core.models import PersonalPage
from core.models import PhotoGallery
from core.models import SideBar
from core.models import Sponsor
from core.models import SponsorPersonalPage
from core.models import User
from core.models import Wiki


# Admin serializer
class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = 'recieveUpdates'


# Change serializer
class ChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Change
        fields = ('user', 'dateTime', 'context', 'textAdded')


# Comment serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('user', 'text', 'dateTime', 'replies')


# Contribution serializer
class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution


# Developer serializer

# DevPersonalPage serializer

# Entry serializer

# Heading serializer

# PersonalPage serializer

# PhotoGallery serializer

# SideBar serializer

# Sponsor serializer
class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = ('companyName', 'page')

# SponsorPersonalPage serializer


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'firstName', 'lastName')


# Wiki serializer
class WikiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wiki
        fields = ('title', 'entries', 'briefDescription')





