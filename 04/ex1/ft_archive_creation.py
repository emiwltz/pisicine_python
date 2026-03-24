def main() -> None:
    file_to_create = "new_discovery.txt"
    file = None
    entries = [
        "[ENTRY 001] New quantum algorithm discovered",
        "[ENTRY 002] Efficiency increased by 347%",
        "[ENTRY 003] Archived by Data Archivist trainee",
    ]

    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print(f"Initializing new storage unit: {file_to_create}")
    try:
        file = open(file_to_create, "w")
        print("Storage unit created successfully...")
        print("Inscribing preservation data...")
        for entry in entries:
            print(entry)
        file.write(f"{entries[0]}\n")
        file.write(f"{entries[1]}\n")
        file.write(entries[2])
    except PermissionError:
        print("ERROR: Preservation access denied. Storage unit not sealed.")
        return
    except Exception as error:
        print(f"ERROR: Archive operation failed gracefully: {error}")
        return
    finally:
        if file is not None:
            file.close()
    print("Data inscription complete. Storage unit sealed.")
    print(f"Archive '{file_to_create}' ready for long-term preservation.")


if __name__ == "__main__":
    main()
