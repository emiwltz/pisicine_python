from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.batch_count = 0
        self.treated_elements = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process the data and return a formatted result string."""

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Return filtered data. Default behavior: no special filtering."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return common statistics about the stream."""
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "batch_count": self.batch_count,
            "treated_elements": self.treated_elements,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "sensor")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_entries = [
                data for data in data_batch if isinstance(data, str) and ":" in data
            ]

            temperature = []
            for entry in valid_entries:
                sensor_type, value = entry.split(":", 1)
                if sensor_type == "temp":
                    temperature.append(float(value))
            self.batch_count += 1
            self.treated_elements += len(valid_entries)

            if temperature:
                avg_temp = sum(temperature) / len(temperature)
                return (
                    f"{len(valid_entries)} reading processed, "
                    f"avg temp: {avg_temp:.1f}°C"
                )
            return f"{len(valid_entries)} reading processed, no temperature detected"

        except (TypeError, ValueError) as e:
            raise ValueError(f"Sensor stream processing failed: {e}") from e


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "transaction")

    def process_batch(self, data_batch: List[Any]) -> str:
        try:
            valid_entries = [
                data for data in data_batch if isinstance(data, str) and ":" in data
            ]

            self.batch_count += 1
            self.treated_elements += len(valid_entries)

            buy_actions = []
            sell_actions = []
            for entrie in valid_entries:
                action_type, value = entrie.split(":", 1)
                if action_type == "buy":
                    buy_actions.append(float(value))
                elif action_type == "sell":
                    sell_actions.append(float(value))
                else:
                    return f"{action_type} is not valid"
            return (
                f"{len(valid_entries)} operations,"
                f"net flows: +{sum(buy_actions) - sum(sell_actions)} units"
            )

        except (ValueError, TypeError) as e:
            raise ValueError(f"Invalid action: {e}") from e


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "event")


def main():
    print("test")


if __name__ == "__main__":
    main()
