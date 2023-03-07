from django import template

from authorization.forms import NewUserForm, UserLoginForm


register = template.Library()


@register.simple_tag()
def get_registration_form():
    return NewUserForm()


@register.simple_tag
def get_login_form():
    return UserLoginForm
