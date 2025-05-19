from abc import ABC, abstractmethod


class PrintObjectCreationMixin:
    """Миксин для вывода информации о создании объекта"""

    def __init__(self, *args, **kwargs):
        class_name = self.__class__.__name__
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{key}={repr(value)}" for key, value in kwargs.items()]
        all_args = ", ".join(args_repr + kwargs_repr)
        print(f"{class_name}({all_args})")
        super().__init__()


class BaseProduct(ABC):
    @property
    @abstractmethod
    def price(self) -> float:
        pass  # pragma: no cover

    @price.setter
    @abstractmethod
    def price(self, new_price: float) -> None:
        pass  # pragma: no cover

    @abstractmethod
    def __str__(self) -> str:
        pass  # pragma: no cover

    @abstractmethod
    def __add__(self, other) -> float:
        pass  # pragma: no cover


class Product(PrintObjectCreationMixin, BaseProduct):
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int) -> None:
        super().__init__(name=name, description=description, price=price, quantity=quantity)
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product: dict) -> "Product":
        return cls(
            name=product["name"],
            price=product["price"],
            description=product["description"],
            quantity=product["quantity"],
        )

    def __str__(self) -> str:
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if isinstance(other, Product):
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Можно складывать только объекты класса Product")


class Smartphone(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        super().__init__(name=name, description=description, price=price, quantity=quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def __add__(self, other: "Smartphone") -> float:
        if type(other) is Smartphone:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Можно складывать только объекты класса Smartphone")


class LawnGrass(Product):
    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        super().__init__(name=name, description=description, price=price, quantity=quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def __add__(self, other: "LawnGrass") -> float:
        if type(other) is LawnGrass:
            return self.price * self.quantity + other.price * other.quantity
        else:
            raise TypeError("Можно складывать только объекты класса LawnGrass")
