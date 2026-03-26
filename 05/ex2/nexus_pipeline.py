from abc import ABC, abstractmethod
from collections import deque
from typing import Any, Deque, Dict, List, Optional, Protocol, Union


class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        """Process one stage of the pipeline."""


class InputStage:
    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            raise TypeError("Pipeline input must be a dictionary")

        if "payload" not in data:
            raise ValueError("Missing payload for pipeline processing")

        payload = data["payload"]
        if payload is None:
            raise ValueError("Payload cannot be empty")
        if isinstance(payload, list) and len(payload) == 0:
            raise ValueError("Payload cannot be empty")

        validated_data: Dict[str, Any] = {
            key: value for key, value in data.items()
        }
        validated_data["validated"] = True
        if "record_count" not in validated_data:
            validated_data["record_count"] = self._count_records(payload)
        return validated_data

    def _count_records(self, payload: Any) -> int:
        if isinstance(payload, list):
            return len(payload)
        return 1


class TransformStage:
    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            raise TypeError("Transform stage expects a dictionary")

        if data.get("force_transform_error"):
            raise ValueError("Invalid data format")

        transformed_data: Dict[str, Any] = {
            key: value for key, value in data.items()
        }
        transformed_data["metadata"] = {
            "pipeline_id": transformed_data.get("pipeline_id", "UNKNOWN"),
            "adapter": transformed_data.get("adapter_type", "unknown"),
            "validated": transformed_data.get("validated", False),
        }
        transformed_data["summary"] = self._build_summary(transformed_data)
        return transformed_data

    def _build_summary(self, data: Dict[str, Any]) -> str:
        data_kind = data.get("data_kind")
        if data_kind == "json":
            return self._build_json_summary(data)
        if data_kind == "csv":
            return self._build_csv_summary(data)
        return self._build_stream_summary(data)

    def _build_json_summary(self, data: Dict[str, Any]) -> str:
        payload = data.get("payload", {})
        if not isinstance(payload, dict):
            raise TypeError("JSON payload must be a dictionary")

        sensor = str(payload.get("sensor", "data"))
        value = payload.get("value")
        unit = str(payload.get("unit", ""))

        if isinstance(value, (int, float)):
            if sensor in ["temp", "temperature"]:
                label = "temperature"
            else:
                label = sensor
            status = "Normal range"
            if sensor in ["temp", "temperature"] and (
                float(value) < 18.0 or float(value) > 28.0
            ):
                status = "Alert range"
            return f"Processed {label} reading: {value}{unit} ({status})"

        return "JSON payload processed: metadata normalized"

    def _build_csv_summary(self, data: Dict[str, Any]) -> str:
        record_count = int(data.get("record_count", 1))
        return f"User activity logged: {record_count} actions processed"

    def _build_stream_summary(self, data: Dict[str, Any]) -> str:
        payload = data.get("payload", [])
        numeric_values = data.get("numeric_values", [])
        if not isinstance(payload, list):
            raise TypeError("Stream payload must be a list")

        if isinstance(numeric_values, list) and numeric_values:
            average = sum(numeric_values) / len(numeric_values)
            return (
                f"Stream summary: {len(payload)} readings, "
                f"avg: {average:.1f}°C"
            )
        return f"Stream summary: {len(payload)} events processed"


class OutputStage:
    def process(self, data: Any) -> Any:
        if not isinstance(data, dict):
            raise TypeError("Output stage expects a dictionary")

        summary = data.get("summary")
        if not isinstance(summary, str) or summary == "":
            raise ValueError("Missing summary for output stage")

        output_data: Dict[str, Any] = {
            key: value for key, value in data.items()
        }
        output_data["output"] = summary
        return output_data


class ProcessingPipeline(ABC):
    def __init__(
        self,
        pipeline_id: str,
        pipeline_type: str,
        stages: Optional[List[ProcessingStage]] = None,
    ) -> None:
        self.pipeline_id = pipeline_id
        self.pipeline_type = pipeline_type
        if stages is None:
            self.stages: List[ProcessingStage] = [
                InputStage(),
                TransformStage(),
                OutputStage(),
            ]
        else:
            self.stages = stages
        self.processed_count = 0
        self.success_count = 0
        self.failure_count = 0
        self.recovery_count = 0
        self.last_output = "No processing yet"
        self.error_history: Deque[str] = deque(maxlen=5)

    @abstractmethod
    def process(self, data: Any) -> Union[str, Any]:
        """Process data through the adapter."""

    def _execute_pipeline(self, data: Dict[str, Any]) -> str:
        current_data: Any = data
        for stage in self.stages:
            current_data = stage.process(current_data)

        if not isinstance(current_data, dict):
            raise TypeError("Pipeline stages must return a dictionary")

        output = current_data.get("output")
        if not isinstance(output, str):
            raise ValueError("Pipeline output is invalid")

        self.processed_count += 1
        self.success_count += 1
        self.last_output = output
        return output

    def _recover_from_error(self, error: Exception) -> str:
        self.processed_count += 1
        self.failure_count += 1
        self.recovery_count += 1
        self.error_history.append(str(error))
        self.last_output = (
            "Recovery successful: Pipeline restored, processing resumed"
        )
        return self.last_output

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        efficiency = 0.0
        if self.processed_count > 0:
            efficiency = (
                self.success_count / self.processed_count
            ) * 100

        return {
            "pipeline_id": self.pipeline_id,
            "pipeline_type": self.pipeline_type,
            "processed_count": self.processed_count,
            "success_count": self.success_count,
            "failure_count": self.failure_count,
            "recovery_count": self.recovery_count,
            "efficiency": round(efficiency, 1),
        }


class JSONAdapter(ProcessingPipeline):
    def __init__(
        self,
        pipeline_id: str,
        stages: Optional[List[ProcessingStage]] = None,
    ) -> None:
        super().__init__(pipeline_id, "json", stages)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            normalized_data = self._normalize_json_input(data)
            return self._execute_pipeline(normalized_data)
        except (TypeError, ValueError) as error:
            return self._recover_from_error(error)

    def _normalize_json_input(self, data: Any) -> Dict[str, Any]:
        if isinstance(data, dict):
            payload = {key: value for key, value in data.items()}
        elif isinstance(data, str):
            payload = self._parse_json_object(data)
        else:
            raise TypeError("JSONAdapter expects a dict or JSON object string")

        return {
            "pipeline_id": self.pipeline_id,
            "adapter_type": self.pipeline_type,
            "data_kind": "json",
            "payload": payload,
            "record_count": int(payload.get("record_count", 1)),
            "force_transform_error": bool(
                payload.get("force_transform_error", False)
            ),
        }

    def _parse_json_object(self, data: str) -> Dict[str, Any]:
        cleaned = data.strip()
        if not cleaned.startswith("{") or not cleaned.endswith("}"):
            raise ValueError("JSON input must be a flat object string")

        content = cleaned[1:-1].strip()
        if content == "":
            return {}

        payload: Dict[str, Any] = {}
        parts = [
            part.strip() for part in content.split(",") if part.strip() != ""
        ]
        for part in parts:
            if ":" not in part:
                raise ValueError("Invalid JSON entry")
            key_text, value_text = part.split(":", 1)
            key = key_text.strip().strip('"')
            payload[key] = self._convert_value(value_text.strip())
        return payload

    def _convert_value(self, value: str) -> Any:
        cleaned = value.strip().strip('"')
        if cleaned.replace(".", "", 1).isdigit():
            if "." in cleaned:
                return float(cleaned)
            return int(cleaned)
        if cleaned.lower() == "true":
            return True
        if cleaned.lower() == "false":
            return False
        return cleaned


class CSVAdapter(ProcessingPipeline):
    def __init__(
        self,
        pipeline_id: str,
        stages: Optional[List[ProcessingStage]] = None,
    ) -> None:
        super().__init__(pipeline_id, "csv", stages)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            normalized_data = self._normalize_csv_input(data)
            return self._execute_pipeline(normalized_data)
        except (TypeError, ValueError) as error:
            return self._recover_from_error(error)

    def _normalize_csv_input(self, data: Any) -> Dict[str, Any]:
        rows: List[str]
        record_count = 1

        if isinstance(data, dict):
            rows = [str(data.get("chained_output", ""))]
            record_count = int(data.get("record_count", 1))
        elif isinstance(data, list):
            rows = [str(row).strip() for row in data if str(row).strip() != ""]
            record_count = len(rows)
        elif isinstance(data, str):
            cleaned = data.strip()
            if cleaned == "":
                raise ValueError("CSV input cannot be empty")
            rows = [
                row.strip() for row in cleaned.splitlines()
                if row.strip() != ""
            ]
            if not rows:
                rows = [cleaned]
            record_count = len(rows)
        else:
            raise TypeError("CSVAdapter expects a string, list, or dict")

        payload = [
            [
                column.strip()
                for column in row.split(",")
                if column.strip() != ""
            ]
            for row in rows
        ]
        if not payload:
            raise ValueError("CSV input cannot be empty")

        return {
            "pipeline_id": self.pipeline_id,
            "adapter_type": self.pipeline_type,
            "data_kind": "csv",
            "payload": payload,
            "record_count": record_count,
        }


class StreamAdapter(ProcessingPipeline):
    def __init__(
        self,
        pipeline_id: str,
        stages: Optional[List[ProcessingStage]] = None,
    ) -> None:
        super().__init__(pipeline_id, "stream", stages)

    def process(self, data: Any) -> Union[str, Any]:
        try:
            normalized_data = self._normalize_stream_input(data)
            return self._execute_pipeline(normalized_data)
        except (TypeError, ValueError) as error:
            return self._recover_from_error(error)

    def _normalize_stream_input(self, data: Any) -> Dict[str, Any]:
        payload: List[Any]
        record_count = 1

        if isinstance(data, dict):
            payload = [data.get("chained_output", "")]
            record_count = int(data.get("record_count", 1))
        elif isinstance(data, list):
            payload = data
            record_count = len(payload)
        elif isinstance(data, str):
            cleaned = data.strip()
            if cleaned == "":
                raise ValueError("Stream input cannot be empty")
            payload = [cleaned]
        else:
            payload = [data]

        numeric_values = self._extract_numeric_values(payload)
        return {
            "pipeline_id": self.pipeline_id,
            "adapter_type": self.pipeline_type,
            "data_kind": "stream",
            "payload": payload,
            "numeric_values": numeric_values,
            "record_count": record_count,
        }

    def _extract_numeric_values(self, payload: List[Any]) -> List[float]:
        numeric_values: List[float] = []

        for entry in payload:
            if isinstance(entry, (int, float)) and not isinstance(entry, bool):
                numeric_values.append(float(entry))
                continue

            if isinstance(entry, str) and ":" in entry:
                _, raw_value = entry.split(":", 1)
                cleaned = raw_value.strip().replace("°C", "")
                if cleaned.replace(".", "", 1).isdigit():
                    numeric_values.append(float(cleaned))

        return numeric_values


class NexusManager:
    def __init__(self) -> None:
        self.pipelines: Dict[str, ProcessingPipeline] = {}
        self.execution_log: Deque[str] = deque(maxlen=10)

    def register_pipeline(self, pipeline: ProcessingPipeline) -> None:
        self.pipelines[pipeline.pipeline_id] = pipeline
        self.execution_log.append(f"Registered {pipeline.pipeline_id}")

    def process_with_pipeline(
        self,
        pipeline_id: str,
        data: Any,
    ) -> Union[str, Any]:
        pipeline = self.pipelines.get(pipeline_id)
        if pipeline is None:
            raise ValueError(f"Unknown pipeline: {pipeline_id}")

        result = pipeline.process(data)
        self.execution_log.append(f"{pipeline_id} processed data")
        return result

    def chain_pipelines(
        self,
        pipeline_ids: List[str],
        data: Any,
    ) -> str:
        record_count = self._count_records(data)
        current_data: Any = data

        for pipeline_id in pipeline_ids:
            result = self.process_with_pipeline(pipeline_id, current_data)
            current_data = {
                "chained_output": result,
                "record_count": record_count,
            }

        return (
            f"{record_count} records processed through "
            f"{len(pipeline_ids)}-stage pipeline"
        )

    def get_global_stats(self) -> Dict[str, Union[str, int, float]]:
        total_processed = sum(
            pipeline.processed_count for pipeline in self.pipelines.values()
        )
        total_failures = sum(
            pipeline.failure_count for pipeline in self.pipelines.values()
        )
        efficiency = 0.0
        if total_processed > 0:
            efficiency = (
                (total_processed - total_failures) / total_processed
            ) * 100

        return {
            "registered_pipelines": len(self.pipelines),
            "total_processed": total_processed,
            "total_failures": total_failures,
            "efficiency": round(efficiency, 1),
        }

    def _count_records(self, data: Any) -> int:
        if isinstance(data, list):
            return len(data)
        if isinstance(data, dict) and "record_count" in data:
            return int(data["record_count"])
        return 1


def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===")
    print("Initializing Nexus Manager...")
    manager = NexusManager()
    print("Pipeline capacity: 1000 streams/second")

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery")

    json_adapter = JSONAdapter("JSON_001")
    csv_adapter = CSVAdapter("CSV_001")
    stream_adapter = StreamAdapter("STREAM_001")

    manager.register_pipeline(json_adapter)
    manager.register_pipeline(csv_adapter)
    manager.register_pipeline(stream_adapter)

    print("=== Multi-Format Data Processing ===")
    json_input = '{"sensor": "temp", "value": 23.5, "unit": "°C"}'
    print("Processing JSON data through pipeline...")
    print(f"Input: {json_input}")
    print("Transform: Enriched with metadata and validation")
    print(f"Output: {manager.process_with_pipeline('JSON_001', json_input)}")

    csv_input = "user,action,timestamp"
    print("Processing CSV data through same pipeline...")
    print('Input: "user,action,timestamp"')
    print("Transform: Parsed and structured data")
    print(f"Output: {manager.process_with_pipeline('CSV_001', csv_input)}")

    stream_input = [
        "temp:21.8",
        "temp:22.0",
        "temp:22.2",
        "temp:22.4",
        "temp:22.1",
    ]
    print("Processing Stream data through same pipeline...")
    print("Input: Real-time sensor stream")
    print("Transform: Aggregated and filtered")
    print(
        f"Output: {manager.process_with_pipeline('STREAM_001', stream_input)}"
    )

    print("=== Pipeline Chaining Demo ===")
    print("Pipeline A -> Pipeline B -> Pipeline C")
    print("Data flow: Raw -> Processed -> Analyzed -> Stored")
    chain_result = manager.chain_pipelines(
        ["JSON_001", "CSV_001", "STREAM_001"],
        {"sensor": "temp", "value": 20.5, "unit": "°C", "record_count": 100},
    )
    print(f"Chain result: {chain_result}")

    stats = manager.get_global_stats()
    print(
        f"Performance: {stats['efficiency']}% efficiency, "
        f"{stats['total_processed']} total pipeline runs"
    )

    print("=== Error Recovery Test ===")
    print("Simulating pipeline failure...")
    print("Error detected in Stage 2: Invalid data format")
    print("Recovery initiated: Switching to backup processor")
    recovery_input = {
        "sensor": "temp",
        "value": 25.0,
        "unit": "°C",
        "force_transform_error": True,
    }
    print(manager.process_with_pipeline("JSON_001", recovery_input))
    print("Nexus Integration complete. All systems operational.")


if __name__ == "__main__":
    main()
