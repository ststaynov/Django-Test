from django.shortcuts import render
from django_facebook.utils import get_registration_backend
from django_facebook.connect import CONNECT_ACTIONS
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required

def register(request):
    """
    A very simplistic register view
    """
    backend = get_registration_backend()
    form_class = backend.get_form_class(request)
    template_name = backend.get_registration_template()

    if request.method == 'POST':
        form = form_class(data=request.POST, files=request.FILES)
        if form.is_valid():
            new_user = backend.register(request,
                                        form=form, **form.cleaned_data)
            # keep the post behaviour exactly the same as django facebook's
            # connect flow
            response = backend.post_connect(
                request, new_user, CONNECT_ACTIONS.REGISTER)
            return response
    else:
        form = form_class()

    context = {'form': form}
    response = render(request, template_name, context)

    return response

# Custom Profile View TODO find how to pass the User object
@login_required
def profile_details(request,
                         template_name='registration/profile.html',
                         extra_context=None):
    context = {}
    if extra_context is not None:
        context.update(extra_context)

    return TemplateResponse(request, template_name, context)