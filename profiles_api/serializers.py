from rest_framework import serializers

from . import models

"""
About serializer 
https://wsvincent.com/django-rest-framework-serializers-viewsets-routers/

A traditional Django app needs a dedicated url, view, and template to translate information from that database onto a webpage. 
In DRF we instead need a url, view, and a serializer. 
The url controls access to the API endpoints, 
views control the logic of the data being sent, 
and the serializer performs the magic of converting our information into a format suitable for transmission over the internet, JSON.

If you’re new to APIs then serializers are probably the most confusing part of the equation.
A normal webpage requires HTML, CSS, and JavaScript (usually). 
But our API is only sending data in the JSON format. 
No HTML. No CSS. Just data. 
The serializer translates our Django models into JSON and then the client app translates JSON into a full-blown webpage. 

The reverse, deserialization, 
also occurs when our API accepts a user input–for example submitting a new todo–which is translated from HTML into JSON,
then converted into our Django model.

So to repeat one last time: urls control access, views control logic, 
and serializers transform data into something we can send over the internet.
"""

class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""

    name = serializers.CharField(max_length=10)

class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """Create and return a new user."""

        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user

class ProfileFeedItemSerializer(serializers.ModelSerializer):
    """A serializer for profile feed items."""

    class Meta:
        model = models.ProfileFeedItem
        fields = ('id', 'user_profile', 'status_text', 'created_on')
        extra_kwargs = {'user_profile': {'read_only': True}}