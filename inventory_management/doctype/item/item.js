// Copyright (c) 2023, muganga SACCO and contributors
// For license information, please see license.txt

frappe.ui.form.on("Item", {
	refresh(frm) {

        console.log('>>>>> I refreshed Send Notiication')
        // didier()

	},
    validate(frm){
        console.log(frm)
        if(frm.doc.asset_type !== 'victor'){
            alert("You Weeee")
        }
    },

    didier() {
        console.log("DIDID")
    }
});
