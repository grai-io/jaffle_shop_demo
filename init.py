from grai_client.endpoints.v1.client import ClientV1
from grai_source_mysql.base import update_server as mysql_update_server, get_nodes_and_edges, MySQLConnector

import os
from dotenv import load_dotenv

load_dotenv()

test_credentials = {
    "host": "localhost",
    "dbname": "dbo",
    "user": "grai",
    "password": "grai",
    "namespace": "demo",
}

user = os.environ.get('CLIENT_USER')
password = os.environ.get('CLIENT_PASSWORD')
workspace = os.environ.get('CLIENT_WORKSPACE')

#client = ClientV1("api.grai.io", "443", workspace=workspace)
#client.authenticate(username=user, password=password)
client = ClientV1('localhost', '8000', workspace='test', insecure=True)
client.authenticate(username='null@grai.io', password='super_secret')

conn = MySQLConnector(**test_credentials)
nodes, edges = get_nodes_and_edges(conn, 'v1')
mysql_update_server(client, **test_credentials)
