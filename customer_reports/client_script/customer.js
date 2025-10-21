frappe.ui.form.on('Customer', {
    refresh: function(frm) {
        if (!frm.is_new()) {
            // Add a custom button in the "Reports" group
            frm.add_custom_button(__('Purchase History'), function() {
                frappe.set_route('query-report', 'Customer Item Purchase History', {
                    customer: frm.doc.name
                });
            }, __('Reports'));
        }
    }
});
