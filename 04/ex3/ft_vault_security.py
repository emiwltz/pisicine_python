def main() -> None:
    extraction_file = "classified_data.txt"
    preservation_file = "security_protocols.txt"

    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    with open(extraction_file, "r", encoding="utf-8") as file:
        print("SECURE EXTRACTION:")
        print(file.read())
    with open(preservation_file, "w", encoding="utf-8") as file:
        file.write("[CLASSIFIED] New security protocols archived")
    with open(preservation_file, "r", encoding="utf-8") as file:
        print("SECURE PRESERVATION:")
        print(file.read())
    print("Vault automatically sealed upon completion")
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
