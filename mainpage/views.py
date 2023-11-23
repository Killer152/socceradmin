from django.shortcuts import render
from rest_framework.response import Response
from mainpage.models import News,Detail_page,Players
from rest_framework import viewsets, status
from mainpage.serializers import News_Serializer_ru,News_Serializer,Detail_page_Serializer,Detail_page_Serializer_ru,Players_Serializer,Players_Serializer_ru

class New_ViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = News_Serializer
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return News_Serializer(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return News_Serializer_ru(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)


class Detail_page_ViewSet(viewsets.ModelViewSet):
    queryset = Detail_page.objects.all()
    serializer_class = Detail_page_Serializer
    def get_serializer(self, *args, **kwargs):
      if self.request.query_params.get('lang') == 'en':
          return Detail_page_Serializer(*args, **kwargs)
      elif self.request.query_params.get('lang') == 'ru':
          return Detail_page_Serializer_ru(*args, **kwargs)
      else:
          return super().get_serializer(*args, **kwargs)


class Players_ViewSet(viewsets.ModelViewSet):
  queryset = Players.objects.all()
  serializer_class = Players_Serializer
  pagination_class = None
  def get_serializer(self, *args, **kwargs):
    if self.request.query_params.get('lang') == 'en':
        return Players_Serializer(*args, **kwargs)
    elif self.request.query_params.get('lang') == 'ru':
        return Players_Serializer_ru(*args, **kwargs)
    else:
        return super().get_serializer(*args, **kwargs)

