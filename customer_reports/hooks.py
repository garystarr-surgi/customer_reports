app_version = "0.0.1"

app_name = "customer_reports"
app_title = "Customer Reports"
app_publisher = "SurgiShop"
app_description = "Custom reports and UI enhancements for customer purchase history"
app_email = "gary.starr@surgishop.com"
app_license = "MIT"

# Includes in fixtures
fixtures = [
    "Custom Field",
    "Client Script",
    "Report"
]

# Desktop module registration
app_include_js = "/assets/customer_reports/js/customer_item_purchase_history.js"

# Optional: register your module in the desktop
app_icon = "octicon octicon-graph"
app_color = "#589494"
app_module = "Customer Reports"

# Optional: if you use patches
# patches = [
#     "customer_reports.patches.patch_customer_report_setup"
# ]
