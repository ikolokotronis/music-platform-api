from django.contrib import admin
from .models import (Conversation, Message, ConversationMessage, ConversationParticipant)

admin.site.register(Conversation)
admin.site.register(Message)
admin.site.register(ConversationMessage)
admin.site.register(ConversationParticipant)
