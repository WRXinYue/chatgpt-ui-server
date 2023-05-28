#!/usr/bin/env python
# Django的命令行工具，用于管理任务

import os
import sys


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
