import logging
from six.moves.urllib import parse

import httpretty

logger = logging.getLogger(__name__)


def get_decorator(placebo):
    """Create a decorator for placebo object."""
    def decorator(fun):
        def _wrapper(*args, **kwargs):
            def _run():
                method = placebo._get_method()

                def get_body(request, uri, _headers):
                    # For some edge cases
                    request_headers = dict(request.headers)
                    # request_headers = headers
                    url = parse.urlparse(uri)
                    response_headers = placebo._get_headers(url,
                                                            request_headers,
                                                            request.body)

                    response_body = placebo._get_body(url,
                                                      request_headers,
                                                      request.body)
                    status = placebo._get_status(url,
                                                 request_headers,
                                                 request.body)
                    return (status, response_headers, response_body)
                    # return response.status, response.headers, response.data
                url = placebo._get_url()
                if isinstance(url, (parse.ParseResult, parse.SplitResult)):
                    url = url.geturl()

                httpretty.register_uri(getattr(httpretty, method),
                                       url,
                                       body=get_body)
                response = fun(*args, **kwargs)
                return response

            # run-time check if httppretty is enabled.
            # We must enable httpretty only once.
            # This is necessary to chain
            # multiple mock objects together.
            if not httpretty.is_enabled():
                _run = httpretty.activate(_run)
            return _run()
        return _wrapper
    return decorator
