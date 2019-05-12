# structure.py - Routines for generation app structure
import os
from jinja2 import Environment, Template, TemplateError, UndefinedError, TemplateNotFound, FileSystemLoader
from smoacks.sconfig import sconfig

class SmoacksStructure:
    def __init__(self):
        self.name = 'SmoacksStructure'
        self.env = [
            {'template': 'Dockerfile.jinja',
             'dir': sconfig['structure']['sourcedir'],
             'outfile': "Dockerfile"},
            {'template': 'app-env.jinja',
             'dir': sconfig['structure']['bindir'],
             'outfile': "app-env"},
            {'template': 'dev-api-server.jinja',
             'dir': sconfig['structure']['kubedir'],
             'outfile': "dev-api-server.yaml"},
            {'template': 'server-loop.jinja',
             'dir': sconfig['structure']['sourcedir'],
             'outfile': "server-loop"},
            {'template': 'server_logging.jinja',
             'dir': sconfig['structure']['sourcedir'],
             'outfile': "server_logging.yaml"},
            {'template': 'schema.jinja',
             'dir': sconfig['structure']['specdir'],
             'outfile': "schema.yaml"},
            {'template': 'requirements.jinja',
             'dir': '.',
             'outfile': "requirements.txt"}
        ]
        self.template_dict = sconfig['env_defaults']
        self.template_dict['smoacks_local_dev_path'] = os.getcwd()

    def renderEnvironment(self):
        env = Environment(
            loader = FileSystemLoader('templates')
        )
        for filespec in self.env:
           template = env.get_template(filespec['template'])
           if not os.path.isdir(filespec['dir']):
              os.makedirs(filespec['dir'], exist_ok=True)
           outfile = open(os.path.join(filespec['dir'], filespec['outfile']), "w")
           try:
               filestring = template.render(self.template_dict)
               outfile.write(filestring)
           except TemplateNotFound:
               print('Caught a TemplateNotFoundError on {}'.format(filespec['template']))
           except UndefinedError:
               print('Caught a UndefinedError on {}'.format(filespec['template']))
           except TemplateError:
               print('Caught a TemplateError on {}'.format(filespec['template']))
           except:
               print('Caught an untyped error on {}'.format(filespec['template']))