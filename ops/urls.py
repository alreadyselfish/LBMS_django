from django.urls import path
from . import views as V

urlpatterns = [
    path('all/', V.all_book_view),
    path('book/<int:pk>/', V.one_book_view),
    path('add/', V.add_book_view),
    path('delete/<int:pk>/', V.one_book_delete),

]
