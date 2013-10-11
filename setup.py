from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='gitsh',
        version='0.1',
        description='Interactive git',
        long_description=readme(),
        classifiers=[
        ],
        keywords='git repl shell',
        url='http://github.com/mike-burns/gitsh',
        author='Mike Burns, thoughtbot',
        author_email='mburns@thoughtbot.com',
        license='BSD',
        packages=['gitsh'],
        entry_points={
            'console_scripts': ['gitsh = gitsh.command_line:main'],
        },
        test_suite='nose.collector',
        tests_require=['nose'])
