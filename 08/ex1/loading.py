import sys
import importlib


def load_modules() -> tuple:
    np = importlib.import_module("numpy")
    pd = importlib.import_module("pandas")
    plt = importlib.import_module("matplotlib.pyplot")
    return np, pd, plt


def show_dependency_check(imports: dict[str, str]) -> int:
    installed = 0
    for key, value in imports.items():
        try:
            module = importlib.import_module(key)
            version = getattr(module, "__version__", "unknown")
            print(f"[OK] {key} ({version}) - {value} ready")
            installed += 1
        except ModuleNotFoundError:
            print(f"[KO] {key} - {value} unavailable")
    return installed


def show_package_managers() -> None:
    print()
    print("Dependency management:")
    print("pip -> installs packages from requirements.txt")
    print("Poetry -> installs packages from pyproject.toml")


def check_import() -> None:
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    imports = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualization",
    }
    installed = show_dependency_check(imports)
    show_package_managers()
    if installed == len(imports):
        main()
        return
    print()
    print("[ERROR] - Not all imports succeeded")
    print()
    print("To install the missing dependencies with pip do the following:")
    print("py -m venv [venv_name]")
    print("source path/to/venv/bin/activate")
    print("pip install -r requirements.txt")
    print("python3 loading.py")
    print()
    print("To install the missing dependencies with poetry do the following:")
    print("poetry install")
    print("poetry run python loading.py")
    return


def main() -> None:
    print()
    print("=====All dependencies installed, running the program=====")
    print()
    print(f"venv_path: {sys.prefix}")

    np, pd, plt = load_modules()

    dataset1 = np.random.randint(0, 100, 1000)
    dataset2 = np.random.randint(0, 100, 1000)

    clean_data1 = pd.DataFrame({"data1": dataset1})
    clean_data2 = pd.DataFrame({"data2": dataset2})

    print()
    print("Analyzing Matrix data...")
    print(f"Processing {len(dataset1)} data points...")

    plt.figure(figsize=(8, 5))
    plt.plot(clean_data1["data1"], label="data1")
    plt.plot(clean_data2["data2"], label="data2")
    plt.title("Matrix Data Analysis")
    plt.xlabel("Index")
    plt.ylabel("Value")
    plt.legend()
    plt.tight_layout()
    print("Generating visualization...")
    plt.savefig("matrix_analysis.png")
    plt.close()
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    check_import()
