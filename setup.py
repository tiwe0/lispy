from setuptools import setup, find_packages

setup(
    name="lispy",
    version="0.0.1",
    keywords=("lisp"),
    description="lisp in python",
    long_description="lisp implement with python",
    license="MIT Licence",

    author="Ivory",
    author_email="",
    packages=find_packages(),
    platforms="any",
    install_requires=[],

    scripts=[],
    entry_points={
        'console_scripts': [
            'lispy = lispy.entry:lispy'
        ]
    }
)
