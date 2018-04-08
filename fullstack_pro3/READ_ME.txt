# Logs Analysis
## Project Description



The task was to create a reporting tool that prints out reports (in plain text) based on the data in the database news.
The Project shows one of the valuable roles of a database server in a real-world application: it's a point where different pieces of software (a web app and a reporting tool, for instance) can share data.
This is also used to help in making the different buisness conclusions and planning for the future making it a part of tha data ware house
In order to view the project take the following steps:

PRE -REQUISITES FOR THE PROJECT 
1.Python installed in latest version
2.Vagrant editor
3.Virtual Box

SETUP THE MACHINE AND DOWNLOAD THE NEWS DATABASE  USING THE  FOLLOWING  LINK
https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip

UNZIP THE DATABASE

In order to start the virtual machine -
1 vagrant up
2 vagrant ssh in the directory having news database
3 psql -d news -f newsdata.sql-load database locally
4 psql -d news- to connect to the database
CREATE THE FOLLOWING VIEWS TO MAKE THE TASK EASIER


1 ---create view log_of_error as select date(time),round(100.0*sum(case log.status when '200 OK'
  then 0 else 1 end)/count(log.status),2) as "err_per" from log group by date(time)
  order by "err_per" desc;

2---create view total_view as select title,author,count(*) as t_views from articles,log where
  log.path like concat('%',articles.slug) group by articles.title,articles.author
  order by t_views desc;


LASTLY RUN THE databaselog.py
