def handle_archive_access(file_to_open: str) -> None:
    try:
        with open(file_to_open, "r", encoding="utf-8") as file:
            content = file.read()
        print(f"ROUTINE ACCESS: Attempting access to '{file_to_open}'...")
        print(f"SUCCESS: Archive recovered - ``{content}''")
        print("STATUS: Normal operations resumed")
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_to_open}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_to_open}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
    except Exception:
        print(f"CRISIS ALERT: Attempting access to '{file_to_open}'...")
        print("RESPONSE: Unexpected system anomaly detected")
        print("STATUS: Crisis handled, system stable")


def main() -> None:
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    handle_archive_access("lost_archive.txt")
    handle_archive_access("classified_vault.txt")
    handle_archive_access("standard_archive.txt")
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
