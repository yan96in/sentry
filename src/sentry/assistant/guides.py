from __future__ import absolute_import

from django.utils.translation import ugettext_lazy as _


GUIDES = {
    'issue': {
        'id': 1,
        'page': 'issue',
        'cue': _('Click here for a tour of the issue page'),
        'required_targets': ['exception'],
        'steps': [
            {
                'title': _('1. Stacktrace'),
                'message': _(
                    'See which line in your code caused the error and the entire call '
                    'stack at that point.'),
                'target': 'exception',
            },
            {
                'title': _('2. Breadcrumbs'),
                'message': _(
                    'See the events that happened leading up to the error, which often provides '
                    'insight into what caused the error. This includes things like HTTP requests, '
                    'database calls, and any other custom data you record. Breadcrumbs integrate '
                    'seamlessly with many popular web frameworks and record .'),
                'target': 'breadcrumbs',
            },
            {
                'title': _('3. Additional Data'),
                'message': _(
                    'Send custom data with every error, and attach tags to them that you can '
                    'later search and filter by.'),
                'target': 'extra',
            },
        ],
    },
    'event_issue': {
        'id': 2,
        'page': 'issue stream',
        'cue': _('Click here to learn about issues and events'),
        'required_targets': ['issues'],
        'steps': [
            {
                'title': _('1. Events at Sentry'),
                'message': _(
                    'When your application throws an error, that error is captured by Sentry as an Event.'),
                'target': 'issues',
            },
            {
                'title': _('2. Issues at Sentry'),
                'message': _(
                    'Individual Events are then automatically rolled up and grouped into Issues with other like Events. '
                    'A single Issue can represent anywhere from one to thousands of individual Events, depending on how many times a specific error is thrown'),
                'target': 'events',
            },
        ]
    },

}
