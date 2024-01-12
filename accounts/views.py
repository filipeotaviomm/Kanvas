from accounts.models import Account
from accounts.serializers import AccountSerializer
from rest_framework.generics import CreateAPIView


class AccountView(CreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer
