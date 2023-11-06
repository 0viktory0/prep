import pytest
from your_app.models import MyModel
from django.core.exceptions import ObjectDoesNotExist


def test_non_existent_record():
    with pytest.raises(ObjectDoesNotExist):
        MyModel.objects.get(id=15000)  # Предположим, что записи с id=15000 не существует
