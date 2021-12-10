from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import action, authentication_classes,api_view,renderer_classes
# from rest_framework.parsers import JsonParser
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
from .models import Events
from .serializers import EventSerializer
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.utils.decorators import method_decorator
from datetime import datetime
# Create your views here.
# crreating class based api views


class EventAPIView(APIView):

    def get(self, request):
        events = Events.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('/')
        return redirect('/')



class EventDetail(APIView):
    # print("hqqqqqq")
    def get_object(self,pk):
        try:
            return Events.objects.get(id = pk)
        except Events.DoesNotExist:
            raise Http404

    def get(self, request,day):
        print(day)
        day = datetime.strptime(day, "%Y-%m-%d")
        # print(day)
        events = Events.objects.filter(created_date = day.date())
        print(events)
        serializer = EventSerializer(events,many=True)
        return Response(serializer.data)


class EventDelete(APIView):
    @csrf_exempt
    def post(self,request,pk,day):
        data =dict()
        print("HII")
        event = Events.objects.get(id = pk)
        if event:
            event.delete()
            data['message'] =  "Room deleted!"
        else:
            data['message'] =  "Error!"
        return JsonResponse(data)
