frappe.listview_settings['Request'] = {
    onload: function(listview) {

        frappe.call({
            method: 'frappe.client.get_value',
            args: {
                doctype: 'User',
                filters: { name: frappe.session.user },
                fieldname: ['department']
            },
            callback: (r) => {
                const userDepartment = r.message.department;
                console.log("User Department: " + userDepartment);
                let workflowState = 'Pending  Approval'; // Adjust as needed

                // Set the filter based on the user's department and workflow state
                frappe.route_options = {
                    
                    
                    "workflow_state": ["=", workflowState]
                    
                };
                console.log("---------------------------------------");



            }
        });


      
    },
    
};


