from setuptools import setup, find_packages

# I attempted to separate test and install dependencies but couldn't figure it out (in 10 minutes). Keeping them
# toegether for now - pytest is lightweight.
setup(name="hgv", version=0.1, description="Hierarchical Global Variables", author='Dane Austin',
      author_email='dane_austin@fastmail.com.au', url='https://github.com/draustin/hgv', license='BSD',
      packages=find_packages(), install_requires=['pytest'], python_requires='>=3.4')
