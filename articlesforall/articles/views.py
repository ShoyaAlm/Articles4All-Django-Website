from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse

from django.views import View
from .models import Author, Article, Topic, Comment
from .forms import ArticleForm


from django.db.models import Q



class homePageView(View):

	template_name = 'article/home-page.html'



	def get(self, request, *args, **kwargs):

		q = request.GET.get('q') if request.GET.get('q') != None else ''

		articles = Article.objects.filter(topic__name__icontains=q)
		
		topics = Topic.objects.all()


		context = {'topics': topics, 'articles': articles}

		return render(request, self.template_name, context)


	def post(self, request, *args, **kwargs):

		topics = Topic.objects.all()

		if request.method == 'POST':

			q = request.POST.get('q') if request.POST.get('q') != None else ''

			articles = Article.objects.filter(Q(title__icontains=q))


		context = {'articles': articles,
				   'topics': topics
				   }

		return render(request, "article/home-page.html", context)


####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$




class ArticleListView(View):

	template_name = 'article/home-page.html'

	query_set = Article.objects.all()


	def get_queryset(self):
		return self.query_set

	def get(self, request, *args, **kwargs):

		context = {'object': self.get_queryset()}

		return render(request, self.template_name, context)



####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$




class AuthorListView(View):

	template_name = 'article/authors.html'


	query_set = Author.objects.all()

	def get_queryset(self):
		return self.query_set

	def get(self, request, *args, **kwargs):
		
		context = {'object': self.get_queryset()}
		return render(request, self.template_name, context)




####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$



class AuthorView(View):
	
	template_name = 'article/profile.html'

	def get(self, request, id=None, *args, **kwargs):

		if id is not None:
			obj = get_object_or_404(Article, id=id)
		
		context = {'object': self.obj}

		return render(request, self.template_name, context)



####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$


class ArticleListView(View):

	template_name = 'article/articles.html'

	query_set = Article.objects.all()


	def get_queryset(self):
		return self.query_set

	def get(self, request, *args, **kwargs):

		context = {'object': self.get_queryset()}

		return render(request, self.template_name, context)


####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$




class AuthorListView(View):

	template_name = 'article/authors.html'


	query_set = Author.objects.all()

	def get_queryset(self):
		return self.query_set

	def get(self, request, *args, **kwargs):
		
		context = {'object': self.get_queryset()}
		return render(request, self.template_name, context)



####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$


class AuthorView(View): 	

	template_name = 'article/profile.html'

	def get(self, request, id=None, *args, **kwargs):

		if id is not None:
			obj = get_object_or_404(Author, id=id)
		
		context = {'object': obj}

		return render(request, self.template_name, context)





####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$

class ArticleListView(View):

	template_name = 'article/articles.html'


	query_set = Article.objects.all()

	def get_queryset(self):

		return self.query_set



	def get(self, request, *args, **kwargs):
		
		context = {'object': self.get_queryset()}
		return render(request, self.template_name, context)



####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$


class ArticleView(View):

	template_name = 'article/article.html'


	def get(self, request, id=None, *args, **kwargs):
		
		obj = get_object_or_404(Article, id=id)

		comments = obj.comment_set.all().order_by('-created')

		context = {'object': obj, 'comments': comments}

		return render(request, self.template_name, context)


	def post(self, request, id=None, *args, **kwargs):

		obj = get_object_or_404(Article, id=id)

		article_comments = obj.comment_set.all().order_by('-created')

		comment = Comment.objects.create(
			user = request.user,
			article = obj,
			body = request.POST.get('body')
		)

		
		# return redirect('article-page', id=obj.id)

		context = {'object': obj, 'comments': article_comments}


		return render(request, self.template_name, context)



####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$




class CreateArticleView(View):

	template_name = 'article/create-article.html'


	def get(self, request, *args, **kwargs):

		form = ArticleForm()
		context = {'form': form}

		return render(request, self.template_name, context)


	def post(self, request, *args, **kwargs):


		form = ArticleForm(request.POST or None)

		if form.is_valid():
			form.save()
			form = ArticleForm()

		context = {'form': form}
		
		return render(request, self.template_name, context)





####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$


class UpdateArticleView(View):

	template_name = 'article/update-article.html'


	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Article, id=id)
			return obj


	def get(self, request, id=None, *args, **kwargs):

		context = {}
		article = self.get_object()
		
		if article is not None:
			form = ArticleForm(instance=article)

			context = {'object': article ,'form': form }
	

		return render(request, self.template_name, context)


	def post(self, request, id=None, *args, **kwargs):

		context = {}

		article = self.get_object()

		if article is not None:
			form = ArticleForm(request.POST or None, instance=article)
			if form.is_valid():
				form.save()
				form = ArticleForm()

		context = {'object': article ,'form': form}

		return render(request, self.template_name, context)



####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$


class DeleteArticleView(View):

	template_name = 'article/delete-article.html'

	def get_object(self):
		id = self.kwargs.get('id')
		obj = None
		if id is not None:
			obj = get_object_or_404(Article, id=id)	
		return obj


	def get(self, request, id=None, *args, **kwargs):

		context = {}
		article = self.get_object()
		if article is not None:
			form = ArticleForm(instance=article)
			
			context = {'object': article, 'form': form}
		return render(request, self.template_name, context)


	def post(self, request, id=None, *args, **kwargs):

		context = {}
		article = self.get_object()
		if article is not None:
			
			article.delete()
			return redirect('articles-page')
				
		context = {'object': article}


		return render(request, self.template_name, context)




####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$



def deleteComment(request, id):

	comment = Comment.objects.get(id=id)

	if request.method == 'POST':

		comment.delete()
		return redirect('article-page', id=comment.article.id)

	context = {'comment': comment}
	return render(request, "article/delete-comment.html", context)



####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$


