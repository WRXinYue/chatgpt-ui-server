"""
ASGI config for chatgpt_ui_server project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

# 异步服务器的 ASGI 配置
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatgpt_ui_server.settings')

application = get_asgi_application()
