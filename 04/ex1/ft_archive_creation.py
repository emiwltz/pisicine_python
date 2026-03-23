def main() -> None:
    file_to_create = "new_discovery.txt"
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {file_to_create}")
    file = open(file_to_create, "w", encoding="utf-8")
    print("Storage unit created successfully...")
    print("Inscribing preservation data...")
    for index, entry in enumerate(entries):
        print(entry)
        if index < len(entries) - 1:
            file.write(f"{entry}\n")
        else:
            file.write(entry)
    file.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file_to_create}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
