from django.urls import path
from rest_framework_simplejwt.views import TokenVerifyView, TokenObtainPairView, TokenRefreshView


urlpatterns = [
    # # URLs that require a user to be logged in with a valid session / token.
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]