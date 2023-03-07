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

client = ClientV1("api.grai.io", "443", workspace=workspace)
client.set_authentication_headers(user, password)


conn = MySQLConnector(**test_credentials)
res = get_nodes_and_edges(conn, 'v1')
breakpoint()
#mysql_update_server(client, **test_credentials)
