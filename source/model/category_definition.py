from sqlalchemy.orm import relationship, foreign, remote

from .base_model import Base, BaseType, StatusValue
from .hotel_info import HotelInfo


class CategoryConditionTypeValue:
    WORD_INCLUDE = 1


class CategoryTypeValue:
    NORMAL = 1


class B(Base):

    __tablename__ = "B"

    id = BaseType("int", primary_key=True)
    category_number = BaseType("int")
    category_name = BaseType("string")


    @classmethod
    def find_all(cls, limit=50, **kwargs):
        """Get list item in database

        Keyword Arguments:
            limit {int} -- number of item (default: {50})

        Returns:
            list(B) -- list of B object
        """

        return cls.build_query(). \
            limit(limit). \
            all()
