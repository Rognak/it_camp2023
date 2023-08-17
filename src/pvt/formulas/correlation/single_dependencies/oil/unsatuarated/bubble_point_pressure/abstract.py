from typing import Union
from abc import ABC, abstractmethod


class BubblePointPressureCorrelation(ABC):
    @classmethod
    def calc(
        cls,
        temp: Union[float, int],
        solubility: Union[float, int],
        dens_oil: Union[float, int],
        dens_gas: Union[float, int],
    ) -> Union[float, int]:
        """
        :param temp: Температуры, К
        :param solubility: Газосодержание м3 / м3
        :param dens_oil: Плотности дегазированной нефти (с.у), доли ед.
        :param dens_gas: Плотность сеперированного газа (с.у), доли ед.
        :return: давление насыщения при данном газосодержании
        """
        pass
