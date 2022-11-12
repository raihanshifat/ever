import json
from rest_framework.views import APIView
from rest_framework.response import Response
from user_profile.serializers import UserProfileSerializer
from rest_framework import status
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from rest_framework import generics
from user_profile.models import UserProfile
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator
import pika



# Create your views here.
class CreateProfile(APIView):

    def post(self,request):
        """post method to create user profile"""
        user_profile_data = request.data

        try:
            user_record = User.objects.get(email=user_profile_data["email"])
        except User.DoesNotExist:
            user_record = None

        if not user_record:
            user_profile_data["password"] = make_password(user_profile_data["password"])
            user_record = User(
                email=user_profile_data['email'],
                password=user_profile_data["password"],
                username=user_profile_data['email']
            )

            user_record.save()
            user_profile_data["user"] = user_record.id

            user_profile_serializer = UserProfileSerializer(
                data=user_profile_data,
                context= {"account_type":user_profile_data["roles"]}
            )

            if user_profile_serializer.is_valid():
                user_profile_serializer.save()
                return Response(status=status.HTTP_201_CREATED)

            user_record.delete()
            return Response(user_profile_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

        return Response(
            {"error":"This email is already taken"},
            status=status.HTTP_400_BAD_REQUEST
        )


class GetProfile(generics.ListAPIView):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer

    # @method_decorator(cache_page(60*15), name='dispatch')
    def get(self,request):
        connection = pika.BlockingConnection(pika.URLParameters('amqps://agedtxxh:pet45m8MD5j8iYRKGBtGuV13jdCdUnvO@puffin.rmq2.cloudamqp.com/agedtxxh'))
        channel = connection.channel()
        channel.queue_declare(queue='hello')


        channel.basic_publish(exchange='',
                      routing_key='hello',
                      body=json.dumps(self.serializer_class(self.get_queryset(), many=True).data))
        connection.close()
        return super().get(request)


