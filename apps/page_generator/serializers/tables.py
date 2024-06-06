from rest_framework import serializers
from ..models.table import Table, TableCodeColumn, TableDirectionColumn


class TableDirectionColumnSerializer(serializers.ModelSerializer):

    class Meta:
        model = TableDirectionColumn
        fields = (
            'direction',
            'status1',
            'status2',
            'links'
        )


class TableCodeColumnSerializer(serializers.ModelSerializer):
    table_directions_column = TableDirectionColumnSerializer(read_only=True, many=True)

    class Meta:
        model = TableCodeColumn
        fields = (
            'code',
            'year',
        )


class TableSerializer(serializers.ModelSerializer):
    table_codes_column = TableCodeColumnSerializer(read_only=True, many=True)

    class Meta:
        model = Table
        fields = (
            'name',
            'table_codes_column'
        )
