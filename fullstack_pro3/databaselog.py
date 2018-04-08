#!/usr/bin/env python3

import psycopg2
import datetime


def get_log():
    """Return all the required log  from the 'database', most recent first."""
    con = psycopg2.connect(database='news')
    cursor = con.cursor()
    print("""THE OUTPUT FOR THE FIRST QUERY
    THE MOST POPULAR THREE ARTICLES OF ALL TIME->""")
# QUERY NO-1
    cursor.execute("""SELECT title, count(*) as no_views FROM articles,
    log where log.path like concat('%',articles.slug) GROUP BY articles.title,
    articles.author ORDER BY no_views desc limit 3""")
    res = cursor.fetchall()
    for i in res:
        print('     %s-->%i' % i)
# QUERY NO-2
    cursor.execute("""SELECT authors.name,sum(total_view.t_views) as views FROM
    total_view,authors where authors.id = total_view.author GROUP BY
    authors.name ORDER BY views desc""")
    r = cursor.fetchall()
    print("""THE OUTPUT FOR THE SECOND QUERY THE MOST POPULAR
    ARTICLE AUTHORS OF ALL TIME ->""")
    for i in r:
        print('     %s-->%i' % i)
# QUERY NO-3
    cursor.execute("SELECT * FROM log_of_error WHERE \"err_per\" > 1")
    r = cursor.fetchall()
    print("""THE OUTPUT FOR THE THIRD QUERY WHICH DAYS DID MORE
    THAN 1% OF REQUESTS LEAD TO ERRORS ->""")
    for i in r:
        print('     %s:%i' % i)
    con.close()

print("         HERE IS THE LOG")
get_log()
