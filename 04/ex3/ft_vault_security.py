def main():
    f1 = "classified_data.txt"
    f2 = "security_protocols.txt"
    print("=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===")
    print()
    print("Initiating secure vault access...")
    print("Vault connection established with failsafe protocols")
    print()
    with open(f1, "r") as file:
        contenu = file.read()
        print("SECURE EXTRACTION:")
        print(contenu)

    print()

    with open(f2, "w") as file:
        file.write("[CLASSIFIED] New security protocols archived")

    with open(f2, "r") as file:
        print("SECURE PRESERVATION:")
        contenu = file.read()
        print(contenu)

    print("Vault automatically sealed upon completion")
    print()
    print("All vault operations completed with maximum security.")


if __name__ == "__main__":
    main()
