from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    lowered_ingredients = ingredients.lower()
    for ingredient in light_spell_allowed_ingredients():
        if ingredient in lowered_ingredients:
            return f"{ingredients} - VALID"
    return f"{ingredients} - INVALID"
