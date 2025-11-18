import os.path
import base64
import mimetypes

import jinja2
from markupsafe import Markup

from flm.main.template import TemplateEngineBase


# TODO/FIXME: support for some type of flmrender() filter (maybe
# {% flmrender %}...{% endflmrender %} ??
#
# exposed by self.document_template.flm_render_standalone()

class Jinja2Template(TemplateEngineBase):

    def initialize(self, template_main_name):

        self.template_main_name = template_main_name

        # load the main template 
        self.jinja2_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(self.template_info_path),
            autoescape=jinja2.select_autoescape()
        )

        self.jinja2_env.filters["embed_dataurl"] = self.jfilter_embed_dataurl

        self.jinja2_env.filters["flmrender"] = self.jfilter_flmrender
        self.jinja2_env.filters["flmrendertext"] = self.jfilter_flmrendertext

        self.main_template = self.jinja2_env.get_template(self.template_main_name)


    def jfilter_embed_dataurl(self, filepath, mime_type=None):

        if mime_type is None:
            mime_type, _ = mimetypes.guess_type(filepath, strict=False)
        if mime_type is None:
            mime_type = 'text/plain;charset=latin1'

        with open( os.path.join(self.template_info_path, filepath), 'rb' ) as f:
            f_data = f.read()

        return f'data:{mime_type};base64,{base64.b64encode(f_data).decode("ascii")}'

    def jfilter_flmrender(self, value):
        return Markup(self.document_template.flm_render_standalone(value))

    def jfilter_flmrendertext(self, value):
        return self.document_template.flm_render_standalone_text(value)

    def render_template(self, config, **kwargs):
        
        return self.main_template.render(**config)
        
