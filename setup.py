from setuptools import setup, find_packages

setup(
    name="portscanner",
    version="1.0.0",
    description="Multithreaded Port Scanner with CLI and GUI",
    author="Tu Nombre",
    packages=find_packages(),
    python_requires=">=3.8",
    entry_points={
        "console_scripts": [
            "portscan=portscanner.cli:main",
        ],
    },
)