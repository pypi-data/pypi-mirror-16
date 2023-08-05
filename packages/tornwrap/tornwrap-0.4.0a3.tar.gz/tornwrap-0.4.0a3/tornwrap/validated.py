from valideer import parse
from functools import wraps
from urlparse import parse_qs
from tornado.web import HTTPError
from tornado.escape import json_decode

from .validators import *


def validated(arguments=None, body=None, extra_arguments=True, extra_body=False):
    if type(body) in (dict, str):
        body = parse(body, additional_properties=extra_body)
    elif body not in (None, False):
        raise ValueError('body must be type None, False, or dict')
    if type(arguments) is dict:
        arguments = parse(arguments, additional_properties=extra_arguments)
    elif arguments not in (None, False):
        raise ValueError('arguments must be type None, False, or dict')

    def wrapper(method):
        @wraps(method)
        def validate(self, *args, **kwargs):
            # ------------------
            # Validate Body Data
            # ------------------
            if body:
                try:
                    _body = json_decode(self.request.body) if self.request.body else {}
                except:
                    # ex. key1=value2&key2=value2
                    try:
                        _body = dict([(k, v[0] if len(v) == 1 else v) for k, v in parse_qs(self.request.body, strict_parsing=True).items()])
                    except:
                        raise HTTPError(400, "body was not able to be decoded")

                kwargs['body'] = body.validate(_body, adapt=True)

            elif body is False and self.request.body:
                raise HTTPError(400, reason='No body arguments allowed')

            # -------------------
            # Validate URL Params
            # -------------------
            if arguments:
                # include url arguments
                if self.request.query_arguments:
                    _arguments = dict([(k, v[0] if len(v) == 1 else v) for k, v in self.request.query_arguments.items() if v != [''] and k[0] != '_'])
                else:
                    _arguments = {}
                kwargs["arguments"] = arguments.validate(_arguments)

            elif arguments is False and self.request.query_arguments and not any(map(lambda a: a[0] == '_', self.request.query_arguments)):
                raise HTTPError(400, reason='No url arguments allowed')

            return method(self, *args, **kwargs)

        return validate
    return wrapper
