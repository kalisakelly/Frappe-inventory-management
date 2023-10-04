# Copyright (c) 2023, muganga SACCO and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class DeliveryNote(Document):
    
	def on_change(self):
		
     
		if self.workflow_state == 'Received':
			for item_requested in self.requested_item:
				item = frappe.get_doc('Item', item_requested.requested_item)
				available_quantity = item.get('quantity', 0)
				quantity_onhold = item.get('quantity_onhold', 0)
				requested_quantity = item_requested.requested_quantity
				new_available_quantity =available_quantity - requested_quantity
				new_quantity_onhold = quantity_onhold - requested_quantity
				
				item.all_requests=+requested_quantity
				item.quantity=new_available_quantity
				item.quantity_onhold = new_quantity_onhold
				item.save()
				frappe.db.commit()

			print('stock evaluated')
			
      
			
   
			
			
