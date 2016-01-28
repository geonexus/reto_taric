from django.http import HttpResponse
from django.shortcuts import render
from django.utils.text import slugify
from .forms import SearchForm, PageForm
import isbn_manager

def index(request):
    form = SearchForm()
    return render(request, 'taric_books/index.html', {'form': form})

def author(request):
    form = PageForm()
    author_name = slugify(request.POST['search_value'])

    print "this is author name" + author_name
    response = isbn_manager.search_by_author(author_name, page=None)
    context = {
        'page_form': form,
        'books_list': response.data,
        'page_count': response.page_count,
        'current_page': response.current_page,
        'next_page': int(response.current_page) + 1,
        'author_name': author_name
    }

    return render(request, 'taric_books/search_result.html', context)

def author_page(request, author):
    form = PageForm()
    author_name = slugify(author)
    page = request.POST['page_value']
    print "this is author name" + author_name
    response = isbn_manager.search_by_author(author_name, page=page)
    context = {
        'page_form': form,
        'books_list': response.data,
        'page_count': response.page_count,
        'current_page': response.current_page,
        'next_page': int(response.current_page) + 1,
        'author_name': author_name
    }

    return render(request, 'taric_books/search_result.html', context)

def results(request):
    response = isbn_manager.search_by_author(request.POST['search_value'])
    context = {
        'books_list': response.data,
        'page_count': response.page_count,
        'current_page': response.current_page,
        'form': request.POST['search_value']
    }

    return render(request, 'taric_books/search_result.html', context)

def isbn(request, isbn):
    response = isbn_manager.search_by_ISBN(isbn)
    context = {
        'book_details': response.data,
    }

    return render(request, 'taric_books/isbn.html', context)
