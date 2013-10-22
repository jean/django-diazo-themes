from setuptools import setup, find_packages

VERSION = '0.1'

REQUIREMENTS = (
    'setuptools>=0.6c11',
    'django-diazo>=0.3',
)
TEST_REQUIREMENTS = (
)


setup(
    name="django_diazo_themes",
    version=VERSION,
    author="Douwe van der Meij",
    description="""Example built-in themes for django-diazo.
    """,
    url="",
    packages=find_packages(),
    include_package_data=True,
    install_requires=REQUIREMENTS,
    tests_require=TEST_REQUIREMENTS,
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ]
)
