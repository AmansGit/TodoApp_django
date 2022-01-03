from django.shortcuts import render

# Create your views here.
def todolist(request):
	context = {
		"welcome": "Welcome to TodoList Page"
	}
	return render(request, 'todolist.html', context)

def contact(request):
	context = {
		"welcome": "Welcome to Contact Page"
	}
	return render(request, 'contact.html', context)

def about(request):
	context = {
		"welcome": "Welcome to About Page"
	}
	return render(request, 'about.html', context)