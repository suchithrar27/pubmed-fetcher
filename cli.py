import argparse
from pubmed_fetcher import fetch_pubmed_papers, fetch_paper_details
from pubmed_fetcher import extract_email
from affiliation_filter import classify_affiliation
from save_results import save_to_csv

def main():
    parser = argparse.ArgumentParser(description="Fetch PubMed papers based on a query.")
    parser.add_argument("query", type=str, help="Search query for PubMed")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")
    parser.add_argument("-f", "--file", type=str, help="Filename to save results")

    args = parser.parse_args()
    pmids = fetch_pubmed_papers(args.query)

    if args.debug:
        print(f"Fetched {len(pmids)} papers.")

    records = fetch_paper_details(pmids)
    data = []

    for record in records["PubmedArticle"]:
        paper_info = {
            "PubmedID": record["MedlineCitation"]["PMID"],
            "Title": record["MedlineCitation"]["Article"]["ArticleTitle"],
            "Publication Date": record["MedlineCitation"]["Article"]["Journal"]["JournalIssue"]["PubDate"],
            "Non-academic Author(s)": [],
            "Company Affiliation(s)": [],
            "Corresponding Author Email": "",
        }

        authors = record["MedlineCitation"]["Article"].get("AuthorList", [])
        for author in authors:
            if "AffiliationInfo" in author:
                for affiliation in author["AffiliationInfo"]:
                    classification = classify_affiliation(affiliation["Affiliation"])
                    if classification == "company":
                        paper_info["Company Affiliation(s)"].append(affiliation["Affiliation"])
                        paper_info["Non-academic Author(s)"].append(author.get("LastName", "Unknown"))

            # Extract email if available
            if "AffiliationInfo" in author:
                for aff in author["AffiliationInfo"]:
                    email = extract_email(aff["Affiliation"])
                    if email:
                        paper_info["Corresponding Author Email"] = email

        data.append(paper_info)

    if args.file:
        save_to_csv(data, args.file)
    else:
        print(data)

if __name__ == "__main__":
    main()
