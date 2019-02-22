#Udacity Full Stack NanoDegree Log Analysis Project
Project Description

    Setting up the database and Creating Views:

    Load the data in local database using the command:

  psql -d news -f newsdata.sql

    Use psql -d news to connect to database.

    Create view numviews_view using:

create view numviews_view as (select title, author, count(*) as num from articles,log where log.path=CONCAT('/article/',articles.slug) group by articles.title,articles.author order by num desc);

Running the queries:

Run logs.py using:

  $ python logs.py
