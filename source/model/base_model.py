from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (Column, SmallInteger, Integer, ForeignKey,
                        String, DateTime, Float, Text)
from source.base.database_connection.sqlalchemy_wrapper import (
    DatabaseConnection)


class BaseModel():

    DBSession = None

    @classmethod
    def build_query(cls, select_param=[]):
        if len(select_param) == 0:
            select_param = [cls]

        if cls.DBSession is None:
            return DatabaseConnection.get_db_session().query(*select_param)

        return cls.DBSession.query(*select_param)

    @classmethod
    def set_db_session(cls, session):
        cls.DBSession = session

    @classmethod
    def delete_by_id(cls, id):
        raise NotImplementedError

    @classmethod
    def find_by_id(cls, id):
        return cls.build_query().filter(cls.id == id).first()

    @classmethod
    def find_all(cls, **kwargs):
        raise NotImplementedError

    @classmethod
    def bulk_create(cls, list_item):

        if not isinstance(list_item, list):
            raise ValueError("list_item is not a list.")

        list_objects = [item for item in list_item if isinstance(item, cls)]
        list_dict = [item for item in list_item if isinstance(item, dict)]

        session = DatabaseConnection.get_db_session()

        result_save_objects = session.bulk_save_objects(list_objects)
        result_save_dict = session.bulk_insert_mappings(cls, list_dict)

        session.commit()

        return [result_save_objects, result_save_dict]


Base = declarative_base(cls=BaseModel)

TypeMap = {
    "int": Integer,
    "smallint": SmallInteger,
    "string": String,
    "datetime": DateTime,
    "text": Text,
    "float": Float
}


def BaseType(column_type, *args, **kwargs):
    """Define a column with the corresponding type. This function
    is similar as `Column()` in default sqlalchemy except that it uses
    TypeMap as string so that Model definition will not depend on sqlobject
    anymore.

    Arguments:
        column_type {string} -- Column type definition. It will be mapped as:
        ```
        {
            "int": Integer,
            "smallint": SmallInteger,
            "string": String,
            "datetime": DateTime,
            "text": Text,
            "float": Float
        }
        ```
    Keyword arguments:
        foreign_key -- ForeignKey definition

    Returns:
        Column() -- similar as Column result
    """

    foreign_key = kwargs.get("foreign_key")

    if foreign_key is not None:
        args = [ForeignKey(foreign_key), *args]

    extracted_kwargs = {
        key: kwargs[key] for key in kwargs if key not in ["foreign_key"]
    }

    return Column(TypeMap[column_type], *args, **extracted_kwargs)


class StatusValue:
    NOT_AVAILABLE = 0
    AVAILABLE = 1
    DELETED = 9
