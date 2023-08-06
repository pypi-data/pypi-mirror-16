# coding:utf-8
from django.views.decorators.cache import cache_page
from django.utils.decorators import available_attrs
from functools import wraps


def cache_anonymous_user(timeout, cache='default'):
    """
    Decorator for views that tries getting the page from the cache but only if user is not logged.

    The request lang is used to generated cache key. Thus, the same page will be 2 times in the
    cache. One time by language.
    """
    def decorator(view_func):

        def _get_parameter(request):
            """
            Add each get parameter to the prefix of cache key
            """
            key_prefix = ""
            for parameter in request.GET:
                if request.GET[parameter.lower()] != "":
                    key_prefix += "".join(["_", parameter.upper(),  "_", request.GET[parameter.lower()]])
            return key_prefix

        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):

            key_prefix = _get_parameter(request)

            if not request.user.is_authenticated():
                key_prefix += "_LANG_" + request.LANGUAGE_CODE
                return cache_page(timeout, key_prefix=key_prefix, cache=cache)(view_func)(request, *args, **kwargs)

            else:
                return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator
