# about.py
import frappe

def get_context(context):
      context.about_seenu = frappe.db.sql(
        """
        SELECT 
           user,
           age,
           jpg
        FROM
           `tabdemo`
        WHERE
           age = 12.0   
        
        """,as_dict=1,
      )
      return context
