import os
import sys
import site


def get_package_path(prefix: str) -> str:
    paths = site.getsitepackages([prefix])
    if not paths:
        return "Unavailable"
    return paths[0]


def main() -> None:
    print()
    global_path = get_package_path(sys.base_prefix)
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Global Environment: {sys.prefix}")
        print("Virtual Environment: None detected")
        print("Global package installation path:")
        print(global_path)
        print()
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print()

        print(
            "To enter the construct, run: \n"
            "python -m venv matrix_env\n"
            "source matrix_env/bin/activate # On Unix\n"
            "matrix_env\\Scripts\\activate  # On Windows"
        )
        print()
        print("Then run this program again.")
    else:
        print("MATRIX STATUS: Welcome to the construct")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {os.path.basename(sys.prefix)}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print()
        print("Global package installation path:")
        print(global_path)
        print("Virtual environment package installation path:")
        print(get_package_path(sys.prefix))


if __name__ == "__main__":
    main()
