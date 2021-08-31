import setuptools
    
with open("README.md", "r") as fh:
    long_description = fh.read()
    
setuptools.setup(
    name='multinherit',
    version='0.1.0',
    author='DovaX',
    author_email='dovax.ai@gmail.com',
    description='Package solving problems with super() builtin for classes with multiple inheritance.',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/DovaX/multinherit',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
          
     ],
    python_requires='>=3.6',
)
    