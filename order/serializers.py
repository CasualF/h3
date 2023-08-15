from rest_framework import serializers
from .models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):
    course_title = serializers.ReadOnlyField(source='course.title')

    class Meta:
        model = OrderItem
        fields = ('course', 'quantity', 'course_title')


class OrderSerializer(serializers.ModelSerializer):
    status = serializers.CharField(read_only=True)
    owner = serializers.ReadOnlyField(source='owner.email')
    courses = OrderItemSerializer(write_only=True, many=True)

    class Meta:
        model = Order
        fields = '__all__'

    def create(self, validated_data):
        courses = validated_data.pop('courses')
        request = self.context.get('request')
        user = request.user
        total_sum = 0

        for course in courses:
            try:
                try:
                    total_sum += course['quantity'] * course['course'].price
                except:
                    total_sum += course['course'].price
            except:
                pass
        order = Order.objects.create(owner=user, status='in_process',
                                     total_sum=total_sum, **validated_data)
        for course in courses:
            try:
                OrderItem.objects.create(order=order,
                                         course=course['course'],
                                         quantity=course['course'].quantity)
            except:
                OrderItem.objects.create(order=order,
                                         course=course['course'])

        return order

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['courses'] = OrderItemSerializer(instance.items.all(),
                                                        many=True).data
        return representation
