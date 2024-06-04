from rest_framework.generics import ListAPIView
from ..serializers.person import PersonSerializer


class PeopleListView(ListAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
