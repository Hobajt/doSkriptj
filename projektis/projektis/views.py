from django.http import HttpResponseRedirect

#jenom redirect
def index(request):
    return HttpResponseRedirect('restaurace/')
