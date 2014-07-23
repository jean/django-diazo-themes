"""
Register the theme.
"""
from django_diazo.theme import DiazoTheme, registry


class IwlearnTheme(DiazoTheme):
    name = 'IW:LEARN'
    slug = 'iwlearn'
    pattern = '^(?!.*admin)'  # Theme everything but /admin


registry.register(IwlearnTheme)
