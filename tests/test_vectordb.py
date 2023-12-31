from config import vector_db_client, vector_db_collection
from qdrant_client.http.models import Distance, VectorParams, PointStruct

vector_db_collection = "pytest" + vector_db_collection


def init_vector_db():
    vector_db_client.recreate_collection(
        collection_name=vector_db_collection,
        vectors_config=VectorParams(size=4, distance=Distance.DOT),
    )


def test_vector_db():
    operation_info = vector_db_client.upsert(
        collection_name=vector_db_collection,
        wait=True,
        points=[
            PointStruct(
                id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "Berlin"}
            ),
            PointStruct(
                id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": "London"}
            ),
            PointStruct(
                id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": "Moscow"}
            ),
            PointStruct(
                id=4, vector=[0.18, 0.01, 0.85, 0.80], payload={"city": "New York"}
            ),
            PointStruct(
                id=5, vector=[0.24, 0.18, 0.22, 0.44], payload={"city": "Beijing"}
            ),
            PointStruct(
                id=6, vector=[0.35, 0.08, 0.11, 0.44], payload={"city": "Mumbai"}
            ),
        ],
    )
    print(operation_info)


def test_search_vector_db():
    search_result = vector_db_client.search(
        collection_name=vector_db_collection, query_vector=[0.2, 0.1, 0.9, 0.7], limit=3
    )

    print(search_result)


def test_delete_vectors():
    print(vector_db_client.delete_vectors(vector_db_collection))
