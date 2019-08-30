from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DatabaseConnection():

    session = None

    @classmethod
    def create_db_session(cls, db_info,
                          connect_string="mysql+pymysql://{user}:{password}@{host}:{port}/{database}",
                          seperate_session=False):
        """Create database connection using sql alchemy

        Arguments:
            db_info {dict} -- a dict contain
            'user', 'password', 'host', 'port', 'database'

        Keyword Arguments:
            connect_string {str} -- Specific connect string
            (default: {"mysql+pymysql://{user}:{password}@{host}:{port}/{database}"})

        Returns:
            [type] -- [description]
        """
        engine = create_engine(connect_string.format_map({
            "user": db_info.get("user", ""),
            "password": db_info.get("password", ""),
            "host": db_info.get("host", ""),
            "port": db_info.get("port", ""),
            "database": db_info.get("database", "")
        }), echo=db_info.get("query_log"))

        connection = engine.connect()

        Session = sessionmaker(bind=engine)
        session = Session()

        if seperate_session:
            return session

        cls.session = session
        return cls.session

    @classmethod
    def get_db_session_from_engine(cls, engine):
        if engine is None:
            return

        Session = sessionmaker(bind=engine)
        cls.session = Session()
        return cls.session

    @classmethod
    def get_db_session(cls):
        if cls.session is None:
            raise Exception("DB connection has not been created yet")

        return cls.session
