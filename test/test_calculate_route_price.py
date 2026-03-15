"""Test calculate_route_price."""

from flight_routes import calculate_route_price


def test_calculate_route_price():
    """Test route price calculation."""
    route = [
        {
            "flight_no": "AA1",
            "origin": "LAX",
            "destination": "DEN",
            "duration": 2.5,
            "price": 180,
        },
        {
            "flight_no": "AA2",
            "origin": "DEN",
            "destination": "JFK",
            "duration": 3.0,
            "price": 150,
        },
    ]

    assert calculate_route_price(route) == 330
