from rest_framework import serializers
from apod.models import Image, Author


class AuthorSerializers(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['name']
    # name = serializers.CharField(read_only=True)
    #
    # def create(self, validated_data):
    #     return Author.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.name = validated_data.get('name', instance.name)
    #     instance.save()
    #     return instance


class ImageSerializers(serializers.Serializer):
    author = serializers.CharField(read_only=True)
    date_photo = serializers.DateTimeField()
    data_save = serializers.DateTimeField()
    explanation = serializers.CharField(read_only=True)
    hd_url_image = serializers.CharField(read_only=True)
    url_image = serializers.CharField(read_only=True)
    media_type = serializers.CharField(read_only=True)
    version = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)

    def create(self, validated_data):
        return ImageSerializers.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get('author', instance.author)
        instance.date_photo = validated_data.get('date_photo', instance.date_photo)
        instance.date_save = validated_data.get('date_save', instance.date_save)
        instance.explanation = validated_data.get('explanation', instance.explanation)
        instance.hd_url_image = validated_data.get('hd_url_image', instance.hd_url_image)
        instance.url_image = validated_data.get('url_image', instance.url_image)
        instance.media_type = validated_data.get('media_type', instance.media_type)
        instance.version = validated_data.get('version', instance.version)
        instance.title = validated_data.get('title', instance.title)
        instance.save()
        return instance

