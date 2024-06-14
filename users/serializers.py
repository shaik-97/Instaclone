from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from .models import UserProfile


class UserCreateSerializers(ModelSerializer):

    def create(self, validate_data):
        # We are overriding create() func in ModelSerializer class bcz we are making serializers specific to our app
        #be it no. of fileds etc etc.....there overiding it to make custom

        # Below command is to insert user data into DB(auth_users table) with multiple fields
        create_newuser = User.objects.create_user(**validate_data)
        # Also creating/inserting user in UserProfile table after inserting data in auth_users table
        UserProfile.objects.create(user=create_newuser)
        return create_newuser

    # This meta class and abstract=true is to tell django that do not create table of main class UserCreateSerializers in DB
    class Meta:
        abstract = True
        # options
        # fields, include, exclude
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'is_active')

    # code to ignore extra fields
    # def __init__(self, *args, **kwargs):
    #     # Call the super().__init__() method
    #     super().__init__(*args, **kwargs)
    #     # Exclude any fields that are not defined in the Meta class
    #     allowed_fields = set(self.fields.keys())
    #     for field_name in list(self.fields.keys()):
    #         if field_name not in allowed_fields:
    #             self.fields.pop(field_name)


# a new serializer UserProfileViewSerializer which is diff from above
class UserProfileViewSerializer(ModelSerializer):
    class Meta:
        model = UserProfile

        # white list approach
        # include all these fields in response.....hide sensitive fields
        fields = ('bio','profile_pic_url', 'user')
        #fields = ['bio']
        # exclude all fields .....black list approach....not include
        #exclude = ('id',)

