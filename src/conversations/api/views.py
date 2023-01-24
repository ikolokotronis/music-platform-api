from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from django.core.exceptions import ObjectDoesNotExist

from conversations.api.serializers import ConversationSerializer, MessageSerializer
from conversations.models import Conversation, Message
from users.models import Account


class ConversationView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        conversations = Conversation.objects.filter(participants=request.user).order_by(
            "-created_at"
        )
        if conversations:
            serializer = ConversationSerializer(conversations, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(
            {"No conversations for this user"}, status=status.HTTP_404_NOT_FOUND
        )


class ConversationDetailView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        conversation = Conversation.objects.get(pk=pk)
        if request.user not in conversation.participants.all():
            return Response(
                {"You are not a participant of this conversation"},
                status=status.HTTP_403_FORBIDDEN,
            )
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data, status=status.HTTP_200_OK)


class MessageView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def post(self, request):
        message = Message(sender=request.user)
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.validated_data["sender"] = request.user
            try:

                receiver = Account.objects.get(id=request.data["receiver"])
            except ObjectDoesNotExist:
                data = {"error": "Receiver with this id does not exist"}
                return Response(data, status=status.HTTP_400_BAD_REQUEST)
            serializer.validated_data["receiver"] = receiver
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
