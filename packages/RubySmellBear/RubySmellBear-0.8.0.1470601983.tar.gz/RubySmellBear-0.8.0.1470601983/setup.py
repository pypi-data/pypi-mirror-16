#!/usr/bin/env python3

from setuptools import find_packages, setup


if __name__ == "__main__":
    try:
        setup(name='RubySmellBear',
              version='0.8.0.1470601983',
              description="'RubySmellBear' bear for coala (http://coala.rtfd.org/)",
              authors={'The coala developers'},
              authors_emails={'coala-devel@googlegroups.com'},
              maintainers={'The coala developers'},
              maintainers_emails={'coala-devel@googlegroups.com'},
              platforms={'any'},
              license='AGPL-3.0',
              packages=find_packages(exclude=["build.*"]),
              long_description="""
    Detect code smells in Ruby source code.

    For more information about the detected smells, see
    <https://github.com/troessner/reek/blob/master/docs/Code-Smells.md>.
    """,
              classifiers=[
                   "Development Status :: 4 - Beta",
                   "Environment :: Console",
                   "Environment :: Win32 (MS Windows)",
                   "Intended Audience :: Science/Research",
                   "Intended Audience :: Developers",
                   "Programming Language :: "
                        "Python :: Implementation :: CPython",
                   "Programming Language :: Python :: 3.4",
                   "Programming Language :: Python :: 3.5",
                   "Programming Language :: Python :: 3 :: Only",
                   "Topic :: Scientific/Engineering :: Information Analysis",
                   "Topic :: Software Development :: Quality Assurance",
                   "Topic :: Text Processing :: Linguistic"])

    finally:
        print('[WARN] If you do not install the bears using the coala '
              'installation tool, there may be problems with the dependencies '
              'and they may not work.')
