from django.shortcuts import render
from django.http import Http404
from django.http import HttpResponse
from django.template import RequestContext, loader
from news.models import *
from datetime import date, timedelta
import datetime
from django.db import connection

def my_custom_sql():
    cursor = connection.cursor()
    sql = "SELECT DISTINCT SUBSTRING_INDEX(SUBSTRING_INDEX(news_card.text, ' ', numbers.n), ' ', -1) news_card FROM (SELECT 1 n UNION ALL SELECT 2 UNION ALL SELECT 3 UNION ALL SELECT 4) numbers INNER JOIN news_card ON CHAR_LENGTH(news_card.text) -CHAR_LENGTH(REPLACE(news_card.text, ' ', ''))>=numbers.n-1 ORDER BY text;"
    cursor.execute(sql)
    row = cursor.fetchall()
    print row
    return row
# Create your views here.


def index(request):

	section = Section.objects.order_by('-publish').filter(status='Active')
	slide = Slide.objects.order_by('-publish').filter(status='Active')
	card = Card.objects.filter(status='Active').order_by('-publish')
	breaking = Breaking.objects.order_by('-publish').filter(status='Active')
	# top = Top_5.objects.order_by('top')
	news_slider=[]
	for i in breaking:
		news_slider.append(i.text+"  "*15)
	context = {'card':card, 'slide':slide, 'breaking':" ***** ".join(news_slider), 'section':section, "lent": [],}
	context['lent'] = range(0, 1)
	return render(request, 'index.html', context)


def editor(request):
	return render(request, 'editor.html')

def search(request, pattern):
	try:
		# pattern = '2016'
		# a='%'+pattern+'%'
		news_slider=[]
		section = Section.objects.order_by('-publish').filter(status='Active')
		this_section = Section.objects.order_by('-publish').filter(status='Active').filter(id = 3)
		breaking = Breaking.objects.order_by('-publish').filter(status='Active')

		for i in breaking:
			news_slider.append(i.text+"  "*15)
		# card = Card.objects.filter(section = 3).filter(status='Active').order_by('-publish')
		card = Card.objects.filter(text__contains=pattern)
		
		if len(card)<=0:
			message = "No Matches Found !!!!"
		else:
			message=""

		context = {'card': card, 'breaking':" ***** ".join(news_slider), 'section':section, 'this_section':this_section, 'message':message}
	except Card.DoesNotExist:
		raise Http404("OOPS, I M LOST")
	return render(request, 'search.html', context )

# def search(request, pattern):
# 	a='%'+pattern+'%'
# 	section = Section.objects.order_by('-publish').filter(status='Active')
# 	slide = Slide.objects.order_by('-publish').filter(status='Active')                   
# 	card = Card.objects.filter(text__like=a)
# 	breaking = Breaking.objects.order_by('-publish').filter(status='Active')
# 	# top = Top_5.objects.order_by('top')
# 	news_slider=[]
# 	for i in breaking:
# 		news_slider.append(i.text+"  "*15)
# 	context = {'card':card, 'slide':slide, 'breaking':" ***** ".join(news_slider), 'section':section, "lent": [],}
# 	context['lent'] = range(0, 1)
# 	return render(request, 'search.html', context)

def share(request, news_url):
	try:
		news_slider=[]
		section = Section.objects.order_by('-publish').filter(status='Active')
		breaking = Breaking.objects.order_by('-publish').filter(status='Active')
		for i in breaking:
			news_slider.append(i.text+"  "*15)
		card = Card.objects.get(url = news_url)
		context = {'card': card, 'breaking':" ***** ".join(news_slider), 'section':section,}
	except Card.DoesNotExist:
		raise Http404("News Does not Exist")
	return render(request, 'shareing.html', context )


def section(request, section_title, section_id):
	try:
		news_slider=[]
		section = Section.objects.order_by('-publish').filter(status='Active')
		this_section = Section.objects.order_by('-publish').filter(status='Active').filter(id = section_id)
		breaking = Breaking.objects.order_by('-publish').filter(status='Active')
		for i in breaking:
			news_slider.append(i.text+"  "*15)
		card = Card.objects.filter(section = section_id).filter(status='Active').order_by('-publish')
		context = {'card': card, 'breaking':" ***** ".join(news_slider), 'section':section, 'this_section':this_section}
	except Card.DoesNotExist:
		raise Http404("OOPS, I M LOST")
	return render(request, 'section.html', context )