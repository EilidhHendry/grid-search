from django.shortcuts import render
from forms import InputForm
from path_search import best_path

def index(request):
    result = ""
    grid = ""
    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            if form.cleaned_data.get('grid'):
                data = form.cleaned_data.get('grid')
                grid = eval(data)
                result = best_path.grid_search(grid)
    else:
        form = InputForm(initial={'text': 'text here'})
    return render(request, 'index.html', {'grid': grid, 'result': result, 'form': form})
