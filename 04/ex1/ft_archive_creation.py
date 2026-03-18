def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    print()
    file_to_create = "new_discovery.txt"
    print(f"Initializing new storage unit: {file_to_create}")
    file = open(file_to_create, "w")
    print("Storage unit created successfully...")
    print()
    file.write("[ENTRY 001] New quantum algorithm discovered\n")
    file.write("[ENTRY 002] Efficiency increased by 347%\n")
    file.write("[ENTRY 003] Archived by Data Archivist trainee")
    print("Data inscription complete. Storage unit sealed")
    print(f"Archive '{file_to_create}' ready for long-term preservation.")
    file.close()
    print()
    print("Reading file...")
    file_to_read = open(file_to_create, "r")
    print(file_to_read.read())
    file_to_read.close()


if __name__ == "__main__":
    main()
