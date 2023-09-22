# Task1(a)

## Overview:

The python script written for task1(a) is to monitor the three services httpd, rabbitMQ and PostgreSQL running on a linux server and check if each service is up or down. Based on the status of each service, a json object is created with service_name, service_status and host name and written them to individual json files.

## Approach:

To achieve this task,I have created two functions "service_json_object" for creating the json objects and "service_status_check" to check the status of a particular service.
Imported various external modules/libraries like subprocess to check the status of a particular service by calling the check_output() method, socket to get the hostname by calling gethostname() and time to get the current time stamp.
Then iterated through the list of service_names and called the above two functions "service_json_object" and "service_status_check" to find the status and create a json object for each service to further send it to the json documents. These json documents were saved in the format of {serviceName}-status-{@timestamp}.json

This scripting file is created on local machine. But to monitor the services and create json files, this scripting file need to be placed in the server where these services were hosted. This can be done in the following steps:

 1. create a directory in the server and store this python script, where the generated json files will also be stored
    mkdir ~/service_monitor

 2. To make the script executable on the server, the following command can be used
    chmod +x ~/service_monitor/pythonscriptfile.py

3. This scripts can be automated to run at specified or scheduled intervals using crontab or using systemd services


# Task1(b):

## OverView:

A python REST webservice is created using the flask framework to create endpoints to handle the http requests coming from the server where the json documents were created. This webservice accepts http requests like sending the json data from the documents and write it to the elasticsearch, search the status of all services or a single service from elastic search. This webservice interacts with the elasticsearch with the help of the python library elasticsearch client.

## Approach:

To achieve this task, a virtual environment is created inside the working directory and installed flask and elastic search which are required to create the Rest API and interact with the elasticsearch respectively. 
since the elasticsearch server details is not provided a elasticsearch local server needs to be installed and run on port 9200
created three endpoints
/add - for indexing documents into the elasticsearch
/health - to search the status of all the services
/health/<string:service_name> - to search the status of a particular service
This application will run in the local host with flask's default port 5000

Note: This application python file(Task2(b).py) is located in the flaskenv folder


# Task2(a):
An ansible inventory file "inventory.yaml" is created to specify the hosts that ansible should manage and interact with for the following services httpd on host1, rabbitMQ on host2, postgreSQL on host3

# Task2(b):
An ansible Playbook with filename assignment.yml is created to define tasks for the following actions
verify_install: it checks if the specified service is installed on the corresponding host.httpd is used in the ansible plabook to check if it is installed or not.
check-disk: it checks disk usage on all hosts and sends an alert email if disk usage is greater than 80%.
check-status: it checks the status of the rbcapp1 application using the REST endpoint created in TEST1. It also identifies and lists down services if the application is "DOWN."

## sample commands that can be used to run the playbook:

### To check Installation:
`ansible-playbook assignment.yml -i inventory -e action=verify_install`

### To check disk usage and send alert if it exceeds 80%:
`ansible-playbook assignment.yml -i inventory -e action=check-disk`

### To check status of all the services mentioned in the inventory and list the services that are down: 
`ansible-playbook assignment.yml -i inventory -e action=check-status`

# Task3:

## Overview: 
A python script is developed to take the csv file assignment_data.csv which contains data regarding sales of properties and create a new csv file with the properties that were sold less than avg price per sq-ft

## Approach:
Converted the csv file into dataframes with the help of pandas and filtered the records with zero sq__ft. 
created a new column 'price_per_sqft' that defines the price per sqr-ft. Then with the mean() method calcuated the average_price_per_sqft and filtered the records that were sold less than avg price per sq-ft into a new dataframe. This dataframe is again converted into csv file named "output_csv_file.csv"









