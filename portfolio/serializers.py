from rest_framework import serializers
from .models import Tag, Project, Post


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name', 'slug']


class ProjectSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = [
            'id', 'title', 'slug', 'tagline', 'description',
            'tags', 'cover_image', 'url', 'github_url',
            'status', 'featured', 'order', 'created_at',
        ]


class PostSerializer(serializers.ModelSerializer):
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = [
            'id', 'title', 'slug', 'excerpt', 'body',
            'tags', 'cover_image', 'published', 'featured',
            'read_time_minutes', 'published_at', 'created_at',
        ]
