import pdb

from ..models.common_models import PageGenerator
from django.db.models import Q


class PageGeneratorService:
    @staticmethod
    def get_pages(cat_id, sub_cat_id, sub_sub_cat_id):
        if sub_sub_cat_id is not None:
            queryset = PageGenerator.objects.filter(
                Q(category_id=cat_id) & Q(subcategory_id=sub_cat_id) & Q(subcategory2_id=sub_sub_cat_id)
            )
        else:
            queryset = PageGenerator.objects.filter(
                Q(category_id=cat_id) & Q(subcategory_id=sub_cat_id)
            )
        # pdb.set_trace()
        return queryset
