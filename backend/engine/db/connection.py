import psycopg2
from psycopg2.extras import RealDictCursor, register_uuid
from django.conf import settings

register_uuid()

def get_conn():
    return psycopg2.connect(
        host=settings.DATABASES["default"]["HOST"],
        dbname=settings.DATABASES["default"]["NAME"],
        user=settings.DATABASES["default"]["USER"],
        password=settings.DATABASES["default"]["PASSWORD"],
        port=settings.DATABASES["default"]["PORT"],
        cursor_factory=RealDictCursor,
    )
