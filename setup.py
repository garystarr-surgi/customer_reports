from setuptools import setup

setup(
    name='customer_reports',
    version='1.0.0',
    description='Custom reports and UI enhancements for customer purchase history',
    author='SurgiShop',
    author_email='gary.starr@surgishop.com',
    packages=["customer_reports"],
    package_dir={"customer_reports": "."},
    package_data={
        "customer_reports": [
            "*.json",
            "*.js",
            "*.css",
            "*.html",
            "*.md",
            "*.txt",
            "custom/**/*",
            "report/**/*",
            "client_script/**/*",
        ]
    },
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'frappe>=15.0.0'
    ]
)
