import openai
import os
import re
from vectordb import create_vectordb_collection, upsert_collection

openai.api_key = os.getenv("OPENAI_API_KEY")
context_length = 8000
datafile = "METAMORPHOSIS.txt"
collection_name = "metamorphosis"


def get_embedding(text, model="text-embedding-ada-002"):
    text = text.replace("\n", " ")
    return openai.Embedding.create(input=[text], model=model)["data"][0]["embedding"]


def read_file(datafile):
    with open(datafile, "r") as filereader:
        dataset = filereader.read()
    return dataset


def get_main_content(dataset):
    # Use regular expressions to find the start and end of the metadata section
    metadata_match = re.search(
        r"\*\*\* START OF (THIS|THE) PROJECT GUTENBERG EBOOK", dataset
    )
    license_match = re.search(
        r"\*\*\* END OF (THIS|THE) PROJECT GUTENBERG EBOOK", dataset
    )

    if metadata_match and license_match:
        metadata_end = metadata_match.end()
        license_start = license_match.start()
        metadata_section = dataset[:metadata_end]
        license_section = dataset[license_start:]
    else:
        print("Metadata or license not found in the text.")

    # Print the main content without metadata and headers
    if metadata_section and license_section:
        main_content = dataset[len(metadata_section) :].strip()
        main_content = main_content[: len(license_section)].strip()
        print(main_content)
    else:
        print("No metadata or license found")

    return main_content


if __name__ == "__main__":
    dataset = read_file(datafile)
    main_content = get_main_content(dataset)
    create_vectordb_collection(collection_name, size=1536)
    # print(len(embeddings))
    paragraphs = main_content.split("\n\n")
    for idx, each in enumerate(paragraphs):
        if len(each.split()) < 5:
            continue
        embedding = get_embedding(each)
        upsert_collection(
            id=idx,
            collection_name=collection_name,
            embedding=embedding,
            payload={"Paragraph" + str(idx): each},
        )
