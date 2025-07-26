from pydantic import BaseModel, Field
from server import mcp
from mcp.server.fastmcp import Context

from langchain_openai.embeddings import OpenAIEmbeddings

# Initialize OpenAI embeddings model for text vectorization
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")


def embedding_to_postgres_vector(embedding: list[float]) -> str:
    """
    Convert a list of embedding floats to a PostgreSQL vector format.

    Args:
        embedding (list[float]): List of floating point numbers representing the embedding vector

    Returns:
        str: A string representation of the vector in PostgreSQL format '[x1,x2,...,xn]'
    """
    return f'[{",".join(str(x) for x in embedding)}]'


class Document(BaseModel):
    """
    Represents a document with its content and relevance score.

    This model is used to structure the response from document queries,
    providing both the document content and how well it matches the query.

    Attributes:
        content (str): The actual text content of the document
        score (float): A relevance score between 0 and 1, where 1 indicates perfect relevance
    """

    content: str = Field(description="The content of the document.")
    score: float = Field(
        description="The relevance score of the document, ranging from 0 to 1."
    )


class ToolInput(BaseModel):
    """
    Input model for document search queries.

    This model validates and structures the input for document searches,
    with special handling for queries prefixed with 'Defra:'.

    Attributes:
        query (str): The search query string. If prefixed with 'Defra:',
                    only the text after the prefix will be used for searching.
    """

    query: str = Field(
        description="The search query string. If prefixed with 'Defra:', only the text after the prefix will be used for searching."
    )


@mcp.tool()
async def call_defra_docs(
    input: ToolInput,
    ctx: Context,
) -> list[Document]:
    """
    Retrieve documents from the database that are most relevant to the given query.

    This function performs semantic search using the following steps:
    1. Takes the input query and generates embeddings using OpenAI's text-embedding-3-large model
    2. Converts the embeddings to PostgreSQL vector format
    3. Queries the database using cosine similarity to find the most relevant documents
    4. Returns the top 5 most relevant documents

    Args:
        input (ToolInput): The search query input model
        ctx (Context): The request context containing database connection

    Returns:
        list[Document]: A list of up to 5 Document objects, sorted by relevance score in ascending order.
                       Each Document contains the content and its relevance score.

    Note:
        - The function uses cosine similarity for relevance scoring
        - Scores are normalized to be between 0 and 1
        - The query uses the '<=> operator for similarity search
        - Results are limited to 5 documents
    """
    input_query = input.query

    # Generate embeddings for the input query
    embedded_query = await embeddings.aembed_query(input_query)
    embedded_query = embedding_to_postgres_vector(embedded_query)

    # SQL query using cosine similarity to find relevant documents
    query = """
    SELECT content, 1 - (embedding <=> $1) AS score 
    FROM documents 
    ORDER BY score 
    ASC LIMIT 5
    """

    # Execute the query and get results
    result = await ctx.request_context.lifespan_context.db.execute_query(
        query,
        embedded_query,
    )

    # Convert database results to Document objects
    return [Document(content=row["content"], score=row["score"]) for row in result]
