import setuptools
with open('chase/README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name="chase",
    version="1.0.0",
    author="Vitalii Shulhan 226454",
    author_email="226454@edu.p.lodz.pl",
    description="simulation how wolf hunts for sheep",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vitaliishulhan/wolf_sheep_simulation",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6'
)