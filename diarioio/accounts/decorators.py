from django.contrib.auth.decorators import user_passes_test
from django.conf import settings


def not_logged(function=None, redirect_field_name=settings.REDIRECT_DASHBOARD):
    """
    Decorator for views that checks that the user not is logged in, redirecting
    to the dashboard page if necessary.
    """
    actual_decorator = user_passes_test(
        lambda u: not u.is_authenticated,
        redirect_field_name=redirect_field_name
    )
    if function:
        return actual_decorator(function)
    return actual_decorator
