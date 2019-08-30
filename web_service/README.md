## Flask project

(When we mention `./` here, we mean `<path-to-project>/web_service/`)

To serve in normal server, please run this command in `../` folder.
Run the project in upper level will help source code access `../source`

```
FLASK_APP=web_service/index.py flask run
```

### 1.Flask project

Before using the command: `flask run`, please make sure that you have install flask and other dependencies using this command from `../` folder:

```
pip install -r package.txt
```

### 2. Configuration

Change configuration inside `./config/env_config.py` before run

**Base Configuration:**

-   `UPLOAD_FOLDER`: temporary upload folder (cache). Remember to delete for not taking space
-   `ALLOWED_EXTENSIONS`: all extensions allowed
-   `DEBUG`: Default DEBUG mode or not (DEBUG mode will show log)
-   `TESTING`: Default TESTING mode or not

**Detail Configuration:**

-   `DEBUG`: Override DEBUG mode
-   `TESTING`: Override TESTING mode
-   `LOG_LEVEL`: Log level in (`ERROR`, `FATAL`, `DEBUG`, `WARNING`, `INFO`)
-   `DB_USER_POSTGRE`, `DB_PASSWORD_POSTGRE`, `DB_HOST_POSTGRE`, `DB_NAME_POSTGRE`, `DB_PORT`: Configuration for Database

### 3.Flask project structure

-   `/config`: Contains configurations for environments.

    -   `/config/env_config`: configurations which will differ by environment.

-   `/server`: Contains source code for flask server.
    -   `/server/common`: Contains source code for common process related to flask web base only. If there're common snippets for analyzing process, please write in `../source/base/common`.
    -   `/server/view`: Contains source code for controlling/rendering process. Requests for business logic/query is also inside this place.
        **NOTE**: If you are writing some calculating process, consider to write it in `../source/model` if it relates to model data, else, consider to write in `/server/common` or `../source/base/common`.
    -   `/server/routing.py`: Contains mapping URL/URL patterns to specific view files.
-   `/static`: Contains static assets to server from front-end side page.
-   `/template`: Contains template written in html for rendering with Jinja2
    -   `/template/block`: Contains blocks/components/common HTML scripts which can be used in multiple times in pages.
    -   `/template/layout`: Contains layouts HTML scripts.
    -   `/template/page`: Contains actually HTML pages which will be built from a layout and fill some components inside/mapping function will handle in JS.
-   `/template_helper`: Contains some helper functions will be used in rendering process.
-   `/translations`: Contains translation for multiple language support.
-   `/index.py`: The main endpoint of the flask project. Only change this file if it's really necessary.
