from setuptools import setup

# @TODO: Fix it! DONE
setup(
    name="codetodo",
    version="1.0",
    install_requires=[
        "tabulate",
        "termcolor",
        "rglob"
    ],
    author = 'Paul Gessinger',
    author_email = 'hello@paulgessinger.com',
    url = 'https://github.com/paulgessinger/todopy',
    py_modules=['todo'],
    entry_points= {
        'console_scripts': [
            'codetodo = todo:main' 
        ]
    }
)
