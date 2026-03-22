from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):
    def __init__(self, processor_name: str) -> None:
        self.processor_name = processor_name

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return a formatted result string."""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate whether the data is appropriate for this processor."""

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Numeric Processor")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, list) or len(data) == 0:
            return False
        return all(isinstance(value, (int, float)) and not isinstance(value, bool)
                   for value in data)

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        try:
            numbers: List[float] = [float(value) for value in data]
            total = sum(numbers)
            average = total / len(numbers)
            result = (
                f"Processed {len(numbers)} numeric values, "
                f"sum={total:g}, avg={average}"
            )
            return self.format_output(result)
        except (TypeError, ValueError) as error:
            raise ValueError(f"Numeric processing failed: {error}") from error


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__("Text Processor")

    def validate(self, data: Any) -> bool:
        return isinstance(data, str) and data.strip() != ""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")

        try:
            text = data.strip()
            char_count = len(text)
            word_count = len(text.split())
            result = (
                f"Processed text: {char_count} characters, "
                f"{word_count} words"
            )
            return self.format_output(result)
        except (AttributeError, TypeError) as error:
            raise ValueError(f"Text processing failed: {error}") from error


class LogProcessor(DataProcessor):
    VALID_LEVELS = {"DEBUG", "INFO", "WARNING", "ERROR"}

    def __init__(self) -> None:
        super().__init__("Log Processor")

    def validate(self, data: Any) -> bool:
        if not isinstance(data, str) or ":" not in data:
            return False

        level, message = data.split(":", 1)
        return level.strip() in self.VALID_LEVELS and message.strip() != ""

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid log data")

        try:
            level, message = data.split(":", 1)
            clean_level = level.strip()
            clean_message = message.strip()

            if clean_level == "ERROR":
                result = f"[ALERT] {
                    clean_level} level detected: {clean_message}"
            elif clean_level == "WARNING":
                result = f"[WARNING] {clean_message}"
            elif clean_level == "INFO":
                result = f"[INFO] {clean_message}"
            else:
                result = f"[DEBUG] {clean_message}"

            return self.format_output(result)
        except (AttributeError, ValueError) as error:
            raise ValueError(f"Log processing failed: {error}") from error


def run_processor(processor: DataProcessor, data: Any) -> None:
    print(f"Initializing {processor.processor_name}...")
    print(f"Processing data: {data!r}")

    try:
        if processor.validate(data):
            print("Validation: Data verified")
            print(processor.process(data))
        else:
            print("Validation: Invalid data")
    except ValueError as error:
        print(f"Error: {error}")

    print()


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    numeric_processor = NumericProcessor()
    text_processor = TextProcessor()
    log_processor = LogProcessor()

    run_processor(numeric_processor, [1, 2, 3, 4, 5])
    run_processor(text_processor, "Hello Nexus World")
    run_processor(log_processor, "ERROR: Connection timeout")

    print("=== Polymorphic Processing Demo ===")

    processors_and_data: list[tuple[DataProcessor, Any]] = [
        (numeric_processor, [10, 20, 30]),
        (text_processor, "Polymorphism is powerful"),
        (log_processor, "WARNING: Disk space is low"),
    ]

    for processor, data in processors_and_data:
        try:
            print(f"{processor.processor_name}: {processor.process(data)}")
        except ValueError as error:
            print(f"{processor.processor_name}: Error - {error}")


if __name__ == "__main__":
    main()
