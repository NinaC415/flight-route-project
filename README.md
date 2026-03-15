# Flight Route Project

This project builds a flight route recommendation system. The program looks for direct flights and one-stop routes between two
airports. It can calculate the total duration and total price of each
route. It can also recommend the best route based on time, price, or
a balanced score that uses both time and price.

## Function Overview
- `find_direct_flights`: Returns all direct flights from an origin airport
  to a destination airport.
- `find_one_stop_routes`: Returns all valid one-stop routes that connect
  origin to destination through one layover airport.
- `calculate_route_duration`: Computes the total travel duration of a route,
  including optional layover time for multi-leg trips.
- `calculate_route_price`: Computes the total ticket price of a route by
  summing prices of all flights in that route.
- `_score_to_five_levels`: Converts a metric into a 1-5 score where lower
  values receive higher points.
- `calculate_route_score`: Generates a positive balanced score by adding
  price points and time points (each from 1 to 5).
- `get_all_routes`: Collects all available routes between two airports,
  including direct and one-stop options.
- `recommend_best_route`: Selects the best route from candidates according
  to the selected preference (`time`, `price`, or `balanced`).
- `format_route`: Converts a route into a readable string such as
  `LAX -> DEN -> JFK`.

## Requirements
- Python 3.8+
- `pytest` (for running tests)

Install test dependency:

```bash
pip install pytest
```

## Example Usage

```python
from flight_routes import get_all_routes
from flight_routes import recommend_best_route
from flight_routes import format_route
from flight_routes import calculate_route_score

flights = [
    {"flight_no": "UA1", "origin": "LAX", "destination": "JFK",
     "duration": 5.5, "price": 420},
    {"flight_no": "AA1", "origin": "LAX", "destination": "DEN",
     "duration": 2.5, "price": 180},
    {"flight_no": "AA2", "origin": "DEN", "destination": "JFK",
     "duration": 3.0, "price": 150},
]

routes = get_all_routes(flights, "LAX", "JFK")

best_time = recommend_best_route(routes, preference="time", layover_time=1.0)
print("Best by time:", format_route(best_time))

best_price = recommend_best_route(routes, preference="price", layover_time=1.0)
print("Best by price:", format_route(best_price))

best_balanced = recommend_best_route(
    routes,
    preference="balanced",
    layover_time=1.0
)
print("Best balanced:", format_route(best_balanced))

# Optional: inspect balanced score in the current candidate range
prices = [sum(f["price"] for f in r) for r in routes]
times = [sum(f["duration"] for f in r) + (1.0 if len(r) > 1 else 0) for r in routes]
score = calculate_route_score(
    best_balanced,
    layover_time=1.0,
    price_min=min(prices),
    price_max=max(prices),
    time_min=min(times),
    time_max=max(times),
)
print("Balanced score:", score)
```

Run tests:

```bash
pytest -q
```
