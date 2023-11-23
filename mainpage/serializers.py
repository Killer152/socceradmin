from mainpage.models import News, Detail_page,Players
from rest_framework import serializers

class News_Serializer(serializers.ModelSerializer):
  detailpage = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model=News
    fields=[
      'id',
      'title_en',
      'post_time',
      'image',
      'detailpage'

    ]
class News_Serializer_ru(serializers.ModelSerializer):
  detailpage=serializers.PrimaryKeyRelatedField(many=True, read_only=True)
  class Meta:
    model=News
    fields=[
      'id',
      'title_ru',
      'post_time',
      'image',
      'detailpage'
    ]


class Detail_page_Serializer(serializers.ModelSerializer):
  post_time = serializers.DateField(source='detailpage.post_time')
  class Meta:
    model=Detail_page
    fields=[
      'id',
      'title_en',
      'post_time',
      'image',
      'text_en',
      'video'

  ]

class Detail_page_Serializer_ru(serializers.ModelSerializer):
  post_time = serializers.DateField(source='detailpage.post_time')
  class Meta:
    model=Detail_page
    fields=[
      'id',
      'title_ru',
      'post_time',
      'video',
      'image',
      'text_ru',
      
  ]

class Players_Serializer(serializers.ModelSerializer):
  
  class Meta:
    model=Players
    fields=[
      'id',
      'amplua_en',
      'height',
      'full_name_en',
      'date_of_brith',
      'club_en',
      'postion_en',
      'image'
    ]
class Players_Serializer_ru(serializers.ModelSerializer):
  
  class Meta:
    model=Players
    fields=[
      'id',
      'amplua_ru',
      'height',
      'full_name_ru',
      'date_of_brith',
      'club_ru',
      'postion_ru',
      'image'
    ]

