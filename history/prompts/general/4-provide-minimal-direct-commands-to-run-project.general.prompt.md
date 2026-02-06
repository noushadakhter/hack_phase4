---
id: 4
title: Provide minimal direct commands to run project
stage: general
date_iso: 2026-01-25
surface: agent
model: gemini-1.5-pro
feature: none
branch: main
user: P.c
command: provide minimal direct run commands
labels: ["project-setup", "run-project", "frontend", "backend", "direct-commands", "minimal"]
links:
  SPEC: null
  TICKET: null
  ADR: null
  PR: null
files_yaml: []
tests_yaml: []
prompt_text: |
  ab yar mujhe sirf command bata mei kese run karu
response_text: |
  **Terminal 1 (Backend):**
  ```bash
  cd C:\Users\P.c\Desktop\hackathon2\phase3\backend
  uvicorn main:app --reload
  ```
  **Terminal 2 (Frontend):**
  ```bash
  cd C:\Users\P.c\Desktop\hackathon2\phase3\frontend
  npm run dev
  ```
  ---
  Dono terminals mein ye commands chalayen.
  ---
outcome: User received minimal explicit terminal commands for running frontend and backend.
evaluation:
  relevance: High
  completeness: Complete
  accuracy: Accurate
  follow_up_qa: None
  performance: Good
  UX: Very concise and direct instructions given as requested.
---