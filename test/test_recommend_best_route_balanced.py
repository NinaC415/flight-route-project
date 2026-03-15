"""Test recommend_best_route with balanced preference."""

from flight_routes import calculate_route_score
from flight_routes import recommend_best_route


def test_recommend_best_route_balanced():
    """Test balanced route recommendation."""
    route_1 = [
        {
            "flight_no": "UA1",
            "origin": "LAX",
            "destination": "JFK",
            "duration": 5.5,
            "price": 420,
        }
    ]
    route_2 = [
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

    best_route = recommend_best_route(
        [route_1, route_2],
        preference="balanced",
        layover_time=1.0,
    )

    assert best_route in [route_1, route_2]
    assert (
        calculate_route_score(best_route, 1, 50, 1.0, 330, 420, 5.5, 6.5) > 0
    )
