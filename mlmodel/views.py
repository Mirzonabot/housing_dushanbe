from django.shortcuts import render,HttpResponse,HttpResponseRedirect

from .forms import NameForm, MyGeoForm


# Create your views here.
def index(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("In if")
        print(request.POST)
        # create a form instance and populate it with data from the request:
        # form = NameForm(request.POST)
        # check whether it's valid:
        # if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            # return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    
    form = MyGeoForm()

    return render(request, 'index.html', {'form': form})