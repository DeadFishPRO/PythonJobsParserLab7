from flask import Flask
from decouple import config
from flask_restx import Api
from core.utils import get_jobs
app = Flask(__name__)
app.config.from_object(config("APP_SETTINGS"))
api = Api(
    app,
    version='1.0',
    title='Вакансии на Python',
    description='<I>Получаем вакансии и предложения о работе с официального сайта Python</I>',
    contact='Бардадымов Даниил',
    contact_url='https://vk.com/donttouchthisplz',
    doc='/',
    prefix='/api/v1'
)
from core import routes