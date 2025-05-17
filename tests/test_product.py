import pytest

from src.product import Product, Smartphone


def test_product_init(product1: Product) -> None:
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_smartphone_init(smartphone1: Smartphone) -> None:
    assert smartphone1.name == "Samsung Galaxy S23 Ultra"
    assert smartphone1.description == "256GB, Серый цвет, 200MP камера"
    assert smartphone1.price == 180000.0
    assert smartphone1.quantity == 5
    assert smartphone1.efficiency == 95.5
    assert smartphone1.model == "S23 Ultra"
    assert smartphone1.color == "Серый"
    assert isinstance(smartphone1, Product)


def test_lawngrass_init(lawngrass1) -> None:
    assert lawngrass1.name == "Газонная трава"
    assert lawngrass1.description == "Элитная трава для газона"
    assert lawngrass1.price == 500.0
    assert lawngrass1.quantity == 20
    assert lawngrass1.country == "Россия"
    assert lawngrass1.germination_period == "7 дней"
    assert lawngrass1.color == "Зеленый"
    assert isinstance(lawngrass1, Product)


def test_price_setter_positive() -> None:
    product = Product("Телефон", "Смартфон", 50000.0, 10)

    product.price = 45000.0

    assert product.price == 45000.0


def test_price_setter_non_positive(capsys: pytest.CaptureFixture[str]) -> None:
    product = Product("Телефон", "Смартфон", 50000.0, 10)

    product.price = -100.0

    assert product.price == 50000.0

    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_new_product() -> None:
    product_data = {
        "name": "iPhone 15 Pro",
        "description": "512GB, Titanium, Triple camera",
        "price": 210000.0,
        "quantity": 3,
    }

    new_product = Product.new_product(product_data)

    assert new_product.name == product_data["name"]
    assert new_product.description == product_data["description"]
    assert new_product.price == product_data["price"]
    assert new_product.quantity == product_data["quantity"]


def test_str() -> None:
    product = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    expected = "Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт."

    assert str(product) == expected


def test_add_two_products() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    total = product1 + product2

    assert total == 2580000.0


def test_add_two_smartphone(smartphone1, smartphone2) -> None:
    total = smartphone1 + smartphone2
    assert total == 2580000.0


def test_add_two_lawngrass(lawngrass1, lawngrass2) -> None:
    total = lawngrass1 + lawngrass2
    assert total == 16750.0


def test_add_with_non_smartphone_raises_error(smartphone1) -> None:
    smartphone2 = 1

    with pytest.raises(TypeError, match="Можно складывать только объекты класса Smartphone"):
        smartphone1 + smartphone2


def test_add_with_non_lawngrass_raises_error(lawngrass1) -> None:
    lawngrass2 = 1

    with pytest.raises(TypeError, match="Можно складывать только объекты класса LawnGrass"):
        lawngrass1 + lawngrass2


def test_add_with_zero_quantity() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 0)
    total = product1 + product2

    assert total == 900000.0


def test_add_with_non_product_raises_error() -> None:
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = "Не товар"

    with pytest.raises(TypeError, match="Можно складывать только объекты класса Product"):
        product1 + product2
