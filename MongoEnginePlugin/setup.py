from setuptools import setup, find_packages


# This call to setup() does all the work
setup(
    name="pyttman_plugin_mongoengine",
    version="1.0.7",
    description="Mongoengine (MongoDB) plugin for Pyttman apps, allowing seamless integration with MongoEngine and Pyttman.",
    long_description_content_type="text/markdown",
    url="https://github.com/Hashmap-Software-Agency/Pyttman-Plugins",
    author="Simon Olofsson, Pyttman framework founder and maintainer.",
    author_email="simon@hashmap.se",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    packages=find_packages(exclude=["*.tests", "*.tests.*",
                                    "tests.*", "tests"]),
    include_package_data=True,
    install_requires=[
        "mongoengine",
        "pyttman_plugin_base"
    ],
)
