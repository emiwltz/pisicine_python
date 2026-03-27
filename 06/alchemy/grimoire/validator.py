def validate_ingredients(ingredients: str) -> str:
    valid_input = ["fire", "water", "earth", "air"]
    for element in valid_input:
        if element in ingredients:
            return f"{ingredients} - VALID"
    else:
        return f"{ingredients} - INVALID"
