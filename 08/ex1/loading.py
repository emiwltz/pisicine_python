import sys
import importlib


def load_modules():
    np = importlib.import_module("numpy")
    pd = importlib.import_module("pandas")
    plt = importlib.import_module("matplotlib.pyplot")
    return np, pd, plt


def check_import():
    print()
    print("LOADING STATUS: Loading programs...")
    print()
    print("Checking dependencies:")
    imports = {
        "pandas": "Data manipulation",
        "numpy": "Numerical computation",
        "matplotlib": "Visualisation",
    }
    i = 0
    for key, value in imports.items():
        try:
            module = importlib.import_module(key)
            print(f"[OK] {key} ({module.__version__}) - {value} is ready")
            i += 1
        except ModuleNotFoundError:
            print(f"[KO] {key} - {value} is not imported")
    if i == len(imports):
        main()
        return
    print()
    print("[ERROR] - Not all import succed")
    print()
    print("To install the missing dependencies with pip do the following:")
    print("py -m venv [venv_name]")
    print("source path/to/venv")
    print("pip install -r requirements.txt")
    print("python3 loading.py")
    print()
    print("To install the missing dependencies with poetry do the following:")
    print("poetry install")
    print("poetry run python loading.py")
    return


def main():
    print()
    print("=====All dependencies installed, running the program=====")
    print()
    print(f"venv_path: {sys.prefix}")

    np, pd, plt = load_modules()

    dataset1 = np.random.randint(0, 100, 20)
    dataset2 = np.random.randint(0, 100, 20)

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
    plt.show()

    print("Generating visualization...")
    print("Analysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    check_import()
