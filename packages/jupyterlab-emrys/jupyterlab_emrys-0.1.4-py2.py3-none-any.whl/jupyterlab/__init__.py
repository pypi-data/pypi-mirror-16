"""Tornado handlers for the Lab view."""

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

import os
from tornado import web
from notebook.base.handlers import IPythonHandler, FileFindHandler
from jinja2 import FileSystemLoader
from notebook.utils import url_path_join as ujoin


#-----------------------------------------------------------------------------
# Module globals
#-----------------------------------------------------------------------------

DEV_NOTE_NPM = """It looks like you're running JupyterLab from source.
If you're working on the TypeScript sources of JupyterLab, try running

    npm run watch

from the JupyterLab repo directory in another terminal window to have the system
incrementally watch and build JupyterLab's TypeScript for you, as you make
changes.
"""

HERE = os.path.dirname(__file__)
FILE_LOADER = FileSystemLoader(HERE)
BUILT_FILES = os.path.join(HERE, 'build')
PREFIX = '/lab'



class LabHandler(IPythonHandler):
    """Render the Jupyter Lab View."""

    @web.authenticated
    def get(self):
        self.write(self.render_template('lab.html',
            static_prefix=ujoin(self.application.settings['base_url'], PREFIX),
            page_title='Emrys Jupyter Lab',
            terminals_available=self.settings['terminals_available'],
            mathjax_url=self.mathjax_url,
            mathjax_config='TeX-AMS_HTML-full,Safe',
            #mathjax_config=self.mathjax_config # for the next release of the notebook
        ))

    def get_template(self, name):
        return FILE_LOADER.load(self.settings['jinja2_env'], name)

#-----------------------------------------------------------------------------
# URL to handler mappings
#-----------------------------------------------------------------------------

default_handlers = [
    (PREFIX, LabHandler),
    (PREFIX+r"/(.*)", FileFindHandler,
        {'path': BUILT_FILES}),
    ]

def _jupyter_server_extension_paths():
    return [{
        "module": "jupyterlab"
    }]


def load_jupyter_server_extension(nbapp):
    base_dir = os.path.realpath(os.path.join(HERE, '..'))
    dev_mode = os.path.exists(os.path.join(base_dir, '.git'))
    if dev_mode:
        nbapp.log.info(DEV_NOTE_NPM)
    nbapp.log.info('JupyterLab alpha preview extension loaded from %s'%HERE)
    webapp = nbapp.web_app
    base_url = webapp.settings['base_url']
    webapp.add_handlers(".*$", [(ujoin(base_url, h[0]),) + h[1:] for h in default_handlers])
