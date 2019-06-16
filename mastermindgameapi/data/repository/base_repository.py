from abc import ABC, abstractmethod
from typing import List


class BaseRepository(ABC):
    __model__ = None

    @abstractmethod
    def create(self, model):
        pass

    @abstractmethod
    def dump(self, model):
        pass

    def all(self) -> List[__model__]:
        models_list = self.__model__.query.all()
        return models_list

    def first_or_404(self, **filters):
        model = self.__model__.query.filter_by(**filters).first_or_404()
        return model
