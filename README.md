```markdown
# GPT-2 Lyric API

A Flask-based API service to generate lyrics using GPT-2. The application is designed to be modular, scalable, and well-structured, supporting integration with **Gunicorn** and **Uvicorn** workers for production deployment.

## 项目结构

```
gpt2-lyric-api/
├── app/
│   ├── __init__.py  # 定义 create_app() 工厂函数
│   ├── routes.py    # Flask API 路由
│   └── swagger.yaml # Swagger 文档
├── app.py           # Flask 启动入口
├── Dockerfile       # Docker 配置文件
├── docker-compose.yml # Docker Compose 配置文件
├── gunicorn.conf.py  # Gunicorn 配置文件
└── requirements.txt  # 依赖包列表
```

## 主要功能

1. **模块化应用**  
   - 该应用使用 Flask **工厂方法**（`create_app()`）进行创建，便于扩展和配置。
   - 通过 `__init__.py` 文件集中管理应用的初始化、路由和配置。

2. **API 路由**  
   - API 路由定义在 `routes.py` 文件中，包含与 GPT-2 模型进行交互的相关端点，支持生成歌词等功能。

3. **Swagger 文档**  
   - Swagger 文档位于 `swagger.yaml` 文件中，方便用户查看 API 端点和请求/响应格式。

4. **生产环境部署**  
   - 支持 **Gunicorn** + **Uvicorn Worker** 部署，在生产环境中实现高效的异步处理。
   - `app.py` 是主入口，Flask 实例在此创建，并由 Gunicorn 启动。

## 部署和运行

### 环境要求

- Docker
- Docker Compose
- Python 3.9 或更高版本

### 使用 Docker 和 Docker Compose 部署

1. **构建 Docker 镜像**

   在项目根目录下，运行以下命令构建 Docker 镜像：

   ```bash
   docker build -t gpt2-lyric-api .
   ```

2. **运行 Docker Compose**

   使用 `docker-compose` 启动应用：

   ```bash
   docker-compose up
   ```

   这将启动包含 **Flask** 服务和数据库（如果有）的容器。你可以访问 API 服务，默认情况下服务会在 `http://localhost:5000` 启动。

### Gunicorn 配置

`gunicorn.conf.py` 文件提供了 Gunicorn 的配置选项。它定义了工作进程数、绑定端口等配置。你可以根据生产环境的需要进行调整。

### 启动 Flask 服务

在容器内部，Flask 应用通过 `app.py` 文件启动，`create_app()` 工厂函数在 `app/__init__.py` 中定义。这样可以确保应用按需进行扩展。

- **app.py**:

   ```python
   from app import create_app

   app = create_app()
   ```

   - `create_app()`：Flask 工厂函数，设置配置、数据库、CORS 等。
   - `app = create_app()`：调用工厂函数，创建 Flask 实例。

### Swagger 文档

Swagger 文档定义了所有支持的 API 端点，存储在 `swagger.yaml` 文件中。你可以使用 Swagger UI 或其他工具来查看 API 文档。

## 开发环境设置

1. **创建虚拟环境并安装依赖**

   ```bash
   python -m venv venv
   source venv/bin/activate  # 在 Linux/MacOS 上
   venv\Scripts\activate  # 在 Windows 上
   pip install -r requirements.txt
   ```

2. **运行应用**

   启动 Flask 开发服务器：

   ```bash
   python app.py
   ```

   默认情况下，应用将在 `http://127.0.0.1:5000/` 上运行。

3. **Swagger UI 访问**  
   如果启用了 Swagger UI，可以通过 `http://127.0.0.1:5000/swagger` 路径查看 API 文档。

## 文件说明

- **`app.py`**：Flask 应用入口，负责创建应用实例。
- **`app/__init__.py`**：定义 `create_app()` 工厂函数，集中管理应用初始化。
- **`app/routes.py`**：API 路由定义，处理 API 请求。
- **`swagger.yaml`**：Swagger API 文档文件。
- **`gunicorn.conf.py`**：Gunicorn 配置文件，管理工作进程和启动参数。
- **`Dockerfile`**：Docker 配置文件，定义如何构建容器镜像。
- **`docker-compose.yml`**：Docker Compose 配置文件，定义多容器部署。
- **`requirements.txt`**：项目依赖，包含所有必需的 Python 包。

## 项目扩展

1. **数据库集成**  
   你可以在 `create_app()` 函数中配置数据库支持（如 SQLAlchemy、MongoDB 等），并根据需求在 `routes.py` 中添加相应的数据库操作。

2. **CORS 支持**  
   如果前端应用需要跨域访问 Flask API，可以在 `create_app()` 函数中启用 CORS。

3. **日志管理**  
   使用 Flask 内建的日志管理功能，或者集成第三方日志库，如 `loguru`、`logging` 等。

## 贡献

欢迎提交问题、建议和 Pull Request 以改善项目。如果有任何问题，随时提出，我们会尽快回复。

---

感谢使用 GPT-2 Lyric API！😊
```

### 说明

- **项目结构**：简要介绍了项目的各个目录和文件。
- **部署说明**：详细介绍了如何使用 Docker 和 Docker Compose 部署应用，如何启动 Flask 服务等。
- **开发环境设置**：列出了如何在本地搭建开发环境并运行应用。
- **扩展功能**：提供了数据库集成、CORS 支持、日志管理等功能扩展的建议。