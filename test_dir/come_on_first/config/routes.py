

from app.views.v1 import *
from config import config


# register blueprints
routes = {
    # url_prefix: blueprint_instance
    # "/url": inst
    "/login": auth,
    "/register": register,
    "/article": article
}


def register_routes(app):
    """register blueprints from route map"""
    print(config.get('APP_API_VERSION'))
    v = config.get('APP_API_VERSION') or ""
    for url, bp in routes.items():
        print(url)
        app.register_blueprint(bp, url_prefix=v+url)


# end
