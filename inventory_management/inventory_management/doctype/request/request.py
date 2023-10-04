# Copyright (c) 2023, muganga SACCO and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Request(Document):
    
    def autoname(doc):
    # Auto-fill the "Username" field with the current logged-in user
        if not doc.username:
            doc.username = frappe.session.user

        # Fetch the department of the user and set it in the "Department" field
        if not doc.department:
            user = frappe.get_doc("User", frappe.session.user)
            if user and user.department:
                doc.department = user.department

    
    def onload(doc):
        if not doc.username:
            doc.username = frappe.session.user

        if not doc.department:
            user = frappe.get_doc("User", frappe.session.user)
            if user and user.department:
                doc.department = user.department
            

    doc_events = {
        "Request": {
            "autoname": autoname,
            "onload": onload
        }
    }

    
    
    
    



    
    

##for saving a new request 
        
    def validate(doc):
        if doc.workflow_state == 'Pending DAF approval':
            child_documents_updated = False  # Initialize the flag

            try:
                for requested_item in doc.requested_item:
                    item = frappe.get_doc('Item', requested_item.requested_item)

                    if not item:
                        frappe.throw('Item not found.')
                        return

                    available_quantity = item.get('quantity', 0)
                    quantity_onhold = item.get('quantity_onhold', 0)
                    requested_quantity = requested_item.requested_quantity or 0

                    if requested_quantity > available_quantity:
                        frappe.throw('Stock Unavailable. Requested quantity is greater than available quantity.')

                    new_quantity_onhold = quantity_onhold + requested_quantity

                    if new_quantity_onhold > available_quantity:
                        frappe.throw('Stock Unavailable. Requested quantity is greater than available quantity.')
                        return
                    print(new_quantity_onhold)

                    item.quantity_onhold = new_quantity_onhold
                    item.save()

                    child_documents_updated = True

            except Exception as e:
                print("Error:", str(e))

    def on_submit(doc):
        if doc.workflow_state == 'Pending DAF approval':
            sequence_number = 1  # Initialize the sequence number
            child_documents_updated = False  # Initialize the flag

            for requested_item in doc.requested_item:
                try:
                    item = frappe.get_doc('Item', requested_item.requested_item)  # Retrieve the item inside the loop

                    child = frappe.new_doc("List of requests")

                    child.name = f"{doc.name}-Request{sequence_number}"
                    sequence_number += 1

                    child.update({ 
                        "parent": doc.name,
                        "parenttype": item, 
                        "parentfield": "list_of_requests",
                        "requestor_name": doc.username,
                        "request_item": requested_item.requested_item,
                        "requested_quantity": requested_item.requested_quantity,
                        "status": requested_item.status  # Set the correct status here
                    })

                    item.append("list_of_requests", child)
                    child.save()
                    
                    print ("Request")

                    child_documents_updated = True

                except Exception as e:
                    print("Error:", str(e))
        
        
    

    
        

        

                

    

    def on_change(self):
        if self.workflow_state == 'Approved':
            
            delivery_note = frappe.new_doc('Delivery Note')
            delivery_note.request_id = self.name
            delivery_note.requestor =self.username
            for requested_item in self.requested_item:
                table = delivery_note.append('requested_item', {})
                table.requested_item = requested_item.requested_item
                table.requested_quantity = requested_item.requested_quantity
              
            
            
            delivery_note.insert(ignore_permissions=True)
    
   

    
    
    
            