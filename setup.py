from setuptools import setup, find_packages
import codecs
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

# Setting up
setup(
    name='cbc',
    version='0.0.1b2',
    author='nemo256 (Amine Neggazi)',
    author_email='<neggazimedlamine@gmail.com>',
    description='Count Blood Cells',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nemo256/cbc',
    install_requires=['opencv-python', 'tensorflow', 'numpy'],
    keywords=['python', 'artificial intelligence', 'deep learning', 'blood cells', 'image segmentation', 'unet'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    scripts=['cbc']
)
