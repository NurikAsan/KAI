from ..models.main import MainPage


class MainPageService:
    @staticmethod
    def get_main_content():
        return MainPage.objects.all()
