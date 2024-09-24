from setuptools import setup, Extension
from pybind11.setup_helpers import Pybind11Extension, build_ext

ext_modules = [
    Pybind11Extension(
        "example",
        ["2.cpp"],  
        include_dirs=[
            "/Library/Frameworks/Python.framework/Versions/3.11/lib/python3.11/site-packages/pybind11/include",  # Path to pybind11 headers
            "/Library/Frameworks/Python.framework/Versions/3.11/include/python3.11"  # Python headers
        ],
    ),
]

setup(
    name="example",
    ext_modules=ext_modules,
    cmdclass={"build_ext": build_ext},
)
