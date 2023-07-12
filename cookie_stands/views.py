from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .models import Cookie_stands
from .permissions import IsOwnerOrReadOnly
from .serializers import Cookie_standsSerializer


class Cookie_standsList(ListCreateAPIView):
    queryset = Cookie_stands.objects.all()
    serializer_class = Cookie_standsSerializer


class Cookie_standsDetail(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Cookie_stands.objects.all()
    serializer_class = Cookie_standsSerializer
