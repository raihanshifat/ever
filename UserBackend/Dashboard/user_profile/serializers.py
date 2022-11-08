from rest_framework import serializers
from user_profile.models import UserProfile

class UserProfileSerializer(serializers.ModelSerializer):

    def __init__(self,*args,**kwargs):
        super(UserProfileSerializer,self).__init__(*args,**kwargs)
        if "account_type" in self.context.keys():
            if self.context["account_type"] == "BUYER":
                self.fields["full_name"] = serializers.CharField(required=True)
            if self.context["account_type"] == "SELLER":
                self.fields["organization_name"] = serializers.CharField(required=True)

    def validate_roles(self,value):

        if not (value=="BUYER" or value=="SELLER"):
            raise serializers.ValidationError("Please provide correct user role")
        return value


    class Meta:
        model = UserProfile
        fields = '__all__'

class UserProfileElasticSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = [
            'email',
            'full_name',
            'organization_name',
            'phone',
        ]



