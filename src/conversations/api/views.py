from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated

from conversations.api.serializers import ConversationSerializer, MessageSerializer
from conversations.models import Conversation, Message
from users.models import Account


class ConversationList(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        conversations = Conversation.objects.filter(
            participants=request.user
        ).order_by('-pk')
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)


class ConversationDetail(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk):
        conversation = Conversation.objects.get(pk=pk)
        serializer = ConversationSerializer(conversation)
        return Response(serializer.data)


class MessageSender(APIView):
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        message = Message(sender=request.user)
        serializer = MessageSerializer(message, data=request.data)
        if serializer.is_valid():
            serializer.validated_data['sender'] = request.user
            serializer.validated_data['receiver'] = Account.objects.get(id=request.data['receiver'])
            serializer.validated_data['conversation'] = Conversation.objects.get(id=request.data['conversation'])
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
