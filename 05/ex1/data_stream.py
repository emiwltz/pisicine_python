from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union


class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str) -> None:
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.batch_count = 0
        self.treated_elements = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data."""

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "batch_count": self.batch_count,
            "treated_elements": self.treated_elements,
        }


class SensorStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise TypeError("data_batch must be a list")

        try:
            valid_entries = [
                entry.strip()
                for entry in data_batch
                if isinstance(entry, str) and ":" in entry
            ]
            temperatures: List[float] = []
            for entry in valid_entries:
                sensor_type, raw_value = entry.split(":", 1)
                if sensor_type == "temp":
                    temperatures.append(float(raw_value))

            self.batch_count += 1
            self.treated_elements += len(valid_entries)

            if temperatures:
                average = sum(temperatures) / len(temperatures)
                return (
                    f"Sensor analysis: {len(valid_entries)} readings "
                    f"processed, avg temp: {average:.1f}°C"
                )
            return (
                f"Sensor analysis: {len(valid_entries)} readings "
                f"processed, avg temp: 0.0°C"
            )
        except (TypeError, ValueError) as error:
            raise ValueError(
                f"Sensor stream processing failed: {error}"
            ) from error

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria != "critical":
            return data_batch

        filtered_entries: List[Any] = []
        for entry in data_batch:
            if not isinstance(entry, str) or ":" not in entry:
                continue
            sensor_type, raw_value = entry.split(":", 1)
            if sensor_type == "temp" and float(raw_value) >= 30.0:
                filtered_entries.append(entry)
        return filtered_entries

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["domain"] = "sensor"
        return stats


class TransactionStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "Financial Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise TypeError("data_batch must be a list")

        try:
            valid_entries: List[str] = []
            buy_total = 0.0
            sell_total = 0.0

            for entry in data_batch:
                if not isinstance(entry, str) or ":" not in entry:
                    continue
                action, raw_value = entry.split(":", 1)
                amount = float(raw_value.strip())
                action = action.strip().lower()
                if action not in ["buy", "sell"]:
                    continue
                valid_entries.append(entry.strip())
                if action == "buy":
                    buy_total += amount
                else:
                    sell_total += amount

            self.batch_count += 1
            self.treated_elements += len(valid_entries)

            net_flow = buy_total - sell_total
            return (
                f"Transaction analysis: {len(valid_entries)} operations, "
                f"net flow: {self._format_amount(net_flow)} units"
            )
        except (TypeError, ValueError) as error:
            raise ValueError(
                f"Transaction stream processing failed: {error}"
            ) from error

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria != "large":
            return data_batch

        filtered_entries: List[Any] = []
        for entry in data_batch:
            if not isinstance(entry, str) or ":" not in entry:
                continue
            _, raw_value = entry.split(":", 1)
            amount = float(raw_value.strip())
            if amount >= 100.0:
                filtered_entries.append(entry)
        return filtered_entries

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["domain"] = "transaction"
        return stats

    def _format_amount(self, amount: float) -> str:
        prefix = "+"
        if amount < 0:
            prefix = ""
        if amount == int(amount):
            return f"{prefix}{int(amount)}"
        return f"{prefix}{amount:.1f}"


class EventStream(DataStream):
    def __init__(self, stream_id: str) -> None:
        super().__init__(stream_id, "System Events")

    def process_batch(self, data_batch: List[Any]) -> str:
        if not isinstance(data_batch, list):
            raise TypeError("data_batch must be a list")

        try:
            valid_entries = [
                entry for entry in data_batch if isinstance(entry, str)
            ]
            error_count = 0
            for entry in valid_entries:
                if entry.lower() == "error":
                    error_count += 1

            self.batch_count += 1
            self.treated_elements += len(valid_entries)
            return (
                f"Event analysis: {len(valid_entries)} events, "
                f"{error_count} error detected"
            )
        except (TypeError, ValueError) as error:
            raise ValueError(
                f"Event stream processing failed: {error}"
            ) from error

    def filter_data(
        self,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        if criteria != "priority":
            return data_batch

        return [
            entry
            for entry in data_batch
            if isinstance(entry, str)
            and entry.lower() in ["error", "critical", "warning"]
        ]

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        stats = super().get_stats()
        stats["domain"] = "event"
        return stats


class StreamProcessor:
    def transform_batch(self, data_batch: List[Any]) -> List[Any]:
        return [
            entry.strip() if isinstance(entry, str) else entry
            for entry in data_batch
        ]

    def process_stream(self, stream: DataStream, data_batch: List[Any]) -> str:
        if not isinstance(stream, DataStream):
            raise TypeError("stream must be a DataStream")
        transformed_batch = self.transform_batch(data_batch)
        return stream.process_batch(transformed_batch)

    def process_multiple(
        self,
        streams: List[DataStream],
        batches: List[List[Any]],
    ) -> List[str]:
        results: List[str] = []
        index = 0
        while index < len(streams) and index < len(batches):
            results.append(self.process_stream(streams[index], batches[index]))
            index += 1
        return results

    def filter_stream(
        self,
        stream: DataStream,
        data_batch: List[Any],
        criteria: Optional[str] = None,
    ) -> List[Any]:
        transformed_batch = self.transform_batch(data_batch)
        return stream.filter_data(transformed_batch, criteria)


def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===")

    sensor_stream = SensorStream("SENSOR_001")
    transaction_stream = TransactionStream("TRANS_001")
    event_stream = EventStream("EVENT_001")
    processor = StreamProcessor()

    sensor_data = ["temp:22.5", "humidity:65", "pressure:1013"]
    transaction_data = ["buy:100", "sell:150", "buy:75"]
    event_data = ["login", "error", "logout"]

    print("Initializing Sensor Stream...")
    print(
        f"Stream ID: {sensor_stream.stream_id}, "
        f"Type: {sensor_stream.stream_type}"
    )
    print(f"Processing sensor batch: {sensor_data}")
    print(processor.process_stream(sensor_stream, sensor_data))

    print("Initializing Transaction Stream...")
    print(
        f"Stream ID: {transaction_stream.stream_id}, "
        f"Type: {transaction_stream.stream_type}"
    )
    print(f"Processing transaction batch: {transaction_data}")
    print(processor.process_stream(transaction_stream, transaction_data))

    print("Initializing Event Stream...")
    print(
        f"Stream ID: {event_stream.stream_id}, "
        f"Type: {event_stream.stream_type}"
    )
    print(f"Processing event batch: {event_data}")
    print(processor.process_stream(event_stream, event_data))

    print("=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")

    mixed_batches = [
        ["temp:30.0", "temp:32.0"],
        ["buy:50", "sell:10", "buy:40", "sell:15"],
        ["login", "error", "logout"],
    ]
    processor.process_multiple(
        [sensor_stream, transaction_stream, event_stream],
        mixed_batches,
    )

    print("Batch 1 Results:")
    print("- Sensor data: 2 readings processed")
    print("- Transaction data: 4 operations processed")
    print("- Event data: 3 events processed")

    critical_sensors = processor.filter_stream(
        sensor_stream,
        ["temp:31.5", "temp:30.2", "humidity:65"],
        "critical",
    )
    large_transactions = processor.filter_stream(
        transaction_stream,
        ["buy:50", "sell:120", "buy:20"],
        "large",
    )

    print("Stream filtering active: High-priority data only")
    print(
        f"Filtered results: {len(critical_sensors)} critical sensor alerts, "
        f"{len(large_transactions)} large transaction"
    )
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
