from neo4j import GraphDatabase

class Database:
    '''
        Database class for connection and execution of queries. 
    '''
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def execute_query(self, query, parameters=None):
        data = []
        with self.driver.session() as session:
            results = session.run(query, parameters)
            for record in results:
                data.append(record)
            return data