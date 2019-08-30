
from .filter import filter_list_mapping

from flask_babel import Babel
from flask import request


def decorate_helper(app):

    # Add custom template filters
    for key, func in filter_list_mapping.items():
        app.template_filter(key)(func)

    babel = Babel(app)

    def get_locale():
        translations = [str(translation)
                        for translation in babel.list_translations()]
        return request.accept_languages.best_match(translations)

    babel.localeselector(get_locale)

    return app
