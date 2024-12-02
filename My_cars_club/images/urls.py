from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('new_car', views.new_car, name='new-car'),
    path('update_car/<int:car_id>', views.car_edit, name='update-car'),
    path('delete_car/<int:car_id>', views.car_delete, name='delete-car'),
    path('edit_and_delete_car/', views.edit_and_delete_car, name='edit-delete-car'),
    path('search_car/', views.search_car, name='search-car'),
    path('upload/', views.upload_video, name='upload_video'),
    path('videos/', views.video_list, name='video_list'),
    path('import_json', views.import_json_file, name='import_json'),
    path('upload_xml', views.upload_xml, name='upload_xml'),
    path('upload_csv', views.upload_csv, name='upload_csv'),
    path('export_to_csv/', views.export_to_csv, name='export_car_csv_file'),
    path('export_json/', views.JsonCarListView.as_view(), name='export_json'),
    path('export_xml', views.XMLCarViewSet.as_view(), name='export_xml'),
]
