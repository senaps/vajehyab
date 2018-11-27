from setuptools import find_packages, setup
import re

# packages required for this module
with open('requirements.txt', 'r') as requirements_file:
    REQUIRED_PACKAGES = requirements_file.read()


# Import the README and use it as the description.
with open('README.md', 'r') as readme_file:
    DESCRIPTION = '\n' + readme_file.read()

# Load the package's __version__.py
regex = r"(\d*\.\d*\.\d*)"
with open('__version__.py') as version_file:
    VERSION = re.findall(regex, version_file.read())[0]



setup(name='vajehyab',
      version=VERSION,
      description='python interface for vajehyab project',
      long_description=DESCRIPTION,
      long_description_content_type='text/markdown',
      author='senaps',
      author_email='gerdakan.sa@gmail.com',
      url='https://www.senaps.blog.ir',
      packages=find_packages(exclude=('tests', 'docs')),
      install_requires=REQUIRED_PACKAGES,
      include_package_data=True,
      license='MIT',
      )

