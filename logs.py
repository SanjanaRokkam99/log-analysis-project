#! /usr/bin/env python
import psycopg2

DBNAME = "news"


def make_query(query):
    ''' Makes a query to the news database '''
    db = psycopg2.connect(database=DBNAME)
    cursor = db.cursor()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()

# 1. What are the most popular three articles of all time?
qry1 = ''' select title,count(*) as num from articles,log where
log.path=CONCAT('/article/',articles.slug) group by articles.title order by
num DESC limit 3; '''

# 2. Who are the most popular article authors of all time?
qry2 = ''' select authors.name, sum(numviews_view.num) as views from
numviews_view,authors where authors.id=numviews_view.author group by
authors.name order by views desc '''

# 3. On which days did more than 1% of requests lead to errors?
qry3 = ''' select * from (select date(time),round(100.0*sum(case log.status
when '200 OK'  then 0 else 1 end)/count(log.status),3) as error from log group
by date(time) order by error desc) as subq where error > 1; '''


def pri_qry1_results(query):
    result = make_query(query)
    print('\n1. The 3 most popular articles of all time are:\n')
    for res in result:
        print ('\t' + str(res[0]) + ' - ' + str(res[1]) + ' views')


def pri_qry2_results(query):
    result = make_query(query)
    print('\n2. The most popular article authors of all time are:\n')
    for res in result:
        print ('\t' + str(res[0]) + ' - ' + str(res[1]) + ' views')


def pri_qry3_results(query):
    result = make_query(query)
    print('\n3. Days with more than 1% of request that lead to an error:\n')
    for res in result:
        print ('\t' + str(res[0]) + ' - ' + str(res[1]) + ' %')

# printing out results
pri_qry1_results(qry1)
pri_qry2_results(qry2)
pri_qry3_results(qry3)
