##############################################################################
#
# Copyright (c) 2016, 2degrees Limited.
# All Rights Reserved.
#
# This file is part of django-pastedeploy-settings
# <https://github.com/2degrees/django-pastedeploy-settings>, which is subject
# to the provisions of the BSD at
# <http://dev.2degreesnetwork.com/p/2degrees-license.html>. A copy of the
# license should accompany this distribution. THIS SOFTWARE IS PROVIDED "AS IS"
# AND ANY AND ALL EXPRESS OR IMPLIED WARRANTIES ARE DISCLAIMED, INCLUDING, BUT
# NOT LIMITED TO, THE IMPLIED WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST
# INFRINGEMENT, AND FITNESS FOR A PARTICULAR PURPOSE.
#
##############################################################################
from logging import getLogger
from os.path import isfile as is_file
from os.path import join as join_path
from sys import executable as PYTHON_INTERPRETER_PATH

from docker_dev.docker_interface import get_docker_compose_config
from docker_dev.subprocess import run_command


_LOGGER = getLogger(__name__)


def build_python_distributions(docker_compose_file_path, project_name):
    docker_compose_config = \
        get_docker_compose_config(docker_compose_file_path, project_name)
    services = docker_compose_config['services'].values()
    build_dir_paths = {s['build']['context'] for s in services if 'build' in s}
    for dir_path in build_dir_paths:
        _generate_egg_info_directory(dir_path)


def _generate_egg_info_directory(distribution_path):
    if _is_dir_python_distribution(distribution_path):
        _LOGGER.info(
            'Generating .egg-info directory for distribution at %r',
            distribution_path,
        )
        run_command(
            PYTHON_INTERPRETER_PATH,
            [
                'setup.py',
                'develop',
                '--editable',
                '--build-directory',
                '.',
                '--no-deps',
                '--dry-run',
            ],
            cwd=distribution_path,
        )
    else:
        _LOGGER.info(
            '%r does not contain a Python distribution',
            distribution_path,
        )


def _is_dir_python_distribution(dir_path):
    return is_file(join_path(dir_path, 'setup.py'))
