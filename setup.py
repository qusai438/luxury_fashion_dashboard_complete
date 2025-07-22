from setuptools import setup, find_packages

setup(
    name="luxury_fashion_dashboard",
    version="1.0.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Flask==2.3.2",
        "Flask-Cors==3.0.10",
        "Flask-Mail==0.9.1",
        "Flask-Login==0.6.3",
        "Flask-SocketIO==5.3.6",
        "Flask-SQLAlchemy==3.1.1",
        "celery==5.3.1",
        "redis==4.6.0",
        "gunicorn==21.2.0",
        "python-dotenv==1.0.1",
        "requests==2.31.0",
        "openai==1.16.0",
        "Pillow==9.5.0",
        "whitenoise==6.6.0"
    ],
)
