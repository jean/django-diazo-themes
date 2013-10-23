"""
Register the theme.
"""
from django_diazo.theme import DiazoTheme, registry


class AngledTheme(DiazoTheme):
    name = 'Angled Theme'
    slug = 'angled_theme'


registry.register(AngledTheme)
