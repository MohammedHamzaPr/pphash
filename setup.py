import setuptools

with open("README.md", "r", encoding="utf-8") as readme:
    long_description = readme.read()


setuptools.setup(
    name="pphash",
    version="0.0.1",

    author="Mohammed Hamza",
    author_email="",

    description=(
        "A lightweight Python library for password hashing, "
        "hash verification, hash detection, and secure password generation."
    ),

    long_description=long_description,
    long_description_content_type="text/markdown",

    url="https://github.com/MohammedHamzaPr/pphash",

    packages=setuptools.find_packages(),

    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Security",
        "Topic :: Software Development :: Libraries",
    ],

    python_requires=">=3.8",

    license="MIT",
)
