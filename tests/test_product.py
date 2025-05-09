from src.product import Product


def test_product_init(product1: Product) -> None:
    assert product1.name == "Samsung Galaxy S23 Ultra"
    assert product1.description == "256GB, Серый цвет, 200MP камера"
    assert product1.price == 180000.0
    assert product1.quantity == 5


def test_price_setter_positive():
    product = Product("Телефон", "Смартфон", 50000.0, 10)

    product.price = 45000.0

    assert product.price == 45000.0


def test_price_setter_non_positive(capsys):
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
        "quantity": 3
    }

    new_product = Product.new_product(product_data)

    assert new_product.name == product_data["name"]
    assert new_product.description == product_data["description"]
    assert new_product.price == product_data["price"]
    assert new_product.quantity == product_data["quantity"]
