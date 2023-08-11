from rest_framework import generics, permissions
from .serializers import OrderSerializer
from rest_framework.response import Response
from .models import Order


class OrderAPIView(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = permissions.IsAuthenticated,

    def get(self, request, *args, **kwargs):
        user = request.user
        orders = user.orders.all()
        serializer = OrderSerializer(instance=orders, many=True)
        return Response(serializer.data, status=200)


class OrderConfirmView(generics.RetrieveAPIView):
    permission_classes = permissions.IsAuthenticated,

    def get(self, request, pk):
        user = request.user
        order = Order.objects.get(pk=pk)
        if user.email != order.owner.email:
            return Response('User doesnt match with the order owner', status=400)
        elif user.balance < order.total_sum:
            return Response('Not enough credits')
        order.status = 'completed'
        order.save()
        user.balance -= order.total_sum
        user.save()
        return Response({'message': 'Order confirmed and payment successful'}, status=200)
