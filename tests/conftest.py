import pytest

from src.category import Category
from src.product import Product


@pytest.fixture
def product1() -> Product:
    return Product(
        name="Samsung Galaxy S23 Ultra", description="256GB, Серый цвет, 200MP камера", price=180000.0, quantity=5
    )


@pytest.fixture
def product2() -> Product:
    return Product(name="Iphone 15", description="512GB, Gray space", price=210000.0, quantity=8)


@pytest.fixture
def category1(product1: Product, product2: Product) -> Category:
    return Category(
        name="Смартфоны",
        description="Смартфоны, как средство не только коммуникации,"
        "но и получения дополнительных функций для удобства жизни",
        product=[product1, product2],
    )
