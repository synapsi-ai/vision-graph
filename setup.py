import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

install_requires = [
    # "requests>=2.25.1",
    # "beautifulsoup4>=4.9.3",
]

dev_requires = [
    # "pytest>=7.0.0",
    # "sphinx>=4.0.0",
    # "flake8>=4.0.0",
]

setuptools.setup(
    name="vision-graph",
    version="0.0.1",
    author="Synapsi.ai",
    author_email="hello@synapsi.ai",
    description="Python library for creating vision ML pipelines.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/tuo_utente/tuo_repo",
    project_urls={  
        "Bug Tracker": "https://github.com/synapsi-ai/vision-graph",
        # "Documentation": "https://tuo_utente.github.io/tuo_repo/",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",  # o 4 - Beta, 5 - Production/Stable
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    packages=setuptools.find_packages(where='.'),
    python_requires=">=3.7",
    install_requires=install_requires,
    extras_require={
        "dev": dev_requires,
    },
)
