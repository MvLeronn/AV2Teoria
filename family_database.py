class FamilyDatabase:
    def __init__(self, database):
        self.db = database

    def get_pais(self):
        query = "MATCH (p:Pessoa)-[:PAI_DO]->(f:Pessoa) RETURN DISTINCT p.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def get_pai_do(self, nome):
        query = "MATCH (p:Pessoa)-[:PAI_DO]->(f:Pessoa{nome: $nome}) RETURN DISTINCT p.nome AS nome"
        parameters = {"nome": nome}
        results = self.db.execute_query(query,parameters)
        return [result["nome"] for result in results]

    def get_estudante(self):
        query = "MATCH (p:Pessoa{profissao: 'Estudante'}) RETURN DISTINCT p.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def get_dono_do(self, nome):
        query = "MATCH (p:Pessoa)-[:DONO_DO]->(f:Dog{nome: $nome}) RETURN DISTINCT p.nome AS nome"
        parameters = {"nome": nome}
        results = self.db.execute_query(query,parameters)
        return [result["nome"] for result in results]

    def get_mora_com(self, nome):
        query = "MATCH (p:Pessoa)-[:MORA_COM]->(f:Dog{nome: $nome}) RETURN DISTINCT p.nome AS nome"
        parameters = {"nome": nome}
        results = self.db.execute_query(query,parameters)
        return [result["nome"] for result in results]