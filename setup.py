import setuptools

setuptools.setup(
    name = "convcsv2json",
    version = "1.6",
    author = "1337kid",
    author_email = "1337kid@proton.me",
    description = "Convert a CSV file into JSON format based on CSV headers",
    long_description = open('README.md').read()  ,
    long_description_content_type = "text/markdown",
    url = "https://github.com/1337kid/convcsv2json",
    project_urls = {'Source': 'https://github.com/1337kid/convcsv2json',},
    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    packages = setuptools.find_packages(),
    python_requires = ">=3.7"
)
