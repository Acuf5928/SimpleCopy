import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="SimpleCopy",
    version="0.0.2",
    author="Acuf5928",
    author_email="alberto.cuffaro@hotmail.it",
    description="library to make easier copy files and folders in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Acuf5928/SimpleCopy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
