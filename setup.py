from setuptools import setup, find_packages

with open('README.rst', encoding="utf-8") as myFile:
    readme = myFile.read()

setup(
    name = 'Monitoringservers',
    version = '1.0',
    description = 'This Script will automate the monitoring of Gnu/Linux servers activities such as Users, Update, Logs, etc... ',
    long_description = readme,
    author = 'Nke S. Yapo',
    author_email = 'contact@nkeyapo.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = []
)