

from rest_framework import serializers
from profiles_api import models

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing our APIView"""
    name = serializers.CharField(max_length=10)

    # This serializer defines a single field 'name' which is a CharField.
    # It limits the maximum length of the 'name' field to 10 characters.

class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )
        return user

    # This serializer is used to serialize and deserialize UserProfile objects.
    # It specifies the model UserProfile and fields to include in the serialized representation.
    # The 'password' field is marked as write_only and styled as a password input.

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """Serializes profile feed items"""
    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {
            'user_profile': {'read_only': True}
        }

    # This serializer is used to serialize and deserialize ProfileFeedItem objects.
    # It specifies the model ProfileFeedItem and fields to include in the serialized representation.
    # The 'user_profile' field is marked as read-only.
