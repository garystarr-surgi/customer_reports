from setuptools import setup, find_packages

setup(
    name='customer_reports',
    version='1.0.0',
    description='Custom reports and UI enhancements for customer purchase history',
    author='SurgiShop',
    author_email='gary.starr@surgishop.com',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'frappe>=15.0.0'
    ]
)
