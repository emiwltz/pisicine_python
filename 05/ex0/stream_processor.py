from abc import ABC, abstractmethod
from typing import Any, Dict, List, Optional, Union

DisplayValue = Union[List[Any], str]


class DataProcessor(ABC):
    def __init__(self) -> None:
        super().__init__()

    @abstractmethod
    def process(self, data: Any) -> str:
        """Process the data and return the result string."""

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Validate whether the data fits the processor."""

    def format_output(self, result: str) -> str:
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            if len(data) == 0:
                return False
            for value in data:
                if value is True or value is False:
                    return False
                float(value)
        except (TypeError, ValueError):
            return False
        return True

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid numeric data")

        try:
            numbers: List[float] = [float(value) for value in data]
            total = sum(numbers)
            average = total / len(numbers)
            return (
                f"Processed {len(numbers)} numeric values, "
                f"sum={total:g}, avg={average:.1f}"
            )
        except (TypeError, ValueError) as error:
            raise ValueError(f"Numeric processing failed: {error}") from error


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        try:
            return data.strip() != ""
        except AttributeError:
            return False

    def process(self, data: Any) -> str:
        if not self.validate(data):
            raise ValueError("Invalid text data")

        text = data.strip()
        char_count = len(text)
        word_count = len(text.split())
        return f"Processed text: {char_count} characters, {word_count} words"


class LogProcessor(DataProcessor):
    VALID_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR"]

    def __init__(self) -> None:
        super().__init__()

    def validate(self, data: Any) -> bool:
        return self._extract_log_parts(data) is not None

    def process(self, data: Any) -> str:
        log_parts = self._extract_log_parts(data)
        if log_parts is None:
            raise ValueError("Invalid log data")

        level = log_parts[0]
        message = log_parts[1]
        prefix = f"[{level}]"
        if level == "ERROR":
            prefix = "[ALERT]"
        return f"{prefix} {level} level detected: {message}"

    def _extract_log_parts(self, data: Any) -> Optional[List[str]]:
        try:
            level, message = data.split(":", 1)
        except (AttributeError, ValueError):
            return None

        clean_level = level.strip()
        clean_message = message.strip()
        if clean_level not in self.VALID_LEVELS:
            return None
        if clean_message == "":
            return None
        return [clean_level, clean_message]


def _format_display_value(data: DisplayValue) -> str:
    try:
        return '"' + data + '"'
    except TypeError:
        return f"{data}"


def _run_demo(
    processor: DataProcessor,
    data: DisplayValue,
    settings: Dict[str, str],
) -> None:
    print(f"Initializing {settings['name']}...")
    print(f"Processing data: {_format_display_value(data)}")
    try:
        result = processor.process(data)
        print(f"Validation: {settings['validation']}")
        print(processor.format_output(result))
    except ValueError as error:
        print(f"Error: {error}")
    print()


def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    processors: List[DataProcessor] = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor(),
    ]
    examples: List[DisplayValue] = [
        [1, 2, 3, 4, 5],
        "Hello Nexus World",
        "ERROR: Connection timeout",
    ]
    settings: List[Dict[str, str]] = [
        {
            "name": "Numeric Processor",
            "validation": "Numeric data verified",
        },
        {
            "name": "Text Processor",
            "validation": "Text data verified",
        },
        {
            "name": "Log Processor",
            "validation": "Log entry verified",
        },
    ]

    index = 0
    while index < len(processors):
        _run_demo(processors[index], examples[index], settings[index])
        index += 1

    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")

    demo_data: List[DisplayValue] = [
        [1, 2, 3],
        "Hello Matrix",
        "INFO: System ready",
    ]

    for index, processor in enumerate(processors, start=1):
        result = processor.process(demo_data[index - 1])
        print(f"Result {index}: {result}")

    print("Foundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
