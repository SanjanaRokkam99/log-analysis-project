# Udacity Full Stack NanoDegree Log Analysis Project
## Project Description
This is a project in the Udacity Full Stack Nanodegree. In this project, a large database with over a million rows is explored by building complex SQL queries to draw business conclusions for the data. The project resembels an internal reporting tool for a newpaper site to discover what kind of articles the site's readers like. The database contains newspaper articles, as well as the web server log for the site.

# Run
To run this project you need to have 
- virtualbox
- Vagrant
- Putty
- Postgresql

## Step -1
Creating a Vagrant Box:
    
    vagrant box add ubuntu/trusty64
   
    vagrant init ubuntu/trusty64
   
    vagrant up

## Step -2

    Using Putty for running the vagrant

    install postresql.
    
## Step -3
Loading the data
    
    psql -d news -f newsdata.sql
    
The data contains 3 relations:
    - articles
    - authors
    - log table

## Step -4
Running the queries:

    Run log.py using:  $ python log.py 
 
The output is redirected to reports.txt file
    $python log.py > reports.txt
    
    
