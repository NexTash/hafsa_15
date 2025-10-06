import frappe

@frappe.whitelist(allow_guest=True)
def issue_book(book, member):
    """
    Issue a Library Book to a Member
    """
    book_doc = frappe.get_doc("Library Book", book)
    if book_doc.status != "Available":
        frappe.throw(f"Book '{book_doc.title}' is not available for issuing. Current status: {book_doc.status}")

    issued_book = frappe.get_doc({
        "doctype": "Issued Book",
        "book": book,
        "member": member,
        "issue_date": frappe.utils.today()
    })
    issued_book.insert()
    book_doc.status = "Issued"
    book_doc.save()

    frappe.db.commit()

    return {
        "message": f"Book '{book_doc.title}' issued successfully to member {member}",
        "issued_id": issued_book.name,
        "book_status": book_doc.status
    }

@frappe.whitelist()
def get_books_by_author(author):
    return frappe.get_all("Library Book", filters={"author": author}, fields=["title", "isbn"])