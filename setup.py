import pathlib
import re
import os

from setuptools import setup

##########################################################
################# to add the setup as cli-command
################# go to the console and use the command to activate the virtualenv
################# source venv/bin/activate
################# pip install --editable .
################# python setup.py sdist
##########################################################


project_path = os.getcwd()


def find_requirements():
    with open(project_path + '/requirements.txt',
              encoding='utf-8') as requirements_file:
        result = [each_line.strip()
                  for each_line in requirements_file.read().splitlines()]
        return result


def find_version():
    with open(project_path + '/src' + '/__init__.py',
              encoding='utf-8') as version_file:
        pattern = '^__version__ = [\'\"]([^\'\"]*)[\'\"]'
        match = re.search(pattern, version_file.readline().strip())
        if match:
            result = match.group(1)
            return result


setup(
    name='kafka_manager',
    description='Kafka project; position manager',
    version=find_version(),
    install_requires=find_requirements(),
    url='https://github.com/bsegot/kafka_position_manager',
    author='bsegot',
    author_email='johnjohnjohnskyjohn@gmail.com',

    entry_points={
        'console_scripts': [
            #'run_data_logic = src.decision_backend:run_data_logic',
            #'manually_add_all_positions_redis = src.decision_backend:manually_add_all_positions_redis'
        ]
    }
)
