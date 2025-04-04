from flask import Flask
from .routes import api
from flask_swagger_ui import get_swaggerui_blueprint

def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix='/api')

    swaggerui_blueprint = get_swaggerui_blueprint(
        '/docs',
        '/static/swagger.yaml',
        config={'app_name': "GPT2 Lyric Generator"}
    )
    app.register_blueprint(swaggerui_blueprint, url_prefix='/docs')

    return app
