import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="example_hogehoge_package",
    version="0.0.1",  # https://www.python.org/dev/peps/pep-0440/
    author="sisii",
    author_email="sisii00.swork@gmail.com",
    description="A small example package",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/sisi100/packaging_tutorial",
    project_urls={
        "Bug Tracker": "https://github.com/sisi100/packaging_tutorial/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={"console_scripts": ["hoge = example_package.example:main"]},
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)
