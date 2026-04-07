from datetime import datetime
from enum import Enum
from pydantic import (  # type: ignore[import-not-found]
    BaseModel,
    Field,
    ValidationError,
    model_validator,
)


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPTAIN = "captain"
    COMMANDER = "commander"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: datetime
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission_id(self) -> "SpaceMission":
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        return self

    @model_validator(mode="after")
    def check_rank(self) -> "SpaceMission":
        has_command = any(
            member.rank in {Rank.CAPTAIN, Rank.COMMANDER}
            for member in self.crew
        )
        if not has_command:
            raise ValueError("Must have at least one Commander or Captain")
        return self

    @model_validator(mode="after")
    def check_long_mission(self) -> "SpaceMission":
        if self.duration_days > 365:
            experienced_members = sum(
                member.years_experience >= 5 for member in self.crew
            )
            experience_ratio = experienced_members / len(self.crew)
            if experience_ratio < 0.5:
                raise ValueError(
                    "Long missions (> 365 days) need 50% "
                    "experienced crew (5+ years)"
                )
        return self

    @model_validator(mode="after")
    def check_active(self) -> "SpaceMission":
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def main() -> None:
    sarah = CrewMember(
        member_id="CM101",
        name="Elena Voss",
        rank=Rank.COMMANDER,
        age=44,
        specialization="Deep Command",
        years_experience=18,
        is_active=True,
    )
    john = CrewMember(
        member_id="CM102",
        name="Noah Kim",
        rank=Rank.LIEUTENANT,
        age=36,
        specialization="Astrogation",
        years_experience=9,
        is_active=True,
    )
    alice = CrewMember(
        member_id="CM103",
        name="Mila Ortega",
        rank=Rank.OFFICER,
        age=31,
        specialization="Systems Engineering",
        years_experience=7,
        is_active=True,
    )
    crew = [sarah, john, alice]

    mission = SpaceMission(
        mission_id="M2026_EUROPA",
        mission_name="Europa Survey Initiative",
        destination="Europa",
        launch_date="2026-06-18T06:30:00",
        duration_days=640,
        crew=crew,
        budget_millions=1840.0,
    )
    print("Space Mission Crew Validation")
    print("=========================================")
    print("Valid mission created:")
    print(f"Mission: {mission.mission_name}")
    print(f"ID: {mission.mission_id}")
    print(f"Destination: {mission.destination}")
    print(f"Duration: {mission.duration_days} days")
    print(f"Budget: ${mission.budget_millions}M")
    print(f"Crew size: {len(mission.crew)}")
    print("Crew members:")
    for member in mission.crew:
        print(
            f"- {member.name} ({member.rank.value}) - {member.specialization}"
        )
    print("=========================================")
    print("Expected validation error:")
    try:
        SpaceMission(
            mission_id="M2026_DRILL",
            mission_name="Outer Rim Recon Drill",
            destination="Ceres",
            launch_date="2026-06-21T11:15:00",
            duration_days=45,
            crew=[
                CrewMember(
                    member_id="CM110",
                    name="Iris Vale",
                    rank=Rank.OFFICER,
                    age=30,
                    specialization="Flight Ops",
                    years_experience=6,
                    is_active=True,
                ),
                CrewMember(
                    member_id="CM111",
                    name="Tomas Reed",
                    rank=Rank.LIEUTENANT,
                    age=35,
                    specialization="Field Science",
                    years_experience=8,
                    is_active=True,
                ),
            ],
            budget_millions=72.0,
        )
    except ValidationError as exc:
        print(exc.errors()[0]["msg"])


if __name__ == "__main__":
    main()
