from distutils.core import setup

setup(
    name='koalaecommerce',
    packages=['koalaecommerce'],  # this must be the same as the name above
    version='0.1.2-alpha',
    description='',
    author='Matt Badger',
    author_email='foss@lighthouseuk.net',
    url='https://github.com/LighthouseUK/koalaecommerce',  # use the URL to the github repo
    download_url='https://github.com/LighthouseUK/koalaecommerce/tarball/0.1.2-alpha',  # I'll explain this in a second
    keywords=['gae', 'lighthouse', 'koala'],  # arbitrary keywords
    classifiers=[],
    requires=['koalacore', 'blinker', 'satchless', 'itsdangerous', 'prices', 'pycrypto'],
)
