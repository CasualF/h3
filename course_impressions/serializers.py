from rest_framework import serializers
from .models import Review, Favorite


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.id')
    owner_email = serializers.ReadOnlyField(source='owner.email')
    course = serializers.ReadOnlyField(source='course.id')

    class Meta:
        model = Review
        fields = '__all__'

    def validate(self, attrs):
        rating = attrs.get('rating')
        if not rating:
            return serializers.ValidationError('Rating was not handed')
        if int(rating) not in range(1, 6):
            return serializers.ValidationError('Rating should be from 1 to 5')
        return attrs

    def create(self, validated_data):
        course = self.context.get('course')
        owner = self.context.get('owner')
        validated_data['course'] = course
        validated_data['owner'] = owner
        return super().create(validated_data)


class FavoriteSerializer(serializers.ModelSerializer):
    owner_email = serializers.ReadOnlyField(source='owner.email')
    course_title = serializers.ReadOnlyField(source='course.title')

    class Meta:
        model = Favorite
        fields = ['owner_email', 'course_title']
