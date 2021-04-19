from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from rest_framework.permissions import AllowAny

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
from core.models import Run
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


class DynamicLogSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicLogSerializer, self).__init__(*args, **kwargs)

        # If there a specified fields
        if fields is not None:
            # If log is present in the fields
            if 'log' in fields:
                # Create and add a new json field field to the dict of fields
                self.fields['log'] = serializers.JSONField(label='log', read_only=True, required=False)


# Log Serializer
class LogSerializer(DynamicLogSerializer):
    class Meta:
        model = Log
        # JSON is by default excluded and must be specifically requested
        fields = ['id', 'dateTime', 'deviceID', 'filePath']


class DynamicRunSerializer(serializers.ModelSerializer):
    """
    A ModelSerializer that takes an additional `fields` argument that
    controls which fields should be displayed.
    """

    def __init__(self, *args, **kwargs):
        from django.contrib.postgres.fields import JSONField
        # Don't pass the 'fields' arg up to the superclass
        fields = kwargs.pop('fields', None)

        # Instantiate the superclass normally
        super(DynamicRunSerializer, self).__init__(*args, **kwargs)

        # If there a specified fields
        if fields is not None:
            # If log is present in the fields
            if 'run' in fields:
                # Create and add a new json field field to the dict of fields
                self.fields['run'] = serializers.JSONField(label='run', read_only=True, required=False)


# Run Serializer
class RunSerializer(DynamicRunSerializer):
    class Meta:
        model = Run
        # JSON is by default excluded and must be specifically requested
        fields = ['id', 'dateTime', 'deviceID', 'runID', 'logID']


# PersonalPage serializer
class PersonalPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalPage
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
        fields = '__all__'

    def create(self, validated_data):
        permission_classes = [AllowAny]
        password = make_password(validated_data['password'])

        (obj, created) = User.objects.get_or_create(
            username=validated_data['username'],
            email=validated_data['email'],
            firstName=validated_data['firstName'],
            lastName=validated_data['lastName'],
            defaults={"password": password}
        )
        return obj


# Wiki serializer
class WikiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wiki
        fields = '__all__'
