import sys


def main():
    print("=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===")
    print()
    archivist_id = input("Input Stream active. Enter archivist ID: ")
    archivist_status = input("Input Stream active. Enter status report: ")
    print()
    print(f"[STANDARD] Archive status from {archivist_id}: {archivist_status}")
    print("[ALERT] System diagnostic: Communication channels verified", file=sys.stderr)
    print("[STANDARD] Data transmission complete", file=sys.stdout)
    print()
    print("Three-channel communication test successful.")


if __name__ == "__main__":
    main()
