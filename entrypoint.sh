#!/bin/bash
# 用于运行Django应用程序的迁移、创建超级用户和启动gunicorn服务器 https://zhuanlan.zhihu.com/p/102716258

# 运行Django迁移
python manage.py migrate

# 创建一个没有输入信息的超级用户
python manage.py createsuperuser --no-input

# 设置工作进程数（默认值为3）
export WORKERS=${SERVER_WORKERS:-3}

# 设置工作进程超时时间（默认值为180秒）
export TIMEOUT=${WORKER_TIMEOUT:-180}

# 使用gunicorn启动Django应用程序，注意以下设置：
# - 绑定0.0.0.0:8000端口以便外部访问
# - 指定chatgpt_ui_server.wsgi作为WSGI应用程序
# - 设置工作进程数量
# - 设置工作进程超时时间
# - 记录访问日志到标准输出(stdout)
exec gunicorn chatgpt_ui_server.wsgi --workers=$WORKERS --timeout $TIMEOUT --bind 0.0.0.0:8000 --access-logfile -