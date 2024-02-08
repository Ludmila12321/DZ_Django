from django.shortcuts import render
from django.http import HttpResponse
import logging

# создаем логгер для записи данных о посещении страниц
logger = logging.getLogger(__name__)

def index(request):
    # содержимое страницы "Главная"
    html_content = """
    <h1>Добро пожаловать на мой первый Django сайт!</h1>
    <p>Это главная страница сайта.</p>
    """
    
    # Запись в лог о посещении страницы "Главная"
    logger.info('Страница "Главная" была посещена')

    return HttpResponse(html_content)

def about(request):
    # содержимое страницы "О себе"
    html_content = """
    <h1>Обо мне</h1>
    <p>Меня зовут Людмила. Я создала этот сайт.</p>
    """
    
    # Запись в лог о посещении страницы "О себе"
    logger.info('Страница "О себе" была посещена')

    return HttpResponse(html_content)
