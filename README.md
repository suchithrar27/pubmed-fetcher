# PubMed Fetcher

This project fetches research papers from PubMed based on a given query. It identifies papers with at least one author affiliated with a pharmaceutical/biotech company and extracts relevant details, saving the results in a CSV file.

## Project Structure

```
pubmed_fetcher/
│── pubmed_fetcher.py       # Fetches papers from PubMed
│── affiliation_filter.py   # Defines heuristics for filtering affiliations
│── save_results.py         # Saves results to a CSV file
│── cli.py                  # Command-line interface
│── README.md               # Documentation
│── pyproject.toml          # Poetry configuration
│── .venv/                  # Virtual environment (if using Poetry)
```

## Installation

### Prerequisites
1. Python 3.10+
2. Poetry (for dependency management)

### Steps to Install

1. **Clone the Repository:**
   ```sh
   git clone <repository_url> 
   cd pubmed_fetcher
   ```

2. **Install Poetry (if not installed):**
   ```sh
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install Dependencies:**
   ```sh
   poetry install
   ```

## Usage

### Running the CLI
To fetch research papers, use:
```sh
poetry run get-papers-list "cancer treatment" -d -f results.csv
```

1. Replace `"cancer treatment"` with your desired query.
2. `-d` enables detailed output.
3. `-f results.csv` specifies the output file.

## Tools & Libraries Used

1. [BioPython](https://biopython.org/) - For fetching data from PubMed.
2. [pandas](https://pandas.pydata.org/) - For data processing and storage.
3. [requests](https://docs.python-requests.org/en/master/) - For making HTTP requests.
4. [Poetry](https://python-poetry.org/) - Dependency management and packaging.

## Notes

1. Ensure you have an active internet connection when running the script.
2. Modify `pubmed_fetcher.py` to adjust the number of papers fetched (`retmax`).
