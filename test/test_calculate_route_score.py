"""Test calculate_route_score."""

from flight_routes import calculate_route_score


def test_calculate_route_score():
    """Test balanced route score."""
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

    score = calculate_route_score(route, layover_time=1.0)
    assert score == 10
