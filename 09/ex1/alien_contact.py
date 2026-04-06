from pydantic import BaseModel, Field, ValidationError, model_validator
from datetime import datetime
from enum import Enum


class ContactType(Enum):
    RADIO = "radio"
    VISUAL = "visual"
    PHYSICAL = "physical"
    TELEPATHIC = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType
    signal_strength: float = Field(ge=0, le=10)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(default=None, max_length=500)
    is_verified: bool = False

    @model_validator(mode="after")
    def check_id(self):
        if not self.contact_id.startswith("AC"):
            raise ValueError("Contact ID must start with 'AC'")
        return self

    @model_validator(mode="after")
    def check_physical(self):
        if self.contact_type is ContactType.PHYSICAL and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")
        return self

    @model_validator(mode="after")
    def check_telepathic(self):
        if self.contact_type is ContactType.TELEPATHIC and self.witness_count < 3:
            raise ValueError("Telepathic contact requires at least 3 witnesses")
        return self

    @model_validator(mode="after")
    def check_strong_signals(self):
        if self.signal_strength > 7 and not self.message_received:
            raise ValueError(
                "Strong signals (> 7.0) should include received messages"
            )
        return self


def main():
    print("Alien Contact Log Validation")
    print("=" * 38)
    print("Valid contact report:")
    first_contact = AlienContact(
        contact_id="AC_2024_001",
        timestamp="2026-04-06T10:00:00",
        location="Area 51, Nevada",
        contact_type="radio",
        signal_strength=8.5,
        duration_minutes=45,
        witness_count=5,
        message_received="Greetings from Zeta Reticuli",
        is_verified=True,
    )
    print(f"ID: {first_contact.contact_id}")
    print(f"Type: {first_contact.contact_type.value}")
    print(f"Location: {first_contact.location}")
    print(f"Signal: {first_contact.signal_strength}/10")
    print(f"Duration: {first_contact.duration_minutes} minutes")
    print(f"Witnesses: {first_contact.witness_count}")
    print(f"Message: '{first_contact.message_received}'")
    print("=" * 38)
    print("Expected validation error:")
    try:
        AlienContact(
            contact_id="AC_2024_002",
            timestamp="2026-04-06T11:00:00",
            location="Roswell, New Mexico",
            contact_type="telepathic",
            signal_strength=6.2,
            duration_minutes=20,
            witness_count=2,
            message_received="We come in peace",
            is_verified=False,
        )
    except ValidationError as exc:
        print(exc.errors()[0]["msg"])


if __name__ == "__main__":
    main()
