import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="wikiscraper-zoharcochavi", 
    version="0.0.1",
    author="zoharcochavi",
    author_email="zohar.cochavi@gmail.com",
    description="Print wikipedia articles to the terminal",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="http://www.github.com/zoharcochavi/wikiscraper",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: MIT",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
