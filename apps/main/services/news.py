from ..models.news import News


class NewsService:
    @staticmethod
    def get_new():
        return News.objects.all()
