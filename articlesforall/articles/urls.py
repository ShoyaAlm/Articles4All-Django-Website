from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (

	RegisterPageView,
	LoginPageView,
	# registerPage,
	# loginPage,

	logoutUser,

	homePageView,
	ArticleListView,

	# authors,
	AuthorListView,

	# profile,
	AuthorView,

	# getArticle,
	ArticleView,

	# createArticle,
	CreateArticleView,


	# updateArticle,
	UpdateArticleView,

	# deleteArticle,
	DeleteArticleView,


	deleteComment,

)

urlpatterns = [
	
	# path('register/', registerPage, name='register-page'),
	# path('login/', loginPage, name='login-page'),
	
	path('register/', RegisterPageView.as_view(), name='register-page'),
	path('login/', LoginPageView.as_view(), name='login-page'),
	

	path('logout/', logoutUser, name='logout-page'),
	
	path('', homePageView.as_view(), name='home-page'),
	
	path('author/', AuthorListView.as_view(), name='author-page'),
	# path('author/', authors, name='authors-page'),

	# path('author/<int:id>', profile, name='author-page'),
	path('author/<int:id>', AuthorView.as_view(), name='author-page'),

	# path('article/<int:id>', getArticle, name='article-page'),
	path('article/<int:id>', ArticleView.as_view(), name='article-page'),
	
	path('article/', ArticleListView.as_view(), name='articles-page'),
	



	# path('article/create/', createArticle, name='create-article'),
	path('article/create/', login_required(CreateArticleView.as_view(), login_url='login-page'), name='create-article'),

	# path('article/update/<int:id>', updateArticle, name='update-article'),
	path('article/update/<int:id>', login_required(UpdateArticleView.as_view(), login_url='login-page'), name='update-article'),

	# path('article/delete/<int:id>', deleteArticle, name='delete-article'),
	path('article/delete/<int:id>', login_required(DeleteArticleView.as_view(), login_url='login-page'), name='delete-article'),

	path('article/delete-comment/<int:id>', deleteComment, name='delete-comment'),


]
