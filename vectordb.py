from config import vector_db_client
from qdrant_client.http.models import Distance, VectorParams, PointStruct


def create_vectordb_collection(collection_name, size):
    return vector_db_client.recreate_collection(
        collection_name=collection_name,
        vectors_config=VectorParams(size=size, distance=Distance.DOT),
    )


def upsert_collection(id, collection_name, embedding, payload):
    vector_db_client.upsert(
        collection_name=collection_name,
        wait=True,
        points=[PointStruct(id=id, vector=embedding, payload=payload)],
    )

    print(
        vector_db_client.get_collection(collection_name=collection_name).vectors_count
    )


# def test_init_vector_db():
#     vector_db_client.recreate_collection(
#         collection_name=vector_db_collection,
#         vectors_config=VectorParams(size=4, distance=Distance.DOT),
#     )

#     print("VectorDB Collections Created")

# def test_vector_db():
#     operation_info = vector_db_client.upsert(
#         collection_name=vector_db_collection,
#         wait=True,
#         points=[
#             PointStruct(
#                 id=1, vector=[0.05, 0.61, 0.76, 0.74], payload={"city": "Berlin"}
#             ),
#             PointStruct(
#                 id=2, vector=[0.19, 0.81, 0.75, 0.11], payload={"city": "London"}
#             ),
#             PointStruct(
#                 id=3, vector=[0.36, 0.55, 0.47, 0.94], payload={"city": "Moscow"}
#             ),
#             PointStruct(
#                 id=4, vector=[0.18, 0.01, 0.85, 0.80], payload={"city": "New York"}
#             ),
#             PointStruct(
#                 id=5, vector=[0.24, 0.18, 0.22, 0.44], payload={"city": "Beijing"}
#             ),
#             PointStruct(
#                 id=6, vector=[0.35, 0.08, 0.11, 0.44], payload={"city": "Mumbai"}
#             ),
#         ],
#     )
#     print(operation_info)


# def test_search_vector_db():
#     search_result = vector_db_client.search(
#         collection_name=vector_db_collection, query_vector=[0.2, 0.1, 0.9, 0.7], limit=3
#     )

#     print(search_result)


# def test_delete_collections():
#     print(
#         vector_db_client.delete_collection(collection_name=vector_db_collection))


# if __name__ == "__main__":
# init_vector_db()
# test_vector_db()
# test_search_vector_db()
# test_delete_collections()
