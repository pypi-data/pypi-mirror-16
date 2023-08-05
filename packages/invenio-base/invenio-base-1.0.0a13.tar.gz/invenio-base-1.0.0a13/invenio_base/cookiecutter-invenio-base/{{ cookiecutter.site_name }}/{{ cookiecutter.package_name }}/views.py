# -*- coding: utf-8 -*-

"""{{ cookiecutter.site_name }} base Invenio configuration."""

from __future__ import absolute_import, print_function

from flask import Blueprint, render_template

blueprint = Blueprint(
    '{{ cookiecutter.package_name }}',
    __name__,
    template_folder='templates',
    static_folder='static',
)


@blueprint.route("/")
def index():
    """Home Page."""
    return render_template('{{ cookiecutter.package_name }}/index.html',
                           module_name='{{ cookiecutter.package_name }}')
