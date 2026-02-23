def count_helper(days: int, count: int):
    print("Day: ", count)
    if count >= days - 1:
        print("Harvest time!")
        return
    count_helper(days, count + 1)
def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    count = 1
    count_helper(days, count)
