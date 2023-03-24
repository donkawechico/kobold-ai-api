from setuptools import setup, find_packages

setup(
    name='kobold-ai-api',
    version='0.1.1',
    description='Python library for interacting with KoboldAi API',
    author='Donnie Karns',
    author_email='',
    packages=find_packages(),
    install_requires=[
        'requests>=2.26.0',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
