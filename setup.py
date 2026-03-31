from setuptools import setup, find_packages

setup(
    name="text-utils-lite_byMe",
    version="0.1.0",
    description="Simple text utilities",
    author="My name and lastname",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[],
    python_requires=">=3.8",
)