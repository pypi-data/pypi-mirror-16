from setuptools import setup, find_packages

setup(
    license = 'Apache License 2.0 (http://www.apache.org/licenses/LICENSE-2.0)',
    long_description = open('README.rst').read(),
    use_scm_version = True,
    zip_safe = True,

    author = 'Reece Hart',
    author_email = 'reecehart@gmail.com',
    description = """miscellaneous simple bioinformatics utilities and lookup tables""",
    name = "bioutils",
    package_data = {'bioutils': ['_data/assemblies/*.json']},
    packages = find_packages(),
    url = 'https://bitbucket.org/biocommons/bioutils',

    classifiers = [
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Healthcare Industry",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python",
        "Topic :: Database :: Front-Ends",
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
    ],

    keywords = [
        'bioinformatics',
    ],

    install_requires = [
        'six',
    ],

    setup_requires = [
        'pytest',
        'pytest-cov',
        'setuptools_scm',
        'recordtype',
    ],

    tests_require = [
    ],
)

## <LICENSE>
## Copyright 2014 Bioutils Contributors (https://bitbucket.org/biocommons/bioutils)
## 
## Licensed under the Apache License, Version 2.0 (the "License");
## you may not use this file except in compliance with the License.
## You may obtain a copy of the License at
## 
##     http://www.apache.org/licenses/LICENSE-2.0
## 
## Unless required by applicable law or agreed to in writing, software
## distributed under the License is distributed on an "AS IS" BASIS,
## WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
## See the License for the specific language governing permissions and
## limitations under the License.
## </LICENSE>
