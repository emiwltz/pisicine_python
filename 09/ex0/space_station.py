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
    print("Space Station Data Validation")
    print("=" * 40)
    print("Valid station created:")
    station1 = SpaceStation(
        station_id="ISS999",
        name="ISS",
        crew_size=5,
        power_level=50,
        oxygen_level=91.3,
        last_maintenance="2026-04-05T12:00:00",
        is_operational=True,
        notes="Primary orbital research station.",
    )
    print(f"ID: {station1.station_id}")
    print(f"Name: {station1.name}")
    print(f"Crew: {station1.crew_size} people")
    print(f"Power: {station1.power_level}%")
    print(f"Oxygen: {station1.oxygen_level}%")
    print(
        "Status: "
        f"{'Operational' if station1.is_operational else 'Non-operational'}"
    )
    print("=" * 40)
    print("Expected validation error:")
    try:
        SpaceStation(
            station_id="ISS002",
            name="Lunar Gateway",
            crew_size=21,
            power_level=20,
            oxygen_level=10,
            last_maintenance="2026-04-05T12:00:00",
            is_operational=True,
            notes="Crew capacity test.",
        )
    except ValidationError as exc:
        print(exc.errors()[0]["msg"])


if __name__ == "__main__":
    main()
