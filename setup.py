try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name="mailmerge",
    description = "A simple, command line mail merge tool",
    version="1.7.2",
    author="Andrew DeOrio",
    author_email="awdeorio@umich.edu",
    url="https://github.com/awdeorio/mailmerge/",
    download_url = "https://github.com/awdeorio/mailmerge/tarball/1.7.2",
    license="MIT",
    packages = ["mailmerge"],
    keywords=["mail merge", "mailmerge", "email"],
    install_requires=[
        "click",
        "configparser",
        "jinja2",
    ],
    test_suite='nose2.collector.collector',

    # Python command line utilities will be installed in a PATH-accessible bin/
    entry_points={
        'console_scripts': [
            'mailmerge = mailmerge.__main__:cli',
        ]
    },
)
