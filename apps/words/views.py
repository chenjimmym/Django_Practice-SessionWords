from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
# Create your views here.
def index(request):
    print strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return render(request, 'words/index.html')

def form_processing(request):
    if request.method == "POST":
        if not 'all_inputs' in request.session:
            request.session['all_inputs'] = []
        else:
            request.session['all_inputs'] = request.session['all_inputs']
        temp = {'word':request.POST['input_word'],'color':request.POST['color'],'font':request.POST['big_font'], 'time':strftime("%Y-%m-%d %H:%M:%S", gmtime())}
        request.session['all_inputs'].append(temp)
    	return redirect("/")
    else:
    	return redirect("/")

def clear_session(request):
    request.session['all_inputs'] = []
    return redirect("/")