
mosdac-helpbot/
│
├── data_ingestion/
│   ├── crawlers/
│   │   ├── mosdac_static_scraper.py
│   │   └── mosdac_dynamic_scraper.py
│   ├── parsers/
│   │   ├── pdf_parser.py
│   │   ├── docx_parser.py
│   │   └── metadata_extractor.py
│   └── cleaned_data/
│       └── <output_jsons>
│
├── knowledge_graph/
│   ├── entity_extraction.py
│   ├── relation_extraction.py
│   ├── kg_builder.py
│   └── neo4j_connector.py
│
├── llm_rag_pipeline/
│   ├── retriever/
│   │   ├── embed_documents.py
│   │   └── vector_store_faiss.py
│   ├── generator/
│   │   └── response_generator.py
│   └── query_pipeline.py
│
├── chatbot_ui/
│   ├── react_app/       # or streamlit_app/
│   │   ├── public/
│   │   └── src/
│   └── static_assets/
│       └── bot_logo.png
│
├── api_services/
│   ├── app.py
│   ├── routes/
│   │   ├── chat.py
│   │   ├── kg.py
│   │   └── document_parser.py
│   └── models/
│
├── deployment/
│   ├── Dockerfile
│   ├── docker-compose.yml
│   └── kubernetes/
│       └── deployment.yaml
│
├── tests/
│   ├── unit_tests/
│   └── integration_tests/
│
├── notebooks/
│   └── exploration.ipynb
│
├── docs/
│   ├── architecture_diagram.png
│   └── user_manual.md
│
└── README.md




🛠️ Recommended Stack Summary

Component	Tool/Tech
Web Scraping	Scrapy, Selenium, BeautifulSoup
NLP + KG	spaCy, NLTK, Neo4j, PyKEEN
LLM + RAG	LangChain, NVIDIA RAG, FAISS, HuggingFace Transformers
Frontend	React, Streamlit, CesiumJS
Backend API	FastAPI, Flask, Node.js
Deployment	Docker, Railway/Fly.io/GCP