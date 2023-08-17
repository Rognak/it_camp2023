import enum
from typing import Union


class TempUnit(enum.Enum):
    Kelvin = 0
    Celsius = 1
    Fahrenheit = 2

    def is_kelvin(self) -> bool:
        return self == self.Kelvin

    def is_celsius(self) -> bool:
        return self == self.Celsius

    def is_fahrenheit(self) -> bool:
        return self == self.Fahrenheit

    def convert_to_fahrenheit(
        self,
        temperature: Union[float, int],
    ) -> Union[float, int]:
        if self.is_kelvin():
            value = 1.8 * (temperature - 273.15) + 32
        elif self.is_celsius():
            value = 1.8 * temperature + 32
        elif self.is_fahrenheit():
            value = temperature
        else:
            raise ValueError("Неизвестная еденица измерения температуры")

        if value > 205:
            print(f"Температура {value}F/{temperature}K выше возможной в рамках корреляции")
            value = 205

        return value


class DensityUnit(enum.Enum):
    SI = 0
    Relative = 1
    API = 2

    def is_relative(self) -> bool:
        return self == self.Relative

    def is_si(self) -> bool:
        return self == self.SI

    def is_api(self) -> bool:
        return self == self.API

    def convert_to_api(
        self,
        density: Union[float, int],
        denominator: Union[float, int] = 1000,
    ) -> Union[float, int]:
        if self.is_si():
            density /= denominator
            value = 141.5 / density - 131.5
        elif self.is_relative():
            value = 141.5 / density - 131.5
        elif self.is_api():
            value = density
        else:
            raise ValueError("Неизвестная еденица измерения плотности")

        if value > 58:
            raise ValueError("Плотность выше возможной в рамках корреляции")

        return value


class PresUnit(enum.Enum):
    Bar = 0
    Pa = 1
    MPa = 2
    At = 3
    atm = 4
    psi = 5

    def is_bar(self) -> bool:
        return self == self.Bar

    def is_pascal(self) -> bool:
        return self == self.Pa

    def is_mega_pascal(self) -> bool:
        return self == self.MPa

    def is_at(self) -> bool:
        return self == self.At

    def is_atm(self) -> bool:
        return self == self.atm

    def is_psi(self) -> bool:
        return self == self.psi

    def __convert_to_pa(
        self,
        pres: Union[float, int],
    ) -> Union[float, int]:
        if self.is_bar():
            pres *= 10**5
        elif self.is_pascal():
            pass
        elif self.is_mega_pascal():
            pres *= 10**6
        elif self.is_at():
            pres *= 98066.5
        elif self.is_at():
            pres *= 101325
        else:
            raise ValueError("Неизвестная еденица измерения давления")

        return pres

    def convert_to_psi(
        self,
        pres: Union[float, int],
    ) -> Union[float, int]:
        if self.is_bar():
            pres *= 14.504
        elif self.is_pascal():
            pres *= 1.4504 * 10**-4
        elif self.is_mega_pascal():
            pres *= 145.04
        elif self.is_psi():
            pass
        elif self.is_at():
            pres *= 14.223
        elif self.is_at():
            pres *= 14.696
        else:
            raise ValueError("Неизвестная еденица измерения давления")

        return pres


class SolubilityUnit(enum.Enum):
    SI = 0
    Foot_per_barrel = 1

    def is_si(self) -> bool:
        return self == self.SI

    def is_foot_per_barrel(self) -> bool:
        return self == self.Foot_per_barrel

    def convert_to_foot_per_barrel(
        self,
        solubility: Union[float, int],
    ) -> Union[float, int]:
        if self.is_si():
            solubility /= 0.17810760667903522
        elif self.is_foot_per_barrel():
            pass
        else:
            raise ValueError("Неизвестная еденица измерения давления")

        return solubility
