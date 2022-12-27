from django.urls import path
from .views import SignUpView


# accounts/
urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup')
]
