import os


def main():
    try:
        from dotenv import load_dotenv
    except ModuleNotFoundError as e:
        print(e)
        return
    print()
    print("ORACLE STATUS: Reading the Matrix...")
    print()

    load_dotenv()

    matrix_mode = os.getenv("MATRIX_MODE")
    database_url = os.getenv("DATABASE_URL")
    api_key = os.getenv("API_KEY")
    log_level = os.getenv("LOG_LEVEL")
    zion_endpoint = os.getenv("ZION_ENDPOINT")

    config = {
        "MATRIX_MODE": matrix_mode,
        "DATABASE_URL": database_url,
        "API_KEY": api_key,
        "LOG_LEVEL": log_level,
        "ZION_ENDPOINT": zion_endpoint,
    }

    missing = [key for key, value in config.items() if not value]

    print("Configuration loaded:")

    if matrix_mode == "development":
        print("Mode: development")
        print("Environment: Local training simulation")
    elif matrix_mode == "production":
        print("Mode: production")
        print("Environment: Production safeguards enabled")
    elif matrix_mode:
        print(f"Mode: invalid value ({matrix_mode})")
    else:
        print("Mode: missing configuration")

    if database_url:
        if database_url.startswith("sqlite:///"):
            print("Database: Local instance configured")
        else:
            print("Database: External instance configured")
    else:
        print("Database: Missing configuration")

    if api_key:
        print("API Access: Authenticated")
    else:
        print("API Access: Missing configuration")

    if log_level:
        print(f"Log Level: {log_level}")
    else:
        print("Log Level: Missing configuration")

    if zion_endpoint:
        print(f"Zion Network: Endpoint configured ({zion_endpoint})")
    else:
        print("Zion Network: Missing configuration")

    print()
    print("Environment security check:")

    if not missing:
        print("[OK] All required configuration variables are present")
    else:
        print(f"[KO] Missing variables: {', '.join(missing)}")

    if matrix_mode in ("development", "production"):
        print("[OK] Production overrides available")
    else:
        print("[KO] MATRIX_MODE must be 'development' or 'production'")


if __name__ == "__main__":
    main()
