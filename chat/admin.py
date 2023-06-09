from django.contrib import admin

from .models import Conversation, Message, Setting


# chat 模块的管理员配置
# 注册 Conversation 类到 Django 管理员后台
@admin.register(Conversation)
class ConversationAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'topic', 'created_at')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_conversation_topic', 'message', 'is_bot', 'tokens','created_at')

    def get_conversation_topic(self, obj):
        return obj.conversation.topic

    get_conversation_topic.short_description = 'Conversation Topic'


@admin.register(Setting)
class SettingAdmin(admin.ModelAdmin):
    list_display = ('name', 'value')