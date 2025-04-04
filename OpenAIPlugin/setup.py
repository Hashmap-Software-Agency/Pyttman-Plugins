from setuptools import setup, find_packages


setup(
    name="pyttman_plugin_openai",
    version="1.2.0",
    description="OpenAI plugin for Pyttman apps, allowing seamless LLM integrations with Pyttman.",
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
        "requests",
        "pyttman_plugin_base",
        "tiktoken"
    ],
)
