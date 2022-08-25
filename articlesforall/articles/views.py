from django.shortcuts import render, redirect, reverse 
from django.http import HttpResponse

from django.views import View

from .models import Author, Article

from .forms import ArticleForm





class ArticleListView(View):

	template_name = 'article/articles.html'

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

def authors(request):

	authors = Author.objects.all()

	context = {'authors': authors}

	return render(request, "article/authors.html", context)



####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$
####<<<<<<<<<<<>>>>>>>>>>>>!!!!!!!!!!!!!%%%%%%%%%%%$$$$$$$$$$$$$$$$$$

def profile(request, id):

	author = Author.objects.get(id=id)

	context = {'author': author}

	return render(request, "article/profile.html", context)



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
