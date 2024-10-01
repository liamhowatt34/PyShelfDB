from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="PyShelfDB",
    version="1.0.0",
    packages=find_packages(),
    description="A lightweight embedded database with a Pythonic API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="liamhowatt34",
    author_email="liamhowatt34@gmail.com",
    url="https://github.com/liamhowatt34/PyShelfDB",
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Topic :: Database",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
    keywords="embedded database pythonic fast lightweight",
)
