"""Test get_all_routes."""

from flight_routes import get_all_routes


def test_get_all_routes():
    """Test collecting all routes."""
    flights = [
        {
            "flight_no": "UA1",
            "origin": "LAX",
            "destination": "JFK",
            "duration": 5.5,
            "price": 420,
        },
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

    routes = get_all_routes(flights, "LAX", "JFK")
    assert len(routes) == 2
