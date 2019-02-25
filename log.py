#!/usr/bin/env python
# Logs Analysis Project

# Import postgresql library
import psycopg2 as pg

DBNAME = "news"

def connect(query):
    db = pg.connect(database=DBNAME) # Connect to database
    c = db.cursor()
    c.execute(query)          # Execute queries
    results = c.fetchall()    # Fetch results
    db.close()
    return results


# Question 1. What are the most popular three articles of all time?


def query1_result(query):
    results = connect(query)
    for i in results:
        print('\t' + str(i[0]) + ' --> ' + str(i[1]) + ' views')
        print(" ")


# Question 2. Who are the most popular article authors of all time?

def query2_result(query):
    results = connect(query)
    for i in results:
        print('\t' + str(i[0]) + ' --> ' + str(i[1]) + ' views')
        print(" ")


# Question 3. On which days did more than 1% of requests lead to errors?

def query3_result(query):
    results = connect(query)
    for i in results:
        print('\t' + str(i[0]) + ' --> ' + str(i[1]) + ' %' + ' errors')
        print(" ")


if __name__ == '__main__':
    # Print results
    print('\n The most popular articles of all time are:\n')
	
    query1 = """
          SELECT title, count(*) FROM articles JOIN
          log ON log.path LIKE concat('%',articles.slug,'%')
          GROUP BY title, path ORDER BY count(*) DESC limit 3;
    """

    query1_result(query1)
    print('\n The most popular authors of all time are:\n')
    query2 = """
        SELECT name, count(title)
        FROM log, articles, authors
        WHERE '/article/' || articles.slug = log.path
        AND authors.id = articles.author
        GROUP BY authors.name
        ORDER BY count DESC
    """

            	
    query2_result(query2)
    print('\n The days when more than 1% of requests lead to error:\n')

    
    query3 = """
        SELECT total.day,
          ROUND(((errors.err_requests * 100.0) / total.requests), 5) AS percent
        FROM (
              SELECT date_trunc('day', time) AS day, count(*) AS err_requests
              FROM log
              WHERE status LIKE '404%'
              GROUP BY day
            ) AS errors
        JOIN (
              SELECT date_trunc('day', time) AS day, count(*) AS requests
              FROM log
              GROUP BY day
            ) AS total
        ON total.day = errors.day
        WHERE (ROUND(((errors.err_requests * 100.0)/total.requests), 5) > 1.0)
        ORDER BY percent DESC;
    """

    query3_result(query3)
