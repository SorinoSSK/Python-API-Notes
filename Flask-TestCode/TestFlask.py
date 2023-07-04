from flask import Flask
from crate import client
import psycopg2
app = Flask(__name__)

conn_crate = client.connect(
    "https://vflowtech-test.aks1.eastus2.azure.cratedb.net:4200", 
    username="Refer To Private Note", 
    password="Refer To Private Note", 
    verify_ssl_cert=True)

conn_pgs = psycopg2.connect(
    host="localhost",
    database="vft_api",
    user="postgres",
    password="VFLOWTECH"
)

@app.route('/testAPI')
def testAPI():
    return {'Success': 'API is Online'}

@app.route('/cratedb/cluster')
def crateStatus():
    try:
        with conn_crate:
            cursor = conn_crate.cursor()
            cursor.execute("SELECT name FROM sys.cluster")
            result = cursor.fetchone()
        return {'cluster': result}
    except Exception as ex:
        return {'Error': 'Failed', 'Error':ex}
    
@app.route('/postgresql/tables')
def postgresqlStatus():
    with conn_pgs:
        cursor = conn_pgs.cursor()
        cursor.execute("Select value FROM vft_api_test;")
        result = cursor.fetchone()
    return {'tables': result}