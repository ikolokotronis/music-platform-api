from django.db import models
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver


class Message(models.Model):
    content = models.CharField(max_length=500)
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='sender', null=True)
    receiver = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='receiver', null=True)
    conversation = models.ForeignKey('Conversation', on_delete=models.CASCADE,
                                     related_name='conversation', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.content}'

    def save(self, *args, **kwargs):
        super(Message, self).save(*args, **kwargs)
        for conversation in Conversation.objects.all():
            if self.sender in conversation.participants.all() and self.receiver in conversation.participants.all():
                conversation.messages.add(self)
                conversation.save()
                self.conversation = conversation
                return
        conversation = Conversation.objects.create()
        conversation.participants.add(self.sender)
        conversation.participants.add(self.receiver)
        conversation.messages.add(self)
        conversation.save()
        self.conversation = conversation
        return


class Conversation(models.Model):
    participants = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='participants', through='ConversationParticipant')
    messages = models.ManyToManyField(Message, related_name='messages', through='ConversationMessages')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk} - {self.participants.all()[0].username} and {self.participants.all()[1].username}'


class ConversationParticipant(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='conversation_participant')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='p_conversation')

    def __str__(self):
        return f'{self.user} - {self.conversation}'


class ConversationMessages(models.Model):
    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='conversation_message')
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE, related_name='m_conversation')

    def __str__(self):
        return f'{self.message} - {self.conversation}'


@receiver(post_save, sender=Message)
def update_conversation(sender, instance, created, **kwargs):

    if created:
        for conversation in Conversation.objects.all():
            if instance.sender in conversation.participants.all() and instance.receiver in conversation.participants.all():
                conversation.messages.add(instance)
                conversation.save()
                message = Message.objects.get(pk=instance.pk)
                message.conversation = conversation
                message.save()
                return

        conversation = Conversation.objects.create()
        conversation.participants.add(instance.sender)
        conversation.participants.add(instance.receiver)
        conversation.messages.add(instance)
        conversation.save()

        message = Message.objects.get(pk=instance.pk)
        message.conversation = conversation
        message.save()
