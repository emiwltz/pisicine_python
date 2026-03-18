
def open_file(file_to_open: str):
    try:
        with open(file_to_open) as file:
            contenue = file.read()
            print(f"ROUTINE ACCESS: Attempting access to '{file_to_open}'...")
            print(f"SUCCESS: Archive recovered - ``{contenue}''")
            print("STATUS: Normal operations resumed")
            print()
    except FileNotFoundError:
        print(f"CRISIS ALERT: Attempting access to '{file_to_open}'...")
        print("RESPONSE: Archive not found in storage matrix")
        print("STATUS: Crisis handled, system stable")
        print()
    except PermissionError:
        print(f"CRISIS ALERT: Attempting access to '{file_to_open}'...")
        print("RESPONSE: Security protocols deny access")
        print("STATUS: Crisis handled, security maintained")
        print()
    except Exception:
        print(f"CRISIS ALERT: Attempting access to '{file_to_open}'...")
        print("Sommething happened")
        print("STATUS: Crisis handled, system stable")
        print()


def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    print()
    f1 = "lost_archive.txt"
    f2 = "classified_vault.txt"
    f3 = "standard_archive.txt"
    open_file(f1)
    open_file(f2)
    open_file(f3)
    print("All crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
