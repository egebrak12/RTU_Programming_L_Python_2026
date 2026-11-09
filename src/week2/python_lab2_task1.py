
def average(values: list[float]) -> float:
    """Return the average of values, or 0.0 for an empty list."""
    if not values:
        return 0.0
    return sum(values) / len(values)


def largest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the largest population."""
    if not populations:
        return ("", 0)
    return max(populations.items(), key=lambda city: city[1])


def smallest_city(populations: dict[str, int]) -> tuple[str, int]:
    """Return (city, population) for the city with the smallest population."""
    if not populations:
        return ("", 0)
    return min(populations.items(), key=lambda city: city[1])


def total_population(populations: dict[str, int]) -> int:
    """Return the sum of all populations."""
    return sum(populations.values())


if __name__ == "__main__":
    temperatures = [3.5, 4.2, 5.0, 2.8, 6.1, 4.6, 3.9]

    city_population = {
        "Riga": 605000,
        "Daugavpils": 78000,
        "Liepaja": 67000,
        "Jelgava": 55000,
        "Valmiera": 23000
    }

    print(f"Average temperature: {average(temperatures):.1f}")

    largest = largest_city(city_population)
    print(f"Largest city: {largest[0]} - {largest[1]}")

    smallest = smallest_city(city_population)
    print(f"Smallest city: {smallest[0]} - {smallest[1]}")

    print(f"Total population: {total_population(city_population)}")
