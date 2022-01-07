from django.shortcuts import render

# Create your views here.
def todolist(request):
	context = {
		"welcome": "Welcome to TodoList Page",
		"title": "Home"
	}
	return render(request, 'todolist.html', context)

def contact(request):
	context = {
		"welcome": "Welcome to Contact Page",
		"title": "Contact"
	}
	return render(request, 'contact.html', context)

def about(request):
	context = {
		"welcome": "Welcome to About Page",
		"title": "About"
	}
	return render(request, 'about.html', context)