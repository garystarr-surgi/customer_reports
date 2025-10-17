frappe.ui.form.on('Customer', {
  refresh(frm) {
    if (frm.doc.__islocal) return;

    const html_field = frm.fields_dict['custom_purchase_report'];
    if (html_field) {
      html_field.$wrapper.html(`
        <button class="btn btn-primary btn-sm" id="view-purchase-report">
          View Purchase History Report
        </button>
      `);

      html_field.$wrapper.find('#view-purchase-report').on('click', () => {
        frappe.set_route('query-report', 'Customer Item Purchase History', {
          customer: frm.doc.name
        });
      });
    }
  }
});
