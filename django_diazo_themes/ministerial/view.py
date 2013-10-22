"""
This file shows an example view.
It is not part of the theme itself but acts more as documentation.
"""
from django_diazo.utils.dict2xml import mark_safe
from django_diazo.views.generic import DiazoGenericXmlHtmlResponse


class ExampleView(DiazoGenericXmlHtmlResponse):
    def get_context_data(self, **kwargs):
        context = {
            'brand': {'name': 'Brandname', 'url': '/'},
            'title': 'Pagetitle',
            'subtitle': 'Subtitle',
            'menu': [
                {'name': 'Home'},
                {'name': 'Contact', 'class': 'active'},
                {'name': 'Test'},
                {'name': 'Bla'},
                {'name': 'More'},
            ],
            'banner': '//lorempixel.com/1120/500/nightlife',
            'content': mark_safe('<p>Blablablablabla</p><p>Blablablablabla</p>'
                                 '<p class="button-style"><a href="/">Home</a></p>'),
            'news': {'title': 'News', 'newsitems': [
                {'date': '21 october 2013', 'text': 'Bla', 'button': {'name': 'Read more', 'url': '/'}},
                {'date': '22 october 2013', 'text': 'Ble', 'button': {'name': 'Read more', 'url': '/'}},
                {'date': '23 october 2013', 'text': 'Bli', 'button': {'name': 'Read more', 'url': '/'}},
                {'date': '24 october 2013', 'text': 'Blo', 'button': {'name': 'Read more', 'url': '/'}},
            ]},
            'lhs_portlet': {'title': 'Left', 'more': {'name': 'More details', 'url': '/'},
                            'content': [
                                {'name': 'Link 1', 'url': '/'},
                                {'name': 'Link 2', 'url': '/'},
                                {'name': 'Link 3', 'url': '/'},
                                {'name': 'Link 4', 'url': '/'},
                                {'name': 'Link 5', 'url': '/'},
                                {'name': 'Link 6', 'url': '/'},
                            ]},
            'center_portlet': {'title': 'Center', 'more': {'name': 'More details', 'url': '/'},
                               'content': mark_safe('<p>blaaaaaaa</p>'
                                                    '<p><img src="//lorempixel.com/500/200/sports" /></p>')},
            'rhs_portlet': {'title': 'Right',
                            'content': [
                                {'image': '//lorempixel.com/78/78/technics',
                                 'text': 'This is a text that should be long enough to cover two lines.',
                                 'posted': {'date': '21 october 2013', 'extra': '(2) Comments'}},
                                {'image': '//lorempixel.com/78/78/food',
                                 'text': 'This is a text that should be long enough to cover two lines.',
                                 'posted': {'date': '22 october 2013', 'extra': '(4) Comments'}},
                                {'image': '//lorempixel.com/78/78/city',
                                 'text': 'This is a text that should be long enough to cover two lines.',
                                 'posted': {'date': '23 october 2013'}},
                            ]},
            'footer': mark_safe('<p>This is the footer</p>'),
        }
        return dict(super(ExampleView, self).get_context_data(**kwargs).items() + context.items())
