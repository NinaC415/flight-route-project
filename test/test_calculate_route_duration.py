"""Test calculate_route_duration."""

from flight_routes import calculate_route_duration


def test_calculate_route_duration():
    """Test route duration calculation."""
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

    assert calculate_route_duration(route) == 5.5
    assert calculate_route_duration(route, layover_time=1.0) == 6.5
