from rest_framework import serializers
from .models import Like, Dislike, Comment


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'


class DislikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dislike
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_email = serializers.ReadOnlyField(source='owner.email')
    lesson = serializers.ReadOnlyField(source='lesson.id')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        lesson = self.context.get('lesson')
        owner = self.context.get('owner')
        validated_data['owner'] = owner
        validated_data['lesson'] = lesson
        return super().create(validated_data)


class CommentListSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')

    class Meta:
        model = Comment
        fields = ['id', 'owner_email', 'body', 'created_at']