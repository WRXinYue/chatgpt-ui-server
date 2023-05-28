# ChatGPT UI Server
This is a simple [ChatGPT UI](https://github.com/WongSaang/chatgpt-ui) server based on the Django framework.

https://wongsaang.github.io/chatgpt-ui/zh/

## 目录结构

```
chatgpt-ui-server                             # ChatGPT UI 服务器项目的根目录
 ├── account                                  # 账户管理相关模块
 │   └── migrations                           # account 模块的数据库迁移文件
 ├── chat                                     # 主聊天功能模块
 │   └── migrations                           # chat 模块的数据库迁移文件
 ├── chatgpt_ui_server                        # 项目配置文件夹
 ├── provider                                 # 提供商模块文件夹
 │   └── migrations                           # provider 模块的数据库迁移文件
 ├── stats                                    # 统计相关模块
 │   └── migrations                           # stats 模块的数据库迁移文件
 ├── utils # 包含各种辅助函数的实用程序模块 
 ├── db.sqlite3                               # SQLite 数据库文件
 ├── docker-compose.yml                       # Docker Compose 配置文件
 ├── Dockerfile                               # 项目的 Docker 构建文件
 ├── entrypoint.sh                            # Docker 容器的入口点脚本
 ├── manage.py                                # Django 的主要管理脚本文件
 ├── nginx.conf                               # Nginx 配置文件
 ├── Pipfile                                  # Pipenv 依赖文件
 ├── Pipfile.lock                             # 锁定特定版本的依赖项
 ├── README.md                                # 项目文档说明
 └── requirements.txt                         # 项目需要的软件包列表
```