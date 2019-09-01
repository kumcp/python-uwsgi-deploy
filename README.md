# I. Basic develop README

## 0. (Optional) Setup environment

### 0.1 Install environment

Create another environment separating with current system environment:

Ubuntu 14.04:

```
$ sudo apt-get install python3.4-venv
```

OR

```
$ sudo apt install python3-venv
```

Then create env with:

```
$ python3 -m venv <env-name>

```

## 0.2 Activate and deactivate environment

- Activate:

```
$ source <path-to-virtual-env>/bin/activate
```

- Deactivate:
  Inside virtual-env:

```
$ deactivate
```

## 1. Installation

**NOTE: Please notify that this tool is built for python3.**

Make sure you have installed `pip`

Install neccessary packages:

```
pip install -r package.txt
```

In developing time, if there are new packages required and installed,
To save all information about current packages using:

```
pip freeze > package.txt
```

For using with DB on Ubuntu, you need:

```
$ sudo apt-get install libmysqlclient-dev python-mysqldb
```

## 2. Run as standalone script (offline)

If you have a separate file, for example call `execute.py`

```
python execute.py
```

To run without creating BYTECODE file, using:

```
env "PYTHONDONTWRITEBYTECODE=1" python execute.py
```

Or setup settings in .vscode.

NOTE: Settings in `path-env.json` has been set for using mysql (as default)
If you want to use another type of database, please change the connection string
in `DatabaseConnection.create_db_session(path_env["db"],connection_string="...")`

### 2.2. Build to executable

```
pyinstaller --onefile execute.py
```

### 2.3. Execute

```
./dist/analyze
```

## 3. Serve as web service

When serve as web service, system use postgreSQL. See more detail in Document inside `web_service/`

### 3.1 Serve the service endpoint

Run and serve in normal server:

```
FLASK_APP=web_service/index.py flask run
```

### 3.1 Serve /debug using VSCode

Setting config has been set inside `./.vscode/` directory

Run Flask Server debug for debuging.

## 4. Migration

The library `alembic` is used for migration task.
Root directory is `{app-root}/migration`

Set up `.env` file with these parameters:

```
DB_USER_POSTGRE=
DB_PASSWORD_POSTGRE=
DB_HOST_POSTGRE=
DB_NAME_POSTGRE=
DB_PORT=
```

Settings use Postgre + SQLAlchemy to connect database.
For more information, please take a look at `./migration/README.md`

### 4.1 Create migration

```
cd ./migration
alembic revision -m "migration_name"
```

Migration file will be created inside `{app-root}/migration/alembic/versions/xxxx_migration_name.py`

Edit neccessary information for migration

### 4.2 Migrate

To execute migration file:

```
cd ./migration

// To update newest version
alembic upgrade head

// To go upper 2 steps from current version
alembic upgrade +2

// To go downgrade 3 steps from current version
alembic downgrade -3

// To go to a specific version start with `ae1...`
alembic upgrade ae1

```

### 5.Setup multilanguage support (i18n):

Go to `./web_service` folder, if `translations/messages.pot` has not been created, create with:

```
    pybabel extract -F mysettings.cfg -o messages.pot .
```

## Pull Request

If you would like to send a pull request to be merged into branch `master` or `develop`, you branch should pass integration test in Circle CI. For this purpose, you should create an issue first and develop with a new branch with name `issue-<issue #>`.

If your branch does not require pull request, you can use other branch name to avoid Circle CI test.

## \*\* Common bugs/issues

#### 1. Cannot run test on VSCode, show Test Discovery failed in output

- There may be 2 python path in workspace settings and users settings. Try to remove one

#### 2. Cannot install psycopg2

- To install psycopg2, you may need to install python-dev or python3-dev.

```
// On Ubuntu/ Ubuntu-base with python 3, run this:
sudo apt-get install python3-dev

// Python 2.7 run this:
sudo apt-get install python-dev

// For specific version python 3.4, run this:
sudo apt-get install python3.4-dev
```

#### 3. Cannot run and discover test in VSCode

- Please check `./.vscode/settings.json` the settings with the correct `extraPaths`

```
"python.autoComplete.extraPaths": [
    "analyze-env/lib/python3.6/site-packages"
],

```

- Add `conftest.py` at root directory.

TL;DR
`pytest` in VSCode treat tests as a sub module and does not contain any module outside `./tests`. In that case, create a blank file name `conftest.py` (`pytest` will detect every file has the `*test*` in the name) in root folder `./` so that pytest will treat `./` as module. Other module inside `./` will be included.

#### 4. [CircleCI][env] Cannot install packages in circle ci environment:

There're some problems with Ubuntu 18.04 that every time you run

```
$ pip freeze > package.txt
```

in the corresponding environment, it will create this package: `pkg-resources==0.0.0`
in the file `package.txt`. Just remove this line and circleci can build environment successfully.
