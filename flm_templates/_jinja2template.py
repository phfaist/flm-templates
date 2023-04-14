import os.path
import base64
import mimetypes

import jinja2



class Jinja2Template:

    def __init__(self, template_info_path, template_info_file, flm_run_info,
                 *, template_main_name):
        super().__init__()

        self.template_info_path = template_info_path # base folder
        self.template_info_file = template_info_file # the .yaml file
        self.template_main_name = template_main_name

        # load the main template 
        self.jinja2_env = jinja2.Environment(
            loader=jinja2.FileSystemLoader(template_info_path),
            autoescape=jinja2.select_autoescape()
        )

        self.jinja2_env.filters["embed_dataurl"] = self.jfilter_embed_dataurl

        self.main_template = self.jinja2_env.get_template(self.template_main_name)


    def jfilter_embed_dataurl(self, filepath, mime_type=None):

        if mime_type is None:
            mime_type, _ = mimetypes.guess_type(filepath, strict=False)
        if mime_type is None:
            mime_type = 'text/plain;charset=latin1'

        with open( os.path.join(self.template_info_path, filepath), 'rb' ) as f:
            f_data = f.read()

        return f'data:{mime_type};base64,{base64.b64encode(f_data).decode("ascii")}'


    def render_template(self, config, **kwargs):
        
        return self.main_template.render(**config)
        
