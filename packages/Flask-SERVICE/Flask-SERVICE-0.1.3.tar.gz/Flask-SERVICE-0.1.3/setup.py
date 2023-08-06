import os
from setuptools import setup, find_packages


here = os.path.abspath(os.path.dirname(__file__))

try:
    README = open(os.path.join(here, 'README.rst')).read()
    CHANGES = open(os.path.join(here, 'CHANGES.rst')).read()
except:
    README = ''
    CHANGES = ''


setup(
    name='Flask-SERVICE',
    version='0.1.3',
    license='BSD',
    url='https://github.com/lufeng4828/flask_service',
    author='Feng Lu',
    author_email='lufeng044@qq.com',
    maintainer='Feng Lu',
    maintainer_email='lufeng044@qq.com',
    description='A service api client for Flask applications.',
    long_description=README + '\n\n' + CHANGES,
    zip_safe=False,
    packages=['flask_service', 'flask_service.services'],
    platforms='any',
    include_package_data=True,
    install_requires=[
        'requests'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
