from qdrant_client import QdrantClient

vector_db_host = "localhost"
vector_db_port = 6333
vector_db_collection = "METAMORPHOSIS"

vector_db_client = QdrantClient(host=vector_db_host, port=vector_db_port)
