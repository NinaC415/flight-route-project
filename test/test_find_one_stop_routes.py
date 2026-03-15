"""Test find_one_stop_routes."""

from flight_routes import find_one_stop_routes


def test_find_one_stop_routes():
    """Test one-stop route search."""
    flights = [
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

    routes = find_one_stop_routes(flights, "LAX", "JFK")
    assert len(routes) == 1
    assert routes[0][0]["origin"] == "LAX"
    assert routes[0][1]["destination"] == "JFK"
