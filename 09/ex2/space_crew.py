from pydantic import BaseModel, Field, ValidationError, model_validator
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
    years_experience: int = Field(min_length=0, max_length=50)
    is_active: bool = True


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    launch_date: str
    duration_days: int = Field(ge=1, le=3650)
    crew: list[CrewMember]
    mission_status: str = "planned"
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator
    def check_mission_id(self):
        if not self.mission_id.startswith("M"):
            raise ValueError("Mission ID must start with 'M'")
        return self

    @model_validator
    def check_rank(self):
        rank_nbr = 0
        for member in self.crew:
            if member.rank is Rank.CAPITAIN or member.rank is Rank.COMMANDER:
                rank_nbr += 1
        if rank_nbr < 1:
            raise ValueError("Must have at least one Commander or Captain")
        return self

    @model_validator
    def check_experience(self):
        rank_nbr = 0
        for member in self.crew:
            if member.rank is Rank.CAPITAIN or member.rank is Rank.COMMANDER:
                rank_nbr += 1
        if rank_nbr < 1:
            raise ValueError("Must have at least one Commander or Captain")
        return self


def main():
    pass


if __name__ == "__main__":
    main()
