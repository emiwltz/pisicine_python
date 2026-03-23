def read_file() -> None:
    file_to_open = "ancient_fragment.txt"

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {file_to_open}")
    try:
        file = open(file_to_open, "r", encoding="utf-8")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return
    print("Connection established...")
    print("RECOVERED DATA:")
    print(file.read())
    file.close()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    read_file()
