def execute(filters=None):
    customer = filters.get("customer")
    item = filters.get("item")

    conditions = ""
    params = []

    if customer:
        conditions += " AND si.customer = %s"
        params.append(customer)
    if item:
        conditions += " AND sii.item_code = %s"
        params.append(item)

    data = frappe.db.sql(f"""
        SELECT
            si.customer AS customer,
            sii.item_code AS item,
            sii.qty AS quantity,
            sii.rate AS rate,
            sii.amount AS net_rate,
            si.posting_date AS date
        FROM `tabSales Invoice` si
        JOIN `tabSales Invoice Item` sii ON sii.parent = si.name
        WHERE si.docstatus = 1 {conditions}
        ORDER BY si.posting_date DESC
    """, tuple(params), as_dict=True)

    columns = [
        {"label": "Customer", "fieldname": "customer", "fieldtype": "Link", "options": "Customer"},
        {"label": "Item", "fieldname": "item", "fieldtype": "Link", "options": "Item"},
        {"label": "Quantity", "fieldname": "quantity", "fieldtype": "Float"},
        {"label": "Rate", "fieldname": "rate", "fieldtype": "Currency"},
        {"label": "Net Rate", "fieldname": "net_rate", "fieldtype": "Currency"},
        {"label": "Date", "fieldname": "date", "fieldtype": "Date"},
    ]

    return columns, data
