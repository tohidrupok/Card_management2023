from django.urls import path
#from book.views import home,store_book,show_books,edit_book
from .import views
urlpatterns = [
    #path('',views.TemplateView.as_view(template_name ='home.html')),
    path('<int:roll>/',views.MyTemplateview.as_view(),{'author':'rupok'}, name ='homepage'),
    # path('store_new_book/', views.store_book, name ='storebook' ),
    path('store_new_book/', views.BookformView.as_view(), name ='storebook' ),
    #path('show_books/', views.show_books, name ='show_books' ),
    path('show_books/', views.BooklistView.as_view(), name ='show_books' ),
      path('book_details/<int:id>', views.BookDetailsView.as_view(), name='book_details'),
    # path('edit_book/<int:pk>',views.edit_book , name='edit_book'),
    path('edit_book/<int:pk>',views.BookUpdateView.as_view() , name='edit_book'),
    path('delete_book/<int:pk>', views.DeleteBookView.as_view(), name='delete_book'),
]
