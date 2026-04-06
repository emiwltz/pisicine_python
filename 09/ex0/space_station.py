from pydantic import BaseModel, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.00, le=100.00)
    oxygen_level: float = Field(ge=0.00, le=100.00)
    last_maintenance: datetime
    is_operational: bool = True
    notes: str | None = Field(default=None, max_length=200)


def main():
    print("Testing with valid station")
    station1 = SpaceStation(
        station_id="M_3421",
        name="artemis",
        crew_size=2,
        power_level=20,
        oxygen_level=10,
        last_maintenance="2026-04-05T12:00:00",
        is_operational=True,
        notes="salut"
    )
    print(station1)
    print()

    print("Trying invalid station")
    try:
        station2 = SpaceStation(
            station_id="M",
            name="artemis",
            crew_size=2,
            power_level=20,
            oxygen_level=10,
            last_maintenance="2026-04-05T12:00:00",
            is_operational=True,
            notes="salut"
        )
        print(station2)
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()
