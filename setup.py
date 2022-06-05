import setuptools

long_description = "[Libcloud](https://libcloud.apache.org/) driver for [vdsina.ru](https://vdsina.ru/)"

setuptools.setup(
    name="vdsinadriver",
    version="0.0.1",
    author="Sergey Mezentsev",
    author_email="thebits@yandex.ru",
    description="Libcloud driver for vdsina.ru",
    license="UNLICENSE",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/thebits/libcloud-vdsina",
    install_requires=["apache-libcloud>=3.0.0"],
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: System Administrators",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
)
