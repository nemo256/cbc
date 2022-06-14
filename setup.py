from setuptools import setup, find_packages
import codecs
import os

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

# Setting up
setup(
    name='cbc',
    version='0.0.4',
    author='nemo256 (Amine Neggazi)',
    author_email='<neggazimedlamine@gmail.com>',
    description='Count Blood Cells',
    packages=find_packages(),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/nemo256/cbc',
    install_requires=required,
    keywords=['python', 'artificial intelligence', 'deep learning', 'blood cells', 'image segmentation', 'unet'],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
    data_files=[
        ('share/cbc/weights', [
            'models/rbc.h5',
            'models/wbc.h5',
            'models/plt.h5'
        ]),
        ('share/cbc/images', [
            'test.jpg',
        ])
    ],
    scripts=['cbc']
)
