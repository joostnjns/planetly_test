from django.urls import path
from .views import top_n, TempByCityCreate, TempByCityDetail, TempByCityUpdate, TempByCityDelete


urlpatterns = [
    path('<int:n>/<int:start>/<int:end>/', top_n, name='top_n'),
    path('create/', TempByCityCreate.as_view(), name='create'),
    path('<int:pk>/', TempByCityDetail.as_view(), name='detail'),
    path('update/<int:pk>/', TempByCityUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', TempByCityDelete.as_view(), name='delete')
]

