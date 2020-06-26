from rest_framework import viewsets
from rest_framework.response import Response
from .models import Snip
from .ApiSerializer import SnipSerializer

from rest_framework.response import Response
from rest_framework import status

class SnippetViewset(viewsets.ModelViewSet):
    serializer_class  = SnipSerializer
    
    def get_queryset(self):
        snips  = Snip.objects.all()
        return snips
    
    def retrieve(self,request,*args,**kwargs):
        pass

    def create(self,request,*args,**kwargs):
        snip_data = SnipSerializer(data=request.data)
        if(snip_data.is_valid()):
            snip_data.save()
            return Response(snip_data.data,status=status.HTTP_201_CREATED)
        else:
            return Response(snip_data.data,status=status.HTTP_400_BAD_REQUEST)