from setuptools import setup, find_packages

setup(
    name="ISWII_Laboratorio_5",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "flake8",
        "pytest",
        "pytest-cov"
    ],
)
