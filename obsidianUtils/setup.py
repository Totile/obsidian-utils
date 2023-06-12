import setuptools

with open("README.md", "r", encoding="utf-8") as fhand:
    long_description = fhand.read()

setuptools.setup(
    name="obsidian_outline_tools_totile",
    version="0.0.1",
    author="Eliott CHOMARD",
    author_email="eliottchomard@gmail.com",
    description = "A tootl for transforming outlines into heading Obsidian",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Totile/obsidian-utils",
    project_urls={
        "Bug Tracker": "https://github.com/Totile/obsidian-utils/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["pyperclip"],
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    entry_points={
        "console_scripts": [
            "obsiutil = src.cli:main",
        ]
    }
)