def read_file():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print()
    file_to_open = "ancient_fragment.txt"
    print(f"Accessing Storage Vault: {file_to_open}")
    print()
    try:
        file = open(file_to_open, "r")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return
    print(file.read())
    file.close()
    print()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    read_file()
