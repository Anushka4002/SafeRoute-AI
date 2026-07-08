import math


def euclidean_distance(location1, location2):
    """
    Calculates the straight-line distance between two locations.

    Parameters:
        location1 (Location): Source location
        location2 (Location): Destination location

    Returns:
        float: Estimated distance
    """

    return math.sqrt(
        (location1.latitude - location2.latitude) ** 2
        +
        (location1.longitude - location2.longitude) ** 2
    )


def manhattan_distance(location1, location2):
    """
    Manhattan distance heuristic.
    Useful for grid-based maps.
    """

    return (
        abs(location1.latitude - location2.latitude)
        +
        abs(location1.longitude - location2.longitude)
    )