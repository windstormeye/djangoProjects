from django.urls import path
from . import views

urlpatterns = [
	# http://localhost:8000/blog/1
	path('<int:blog_pk>', views.blog_detail, name="blog_detail"),
	path('type/<int:blogs_type_pk>', views.blogs_with_type, name="blogs_with_type")
]	