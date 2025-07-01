from neo4j import GraphDatabase
from neo4j_backup import Extractor

uri = "bolt://<YOUR-BOLT-URL>"
username = "<USERNAME>"
password = "<PASSWORD>"
driver = GraphDatabase.driver(uri, auth=(username, password))

extractor = Extractor(
    project_dir="data_dump",
    driver=driver,
    database="neo4j",
    compress=False,
    input_yes=True,
)
extractor.extract_data()

