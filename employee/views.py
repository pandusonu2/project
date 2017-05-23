from django.http import HttpResponse

#How to access data present in the servers for printing the same in the webpages
def index(request):
	details = employees_company.objects.all()
	return HttpResponse(details)
