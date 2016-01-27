from django.http import HttpResponse
from django.shortcuts import render
from .forms import SearchForm
import isbn_manager

def index(request):
    form = SearchForm()
    return render(request, 'taric_books/index.html', {'form': form})

def results(request):
    response = isbn_manager.search_by_author(request.POST['search_value'])
    context = {
        'books_list': response,
        'form': request.POST['search_value']
    }

    return render(request, 'taric_books/search_result.html', context)

def detail(request, isbn):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'question': question})

def vote(request, isbn):
    return HttpResponse("You're voting on question %s." % isbn)

# def about(request):
#     context = RequestContext(request)
#     return render_to_response('rango/about.html', {}, context)