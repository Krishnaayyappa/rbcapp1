from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)

#we need to initialize the elasticsearch client and connect to the elasticsearch

es = Elasticsearch([{'host':"localhost", 'port':9200}])  #since the elasticsearch server details is not provided we use the local host

@app.route("/add", methods=['POST'])
def insert_to_elasticsearch():
    try:
        data = request.json # to retrive the json data that is sent through http request body header
        es.index(index="service_status", doc_type="_doc", body=data)
        return jsonify({"message":"json data is added successfully to the elastic seaac"}), 201
    except Exception as e:
        return jsonify({"error occured":e}), 500
    

@app.route("/healthcheck", methods=["GET"])
def getHealthCheck():
    try:
        result = es.search(index="service_status", size=1000)
        hits = result['hits']['hits']
        statuses = [{"service_name":hit['_source']['service_name'],"service_status":hit["_source"]["service_status"]} for hit in hits]
        return jsonify(statuses), 200
    except Exception as e:
        return jsonify({"error occured": e}), 500
    
@app.route('/healthcheck/<string:service_name>', methods=['GET'])
def getHealthcheckByService(service_name):
    try:
        result = es.search(index='service_status', body={"query": {"match": {"service_name": service_name}}})
        hits = result['hits']['hits']
        if hits:
            service_status = hits[0]['_source']['service_status']
            return jsonify({"service_name": service_name, "service_status": service_status}), 200
        else:
            return jsonify({"message": "requested Service status is not found"}), 404
    except Exception as e:
        return jsonify({"error occured":e}), 500

if __name__ == '__main__':
    app.run(debug=True) #it will run in the local host with flask's default port 5000 


