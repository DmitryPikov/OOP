from src.category import Category


def test_category_init(category1: Category) -> None:
    assert category1.name == "Смартфоны"
    assert (
        category1.description == "Смартфоны, как средство не только коммуникации,"
                                 "но и получения дополнительных функций для удобства жизни"
    )
    assert category1.category_count == 1
    assert len(category1.products) == 2
