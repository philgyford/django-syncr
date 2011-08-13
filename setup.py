from setuptools import setup, find_packages
 
setup(
    name='django-syncr',
    version='0.60',
    description='Synchronize Django with the web',
    author='Phil Gyford',
    author_email='phil@gyford.com',
    url='http://github.com/philgyford/django-syncr',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    include_package_data=True,
    zip_safe=False,
)
