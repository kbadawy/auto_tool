import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="project",
    version="1.0",
    author="Karim Badawy",
    author_email="kbadawy@amazon.com",
    description="Auto-scrub/cluster tool",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kbadawy/auto_tool",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.7.0",
        "License :: OSI Approved :: Apache 2.0 License",
        "Operating System :: OS Independent",
    ],
)
