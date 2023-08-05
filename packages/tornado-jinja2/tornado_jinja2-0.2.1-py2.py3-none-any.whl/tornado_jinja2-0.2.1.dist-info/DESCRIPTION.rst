Integrate Jinja2 into Tornado Framework
=======================================

This package makes you have the ability that using Jiaja2 Template Engine with Tornado Web Framework.
It will replace the default Tornado Templates.

How to use:
-----------

Import Jinja2Loader to your project 

.. code-block:: python

    from tornado_jinja2 import Jinja2Loader


Pass the instance of Jinja2Loader to `tornado.web.Application` as the value of "template_loader" parameter.  
You can use the [particular Loader][1] from jinja2 and configuring jinaja2 [environment][2] by your self.

.. code-block:: python

    import tornado.web

    jinja2loader = Jinja2Loader('templates_path')
    settings = dict(template_loader=jinja2loader)

    application = tornado.web.Application(handler=[],
                                        **settings)
    import tornado.web
    import jinja2

    # Create a instance of Jinja2Loader
    jinja2_env = jinja2.Environment(loader=jinja2.FileSystemLoader('template/path/'), autoescape=False)
    jinja2_loader = Jinja2Loader(jinja2_env)

    # Give it to Tornado to replace the default Loader.
    settings = dict(template_loader=jinja2_loader)
    application = tornado.web.Application(handler=[],
                                          **settings)



[1]: http://jinja.pocoo.org/docs/dev/api/#loaders
[2]: http://jinja.pocoo.org/docs/dev/api/#jinja2.Environment


