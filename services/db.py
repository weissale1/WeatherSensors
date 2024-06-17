import os
import psycopg2
from flask import g
from ..domain.WeatherData import WeatherData

# currently unused

def load_last_weather_data() -> WeatherData:
    db_conn = _get_db()
    cur = db_conn.cursor()
    cur.execute('SELECT * FROM weather_data LIMIT 1')
    raw_data = cur.fetchone()
    wd = WeatherData(raw_data[0], raw_data[1], raw_data[2]) 
    cur.close()
    return wd

def save_weather_data(wd: WeatherData):
    db_conn = _get_db()
    cur = db_conn.cursor()
    cur.execute(
        'INSERT INTO weather_data () VALUES (%s, %s, %s);',
        (wd.timestamp, wd.temp, wd.humid)
    )
    cur.close()

def init_app(app):
    app.teardown_appcontext(_close_db())

def _get_db():
    if 'db' not in g:
        g.db = psycopg2.connect(
            host = "db",
            database = os.environ.get("POSTGRES_DB"),
            user = os.environ.get("POSTGRES_USER"),
            password =  os.environ.get("POSTGRES_PASSWORD")
        )
    return g.db

def _close_db():
    db = g.pop('db', None)

    if db is not None:
        db.close()
