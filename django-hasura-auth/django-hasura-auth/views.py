from rest_framework import serializers, status, permissions, generics, views
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt import authentication
from rest_framework.response import Response
from django.contrib.auth.models import User


class HasuraTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        token['user_name'] = user.username
        token['hasura'] = {}
        token['hasura']['x-hasura-allowed-roles'] = ["admin", "user"]
        if user.is_superuser:
            token['hasura']['x-hasura-role'] = "admin"
        else:
            token['hasura']['x-hasura-role'] = "user"
        token['hasura']['x-hasura-user-id'] = user.id

        return token


class HasuraTokenObtainPairView(TokenObtainPairView):
    serializer_class = HasuraTokenObtainPairSerializer


class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ("username", "password", "email")


class CreateUserView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [
        permissions.AllowAny  # Or anon users can't register
    ]


class UserDetails(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.JWTAuthentication]

    def get(self, request, format=None):
        return Response({"id": request.user.id, "username": request.user.username, "email": request.user.email})
