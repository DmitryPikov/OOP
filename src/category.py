class Category:
    name: str
    description: str
    product: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, product: list):
        self.name = name
        self.description = description
        self.__products = product
        Category.category_count += 1
        Category.product_count += len(product)

    @property
    def products(self) -> str:
        product_list = []
        for product in self.__products:
            product_list.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.")
        return "\n".join(product_list)

    def add_product(self, product: list) -> None:
        self.__products.append(product)
        Category.category_count += 1

    def __str__(self) -> str:
        total_quantity = sum(product.quantity for product in self.__products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def middle_price(self) -> float:
        try:
            total_price = sum(product.price for product in self.__products)
            return total_price / len(self.__products)
        except ZeroDivisionError:
            return 0
