class Category:
    name: str
    description: str
    product: list
    category_count: int = 0
    product_count: int = 0

    def __init__(self, name: str, description: str, product: list, category_count: int=0, product_count: int=0):
        self.name = name
        self.description = description
        self.products = product
        Category.category_count += 1
        Category.product_count += 1
