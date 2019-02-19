from flask import render_template
from app import app
from .request import get_news, get_sources
from flask import render_template,request,redirect,url_for

@app.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''

    # Getting popular news
    title = 'News Highlight'
    general_sources = get_sources('general')
    business_sources = get_sources('business')
    sports_sources = get_sources('sports')
    technology_sources = get_sources('technology')

    return render_template('index.html', title = title, general = general_sources, business = business_sources, sports = sports_sources, technology = technology_sources)

@app.route('/news/<id>')
def news(id):
    '''View a specific source page and its articles'''
    news = get_news(id)
    title = f'{id}'
    return render_template('news.html',id = id, news = news)

@app.route('/call/<data>')
def call(data):
    '''View a specific source page and its articles'''
    # news = get_news(id)
    # title = f'{id}'
    return render_template('call.html',data = data)
 