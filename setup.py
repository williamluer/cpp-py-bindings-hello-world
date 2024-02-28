from setuptools import setup, Extension
import pybind11

setup(
    name='rectangle',
    version='1.0',
    ext_modules=[
        Extension(
            'rectangle',
            ['bindings.cpp', 'Rectangle.cpp'],
            include_dirs=[pybind11.get_include()],
            language='c++',
            extra_compile_args=['-std=c++14']
        ),
    ],
)

