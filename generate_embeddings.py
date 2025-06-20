from vertexai.language_models import TextEmbeddingModel
import vertexai

vertexai.init(project="boxwood-theory-450601-g5", location="us-central1")
embedding_model = TextEmbeddingModel.from_pretrained("text-embedding-large-exp-03-07")

def get_embedding(text: str) -> list[float]:
    if not text.strip():
        return []
    return embedding_model.get_embeddings([text])[0].values
