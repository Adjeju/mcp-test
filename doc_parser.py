FOLDER_URL = "./docs"
# read all files in the folder
import asyncio
from pathlib import Path
import asyncpg
from langchain_openai.embeddings import OpenAIEmbeddings

from config import config

embeddings = OpenAIEmbeddings(
    model="text-embedding-3-large",
)


def read_all_files(folder_path: str = FOLDER_URL):
    """Read all files from the specified folder"""
    files_content = {}

    try:
        folder = Path(folder_path)
        if not folder.exists():
            print(f"Folder {folder_path} does not exist")
            return files_content

        if not folder.is_dir():
            print(f"{folder_path} is not a directory")
            return files_content

        # Iterate through all files in the folder
        for file_path in folder.iterdir():
            if file_path.is_file():
                try:
                    with open(file_path, "r", encoding="utf-8") as file:
                        files_content[str(file_path)] = file.read()
                        print(f"Read file: {file_path}")
                except UnicodeDecodeError:
                    # Try with different encoding for binary or non-UTF-8 files
                    try:
                        with open(file_path, "r", encoding="latin-1") as file:
                            files_content[str(file_path)] = file.read()
                            print(f"Read file (latin-1): {file_path}")
                    except Exception as e:
                        print(f"Error reading file {file_path}: {e}")
                except Exception as e:
                    print(f"Error reading file {file_path}: {e}")

    except Exception as e:
        print(f"Error accessing folder {folder_path}: {e}")

    return files_content


async def get_db():
    db = await asyncpg.create_pool(
        config.DATABASE_URL,
        min_size=1,
        max_size=10,
    )
    return db


# Read all files from the docs folder
all_files = read_all_files()


def embedding_to_postgres_vector(embedding: list[float]) -> str:
    return f'[{",".join(str(x) for x in embedding)}]'


async def main():
    db = await get_db()
    chunks = []
    for file_path, file_content in all_files.items():
        chunks.extend(file_content.replace("\n", "").split("---"))

    data = await embeddings.aembed_documents(chunks)

    await db.executemany(
        "INSERT INTO documents (embedding, content) VALUES ($1, $2)",
        [
            (embedding_to_postgres_vector(embedding), chunk)
            for embedding, chunk in zip(data, chunks)
        ],
    )


if __name__ == "__main__":
    asyncio.run(main())
