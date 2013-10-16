import os
from distutils.core import setup


def read_file_into_string(filename):
    path = os.path.abspath(os.path.dirname(__file__))
    filepath = os.path.join(path, filename)
    try:
        return open(filepath).read()
    except IOError:
        return ''


def get_readme():
    for name in ('README', 'README.rst', 'README.md'):
        if os.path.exists(name):
            return read_file_into_string(name)
    return ''


setup(
    name='pkimber-hatherleigh-net',
    packages=['project', 'project.templatetags', 'project.management', 'project.management.commands', 'settings'],
    package_data={
        'project': [
            'templates/*.*',
            'templates/project/*.*',
        ],
    },
    version='0.0.21',
    description='hatherleigh web site',
    author='Patrick Kimber',
    author_email='patrick.kimber@connexionsw.com',
    url='ssh://hg@bitbucket.org/pkimber/hatherleigh_net',
    classifiers=[
        'Development Status :: 1 - Planning',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Office/Business :: Scheduling',
    ],
    long_description=get_readme(),
)