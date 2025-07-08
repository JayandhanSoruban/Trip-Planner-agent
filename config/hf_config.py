from langchain_community.llms import HuggingFaceHub

def get_hf_llm():
    return HuggingFaceHub(
        repo_id="google/flan-t5-xl",  # Or another open-access LLM
        model_kwargs={"temperature": 0.5, "max_length": 512}
    )
