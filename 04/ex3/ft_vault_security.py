def main() -> None:
    extraction_file = "classified_data.txt"
    preservation_file = "security_protocols.txt"
    preservation_ready = False

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    try:
        with open(extraction_file, "r") as file:
            print("SECURE EXTRACTION:")
            print(file.read())
    except FileNotFoundError:
        print(f"SECURITY ALERT: Vault '{extraction_file}' not found")
    except PermissionError:
        print(f"SECURITY ALERT: Access denied to '{extraction_file}'")
    except Exception as error:
        print(f"SECURITY ALERT: Extraction anomaly detected: {error}")

    try:
        with open(preservation_file, "w") as file:
            file.write("[CLASSIFIED] New security protocols archived")
        preservation_ready = True
    except PermissionError:
        print(f"SECURITY ALERT: Access denied to '{preservation_file}'")
    except Exception as error:
        print(f"SECURITY ALERT: Preservation anomaly detected: {error}")

    if preservation_ready:
        try:
            with open(preservation_file, "r") as file:
                print("SECURE PRESERVATION:")
                print(file.read())
        except FileNotFoundError:
            print(f"SECURITY ALERT: Vault '{preservation_file}' not found")
        except PermissionError:
            print(f"SECURITY ALERT: Access denied to '{preservation_file}'")
        except Exception as error:
            print(
                "SECURITY ALERT: Preservation verification anomaly "
                f"detected: {error}"
            )
    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
