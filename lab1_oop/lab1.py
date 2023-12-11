import doctest
from typing import Union


class LivingBeing:
    def __init__(self, name: str, age: Union[int, float]):
        """
        Абстрактный класс, описывающий живое существо.

        :param name: Имя существа.
        :param age: Возраст существа.

        Примеры:
        >>> being = LivingBeing("John", 25)
        """
        if not isinstance(name, str):
            raise TypeError("Имя существа должно быть строкой")
        self.name = name

        if not isinstance(age, (int, float)):
            raise TypeError("Возраст существа должен быть числом")
        if age < 0:
            raise ValueError("Возраст существа не может быть отрицательным")
        self.age = age

    def eat(self, food: str) -> None:
        """
        Метод, описывающий действие поедания пищи.

        :param food: Пища, которую существо ест.

        Примеры:
        >>> being = LivingBeing("John", 25)
        >>> being.eat("Apple")
        """
        ...

    def sleep(self, hours: float) -> None:
        """
        Метод, описывающий действие сна существа.

        :param hours: Количество часов сна.

        Примеры:
        >>> being = LivingBeing("John", 25)
        >>> being.sleep(8)
        """
        ...


class ElectronicDevice:
    def __init__(self, brand: str, power_consumption: float):
        """
        Абстрактный класс, описывающий электронное устройство.

        :param brand: Марка устройства.
        :param power_consumption: Потребляемая мощность устройства в ваттах.

        Примеры:
        >>> device = ElectronicDevice("Samsung", 50.5)
        """
        if not isinstance(brand, str):
            raise TypeError("Марка устройства должна быть строкой")
        self.brand = brand

        if not isinstance(power_consumption, (int, float)):
            raise TypeError("Потребляемая мощность должна быть числом")
        if power_consumption < 0:
            raise ValueError("Потребляемая мощность не может быть отрицательной")
        self.power_consumption = power_consumption

    def turn_on(self) -> None:
        """
        Метод, описывающий действие включения устройства.

        Примеры:
        >>> device = ElectronicDevice("Samsung", 50.5)
        >>> device.turn_on()
        """
        ...

    def turn_off(self) -> None:
        """
        Метод, описывающий действие выключения устройства.

        Примеры:
        >>> device = ElectronicDevice("Samsung", 50.5)
        >>> device.turn_off()
        """
        ...


class Vehicle:
    def __init__(self, model: str, speed: float):
        """
        Абстрактный класс, описывающий транспортное средство.

        :param model: Модель транспортного средства.
        :param speed: Максимальная скорость транспортного средства в км/ч.

        Примеры:
        >>> car = Vehicle("Toyota Camry", 180.5)
        """
        if not isinstance(model, str):
            raise TypeError("Модель транспортного средства должна быть строкой")
        self.model = model

        if not isinstance(speed, (int, float)):
            raise TypeError("Скорость должна быть числом")
        if speed < 0:
            raise ValueError("Скорость не может быть отрицательной")
        self.speed = speed

    def start_engine(self) -> None:
        """
        Метод, описывающий действие запуска двигателя транспортного средства.

        Примеры:
        >>> car = Vehicle("Toyota Camry", 180.5)
        >>> car.start_engine()
        """
        ...

    def stop_engine(self) -> None:
        """
        Метод, описывающий действие остановки двигателя транспортного средства.

        Примеры:
        >>> car = Vehicle("Toyota Camry", 180.5)
        >>> car.stop_engine()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()
