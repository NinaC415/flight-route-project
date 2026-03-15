"""Functions used in the flight route project.

Project repository:
https://github.com/NinaC415/flight-route-project
"""


def find_direct_flights(flights, origin, destination):
    """
    Find direct flights from origin to destination.

    Parameters
    ----------
    flights : list
        List of flight dictionaries.
    origin : str
        Starting airport.
    destination : str
        Ending airport.

    Returns
    -------
    list
        Direct flights that match the route.
    """

    direct_flights = []

    for flight in flights:
        if flight["origin"] == origin and flight["destination"] == destination:
            direct_flights.append(flight)

    return direct_flights


def find_one_stop_routes(flights, origin, destination):
    """
    Find routes with one layover.

    Parameters
    ----------
    flights : list
        List of flight dictionaries.
    origin : str
        Starting airport.
    destination : str
        Ending airport.

    Returns
    -------
    list
        List of routes (each route has two flights).
    """

    routes = []

    for first_flight in flights:

        if first_flight["origin"] == origin:

            layover_airport = first_flight["destination"]

            # avoid routes like LAX -> LAX
            if layover_airport != origin and layover_airport != destination:

                for second_flight in flights:

                    if (
                        second_flight["origin"] == layover_airport
                        and second_flight["destination"] == destination
                    ):
                        routes.append([first_flight, second_flight])

    return routes


def calculate_route_duration(route, layover_time=0):
    """
    Calculate total travel time.

    Parameters
    ----------
    route : list
        A list of flights.
    layover_time : float
        Extra time added for layovers.

    Returns
    -------
    float
        Total duration.
    """
    # error handling
    if not route:
        raise ValueError("route must be a non-empty list of flights")

    total_time = 0

    for flight in route:
        if "duration" not in flight:
            raise KeyError("each flight must include 'duration'")
        if not isinstance(flight["duration"], (int, float)):
            raise TypeError("flight 'duration' must be numeric")
        total_time += flight["duration"]

    if len(route) > 1:
        total_time += layover_time

    return total_time


def calculate_route_price(route):
    """
    Calculate total price for a route.

    Parameters
    ----------
    route : list
        A list of flights.

    Returns
    -------
    float
        Total price.
    """
    # error handling
    if not route:
        raise ValueError("route must be a non-empty list of flights")

    total_price = 0

    for flight in route:
        # error handling
        if "price" not in flight:
            raise KeyError("each flight must include 'price'")
        if not isinstance(flight["price"], (int, float)):
            raise TypeError("flight 'price' must be numeric")
        total_price += flight["price"]

    return total_price


def _score_to_five_levels(value, min_value, max_value):
    """
    Convert a metric into 1-5 points where lower is better.

    Parameters
    ----------
    value : float
        Current route metric value.
    min_value : float
        Best (lowest) value in candidates.
    max_value : float
        Worst (highest) value in candidates.

    Returns
    -------
    int
        Score from 1 to 5.
    """

    if max_value == min_value:
        return 5

    normalized = (value - min_value) / (max_value - min_value)
    score = 5 - int(normalized * 4)

    if score < 1:
        return 1
    if score > 5:
        return 5

    return score


def calculate_route_score(route, price_weight=1, time_weight=50, layover_time=0,
                          price_min=None, price_max=None, time_min=None,
                          time_max=None):
    """
    Calculate a score using 1-5 points for price and travel time.

    Lower price and shorter duration receive higher points.
    Final score is price points + time points.

    Parameters
    ----------
    route : list
        A list of flights.
    price_weight : number
        Kept for backward compatibility (not used in point scoring).
    time_weight : number
        Kept for backward compatibility (not used in point scoring).
    layover_time : float
        Extra time for layovers.
    price_min : float or None
        Minimum price among candidate routes.
    price_max : float or None
        Maximum price among candidate routes.
    time_min : float or None
        Minimum duration among candidate routes.
    time_max : float or None
        Maximum duration among candidate routes.

    Returns
    -------
    int
        Score for the route.
    """

    price = calculate_route_price(route)
    time = calculate_route_duration(route, layover_time)

    if price_min is None:
        price_min = price
    if price_max is None:
        price_max = price
    if time_min is None:
        time_min = time
    if time_max is None:
        time_max = time

    price_score = _score_to_five_levels(price, price_min, price_max)
    time_score = _score_to_five_levels(time, time_min, time_max)
    score = price_score + time_score

    return score


def get_all_routes(flights, origin, destination):
    """
    Get all possible routes.

    Parameters
    ----------
    flights : list
        List of flight dictionaries.
    origin : str
        Starting airport.
    destination : str
        Ending airport.

    Returns
    -------
    list
        List of routes.
    """

    routes = []

    # treat direct flights as routes with one flight
    direct = find_direct_flights(flights, origin, destination)

    for flight in direct:
        routes.append([flight])

    one_stop = find_one_stop_routes(flights, origin, destination)

    for route in one_stop:
        routes.append(route)

    return routes


def recommend_best_route(routes, preference="time", layover_time=0,
                         price_weight=1, time_weight=50):
    """
    Choose the best route.

    Parameters
    ----------
    routes : list
        List of routes.
    preference : str
        "time", "price", or "balanced".
    layover_time : float
        Extra time for layovers.

    Returns
    -------
    list or None
        Best route.
    """

    if len(routes) == 0:
        return None

    best_route = routes[0]

    if preference == "balanced":
        prices = [calculate_route_price(route) for route in routes]
        times = [
            calculate_route_duration(route, layover_time)
            for route in routes
        ]
        price_min = min(prices)
        price_max = max(prices)
        time_min = min(times)
        time_max = max(times)

    for route in routes[1:]:

        if preference == "time":
            value = calculate_route_duration(route, layover_time)
            best_value = calculate_route_duration(best_route, layover_time)

        elif preference == "price":
            value = calculate_route_price(route)
            best_value = calculate_route_price(best_route)

        elif preference == "balanced":
            value = calculate_route_score(route, price_weight,
                                          time_weight, layover_time,
                                          price_min, price_max,
                                          time_min, time_max)
            best_value = calculate_route_score(best_route, price_weight,
                                               time_weight, layover_time,
                                               price_min, price_max,
                                               time_min, time_max)

        else:
            return None

        if preference == "balanced":
            if value > best_value:
                best_route = route
        else:
            if value < best_value:
                best_route = route

    return best_route


def format_route(route):
    """
    Turn a route into a readable string.

    Parameters
    ----------
    route : list
        A list of flights.

    Returns
    -------
    str
        Route as text.
    """

    airports = [route[0]["origin"]]

    for flight in route:
        airports.append(flight["destination"])

    return " -> ".join(airports)
