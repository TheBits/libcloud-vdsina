import setuptools

with open("README.md") as fh:
    long_description = fh.read()

setuptools.setup(
    name="vdsinadriver",
    version="0.0.1",
    author="Sergey Mezentsev",
    author_email="thebits@yandex.ru",
    description="Libcloud driver for vdsina",
    license="UNLICENSE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thebits/libcloud-vdsina",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
