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
from core.models import Log
from core.models import PersonalPage
from core.models import Robot
from core.models import Run
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
        # Fields needs to be either a list or a tuple, so since it's a single item it must be a list
        fields = '__all__'


# Change serializer
class ChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Change
        fields = '__all__'


# Comment serializer
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


# Contribution serializer
class ContributionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contribution
        fields = '__all__'


# Developer serializer
class DeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = '__all__'


# DevPersonalPage serializer
class DevPersonalPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = DevPersonalPage
        fields = '__all__'


# Entry serializer
class EntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Entry
        fields = '__all__'


# Heading serializer
class HeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Heading
        fields = '__all__'


# Log Serializer
class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = '__all__'


# PersonalPage serializer
class PersonalPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalPage
        fields = '__all__'


# Robot Serializer
class RobotSerializer(serializers.ModelSerializer):
    class Meta:
        model = Robot
        fields = '__all__'


# Run Serializer
class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = '__all__'


# PhotoGallery serializer
class PhotoGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoGallery
        fields = '__all__'


# SideBar serializer
class SideBarSerializer(serializers.ModelSerializer):
    class Meta:
        model = SideBar
        # Fields needs to be either a list or a tuple, so since it's a single item it must be a list
        fields = '__all__'


# Sponsor serializer
class SponsorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sponsor
        fields = '__all__'


# SponsorPersonalPage serializer
class SponsorPersonalPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = SponsorPersonalPage
        fields = '__all__'


# User serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'firstName', 'lastName')


# Wiki serializer
class WikiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wiki
        fields = '__all__'
