import logging
from flask import Flask

# Route definition
from .server.routing import blueprint_list

# Configuration
from .config.env_config import configuration

# Database connection
from source.base.database_connection.sqlalchemy_wrapper import DatabaseConnection

# Decorate necessary helpers
from .template_helper.decorator import decorate_helper

app = Flask("Analysis Server Flask-Python",
            template_folder="web_service/template",
            static_folder="web_service/static",
            static_url_path="/static")


app = decorate_helper(app)

#
# DEPLOY NOTE
#
# *Static folder:
# static_folder and static_url_path should only be used for develop mode.
# In Production mode, use web service (nginx/apache) to handle instead
# and point to the web_service/static folder instead
#


# Routing control / -> map to blueprint. See `server/routing.py` for more detail
for (url_prefix, blueprint) in blueprint_list.items():
    app.register_blueprint(blueprint, url_prefix=url_prefix)


# Add environment variable into project.
app.config.from_object(configuration[app.config["ENV"]])


# Config database.
DatabaseConnection.create_db_session({
    "user": app.config["DB_USER_POSTGRE"],
    "host": app.config["DB_HOST_POSTGRE"],
    "port": app.config["DB_PORT"],
    "password": app.config["DB_PASSWORD_POSTGRE"],
    "database": app.config["DB_NAME_POSTGRE"],
    "query_log": app.config["DEBUG"]
}, "postgresql://{user}:{password}@{host}:{port}/{database}")


# Config log
LOG_FORMAT = '%(asctime)-15s - %(levelname)-8s - %(name)-8s\n%(message)s'

logging.basicConfig(format=LOG_FORMAT, level=getattr(
    logging, app.config["LOG_LEVEL"])
)

if __name__ == "__main__":
    app.run(debug=True)
