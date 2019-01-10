from setuptools import setup

 

def readme():
    with open('README.md', encoding='utf-8') as f:
        README = f.read()
    return README


setup(
    name="ikwilnaarhuis",
    version="0.0.0.0.3.1",
    description="A Python CLI package for people who think 'IK WIL NAAR HUIS'.",
    long_description=readme(),
    long_description_content_type="text/plain",
    url="https://github.com/lucassel/ikwilnaarhuis",
    author="Lucas Selfslagh",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["ikwilnaarhuis"],
    include_package_data=True,
    entry_points={
        "console_scripts": [
            "ikwilnaarhuis=ikwilnaarhuis.cli:main",
        ]
    },
)