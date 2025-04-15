from setuptools import setup, find_packages

setup(
    name="commitpal",
    version="1.0.0",
    description="AI-powered CLI tool for generating Git commit messages and changelogs.",
    author="Hardik Jaiswal",
    author_email="your_email@example.com",
    url="https://github.com/pythonicforge/CommitPal",
    packages=find_packages(),
    install_requires=[
        "groq",
        "python-dotenv",
        "loguru"
    ],
    entry_points={
        "console_scripts": [
            "comitpal=main:main", 
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
