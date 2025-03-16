from Bio import Entrez
import re

Entrez.email = "suchitrar678@gmail.com"  # Required for PubMed API requests

def fetch_pubmed_papers(query: str, max_results: int = 10):
    """Fetches papers from PubMed using a search query."""
    handle = Entrez.esearch(db="pubmed", term=query, retmax=100, retmode="xml")

   # handle = Entrez.esearch(db="pubmed", term=query, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()

    pmids = record["IdList"]
    return pmids

def fetch_paper_details(pmids: list):
    """Fetches detailed metadata for given PubMed IDs."""
    handle = Entrez.efetch(db="pubmed", id=",".join(pmids), retmode="xml")
    records = Entrez.read(handle)
    handle.close()
    return records

def extract_email(text: str) -> str:
    """Extracts an email address from a given text."""
    email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    match = re.search(email_pattern, text)
    return match.group(0) if match else None
