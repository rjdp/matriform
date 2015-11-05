from django.shortcuts import render
from .models import matriaspirant
from .forms import regform
from django.http import HttpResponse
from django.shortcuts import redirect
from wkhtmltopdf.views import PDFTemplateView
from django.views.generic.base import TemplateView
from django.contrib.auth.decorators import login_required
from django_datatables_view.base_datatable_view import BaseDatatableView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.core.urlresolvers import reverse_lazy
from django.core.urlresolvers import reverse
from django.views.generic import DetailView


class MatriaspirantDetailView(DetailView):

    queryset = matriaspirant.objects.all()

    def get_object(self):
        # Call the superclass
        object = super(MatriaspirantDetailView, self).get_object()
        # Record the last accessed date
        # object.last_accessed = timezone.now()
        # object.save()
        # Return the object
        return object

# https://coderwall.com/p/bz0sng/simple-django-image-upload-to-model-imagefield


# def main(request):
# 	return render(request, 'main.html')

class PDFTemp(PDFTemplateView):
	template_name = "v.html"
	title = "just test"

class PDF(TemplateView):
	template_name = "v.html"
	title = "just test"	





# class AuthorCreate(CreateView):
#     model = Author
#     fields = ['name']

class matriaspirantUpdate(UpdateView):
    model = matriaspirant
    fields = ['profilepic','name','gender','caste']	

class OrderListJson(BaseDatatableView):
        # The model we're going to show
    model = matriaspirant
    columns = ['profilepic.url', 'gender', 'caste', 'dob', 'complexion']

olistjson = login_required(OrderListJson.as_view())

PDFTempview = login_required(PDFTemp.as_view())	



def main(request):

	if request.method == 'POST':
		form = regform(request.POST, request.FILES)

		if form.is_valid():
			form.save()
			# return redirect('main')
			form = regform(initial={'creator': request.user})
			return render(request, 'main.html',{'form':form, 'msg': "Success",'alerttype' : "success"})
		else:
			return render(request, 'main.html',{'form':form, 'msg': "Failed",'alerttype' : "danger"})
	else:
		form = regform(initial={'creator': request.user})
	return render(request, 'main.html',{'form':form})