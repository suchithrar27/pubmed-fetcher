import pandas as pd

def save_to_csv(data: list, filename: str):
    """Save the list of paper details to a CSV file."""
    df = pd.DataFrame(data)
    df.to_csv(filename, index=False)
    print(f"Results saved to {filename}")
