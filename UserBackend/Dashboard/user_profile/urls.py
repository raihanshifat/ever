from django.urls import path
from user_profile.views import (
    CreateProfile,
    GetProfile
    # UpdateProfile,
)
from .elastic_views import SearchUser

urlpatterns = [
    path('create/',CreateProfile.as_view()),
    path('user_list/',GetProfile.as_view()),
    path('search_user/',SearchUser.as_view())
    # path('update/<int:pk>',UpdateProfile.as_view())
]