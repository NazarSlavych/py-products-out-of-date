from unittest.mock import patch
import datetime
from app.main import outdated_products


class MockDate(datetime.date):
    @classmethod
    def today(cls) -> datetime.date:
        return cls(2022, 2, 2)


def test_outdated_products_empty_list() -> None:
    with patch("datetime.date", MockDate):
        assert outdated_products([]) == []


def test_outdated_products_no_outdated() -> None:
    with patch("datetime.date", MockDate):
        products = [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10), "price": 600},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 2, 5), "price": 120}
        ]
        assert outdated_products(products) == []


def test_outdated_products_some_outdated() -> None:
    with patch("datetime.date", MockDate):
        products = [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 10), "price": 600},
            {"name": "duck",
             "expiration_date": datetime.date(2022, 2, 1), "price": 160}
        ]
        assert outdated_products(products) == ["duck"]


def test_outdated_products_all_outdated() -> None:
    with patch("datetime.date", MockDate):
        products = [
            {"name": "duck",
             "expiration_date": datetime.date(2022, 2, 1), "price": 160},
            {"name": "chicken",
             "expiration_date": datetime.date(2022, 1, 31), "price": 120}
        ]
        assert outdated_products(products) == ["duck", "chicken"]


def test_outdated_products_boundary_case() -> None:
    with patch("datetime.date", MockDate):
        products = [
            {"name": "salmon",
             "expiration_date": datetime.date(2022, 2, 2), "price": 600},
            {"name": "duck",
             "expiration_date": datetime.date(2022, 2, 1), "price": 160}
        ]
        assert outdated_products(products) == ["duck"]
