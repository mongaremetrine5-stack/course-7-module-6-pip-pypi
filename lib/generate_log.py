from datetime import datetime


def generate_log(log_data):
    """
    Generates a dated log file from a list of log entries.
    Returns the filename.
    """

    if not isinstance(log_data, list):
        raise ValueError("Input must be a list.")

    timestamp = datetime.now().strftime("%Y%m%d")
    filename = f"log_{timestamp}.txt"

    with open(filename, "w") as file:
        for entry in log_data:
            file.write(f"{entry}\n")

    return filename


if __name__ == "__main__":
    sample_data = [
        "User logged in",
        "User updated profile",
        "Report exported"
    ]

    print("Starting script...")
    created_file = generate_log(sample_data)
    print(f"Log successfully written to {created_file}")
    print("Script completed successfully.")