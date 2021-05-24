from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.reverse import reverse
from tasks.models import Neo
from tasks.serializers import NeoSerializer
from rest_framework.decorators import api_view
from rest_framework import status
from tasks.jsondict import *
import logging
logger = logging.getLogger(__name__)

@api_view(['GET', 'POST'])
def neo_list(request):
    if request.method == 'GET':
        neos = Neo.objects.all()
        neos_serializer = NeoSerializer(neos, many=True)
        return Response(neos_serializer.data)

    elif request.method == 'POST':
        data = request.data
        json_data = data
        first_dict = {k:v for (k,v) in json_data.items() if k == 'element_count' }
        secound_list = [v for (k,v) in json_data.items() if k == 'near_earth_objects' ]
        third_list = []
        fourth_list = []
        keys = ['id', 'neo_reference_id', 'name','nasa_jpl_url', 'is_potentially_hazardous_asteroid']
        q = len(keys)
        for element in secound_list:
            for key, value in element.items():
                foo = value
                for bar in foo:
                    for key , value in bar.items():
                        if key in keys:
                            third_list.append(value)
        multiple_lists = [third_list[i * q:(i + 1) * q] for i in range((len(third_list) + q - 1) // q )]
        list_of_dictiories = [] 
        for item in multiple_lists:
            rtmp =  dict(zip(keys, item))
            list_of_dictiories.append(rtmp)                    
        

        print("hey testing it")
        for item in list_of_dictiories:
            neo_serializer = NeoSerializer(data=item)
            print(item)
            neo_serializer.is_valid(raise_exception=True)
            print("randakaa")
            neo_serializer.save()
        return Response(neo_serializer.data, status=status.HTTP_201_CREATED)    
        return Response(neo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
                
            

        
        
            
            
                
        
        

@api_view(['GET', 'PUT', 'DELETE'])
def neo_detail(request, pk):
    try:
        neo = Neo.objects.get(pk=pk)
    except Neo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 

    if request.method == 'GET':
        neo_serializer = NeoSerializer(neo)
        return Response(neo_serializer.data)

    elif request.method == 'PUT':
        neo_serializer = NeoSerializer(neo, data=request.data)
        neo_serializer.save()
        return Response(neo_serializer.data)
        return Response(neo_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        neo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)    



    
   
    

#context = {'data': serializer.data, 'names': list_of_names, 'usernos': list_of_usernos} # change it as per your requirement
        #return Response(context)
#response = {"uploadFiletotheYoutubeVideo" : "uploadFiletotheYoutubeVideo"}
        #return Response(json.dumps(response, default=json_util.default))
 

#if neo_serializer.is_valid():









# Create your views here.
