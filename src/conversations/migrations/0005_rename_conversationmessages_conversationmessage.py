# Generated by Django 4.0.3 on 2022-04-07 14:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conversations', '0004_alter_message_receiver'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ConversationMessages',
            new_name='ConversationMessage',
        ),
    ]