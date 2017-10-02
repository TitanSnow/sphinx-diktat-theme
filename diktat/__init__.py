import os
import pkg_resources


def setup(app):
    app.add_html_theme('diktat', os.path.dirname(__file__))
    return {
        'version': pkg_resources.get_distribution('diktat').version
    }
