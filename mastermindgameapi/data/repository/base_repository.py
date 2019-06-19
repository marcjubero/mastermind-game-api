from abc import ABC, abstractmethod
from typing import List

from mastermindgameapi.app import db
from mastermindgameapi.data.exceptions import DataNotFoundException


class BaseRepository(ABC):
    __model__ = None

    @abstractmethod
    def create(self, model, **kwargs):
        pass  # pragma: no cover

    @abstractmethod
    def dump(self, model):
        pass  # pragma: no cover

    def save(self):
        db.session.commit()

    def all(self) -> List[__model__]:
        datas = self.__model__.query.all()
        return datas

    def first_or_raise(self, **filters) -> __model__:
        data = self.__model__.query.filter_by(**filters).first()
        if data is None:
            raise DataNotFoundException('Data not found for {0}'.format(filters))
        return data
