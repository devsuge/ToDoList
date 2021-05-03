from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('task/<int:task_id>', task_detail, name='task'),
    path('add', task_add, name='task_add'),
    path('edit/<int:task_id>', task_edit, name='task_edit'),
    path('delete/task/<int:task_id>', task_delete, name='task_delete'),
    path('delete/file/<int:file_id>', file_delete, name='file_delete'),
    #     path('registration/account', reg_account, name='registration/account'),
    #     path('registration/client', reg_client, name='registration/client'),
    #     path('booking/', empty_rooms, name='empty_rooms'),
    #     path('booking/room/<int:room>', booking_room, name='booking'),
    #     path('client/<int:client_id>', get_client, name='client'),
    #     path('reports/', reports, name='reports'),
    #     path('reports/<int:report_id>/', get_report, name='report'),
]
