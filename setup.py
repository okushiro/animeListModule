from setuptools import setup, find_packages

setup(
    name='animeList',
    version="1.0.0",
    install_requires=["pandas", "requests"],
    description="get Anime Infomation",
    long_description="get Anime Infomation",
    author='Okushiro Kentaro',
    packages=find_packages()
)