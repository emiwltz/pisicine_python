
def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    count = 1
    while count != days:
        print("Day: ", count)
        count = count + 1
    print("Harvest time!")
