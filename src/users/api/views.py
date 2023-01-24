from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from users.api.serializers import RegistrationSerializer, AccountPropertiesSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated

from users.models import Account


class RegistrationView(APIView):
    def post(self, request):
        """
        Creates a new user.
        """
        serializer = RegistrationSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            account = serializer.save()
            data["response"] = "Successfully registered new user."
            data["email"] = account.email
            data["username"] = account.username
            token = Token.objects.get(user=account).key
            data["token"] = token
            return Response(data, status=status.HTTP_201_CREATED)
        data["error"] = "Registration failed"
        return Response(data, status=status.HTTP_400_BAD_REQUEST)


class AccountView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        """
        Get the account information
        """
        try:
            user = Account.objects.get(pk=pk)
        except Account.DoesNotExist:
            return Response(
                {"Account with this pk doesn't exist"}, status=status.HTTP_404_NOT_FOUND
            )
        serializer = AccountPropertiesSerializer(user)
        if serializer.is_valid():
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        """
        Update the account information
        """
        try:
            user = request.user
        except Account.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        user_from_url = Account.objects.get(pk=pk)
        data = {}
        if user_from_url != request.user:
            data["error"] = "Request user is not the account owner"
            return Response(data, status=status.HTTP_403_FORBIDDEN)

        serializer = AccountPropertiesSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            new_password = serializer.validated_data["new_password"]
            if new_password != "":
                user.set_password(new_password)
                user.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
