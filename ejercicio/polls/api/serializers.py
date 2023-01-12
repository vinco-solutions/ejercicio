from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.utils import timezone
from polls.models import Question

class question_serializer(serializers.ModelSerializer):

    days_since_created = serializers.SerializerMethodField('get_days_since_created')

    def get_days_since_created(self, obj):
        days = (timezone.now().date() - obj.pub_date.date())/(24*60*60)
        return days

    class Meta:
        model = Question
        fields = "__all__"
        extra_fields = ['days_since_created']

        def validate(self,data):
            print(data)
            if len(data['question_text'])<=10:
                raise serializers.ValidationError('Field with less than ten characters')
            return data


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email")

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "password", "email")
        extra_kwargs = {"password":{"write_only":True}}

        def create(self, validate_data):
            user = User.objects.create_user(validate_data["username"], validate_data["password"], validate_data["email"])
            return user

# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


