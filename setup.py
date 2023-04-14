from setuptools import setup, find_packages

setup(
    name="one-api-sid-sdk",
    version="0.1.0",
    packages=find_packages(),
    install_requires=["requests"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
    author="Sid Srikumar",
    author_email="sid@sidhant.co",
    description="An SDK for The One API",
    keywords="lord of the rings, the one api, sdk",
    url="https://github.com/sid9102/sid-one-sdk",
    project_urls={
        "Bug Tracker": "https://github.com/sid9102/sid-one-sdk/issues",
    },
    python_requires=">=3.6",
)