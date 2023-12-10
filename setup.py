import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="battleships-pkg-smcmullen",
    version="0.0.1",
    author="Sam McMullen",
    author_email="sm1441@exeter.ac.uk",
    description="A simulation of a battleships board game using a web interface.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sfmcmullen/ECM1400ProgrammingCoursework",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.10'
)