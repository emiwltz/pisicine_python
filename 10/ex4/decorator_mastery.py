from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable[..., str]) -> Callable[..., str]:
    @wraps(func)
    def wrapper(*args: object, **kwargs: object) -> str:
        print(f"Casting {func.__name__}...")
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        duration = end - start
        print(f"Spell completed in {duration:.3f} seconds")
        return result

    return wrapper


def power_validator(
    min_power: int,
) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> str:
            if "power" in kwargs:
                power = kwargs["power"]
            elif len(args) >= 3 and isinstance(args[2], int):
                power = args[2]
            elif args and isinstance(args[0], int):
                power = args[0]
            else:
                return "Insufficient power for this spell"

            if power < min_power:
                return "Insufficient power for this spell"

            return func(*args, **kwargs)

        return wrapper

    return decorator


def retry_spell(
    max_attempts: int,
) -> Callable[[Callable[..., str]], Callable[..., str]]:
    def decorator(func: Callable[..., str]) -> Callable[..., str]:
        @wraps(func)
        def wrapper(*args: object, **kwargs: object) -> str:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying... "
                            f"(attempt {attempt}/{max_attempts})"
                        )

            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return (
            len(name) >= 3
            and all(char.isalpha() or char.isspace() for char in name)
        )

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.1)
    return "Fireball cast!"


@power_validator(10)
def iceball(power: int) -> str:
    return "Iceball cast!"


def make_failing_spell() -> Callable[[], str]:
    @retry_spell(3)
    def failing_spell() -> str:
        raise ValueError("Spell failed")

    return failing_spell


def make_unstable_spell() -> Callable[[], str]:
    attempts = 0

    @retry_spell(3)
    def unstable_spell() -> str:
        nonlocal attempts
        attempts += 1
        if attempts < 3:
            raise ValueError("Spell failed")
        return "Waaaaaaagh spelled !"

    return unstable_spell


def main() -> None:
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")
    print()

    print("Testing power validator...")
    print(iceball(15))
    print(iceball(5))
    print()

    print("Testing retrying spell...")
    failing_spell = make_failing_spell()
    print(failing_spell())
    unstable_spell = make_unstable_spell()
    print(unstable_spell())
    print()

    print("Testing MageGuild...")
    print(MageGuild.validate_mage_name("Gandalf"))
    print(MageGuild.validate_mage_name("M4ge"))
    guild = MageGuild()
    print(guild.cast_spell("Lightning", 15))
    print(guild.cast_spell("Spark", 5))


if __name__ == "__main__":
    main()
