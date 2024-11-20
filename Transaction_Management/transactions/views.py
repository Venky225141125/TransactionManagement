from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Transaction
from .serializer import TransactionSerializer

class TransactionListCreateAPIView(generics.ListCreateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    def get_queryset(self):
        user_id = self.request.query_params.get('user_id')
        if user_id:
            return Transaction.objects.filter(user_id=user_id)
        return Transaction.objects.all()

  
    def perform_create(self, serializer):
        user_id = self.request.data.get('user')
        user = get_object_or_404(User, id=user_id) 
        serializer.save(user=user) 

    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)
    
class TransactionDetailAPIView(generics.RetrieveUpdateAPIView):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)
    
    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        status_update = request.data.get('status')
        
        if status_update not in ['COMPLETED', 'FAILED']:
            return Response({"error": "Invalid status value."}, status=status.HTTP_400_BAD_REQUEST)
        
        instance.status = status_update
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
