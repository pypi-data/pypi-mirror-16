Using
=====

``settings.py``::

    INSTALLED_APPS = [
        ...
        'django_auth_email',
        ...
    ]

And run command::

    ./manager migrate

Will be create table in the DB -- ``django_auth_email_option``. Model::



Sign-in/up::

    >>> from django_auth_email.models import DEAMng
    >>> auth = DEAMng()
    >>> code = auth.set_code(form.instance.email)
    >>> print(code)
    c0fca3619e2a0692a0f7bc79388cc51b5c805b22f5718e342bafd986


Authorization::

    >>> check = DEAMng()
    >>> if check.is_valid(code):
    >>>     auth.login(request, check.get_user())
    >>>     check.clean_dea()

