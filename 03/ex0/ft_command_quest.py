import sys


def main():
    print("=== Command Quest ===")
    print(f"Programe name: {sys.argv[0]}")
    if len(sys.argv) <= 1:
        print("No arguments")
    else:
        print(f"Arguments passed: {len(sys.argv) - 1}")
        for i in range(1, len(sys.argv)):
            print(f"Argument {i}: {sys.argv[i]}")
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    main()
