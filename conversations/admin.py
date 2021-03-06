from django.contrib import admin
from . import models


@admin.register(models.Message)
class MessageAdmin(admin.ModelAdmin):

    """Message Admin Object"""

    list_display = (
        "__str__",
        "created",
    )


@admin.register(models.Conversations)
class ConversationAdmin(admin.ModelAdmin):

    """Conversation Admin Object"""

    list_display = (
        "__str__",
        "count_messages",
        "count_participants",
    )
