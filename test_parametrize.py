import pytest
from your_app.models import Order


@pytest.mark.django_db
@pytest.mark.parametrize("name, price, quantity, total", [
    ("Product A", 100, 5, 500),  # Создание товара в наличии
    ("Product B", 200, 0, 0),  # Создание товара, который не в наличии
])

def test_create_product(name, price, quantity, total):
    order = Order.objects.create(
        name=name,
        price=price,
        quantity=quantity,
    )
    assert order.calculate_total() == total     # предположим, что у модели Order есть метод calculate_total() для получения общей стоимости заказа
