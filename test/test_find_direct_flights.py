"""Test find_direct_flights."""

from flight_routes import find_direct_flights


def test_find_direct_flights():
    """Test direct flight search."""
    flights = [
        {
            "flight_no": "UA1",
            "origin": "LAX",
            "destination": "JFK",
            "duration": 5.0,
            "price": 420,
        },
        {
            "flight_no": "UA2",
            "origin": "LAX",
            "destination": "SFO",
            "duration": 1.5,
            "price": 120,
        },
    ]

    result = find_direct_flights(flights, "LAX", "JFK")
    assert len(result) == 1
    assert result[0]["flight_no"] == "UA1"
