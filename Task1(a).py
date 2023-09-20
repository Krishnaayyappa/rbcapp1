import subprocess
import socket
import json
import time

list_of_services_to_monitor = ["httpd", "rabbitMQ", "postgreSQL"]

#function to check if a particular service from the list is running or not
def service_status_check(serviceName):
    try:
        subprocess.check_output(["systemct1", "is-active", "--quiet", serviceName])
        return "UP"
    except subprocess.CalledProcessError:
        return "DOWN"
    

# Function to create JSON object for each service
def service_json_object(serviceName, serviceStatus, hostName):
    serviceData = {
        "service_name":serviceName,
        "service_status":serviceStatus,
        "host_name":hostName
    }
    return serviceData

hostName = socket.gethostname()

currentTimeStamp = int(time.time())

#now we need to iterate through the list of services we defined earlier to check their status.

for serviceName in list_of_services_to_monitor:
    serviceStatus = service_status_check(serviceName)
    serviceData = service_json_object(serviceName, serviceStatus, hostName)

    # once the json object is created, we need to write it to json file by creating it with filename {serviceName}-status-{@timestamp}.json 
    fileName = f"{serviceName}-status-{currentTimeStamp}.json"
    try:
        with open(fileName, "w") as jsonFile:
            json.dump(serviceData, jsonFile, indent=4)
        print(f"Created json file successfully for {serviceName}")
    except Exception as e:
        print(f"error creating json file for {serviceName}: {e}")

print("Monitoring of all the three services is done")