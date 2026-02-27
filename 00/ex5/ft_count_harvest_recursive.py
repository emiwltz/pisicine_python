def count_helper(current_day: int, total_days: int):
    if current_day > total_days:
        return
    print(f"Day {current_day}")
    count_helper(current_day + 1, total_days)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count_helper(1, days)
    print("Harvest time!")
