"""Defines various one-off helpers for the package."""
from functools import wraps
from time import time

from sqlalchemy.exc import IntegrityError
from update_checker import parse_version
import requests

from .models import IPAddr, Installation, Package, Platform, PythonVersion, db


def configure_logging(app):
    """Send ERROR log to ADMINS emails."""
    ADMINS = ['bbzbryce@gmail.com']
    if not app.debug:
        import logging
        from logging.handlers import SMTPHandler
        mail_handler = SMTPHandler(
            '127.0.0.1', 'server-error@updatechecker.bryceboe.com',
            ADMINS, 'UpdateChecker Failed')
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)


def normalize(string):
    """Return stripped and lower-cased string."""
    return string.strip().lower()


def package_cache(function):
    """Memoize the wrapped function."""
    CACHE_TIME = 600
    stored = {}

    @wraps(function)
    def wrapped(*args):
        now = time()
        if args in stored:
            updated, data = stored[args]
            if now < updated + CACHE_TIME:
                return data
        data = function(*args)
        stored[args] = (now, data)
        return data
    return wrapped


@package_cache
def get_current_version(package, include_prereleases):
    """Return information about the current version of package."""
    try:
        response = requests.get('http://pypi.python.org/pypi/{0}/json'
                                .format(package))
    except requests.exceptions.RequestException:
        return {'success': False}
    if response.status_code != 200:
        return {'success': False}
    data = response.json()
    versions = list(data['releases'].keys())
    versions.sort(key=parse_version, reverse=True)

    version = versions[0]
    for tmp_version in versions:
        if include_prereleases or standard_release(tmp_version):
            version = tmp_version
            break

    upload_time = None
    for file_info in data['releases'][version]:
        if file_info['upload_time']:
            upload_time = file_info['upload_time']

    return {'success': True, 'data': {'upload_time': upload_time,
                                      'version': version}}


def record_check(name, version, platform_str, python_version_str, ip):
    """Record the update check."""
    package = Package.fetch_or_create(package_name=name,
                                      package_version=version)
    platform = Platform.fetch_or_create(value=platform_str)
    python_version = PythonVersion.fetch_or_create(value=python_version_str)
    ipaddr = IPAddr.fetch_or_create(value=ip)

    update = False
    if ipaddr.id and package.id and platform.id and python_version.id:
        update = Installation.query.filter_by(
            day=db.func.Date(db.func.now()), ipaddr=ipaddr, package=package,
            platform=platform, python_version=python_version).update(
                {Installation.count: Installation.count + 1},
                synchronize_session=False)
    if not update:
        installation = Installation(count=1, ipaddr=ipaddr, package=package,
                                    platform=platform,
                                    python_version=python_version)
        db.session.add(installation)

    try:
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        record_check(name, version, platform_str, python_version_str, ip)


def standard_release(version):
    return version.replace('.', '').isdigit()


def versions_table(versions, unique_counts, total_counts):
    rows = ['<tr><th>Version</th><th>Unique</th><th>Total</th></tr>']
    for i, version in enumerate(versions):
        rows.append('<tr><td>{0}</td><td>{1}</td><td>{2}</td></tr>'
                    .format(version, unique_counts[i], total_counts[i]))
    rows.append('<tr><td>Sum</td><td>{0}</td><td>{1}</td></tr>'
                .format(sum(unique_counts), sum(total_counts)))
    return '<table>\n{0}</table>\n'.format('\n'.join(rows))
