# about.py
import frappe

def get_context(context):
    # context.about_us_settings = frappe.db.get_list('demo')
    context.about_seenu1 = "seenu"
    return context
