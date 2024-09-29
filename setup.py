from setuptools import setup, find_packages

setup(
    name="PyShelfDB", 
    version="0.1.0",
    packages=find_packages(),
    description="A lightweight embedded database with a Pythonic API",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="liamhoatt34",
    author_email="liamhowatt34@gmail.com",
    url="https://github.com/yourusername/my-embedded-db",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
