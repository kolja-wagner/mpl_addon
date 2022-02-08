from setuptools import setup, find_packages

setup(
    name='addon_mpl',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=False,
    zip_safe=True,
    install_requires=[
        'matplotlib'
    ]
)
