import setuptools

setuptools.setup(
    name="cmos_tools_py",
    version="0.0.1",
    description="Software used for the CMOS system.",
    url="https://github.com/foxsi/cmos-tools",
    install_requires=[
            "numpy", 
            "scipy",
            "matplotlib"
        ],
    packages=setuptools.find_packages(),
    zip_safe=False
)