from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from .views import IllnessListView, IllnessCreateView, IllnessUpdateView

router = routers.DefaultRouter()
# router.register(r'category', CategoryView, 'category')
# router.register(r'illness', IllnessView, 'illness')
# urlpatterns = [
#     # path('', include(router.urls)),
#     path('illness/', user_list, name='illness'),
# ] 
urlpatterns = [
    # path('', include(router.urls)),
    path('create', IllnessCreateView.as_view()),
    path('<str:icd10_code>/', IllnessListView.as_view()),
    path('<str:icd10_code>/update', IllnessUpdateView.as_view()),
]
# urlpatterns = [
# 	# url(r'date-list/(?P<movie_id>.+)/', views.DateListView.as_view())
# 	path('<str:icd10_code>/', IllnessView.as_view()),
#     # path('', include(router.urls)),
#     # path('illness/<int:year>', user_list, name='illness'),
# ]
# urlpatterns = patterns('',
# 	path('<int:year>/', IllnessView),
#     #...
#     # url(r'^article/(\d+)/$', IllnessView, name='article_by_id'),
#     #...
# )
