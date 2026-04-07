from pydantic import BaseModel, Field, model_validator
from datetime import datetime
from enum import Enum


class Rank(Enum):
    CADET = "cadet"
    OFFICER = "officer"
    LIEUTENANT = "lieutenant"
    CAPITAIN = "capitain"
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
    crew: list[CrewMember]
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def check_mission_id(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        return self

    @model_validator(mode="after")
    def check_rank(self):
        rank_nbr = 0
        for member in self.crew:
            if member.rank is Rank.CAPITAIN or member.rank is Rank.COMMANDER:
                rank_nbr += 1
        if rank_nbr < 1:
            raise ValueError("Must have at least one Commander or Captain")
        return self

    @model_validator(mode="after")
    def check_experience(self):
        rank_nbr = 0
        for member in self.crew:
            if member.rank is Rank.CAPITAIN or member.rank is Rank.COMMANDER:
                rank_nbr += 1
        if rank_nbr < 1:
            raise ValueError("Must have at least one Commander or Captain")
        return self

    @model_validator(mode="after")
    def check_long_mission(self):
        if self.duration_days > 365:
            experience_percentage = 0
            experience_member = 0
            for member in self.crew:
                if member.years_experience >= 5:
                    experience_member += 1
            experience_percentage = experience_member / len(self.crew) * 100
            if experience_percentage <= 50:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew (5+ years)"
                )
        return self

    @model_validator(mode="after")
    def check_active(self):
        for member in self.crew:
            if not member.is_active:
                raise ValueError("All crew members must be active")
        return self


def main():
    sarah = CrewMember(
        member_id="CM001",
        name="Sarah Connor",
        rank=Rank.COMMANDER,
        age=42,
        specialization="Command",
        years_experience=15,
        is_active=True,
    )
    john = CrewMember(
        member_id="CM002",
        name="John Smith",
        rank=Rank.LIEUTENANT,
        age=34,
        specialization="Navigation",
        years_experience=8,
        is_active=True,
    )
    alice = CrewMember(
        member_id="CM003",
        name="Alice Johnson",
        rank=Rank.OFFICER,
        age=29,
        specialization="Engineering",
        years_experience=6,
        is_active=True,
    )
    crew = [alice, john, sarah]

    mission = SpaceMission(
        mission_id="M2024_MARS",
        mission_name="Mars Colony Establishment",
        destination="Mars",
        launch_date="2026-04-06",
        duration_days=350,
        crew=crew,
        budget_millions=3000,
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


if __name__ == "__main__":
    main()
