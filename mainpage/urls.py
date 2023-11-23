from rest_framework import routers
from mainpage.views import New_ViewSet,Detail_page_ViewSet,Players_ViewSet

router = routers.DefaultRouter()

router.register(r'news',New_ViewSet,'news')
router.register(r'detail_page',Detail_page_ViewSet,'detail_page')
router.register(r'players_info',Players_ViewSet,'players_info')

urlpatterns = router.urls