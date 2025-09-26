import frappe
import requests

@frappe.whitelist()
def fetch_books_from_openlibrary(query="python"):
    url = f"https://openlibrary.org/search.json?q={query}"
    response = requests.get(url)

    if response.status_code != 200:
        frappe.throw("Failed to fetch data from OpenLibrary")

    data = response.json()

    for book in data.get("docs", [])[:5]:  # limit to 5 results for testing
        title = book.get("title")
        author = ", ".join(book.get("author_name", [])) if book.get("author_name") else "Unknown"
        isbn = book.get("isbn")[0] if book.get("isbn") else None

        if not isbn:
            continue  # skip if ISBN missing

        if not frappe.db.exists("Library Book", {"isbn": isbn}):
            doc = frappe.get_doc({
                "doctype": "Library Book",
                "title": title,
                "author": author,
                "isbn": isbn,
                "status": "Available"
            })
            doc.insert()

    return "Books imported successfully"