from neo4j import GraphDatabase
from neo4j_backup import Extractor

uri = "neo4j+s://94f88fc9.databases.neo4j.io"
username = "neo4j"
password = "Fc5AbIWI18MK5L2cPxbjb4urp13brPMPCK79-AOUk48"
driver = GraphDatabase.driver(uri, auth=(username, password))

extractor = Extractor(
    project_dir="data_dump",
    driver=driver,
    database="neo4j",
    compress=False,
    input_yes=True,
)
extractor.extract_data()

