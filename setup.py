import os
from setuptools import find_packages, setup

def read(fname):
    try:
        return open(os.path.join(os.path.dirname(__file__), fname)).read()
    except IOError:
        return ''

setup(
    name='django-admin-multiple-choice-list-filter',
    version=__import__('django_admin_multiple_choice_list_filter').__version__,
    description=read('DESCRIPTION'),
    license='GNU General Public License (GPL)',
    author='Ivan Surov',
    author_email='ivansurovv@gmail.com',
    packages=find_packages(),
    include_package_data=True,
    long_description=read('README'),
    url='https://github.com/ivansurov/django_admin_multiple_choice_list_filter',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)