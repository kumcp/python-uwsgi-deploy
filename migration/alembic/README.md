
## 4. Migration

The library `alembic` is used for migration task.
Root directory is `{app-root}/migration`

For detail information, please read here: [alembic document](https://alembic.sqlalchemy.org/en/latest/tutorial.html#the-migration-environment)


To config migration, open `alembic.ini`
Change the `sqlalchemy.url = ` part to the correct connection string
`driver://user:pass@localhost/dbname`

In current stage, we use `sqlalchemy.url` as reference string:

`postgresql://{user}:{password}@{host}:{port}/{database}`

Set up `.env` file with these parameters:

```
DB_USER_POSTGRE=        # This parameter will replace {user}
DB_PASSWORD_POSTGRE=    # This parameter will replace {password}
DB_HOST_POSTGRE=        # This parameter will replace {host}
DB_NAME_POSTGRE=        # This parameter will replace {database}
DB_PORT=                # This parameter will replace {port}
```

Default port for postgre is `5432`

If you want to use another type of database, please change `postgresql` connection
driver and see settings definition at [sqlalchemy doc](https://docs.sqlalchemy.org/en/13/core/connections.html)

After that, install the connection driver properly.


### 4.1 Create migration

```
cd ./migration
alembic revision -m "migration_name"
```

Migration file will be created inside `{app-root}/migration/alembic/versions/xxxx_migration_name.py`

Inside `xxx_migration_name.py`, the structure will be like this:

```
def upgrade():
    op.create_table('preprocess_sentence',
                    sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('sentence', sa.String(200), nullable=False),
                    sa.Column('created_at', sa.DateTime, nullable=False,
                              server_default=sa.func.current_timestamp()),
                    sa.Column('raw_data', sa.Unicode(200)),
                    )


def downgrade():
    op.drop_table('preprocess_sentence')

```

Function `upgrade()` will be executed when run migrate upgrade (see below).
Function `downgrade()` will be executed when run migrate downgrade (see below).

### 4.2 Migrate

```
cd ./migration

// To update newest version
alembic upgrade head

// To go upper 2 version
alembic upgrade +2

// To go downgrade 3 version
alembic downgrade -3

// To go to a specific version start with `ae1...`
alembic upgrade ae1

```

Inside database, there is a table named `alembic_version` to store
the current version of the database.

The migration files should never be changed, if you want to edit/update
anything in database, please write a new migration file to update table schema.


### 4.3 Grant permission to new tables

For account which has created tables (owners), there's no need to grant permission. But for other one to access these new tables, they need the owner the grant permission. To grant permission, login to owner account by (replace the corresponding info to login):

```
$ psql -h <host_db> -U <user_db> <db_name>;
// Then login with your password.
```

And then, in the psql console:

```
// Create access DB (if there's a new user)
$ analysis_db=> CREATE USER <user_namae>;


// Grant permission for admin + sever on tables
$ analysis_db=> GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO tradfitadmin;
$ analysis_db=> GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO tradfitserver;
$ analysis_db=> GRANT <some_previleges> ON <specific_table> IN SCHEMA public TO <other_user>;
```