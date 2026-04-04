import sys
import site


def main():
    print()
    if sys.prefix == sys.base_prefix:
        print("MATRIX STATUS: You're still plugged in")
        print()
        print(f"Current Python: {sys.executable}")
        print(f"Current Python: {sys.prefix}")
        print("Virtual Environment: None detected")
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
        env_name = sys.prefix.rsplit("/", 1)
        print(f"Virtual Environment: {env_name[1]}")
        print(f"Environment Path: {sys.prefix}")
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system")
        print()
        paths = site.getsitepackages()
        install_path = paths[0]
        print("Package installation path:")
        print(install_path)


if __name__ == "__main__":
    main()
