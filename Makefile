int-vector-db:
	docker pull qdrant/qdrant && docker run --name qdrant_db -p 6333:6333 \
    -v /Users/nikesh/projects/LLM_recipes/RAG/qdrant_storage:/qdrant/storage:z \
    qdrant/qdrant

spin-up-vector-db:
	docker start qdrant_db
wind-down-vector-db:
	docker stop qdrant_db