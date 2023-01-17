import logging
from uuid import UUID

import spacy 
import requests
from bs4 import BeautifulSoup

from app.core.celery_app import celery_app
from news.crud import crud_get_website, crud_create_article_and_entities


nlp = spacy.load('en_core_web_sm')
logger = logging.getLogger(__name__)


@celery_app.task(name="process_news_website")
def process_news_website(website_id: UUID):
    website = crud_get_website(website_id)
    soup, _ = get_soup_request(website.url)
    hrefs = [a['href'] for a in soup.select('a', href=True) if a['href']]
    for href in hrefs:
        process_article.s(website_url, href) | get_entities_and_save.s(website_id, href)


@celery_app.task(name="process_article")
def process_article(base_url: str, href: str):
    soup, _ = get_soup_request(base_url + href)

    # TODO: save those fields
    json_ld = soup.find('script', type='application/ld+json').text
    title = soup.find('title').text
    h1s = [h1.text for h1 in soup.select('h1')]

    text = soup.find('article').text
    return text


@celery_app.task(name="get_entities_and_save")
def get_entities_and_save(website_id: UUID, href: str, content: str):
    doc = nlp(content)
    for ent in doc.ents:
        entities = (ent.text, ent.label_)
    crud_create_article_and_entities(website_id, content, entities)
    

def get_soup_request(url: str):
    headers = {}
    response = requests.get(website_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup, response
