"""
Register the theme.
"""
from django_diazo.theme import DiazoTheme, registry


class MinisterialTheme(DiazoTheme):
    name = 'Ministerial'
    slug = 'ministerial'


registry.register(MinisterialTheme)
