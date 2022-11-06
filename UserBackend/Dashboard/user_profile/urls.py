from django.urls import path
from user_profile.views import (
    CreateProfile,
    # UpdateProfile,
)

urlpatterns = [
    path('create/',CreateProfile.as_view()),
    # path('update/<int:pk>',UpdateProfile.as_view())
]