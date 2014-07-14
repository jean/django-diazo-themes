"""
This file shows an example view.
It is not part of the theme itself but acts more as documentation.
"""
from django.conf import settings
from django.http import Http404, HttpResponsePermanentRedirect
from django_diazo.utils.dict2xml import mark_safe
from django_diazo.views.generic import DiazoGenericXmlHtmlResponse


class ExampleView(DiazoGenericXmlHtmlResponse):
    def get_context_data(self, **kwargs):
        context = {
            'brand': {'name': 'Brandname', 'url': '/'},
            'title': 'Pagetitle',
            'subtitle': 'Subtitle',
            'menu': [
                {'name': 'Home', 'url': '/'},
                {'name': 'Contact', 'url': '/contact'},
                {'name': 'Test', 'url': '/test'},
                {'name': 'Bla', 'url': '/bla'},
                {'name': 'More', 'url': '/more'},
            ],
            'banner': '//lorempixel.com/1120/500/nightlife',
            'content': mark_safe('<p>Blablablablabla</p><p>Blablablablabla</p>'
                                 '<p class="button-style"><a href="/">Home</a></p>'),
            'news': {'title': 'News', 'newsitems': [
                {'title': 'Aaa', 'date': '21 october 2013', 'text': 'Bla', 'button': {'name': 'Read more', 'url': '/'}},
                {'title': 'Bbb', 'date': '22 october 2013', 'text': 'Ble', 'button': {'name': 'Read more', 'url': '/'}},
                {'title': 'Ccc', 'date': '23 october 2013', 'text': 'Bli', 'button': {'name': 'Read more', 'url': '/'}},
                {'title': 'Ddd', 'date': '24 october 2013', 'text': 'Blo', 'button': {'name': 'Read more', 'url': '/'}},
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

        def menu_item(page):
            if not page:
                return context['menu'][0]
            else:
                for item in context['menu']:
                    if page == '/' or item['url'] == page[0:-1]:
                        return item
            return None

        item = menu_item(self.request.path)
        if item:
            item['class'] = 'active'

        return dict(super(ExampleView, self).get_context_data(**kwargs).items() + context.items())

    def dispatch(self, request, *args, **kwargs):
        if not request.path.endswith('/') and settings.APPEND_SLASH:
            return HttpResponsePermanentRedirect('{0}/'.format(request.path))
        return super(ExampleView, self).dispatch(request, *args, **kwargs)
