from src.category import Category
from src.product import Product


def test_category_init(category1: Category) -> None:
    assert category1.name == "Смартфоны"
    assert (
        category1.description == "Смартфоны, как средство не только коммуникации,"
                                 "но и получения дополнительных функций для удобства жизни"
    )
    assert category1.category_count == 1


def test_products_property(category1: Category, product1: Product, product2: Product) -> None:
    expected_output = "\n".join([
        f"{product1.name}, {product1.price} руб. Остаток: {product1.quantity} шт.",
        f"{product2.name}, {product2.price} руб. Остаток: {product2.quantity} шт."
    ])
    assert category1.products == expected_output


def test_add_product(category1: Category, product2: Product) -> None:
    initial_products_count = len(category1._Category__products)

    category1.add_product(product2)

    assert len(category1._Category__products) == initial_products_count + 1
    assert product2 in category1._Category__products
