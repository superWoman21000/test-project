# Test Repo for Code Review Pipeline

This is a tiny throwaway project used only to exercise the automated
code review pipeline (syntax via flake8, semantic + security via Gemini).

It has no real purpose beyond giving the pipeline something to analyze.

## Structure
- `app/inventory.py` — a minimal inventory tracker (clean baseline on `main`)

A follow-up pull request introduces a new file with deliberate issues
to confirm the pipeline catches problems across all three review
dimensions.
