import psycopg2


def connection():
    try:
        connection = psycopg2.connect(user='decagon',
                                      password='fezzo', host='localhost', database='library')
        return connection
    except (Exception, psycopg2.Error) as error:
        print('Connection Error', error)
