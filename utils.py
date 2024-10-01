from custom_types import EV_API_Data, EV_Make_Metadata

def calculate_average_range(cars: list[EV_API_Data], ignore_zero_range: bool = False) -> float:
    total_range = 0
    valid_range_count = 0

    for car in cars:
        if ignore_zero_range and car.electric_range == 0:
            continue
        total_range += car.electric_range
        valid_range_count += 1

    # Deal with divide by zero
    if valid_range_count == 0:
        return 0

    return round(total_range / valid_range_count, 1)


def get_make_details(cars: list[EV_API_Data]) -> list[EV_Make_Metadata]:
    # TODO consider exposing ignore_zero_range
    makes = {make: [car for car in cars if car.make == make]
             for make in set(car.make for car in cars)}
    return [EV_Make_Metadata(
        make=make,
        count=len(make_cars),
        average_range=calculate_average_range(make_cars)
    ) for make, make_cars in makes.items()]
