# Shamelessly recycled from https://github.com/hjwp/book-example/blob/master/deploy_tools/fabfile.py

from fabric.contrib.files import append, exists, sed
from fabric.api import env, local, run
import random

REPO_URL = "https://github.com/onnudilol/vetcalc.git"


def deploy():
    site_folder = '/home/{}/sites/{}'.format(env.user, env.host)
    source_folder = site_folder + '/source'
    env.virtualenv = '/home/{}/.virtualenvs/vetcalc/bin/python3'.format(env.user)
    _create_directory_structure_if_necessary(site_folder)
    _get_latest_source(source_folder)
    _update_settings(source_folder, env.host)
    _update_static_files(source_folder)
    _update_database(source_folder)


def _create_directory_structure_if_necessary(site_folder):
    for subfolder in ('database', 'static', 'source'):
        run('mkdir -p {}/{}'.format(site_folder, subfolder))


def _get_latest_source(source_folder):
    if exists(source_folder + '/.git'):
        run('cd {} && git fetch'.format(source_folder))
    else:
        run('git clone {} {}'.format(REPO_URL, source_folder))
    current_commit = local("git log -n 1 --format=%H", capture=True)
    run('cd {} && git reset --hard {}'.format(source_folder, current_commit))


def _update_settings(source_folder, site_name):
    settings_path = source_folder + '/vetcalc/settings.py'
    sed(settings_path, "DEBUG = True", "DEBUG = False")
    sed(settings_path, 'DOMAIN = "localhost"', 'DOMAIN = "{}"'.format(site_name))
    sed(settings_path, 'db.sqlite3', '../database/db.sqlite3')
    secret_key_file = source_folder + '/vetcalc/secret_key.py'

    if not exists(secret_key_file):
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        key = ''.join(random.SystemRandom().choice(chars) for _ in range(50))
        append(secret_key_file, 'SECRET_KEY = "{}"'.format(key))

    append(settings_path, '\nfrom .secret_key import SECRET_KEY')


def _update_static_files(source_folder):
    run('cd {} && {} manage.py collectstatic --noinput'.format(source_folder, env.virtualenv))


def _update_database(source_folder):
    run('cd {} && {} manage.py migrate --noinput'.format(source_folder, env.virtualenv))

