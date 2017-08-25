from django.shortcuts import render

def index(request): 
    number = 6
    # this is your new view - urls.py will catch that someone wants the homepage 
    #and points to this piece of code, which will render the index.html template.
    return render(request, 'index.html', {'number':number,})





"""
There are a ton of different ways to display a template simply in the views, 
and my favorite is Django's shortcut function called render. This is something 
you'll need to import, but Django anticipates that you'll use it and already 
has it added to the top of views.py for us.
"""