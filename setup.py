from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='Converter',
    version='1.0',
    author='XTITAX',
    author_email='xtitax@yandex.ru',
    description='Библиотека конвертера чисел',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/XTITAX/Converter',
    packages=find_packages(include=['Converter']),

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
