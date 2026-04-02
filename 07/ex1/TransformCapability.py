from abc import ABC, abstractmethod


class TransformCapability(ABC):
    @abstractmethod
    def transform(self) -> str:
        """Switch the Creature to its transformed state."""

    @abstractmethod
    def revert(self) -> str:
        """Return the Creature to its normal state."""
