from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

from scan.models import Patient



@register.filter(name='docyname')
def docyname(patient: Patient):
    if not patient.first_name and not patient.last_name:
        return 'Anonymous'

    return patient.first_name + ' ' + patient.last_name


@register.filter(name='docygender')
def docygender(patient: Patient):
    if patient.gender == 1:
        return mark_safe('<b class="text-babyblue">♂</b>')
    else:
        return mark_safe('<b class="text-babypink">♀</b>')
