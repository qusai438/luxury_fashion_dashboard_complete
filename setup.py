from setuptools import setup, find_packages

setup(
    name="luxury_fashion_dashboard",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        # نتركها فارغة لأن Render سيقرأ من requirements.txt
    ],
)
