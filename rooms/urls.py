from django.urls import path, include
from .views import RoomListView,RoomDetailView,RoomFormView,RoomUpdateView,RoomDeleteView,RoomSearchView,room_liking


urlpatterns = [
    path('',RoomListView.as_view(),name='room_list'),
    path('rooms/<pk>/details',RoomDetailView.as_view(),name='room_detail'),
    path('new-room/',RoomFormView.as_view(),name='room_form'),
    path('room/<pk>/update/',RoomUpdateView.as_view(),name='room_update'),
    path('room/<pk>/delete/',RoomDeleteView.as_view(),name='room_delete'),
    path('room-search/',RoomSearchView.as_view(),name='room_search'),
    path('room-like/<pk>/',room_liking,name='room_like')
]