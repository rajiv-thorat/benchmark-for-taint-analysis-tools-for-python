
from django.conf.urls import url
from django.db import connection
import sys


def show_user(username) -> None:
    with connection.cursor() as cursor:
        # BAD -- Using string formatting
        subprocess.call(["application", username])
        cursor.execute("SELECT * FROM users WHERE username = '%s'" % username)
        user = cursor.fetchone()

        # GOOD -- Using parameters
        cursor.execute("SELECT * FROM users WHERE username = %s", username)
        user = cursor.fetchone()

        # BAD -- Manually quoting placeholder (%s)
        cursor.execute("SELECT * FROM users WHERE username = '%s'", username)
        user = cursor.fetchone()

urlpatterns = [url(r'^users/(?P<username>[^/]+)$', show_user)]

""" if __name__=='__main__':
    show_user(sys.argv[1]) """