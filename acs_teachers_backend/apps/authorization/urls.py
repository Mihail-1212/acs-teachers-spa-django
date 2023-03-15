from django.urls import path
from dj_rest_auth.views import (
    LoginView, LogoutView, UserDetailsView,
)
from dj_rest_auth.app_settings import api_settings
# from . import api


urlpatterns = [
    # path('', include('dj_rest_auth.urls'))

    path('login/', LoginView.as_view(), name='rest_login'),
    # URLs that require a user to be logged in with a valid session / token.
    path('logout/', LogoutView.as_view(), name='rest_logout'),
    path('user/', UserDetailsView.as_view(), name='rest_user_details')
]


if api_settings.USE_JWT:
    from rest_framework_simplejwt.views import TokenVerifyView

    from dj_rest_auth.jwt_auth import get_refresh_view

    urlpatterns += [
        path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
        path('token/refresh/', get_refresh_view().as_view(), name='token_refresh'),
    ]