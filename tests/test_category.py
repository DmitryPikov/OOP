import pytest

from src.category import Category
from src.product import Product


def test_category_init(category1: Category) -> None:
    assert category1.name == "Смартфоны"
    assert (
        category1.description == "Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни"
    )
    assert category1.category_count == 1


def test_products_property(category1: "Category", product1: "Product", product2: "Product") -> None:
    expected_output = "\n".join(
        [
            f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт.",
            f"{product2.name}, {product2.price} руб. Остаток: {product2.quantity} шт.",
        ]
    )
    assert category1.products == expected_output


def test_add_product(category1: Category, product2: Product) -> None:
    initial_products_count = len(category1._Category__products)

    category1.add_product(product2)

    assert len(category1._Category__products) == initial_products_count + 1
    assert product2 in category1._Category__products


@pytest.fixture
def sample_products() -> list:
    return [
        Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5),
        Product("Iphone 15", "512GB, Gray space", 210000.0, 8),
        Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14),
    ]


def test_category_str_with_products(sample_products: list) -> None:
    category = Category("Смартфоны", "Описание", sample_products)
    expected_output = "Смартфоны, количество продуктов: 27 шт."

    assert str(category) == expected_output


def test_category_str_with_no_products() -> None:
    category = Category("Пустая категория", "Описание", [])
    expected_output = "Пустая категория, количество продуктов: 0 шт."

    assert str(category) == expected_output


def test_middle_price_with_multiple_products(sample_products: list) -> None:
    category = Category("Смартфоны", "Описание", sample_products)

    assert category.middle_price() == 140333.33333333334


def test_middle_price_with_zero_products() -> None:
    category = Category("Категория", "Описание", [])

    assert category.middle_price() == 0.0
