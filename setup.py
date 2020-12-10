import numpy as np
from setuptools import Extension, setup

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'densecapeval._mask',
        sources=['densecapeval/maskApi.c', 'densecapeval/_mask.pyx'],
        include_dirs=[np.get_include(), 'densecapeval'],
        extra_compile_args=['-Wno-cpp', '-Wno-unused-function', '-std=c99'],
    )
]

setup(
    name='densecapeval',
    packages=['densecapeval'],
    package_dir={'densecapeval': 'densecapeval'},
    install_requires=[
        'setuptools>=18.0',
        'cython>=0.27.3',
        'matplotlib>=2.1.0'
    ],
    version='0.1',
    ext_modules=ext_modules
)
