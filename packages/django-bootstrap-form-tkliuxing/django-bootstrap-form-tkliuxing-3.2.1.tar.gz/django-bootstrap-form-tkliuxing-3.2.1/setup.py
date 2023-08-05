from setuptools import setup, find_packages
from bootstrapform.meta import VERSION

setup(
    name='django-bootstrap-form-tkliuxing',
    version=str(VERSION),
    description="django-bootstrap-form-tkliuxing",
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Django",
        "Environment :: Web Environment",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
    keywords='bootstrap,django',
    author='tkliuxing',
    author_email='ouyanghongyu@gmail.com',
    url='http://github.com/tkliuxing/django-bootstrap-form',
    license='BSD',
    test_suite='runtests.runtests',
    install_requires = [
        "django>=1.3",
    ],
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)
