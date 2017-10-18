from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'words/index.html')

def form_processing(request):
    if request.method == "POST":
        if not 'all_inputs' in request.session:
            request.session['all_inputs'] = []
        else:
            request.session['all_inputs'] = request.session['all_inputs']
        temp = {'word':request.POST['input_word'],'color':request.POST['color'],'font':request.POST['big_font']}
        request.session['all_inputs'].append(temp)
    	return redirect("/")
    else:
    	return redirect("/")