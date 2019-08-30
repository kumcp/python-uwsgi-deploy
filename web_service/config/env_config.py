
import os

app_dir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig:
    UPLOAD_FOLDER = './web_service/upload_assets'
    ALLOWED_EXTENSIONS = set(['csv'])
    DEBUG = False
    TESTING = False


class ProductionConfig(BaseConfig):
    pass


class DevelopmentConfig(BaseConfig):
    DEBUG = False
    TESTING = True
    LOG_LEVEL = "DEBUG"

    DB_USER_POSTGRE = "kum"
    DB_PASSWORD_POSTGRE = ""
    DB_HOST_POSTGRE = ""
    DB_NAME_POSTGRE = ""
    DB_PORT = 5432


configuration = {
    "development": "web_service.config.env_config.DevelopmentConfig",
    "production": "web_service.config.env_config.ProductionConfig",
}
