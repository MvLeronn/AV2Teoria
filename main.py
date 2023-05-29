from database import Database
from family_database import FamilyDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://18.206.124.99:7687", "neo4j", "outboards-accommodation-governor")

family = FamilyDatabase(db)

print(family.get_pais())

print(family.get_pai_do("Marcos"))

print(family.get_estudante())

print(family.get_dono_do("Melissa"))

print(family.get_mora_com("Melissa"))