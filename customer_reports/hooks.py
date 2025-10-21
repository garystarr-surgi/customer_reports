app_version = "0.0.1"
app_name = "customer_reports"
app_title = "Customer Reports"
app_publisher = "SurgiShop"
app_description = "Custom reports and UI enhancements for customer purchase history"
app_email = "gary.starr@surgishop.com"
app_license = "MIT"

# Includes in fixtures
fixtures = [
    {
        "dt": "Report",
        "filters": [
            ["name", "in", ["Customer Item Purchase History"]]
        ]
    },
    {
        "dt": "Custom Field",
        "filters": [
            ["dt", "=", "Customer"],
            ["fieldname", "like", "customer_reports%"]
        ]
    },
    {
        "dt": "Client Script",
        "filters": [
            ["dt", "=", "Customer"],
            ["name", "like", "%customer_reports%"]
        ]
    }
]

# Include JS files
# app_include_js = "/assets/customer_reports/js/customer_reports.bundle.js"

# Include CSS files
# app_include_css = "/assets/customer_reports/css/customer_reports.css"

# Optional: register your module in the desktop
app_icon = "octicon octicon-graph"
app_color = "#589494"

# Module registration
# This makes your app appear in the modules list
app_include_js = [
   "/assets/customer_reports/js/customer_reports.min.js"
]

# Doctype JS (optional - if you want to override Customer form)
# doctype_js = {
#     "Customer": "public/js/customer.js"
# }

# Boot session info (optional)
# boot_session = "customer_reports.boot.boot_session"

# Scheduled Tasks (optional)
# scheduler_events = {
#     "daily": [
#         "customer_reports.tasks.daily"
#     ]
# }

# Optional: if you use patches
# patches = [
#     "customer_reports.patches.v0_0.setup_customer_reports"
# ]
