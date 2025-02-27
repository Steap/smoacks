from setuptools import setup

with open('README.md') as f:
    long_description = f.read()

setup(name='smoacks',
      version='0.2.7',
      description='Simple Microservices with OpenAPI, Connexion, Kubernetes, and SQLAlchemy',
      url='https://github.com/wittlesouth/smoacks',
      author='Wittle South Ventures, LLC',
      author_email='service@wittlesouth.com',
      classifiers=[
          'License :: OSI Approved :: MIT License',
      ],
      packages=['smoacks'],
      include_package_data=True,
      data_files=[('conf', ['conf/smoacks_default.yaml']),
                  ('templates', ['templates/api_util.jinja',
                                 'templates/app-env.jinja',
                                 'templates/base.jinja',
                                 'templates/ConnexionApis.jinja',
                                 'templates/dev-api-server.jinja',
                                 'templates/DataModel.jinja',
                                 'templates/DataModelObject.jinja',
                                 'templates/Dockerfile.jinja',
                                 'templates/gitignore.jinja',
                                 'templates/local-env.jinja',
                                 'templates/login.jinja',
                                 'templates/ModelApis.jinja',
                                 'templates/NoseTests.jinja',
                                 'templates/schema.jinja',
                                 'templates/server_logging.jinja',
                                 'templates/server-loop.jinja',
                                 'templates/server.jinja',
                                 'templates/shutdown.jinja',
                                 'templates/SQLAlchemyModel.jinja',
                                 'templates/test-api-server.jinja',
                                 'templates/test-login-api.jinja',
                                 'templates/testme.jinja',
                                 'templates/TestUtil.jinja'])],
      install_requires=[
          'connexion',
          'coverage',
          'flask_jwt_extended',
          'jinja2',
          'nose',
          'openapi-spec-validator',
          'PyYAML',
          'SQLAlchemy'
          ],
      entry_points={
          'console_scripts': ['smoacks-setup=smoacks.command_line:main',
                              'smoacks-gen=smoacks.command_line:gen']
      },
      long_description=long_description,
      long_description_content_type='text/markdown',
      zip_safe=False)
