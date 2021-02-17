import setuptools

version = '0.0.2'

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='postman2py',
    packages=['postman2py'],
    version=version,
    author='Bohdan Lesiv',
    author_email='boghdanlesiv@gmail.com',
    description='A library to use postman collections V2.1 in python.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/bodharma/postman2py',
    download_url='https://codeload.github.com/bodharma/postman2py/zip/master',
    keywords=['postman', 'rest', 'api'],  # arbitrary keywords
    install_requires=[
        'requests',
        'python-magic',
        'loguru'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
