from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims
        token['last_name'] = user.last_name
        token['first_name'] = user.first_name
        token['second_name'] = user.second_name
        token['email'] = user.email
        token['username'] = user.username
        token['is_staff'] = user.is_staff

        return token
