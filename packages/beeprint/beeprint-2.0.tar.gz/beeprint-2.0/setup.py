from setuptools import setup
setup(
    name = 'beeprint',
    packages = ['beeprint'], # this must be the same as the name above
    version = '2.0',
    description = 'print object in beautiful format, like pprint',
    author = 'Yangyang Pan',
    author_email = '568397440@qq.com',
    url = 'https://github.com/panyanyany/beeprint', # use the URL to the github repo
    download_url = 'https://github.com/panyanyany/beeprint/archive/master.zip', # I'll explain this in a second
    keywords = ['print', 'pprint', 'format'], # arbitrary keywords
    classifiers = [
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",

        "Environment :: Console",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development",
        "Topic :: Utilities",
    ],
    install_requires=[
        'urwid',
    ],
)
