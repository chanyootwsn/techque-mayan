from __future__ import unicode_literals

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe

from common.utils import encapsulate
from common.widgets import exists_widget

from .api import settings
from .utils import return_type  # TODO: remove return_type, all settings must be simple types


def setting_list(request):
    new_settings = []
    for namespace, sub_settings in settings.items():
        for sub_setting in sub_settings:
            new_settings.append({
                'module': sub_setting['module'],
                'name': sub_setting['name'],
                'global_name': sub_setting['global_name'],
                'description': sub_setting.get('description', None),
                'exists': sub_setting.get('exists', False),
                'default': sub_setting['default'],
            })

    context = {
        'title': _('Settings'),
        'object_list': sorted(new_settings, key=lambda entry: entry['global_name']),
        'hide_link': True,
        'hide_object': True,
        'extra_columns': [
            {
                'name': _('Name'),
                'attribute': encapsulate(lambda x: mark_safe('<span style="font-weight: bold;">%s</span><br />%s' % (x.get('global_name'), x.get('description'))))
            },
            {
                'name': _('Value'),
                'attribute': encapsulate(
                    lambda x: mark_safe(
                        '<div class="nowrap">%s&nbsp;%s</div>' % (
                            return_type(getattr(x['module'], x['name'])),
                            exists_widget(getattr(x['module'], x['name'])) if x['exists'] else ''
                        )
                    )
                )
            },
        ]
    }

    return render_to_response(
        'appearance/generic_list.html', context,
        context_instance=RequestContext(request)
    )
