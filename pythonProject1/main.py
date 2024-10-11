import sys
from backend.core import run_llm
from ingestion import ingest_docs

def main():
    print("Documentation Assistant Main Menu")
    print("1: Ingest Documents")
    print("2: Query the System")
    choice = input("Enter your choice (1-2): ")

    if choice == '1':
        path = input("Please enter the directory path to the HTML files: ")
        print("Ingesting documents from:", path)
        ingest_docs(path)
        print("Ingestion complete.")

    elif choice == '2':
        while True:
            query = input("Enter your query (or type 'exit' to return to the main menu): ")
            if query.lower() == 'exit':  # Allows the user to exit the query loop
                break
            response = run_llm(query)
            print("Query results:")
            print(response)

    else:
        print("Invalid choice. Exiting.")
        sys.exit(1)

if __name__ == "__main__":
    main()
