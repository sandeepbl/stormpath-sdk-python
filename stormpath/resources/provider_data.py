"""Stormpath Provider Data resource mappings."""


from .base import Resource, DictMixin


class ProviderData(Resource, DictMixin):
    """Stormpath Provider Data resource.

    More info in documentation:
    http://docs.stormpath.com/python/product-guide/#integrating-with-google
    http://docs.stormpath.com/python/product-guide/#integrating-with-facebook
    """
