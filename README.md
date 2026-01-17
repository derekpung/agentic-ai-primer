# Agentic AI Primer

Just figuring out a reusable, containerised setup for local LLM projects

1. Basic web UI
   - ChatGPT clone:
     - [x] Login
     - [x] Simple user input
     - [ ] Upload files (for RAG)
     - [ ] Chat History
     - [ ] Feedback

1. Backend
   - [x] Issue JWT after Auth
   - [ ] Agent endpoint

1. Keycloak
   - test user:
     - username: bob
     - password: thebuilder

## Setup

1. add `127.0.0.1 dev.local` to `host` file
1. run `docker compose up nginx`
1. access from ui browser: `dev.local`
