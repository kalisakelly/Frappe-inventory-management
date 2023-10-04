# Copyright (c) 2023, muganga SACCO and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class ItemsReception(Document):
    
    
    def on_submit(self):
        
        for item in self.items:
            
            Total_price=item.quantity*item.unit_price
            child=frappe.new_doc('Item')
            child.update(
            {
				
				"parent": self.name,
				"parenttype": child, 
				"parentfield": "items",
				"item_name": item.item_name,
				"quantity": item.quantity,
                "unit_price":item.unit_price,
                "total_value":Total_price,
				"description": item.description
				
			})
            
            child.save()
            print("successfully")
            
			
         
         

    
		
     
    
        
         
     
     
