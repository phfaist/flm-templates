import os.path

def get_template_path():
    return os.path.join(os.path.dirname(__file__), 'templates')


from ._jinja2template import Jinja2Template
