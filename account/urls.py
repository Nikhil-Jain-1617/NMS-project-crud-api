from django.urls import path
from .views import SignupAPI


from django.urls import path
from .views import (
    SignupAPI,ResetPassword,
    # DetailApiView
)


urlpatterns = [
    
    path('signup/', SignupAPI.as_view()),
    #path('<int:id>/',DetailApiView.as_view()),
    path('reset/',ResetPassword.as_view()),
    
]