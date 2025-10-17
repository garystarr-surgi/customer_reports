frappe.query_reports["Customer Item Purchase History"] = {
  filters: [
    {
      fieldname: "customer",
      label: __("Customer"),
      fieldtype: "Link",
      options: "Customer",
      reqd: 1
    },
    {
      fieldname: "item",
      label: __("Item"),
      fieldtype: "Link",
      options: "Item"
    }
  ]
};
