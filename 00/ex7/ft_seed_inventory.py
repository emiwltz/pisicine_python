
def ft_seed_inventory(seed_type: str, quantity: int, unit: str):

    if unit not in ("packets", "grams", "area"):
        print("Unknown unit type")
        return
    if unit == "packets":
        unit = quantity + unit + " avaible"
    if unit == "grams":
        unit = unit + "total"
    else:
        unit = "covers" + quantity + "metters"
    seed_type = seed_type.title()
    print(seed_type, ":", quantity)
