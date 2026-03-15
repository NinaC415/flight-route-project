"""Test format_route."""

from flight_routes import format_route


def test_format_route():
    """Test route formatting."""
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

    assert format_route(route) == "LAX -> DEN -> JFK"
