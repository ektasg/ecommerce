from django.shortcuts import render

# create index view for landing page
def index(request):
    return render(request, 'template.html')

def store(request):
    return render(request, 'store.html')


