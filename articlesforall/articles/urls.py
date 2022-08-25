from django.urls import path

from .views import (

	# homePage,
	ArticleListView,

	authors,
	profile,
	article,
	getArticle,
	createArticle,
	deleteArticle,
	updateArticle,


)

urlpatterns = [

	# path('', homePage, name='home-page'),
	path('', ArticleListView.as_view(), name='home-page'),
	
	path('author/', authors, name='authors-page'),
	path('author/<int:id>', profile, name='author-page'),

	path('article/', article, name='articles-page'),
	path('article/<int:id>', getArticle, name='article-page'),
	path('article/create/', createArticle, name='create-article'),
	path('article/delete/<int:id>', deleteArticle, name='delete-article'),
	path('article/update/<int:id>', updateArticle, name='update-article'),



]