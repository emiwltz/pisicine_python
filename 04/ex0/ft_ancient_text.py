def read_file() -> None:
    file_to_open = "ancient_fragment.txt"
    file = None

    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===")
    print(f"Accessing Storage Vault: {file_to_open}")
    try:
        file = open(file_to_open, "r")
        print("Connection established...")
        print("RECOVERED DATA:")
        print(file.read())
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")
        return
    except PermissionError:
        print("ERROR: Access denied to storage vault.")
        return
    except Exception as error:
        print(f"ERROR: Unexpected archive anomaly detected: {error}")
        return
    finally:
        if file is not None:
            file.close()
    print("Data recovery complete. Storage unit disconnected.")


if __name__ == "__main__":
    read_file()
