#!/usr/bin/env python

import os, sys, logging

from agno.agent import Agent, RunOutput
from agno.models.ollama import Ollama
from agno.models.openai import OpenAIChat
from agno.knowledge.embedder.ollama import OllamaEmbedder
from agno.vectordb.lancedb import LanceDb, SearchType
from agno.db.sqlite.sqlite import SqliteDb
from agno.vectordb.qdrant import Qdrant
from agno.knowledge.knowledge import Knowledge
from agno.tools.reasoning import ReasoningTools
from agno.tools.knowledge import KnowledgeTools


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s') 


good_models = ["llama3.1:8b", "granite4:micro", "granite4", "cogito:8b", "cogito:14b","gpt-oss:20b"]


def find_markdown_files(
    start_path: str, ignore_patterns: list[str] = None
) -> list[str]:
    if ignore_patterns is None:
        ignore_patterns = [".venv", "node_modules", ".git", "__pycache__", ".tmp"]

    markdown_files = []
    if not os.path.isdir(start_path):
        print(f"Error: Path '{start_path}' is not a valid directory.")
        return []

    for root, dirs, files in os.walk(start_path):
        # Filter out directories that match ignore patterns
        dirs[:] = [
            d for d in dirs if not any(pattern in d for pattern in ignore_patterns)
        ]

        # Check if current path contains any ignore patterns
        if any(pattern in root for pattern in ignore_patterns):
            continue

        for file in files:
            # Check if the file ends with .md or .markdown
            if file.endswith(".md") or file.endswith(".markdown"):
                # If it is, join the root path and file name to get the full path
                full_path = os.path.join(root, file)
                markdown_files.append(full_path)
    return markdown_files


class Cheetsheetz:
    def __init__(self,vdb="lancedb",max_results=1000):
        contents_db = SqliteDb(db_file="my_knowledge.db")

        if 'QDRANT_URL' in os.environ:
            qdrant_url = os.environ['QDRANT_URL']
        else:
            qdrant_url = "http://localhost:6333"

        if vdb == "lancedb":
            self.knowledge = Knowledge(
                max_results=max_results,
                contents_db=contents_db,
                vector_db=LanceDb(
                    name="Lance Job Description",
                    uri=".tmp/lancedb",
                    table_name="cheetsheetz",
                    search_type=SearchType.hybrid,
                    # embedder=OllamaEmbedder(id="openhermes", dimensions=4096),
                    # embedder=OllamaEmbedder(id="nomic-embed-test"),
                )
            )
        elif vdb == "qdrant":
           self.knowledge = Knowledge(
                max_results=max_results,
                contents_db=contents_db,
                vector_db=Qdrant(
                name="Qdrant Job Description",
                collection="vectors",
                url=qdrant_url
            )
        )         
    def add_md(self, mdfile):
        self.knowledge.add_content(name=mdfile, path=mdfile)

if __name__ == "__main__":
    c = Cheetsheetz("qdrant")
    memory_db = SqliteDb(db_file="agno-memory.db")

    if sys.argv[1] == "ingest":
        mdlist = find_markdown_files(sys.argv[2])
        print(f"Found {len(mdlist)}")
        for f in mdlist:
            print(f)
            c.add_md(f)
    elif sys.argv[1] == "chat":
        if sys.argv[2] not in good_models:
            print(f"You did not pick from {good_models}")
            my_model = OpenAIChat(id="gpt-5-nano")
        else:
            my_model = Ollama(id=sys.argv[2])

        print(f"Using {my_model}")

        knowledge_tools = KnowledgeTools(
            knowledge=c.knowledge,
            search=True,
            analyze=True,
            add_few_shot=True,
        )



        agent = Agent(
            name=f"Agno Assistant",
            model=my_model,
            instructions=[
                "Search the list of markdown files to find which file has the content",
                "Search your knowledge before answering the question.",
                "Only include the output in your response. No other text.",
                "You must include sources in your response and NOT use other information.",
            ],
            knowledge=c.knowledge,
            tools=[ReasoningTools(add_instructions=True),knowledge_tools],
            add_datetime_to_context=False,
            markdown=True,
            debug_mode=True,
            db=memory_db,
            add_history_to_context=True,
            num_history_runs=3,
        )
        while True:
            user_prompt = input("\nEnter your question (or '!exit' to quit): ")
            if user_prompt.strip() == "!exit":
                print("Exiting chat...")
                break
            if user_prompt.strip():
                agent.print_response(
                    user_prompt,
                    stream=True,
                    show_full_reasoning=True,
                    stream_events=True,
                )
