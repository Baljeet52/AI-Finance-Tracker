from rest_framework import viewsets
from .models import Transaction
from .serializers import TransactionSerializer
from ai_engine.autogen_agent import categorize_transaction

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def perform_create(self, serializer):
        description = self.request.data.get("description", "")
        category = categorize_transaction(description)
        serializer.save(category=category)
