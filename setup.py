
from setuptools import setup, find_packages

setup(

    # Vitals
    name='usb_descriptors',
    license='BSD',
    url='https://github.com/hansfbaier/python-usb-descriptors',
    author='Hans Baier',
    author_email='hansfbaier@gmail.com',
    description='python library providing utilities, data structures, constants, parsers, and tools for working with USB data',
    use_scm_version= {
        "root": '..',
        "relative_to": __file__,
        "version_scheme": "guess-next-dev",
        "local_scheme": lambda version : version.format_choice("+{node}", "+{node}.dirty"),
        "fallback_version": "0.1.1"
    },

    # Imports / exports / requirements.
    platforms='any',
    packages=find_packages(),
    include_package_data=True,
    python_requires="~=3.7",
    install_requires=['construct'],
    setup_requires=['setuptools', 'setuptools_scm', 'wheel'],

    # Metadata
    classifiers = [
        'Programming Language :: Python',
        'Development Status :: 1 - Planning',
        'Natural Language :: English',
        'Environment :: Console',
        'Environment :: Plugins',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering',
        'Topic :: Security',
        ],
)
