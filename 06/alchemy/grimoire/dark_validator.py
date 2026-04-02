from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lowered_ingredients = ingredients.lower()
    for ingredient in dark_spell_allowed_ingredients():
        if ingredient in lowered_ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
