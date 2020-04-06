#from django.shortcuts import render
from django.views.generic import CreateView
from .models import Upload
from .response import JSONResponse, response_mimetype

class FileCreateView(CreateView):
    model = Upload
    fields = '__all__'

    def form_valid(self, form):
        self.object = form.save()
        data = {'status': 'success'}
        response = JSONResponse(data, mimetype=response_mimetype(self.request))
        return response