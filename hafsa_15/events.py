import frappe

def notify_new_book(doc, method):
    recipients = ["itx.ammarshahid123@gmail.com"] 
    subject = f"New Book Added: {doc.title}"
    message = (
        f"A new book has been added to the library:\n\n"
        f"Title: {doc.title}\nAuthor: {doc.author}\nISBN: {doc.isbn}"
    )

    frappe.sendmail(
        recipients=recipients,
        subject=subject,
        message=message
    )
