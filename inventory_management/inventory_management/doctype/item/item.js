// Copyright (c) 2023, muganga SACCO and contributors
// For license information, please see license.txt

// frappe.ui.form.on('Item', {
//     refresh: function(frm) {
//         // Fetch requested items data and update the requested_items table
//         frappe.call({
//             method: 'inventory_management.item_methods.fetch_requested_items',  // Replace with actual method path
//             args: {
//                 item_name: frm.doc.item_name  // Pass the item name
//             },
//             callback: function(response) {
//                 if (response.message) {
//                     frm.doc.requested_items = response.message;
//                     frm.refresh_field('requested_items');
//                 }
//             }
//         });
//     }
// });
