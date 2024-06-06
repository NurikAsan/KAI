from ..models.common_models import Category


class CategoryService:
    @staticmethod
    def get_categories():
        return Category.objects.all()
