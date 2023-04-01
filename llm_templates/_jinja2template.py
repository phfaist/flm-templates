import jinja2



class Jinja2Template:

    def __init__(self, template_info_path, template_info_file, llm_run_info,
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

        self.main_template = self.jinja2_env.get_template(self.template_main_name)


    def render_template(self, config, **kwargs):
        
        return self.main_template.render(**config)
        
