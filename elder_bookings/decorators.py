from functools import wraps
from django.shortcuts import redirect

def custom_login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('login_page')  # or your actual login route name
        return view_func(request, *args, **kwargs)
    return _wrapped_view