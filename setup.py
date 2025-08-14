import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()
    
REQUIREMENTS = [i.strip() for i in open("requirements.txt").readlines()]

setuptools.setup(
    name="nse",
    version="0.0",
    description="Python implementation of the near-surface expansion for vacuum stellarator",
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: GNU Lesser General Public License v3 or later (LGPLv3+)",
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering",
    ],
    url="https://github.com/liuk2020/pyNSE",
    author="Ke Liu",
    author_email="lk2020@mail.ustc.edu.cn",
    license="GNU 3.0",
    packages=setuptools.find_packages(),
    install_requires=REQUIREMENTS
)

