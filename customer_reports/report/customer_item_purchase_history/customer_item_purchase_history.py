import frappe

def execute(filters=None):
    columns = [
        {
            "fieldname": "posting_date",
            "label": "Date",
            "fieldtype": "Date",
            "width": 100
        },
        {
            "fieldname": "invoice",
            "label": "Invoice",
            "fieldtype": "Link",
            "options": "Sales Invoice",
            "width": 150
        },
        {
            "fieldname": "item_code",
            "label": "Item Code",
            "fieldtype": "Link",
            "options": "Item",
            "width": 150
        },
        {
            "fieldname": "item_name",
            "label": "Item Name",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "fieldname": "qty",
            "label": "Quantity",
            "fieldtype": "Float",
            "width": 100
        },
        {
            "fieldname": "rate",
            "label": "Rate",
            "fieldtype": "Currency",
            "width": 120
        },
        {
            "fieldname": "amount",
            "label": "Amount",
            "fieldtype": "Currency",
            "width": 120
        }
    ]
    
    return columns, get_data(filters)

def get_data(filters):
    conditions = "si.docstatus = 1"
    
    if filters.get("customer"):
        conditions += f" AND si.customer = '{filters.get('customer')}'"
    
    if filters.get("item_code"):
        conditions += f" AND sii.item_code = '{filters.get('item_code')}'"
    
    if filters.get("from_date"):
        conditions += f" AND si.posting_date >= '{filters.get('from_date')}'"
    
    if filters.get("to_date"):
        conditions += f" AND si.posting_date <= '{filters.get('to_date')}'"
    
    data = frappe.db.sql(f"""
        SELECT 
            si.posting_date,
            si.name as invoice,
            sii.item_code,
            sii.item_name,
            sii.qty,
            sii.rate,
            sii.amount
        FROM `tabSales Invoice` si
        INNER JOIN `tabSales Invoice Item` sii ON si.name = sii.parent
        WHERE {conditions}
        ORDER BY si.posting_date DESC
    """, as_dict=1)
    
    return data
