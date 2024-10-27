from setuptools import find_packages, setup
from esp8266_tshcli import __meta__
 
def read(f):
    return open(f, 'r', encoding='utf-8').read()
 
setup(
    name='esp8266_tshcli',
    version=__meta__.__version__,
    url='https://github.com/xeronm/esp8266-tsh',
    license=__meta__.__license__,
    description=__meta__.__title__,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    maintainer='Denis Muratov',
    maintainer_email='xeronm@gmail.com',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    # install_requires=open('requirements.txt').readlines(),
    python_requires=">=3.7",
    zip_safe=False,
    classifiers=[
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Development Status :: 5 - Production/Stable',
        'Environment :: Other Environment',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3 :: Only',
        'Topic :: Home Automation',
    ],
    project_urls={
    },
)