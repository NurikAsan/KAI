from rest_framework.generics import ListAPIView
from ..serializers.tables import TableSerizalizer


class TableVListView(ListAPIView):
    queryset = Table.objects.all()
    serializer_class = TableSerizalizer
