from setuptools import setup, find_packages

VERSION = '0.0.1' 
DESCRIPTION = 'Unofficial LS-Dyna Python pre-processor'
LONG_DESCRIPTION = 'Something will be added.'

# Setting up
setup(
       # the name must match the folder name 'verysimplemodule'
        name="PyDynasty", 
        version=VERSION,
        author="Paolo ascia",
        author_email="<youremail@email.com>",
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        package_dir={"": "PyDynasty"},
        install_requires=[], # add any additional packages that 
        # needs to be installed along with your package. Eg: 'caer'

        keywords=['python', 'LS Dyna'],
        classifiers= [
            "Development Status :: 3 - Alpha",
            "Intended Audience :: Education",
            "Programming Language :: Python :: 3",
            "Operating System :: MacOS :: MacOS X",
            "Operating System :: Microsoft :: Windows",
        ]
)