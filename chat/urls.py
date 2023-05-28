from django.urls import include, path
from rest_framework import routers
from .views import ConversationViewSet, MessageViewSet, PromptViewSet, EmbeddingDocumentViewSet, SettingViewSet


# 使用自动URL路由连接我们的API。
# 另外，我们还包括了可浏览API的登录URL。
# chat模块的URL路由

# 创建一个简单路由器
router = routers.SimpleRouter()

# 将ConversationViewSet注册到路由器，并设置基本名称为'conversationModel'
router.register(r'conversations', ConversationViewSet, basename='conversationModel')
router.register(r'messages', MessageViewSet, basename='messageModel')
router.register(r'prompts', PromptViewSet, basename='promptModel')
router.register(r'embedding_document', EmbeddingDocumentViewSet, basename='embeddingDocumentModel')
router.register(r'settings', SettingViewSet, basename='settingModel')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# 定义URL模式：将路由器的urls包含在path中
urlpatterns = [
    path('', include(router.urls)),
]