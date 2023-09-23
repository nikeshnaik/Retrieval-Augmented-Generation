## Retrieval-augmented generation ( RAG ) 

### Requirments:

1. User will upload a file, current support only .txt file.
2. A local LLM or API will be used to find embeddings and store in VectorDB.
3. A search bar will be available which lets users search document, ask questions and even chat.

### Todo

- [x] System Design of how data will flow.
- [x] Use Gutenberg Project book and cleanup for demo
- [x] buy openai credits for MVP
- [x] Find right VectorDB, settled with Qdrant
- [x] Use simple text file with content for v1, move to Squad v2 dataset
- [x] Dump openAI embeddings of text file to vectorDB.
- [ ] Take question for text file from Args
- [ ] Sort and get top 3 Chunks based on similarity scores
- [ ] Use each chunk, fire 3 APIs calls with question and get answer.


### Learning Goals

- Checkout VectorDBs and how it works.
- Embeddings from LLM extraction
- search and doing similarity search
- Frontend for search experience + chatbot design.


### System Design
![Alt text](design.png)