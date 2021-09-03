from rest_framework import fields, serializers
from blog.models import Post
#modeldagi malumotlarni json kurinshga uzgartirish
from django.contrib.auth import get_user_model

class PostSerializer(serializers.ModelSerializer):
    #author-username
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ['id','title','content','date_posted','author','likes'] #'__all__'
        
class UserSerializers(serializers.ModelSerializer):
    #user-posts-id
    posts = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = get_user_model()
        fields = ["id","username",'password','posts']