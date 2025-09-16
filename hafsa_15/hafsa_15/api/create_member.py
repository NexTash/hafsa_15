import frappe

@frappe.whitelist(allow_guest=True)
def create_member(full_name, gmail, library_card_number, phone_number=None):
    """
    API to create a new Library Member
    """
    # Check if member already exists by card number or gmail
    if frappe.db.exists("Library Member", {"library_card_number": library_card_number}):
        frappe.throw(f"Library Member with card {library_card_number} already exists")
    
    if frappe.db.exists("Library Member", {"email": email}):
        frappe.throw(f"Library Member with email {email} already exists")

    member = frappe.get_doc({
        "doctype": "Library Member",
        "full_name": full_name,
        "email": gmail,
        "library_card_number": library_card_number,
        "phone": phone_number
    })

    member.insert()
    frappe.db.commit()

    return {
        "message": "Library Member created successfully",
        "member_id": member.name
    }
