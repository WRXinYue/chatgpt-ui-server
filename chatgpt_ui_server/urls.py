"""chatgpt_ui_server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from chat.views import conversation, gen_title, upload_conversations

# 项目的主 URL 路由
urlpatterns = [
    # 引入 chat 模块 urls
    path('api/chat/', include('chat.urls')),

    # 添加 api/conversation/ 路径，映射到 conversation 视图，并命名为 'conversation'
    path('api/conversation/', conversation, name='conversation'),

    # 添加 api/upload_conversations/ 路径，映射到 upload_conversations 视图，并命名为 'upload_conversations'
    path('api/upload_conversations/', upload_conversations, name='upload_conversations'),

    # 添加 api/gen_title/ 路径，映射到 gen_title 视图，并命名为 'gen_title'
    path('api/gen_title/', gen_title, name='gen_title'),

    # 引入 account 应用中的 urls
    path('api/account/', include('account.urls')),

    # 添加 admin/ 路径，映射到 Django admin 网站
    path('admin/', admin.site.urls),
]
