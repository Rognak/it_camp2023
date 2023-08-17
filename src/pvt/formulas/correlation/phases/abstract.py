from typing import Union
from pydantic import BaseModel, Field
from abc import ABC, abstractmethod


class NormalVolume(BaseModel):
    oil: Union[float, int] = Field()
    wat: Union[float, int] = Field()
    gas: Union[float, int] = Field()

    @property
    def gor(self) -> Union[float, int]:
        try:
            return self.gas / self.oil
        except ZeroDivisionError:
            return 0

    @property
    def wct(self) -> Union[float, int]:
        try:
            return self.wat / (self.wat + self.oil)
        except ZeroDivisionError:
            return 0


class Phase(ABC):
    @abstractmethod
    def calc_viscosity(
        self,
        normal_condition_value: NormalVolume,
        pressure: Union[float, int],
        temperature: Union[float, int],
    ) -> Union[float, int]:
        pass

    @abstractmethod
    def calc_density(
        self,
        normal_condition_value: NormalVolume,
        pressure: Union[float, int],
        temperature: Union[float, int],
    ) -> Union[float, int]:
        pass

    @abstractmethod
    def calc_value(
        self,
        normal_condition_value: NormalVolume,
        pressure: Union[float, int],
        temperature: Union[float, int],
    ) -> Union[float, int]:
        pass
