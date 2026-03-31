from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="text-utils-lite",
    version="0.1.0",
    description="Simple text utilities",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="My name and lastname",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.8",
)