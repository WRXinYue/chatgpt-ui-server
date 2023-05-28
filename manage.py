#!/usr/bin/env python
# Django的命令行工具，用于管理任务

import os
import sys


"""
`manage.py` 文件并不直接运行其他模块。它主要是作为一个命令行工具，根据提供的参数来执行相应的 Django 命令。
例如：启动服务器、执行数据库迁移等。Django 框架本身负责调用和运行其他模块。

当你使用 `manage.py` 运行服务器时（例如，执行 `python manage.py runserver`），Django 会自动找到并加载在
`DJANGO_SETTINGS_MODULE` 环境变量中指定的设置文件（在这里是 `'chatgpt_ui_server.settings'`）。这个设置文件包含了项目的配置信息，
包括已安装的应用、中间件、URL 路由等。

在加载设置文件后，Django 将知道如何找到其他模块（因为它们已在设置文件中注册为已安装的应用程序），以及如何处理请求。
当用户发起请求时，Django 根据在设置文件中定义的路由规则将请求分发给相应的模块视图函数。然后该模块会处理请求并返回响应。

总之，`manage.py` 文件并不直接运行其他模块，而是通过调用 Django 的命令和功能来实现。其他模块的实际运行由 Django 框架负责。
"""
def main():
    """运行管理任务"""
    # 设置默认的Django设置模块
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'chatgpt_ui_server.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
