from rest_framework import serializers
from conversations.models import Conversation, Message
from users.api.serializers import AccountPropertiesSerializer


class ConversationSerializer(serializers.ModelSerializer):

    messages = serializers.SerializerMethodField('get_messages')

    participants = serializers.SerializerMethodField('get_participants')

    class Meta:
        model = Conversation
        fields = ('pk', 'participants', 'messages', 'created_at', 'updated_at')

    def get_messages(self, conversation):
        for message in conversation.messages.all():
            yield MessageSerializer(message).data

    def get_participants(self, conversation):
        for participant in conversation.participants.all():
            yield AccountPropertiesSerializer(participant).data


class MessageSerializer(serializers.ModelSerializer):

    sender = serializers.SerializerMethodField('get_sender')

    receiver = serializers.SerializerMethodField('get_receiver')

    class Meta:
        model = Message
        fields = ('pk', 'content', 'sender', 'receiver', 'conversation',  'created_at', 'updated_at')

    def get_sender(self, message):
        return AccountPropertiesSerializer(message.sender).data

    def get_receiver(self, message):
        return AccountPropertiesSerializer(message.receiver).data


