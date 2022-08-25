from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse

from django.views import View

from .models import Author, Article

from .forms import ArticleForm





class ArticleListView(View):

	template_name = 'article/home-page.html'

	query_set = Article.objects.all()


	def get_queryset(self):
		return self.query_set

	def get(self, request, *args, **kwargs):

		context = {'object': self.get_queryset()}

		return render(request, self.template_name, context)



# def homePage(request):

# 	articles = Article.objects.all()

# 	context = {'articles': articles}

# 	return render(request, "article/home-page.html", context)


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


# def authors(request):

# 	authors = Author.objects.all()

# 	context = {'authors': authors}

# 	return render(request, "article/authors.html", context)



####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$


class AuthorView(View): 	### THIS FUNCTION WORKS FOR SEARCHING 1 OR MORE AUTHORS
	
	template_name = 'article/profile.html'

	

	def get(self, request, id=None, *args, **kwargs):

		if id is not None:
			# query_set = Article.objects.get(id=id)
			obj = get_object_or_404(Article, id=id)
		
		context = {'object': self.obj}

		return render(request, self.template_name, context)

# def profile(request, id):

# 	author = Author.objects.get(id=id)

# 	context = {'author': author}

# 	return render(request, "article/profile.html", context)



####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$


def article(request):

	articles = Article.objects.all()

	context = {'articles': articles}

	return render(request, "article/articles.html", context)



####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$

def getArticle(request, id):

	article = Article.objects.get(id=id)

	context = {'article': article}

	return render(request, "article/article.html", context)

####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$



def createArticle(request):

	form = ArticleForm()

	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('articles-page')

	context = {'form': form}
	return render(request, "article/create-article.html", context)


####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$

def updateArticle(request, id):

	article = Article.objects.get(id=id)
	
	form = ArticleForm(instance=article)


	if request.method == 'POST':

		form = ArticleForm(request.POST, instance=article)
		
		if form.is_valid():
			form.save()
			form = ArticleForm()
			return redirect('articles-page')


	context = {'form': form}
	return render(request, "article/create-article.html", context)


####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$	


def deleteArticle(request, id):


	article = Article.objects.get(id=id)

	if request.method == 'POST':
		article.delete()
		return redirect('articles-page')

	return render(request, "article/delete-article.html", {'article': article})
