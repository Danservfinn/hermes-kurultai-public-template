# Contributing

This repository is public. Treat every contribution as potentially visible forever.

## Do not commit

- Tokens, API keys, private keys, OAuth files, cookies, chat IDs, phone numbers, customer data, payment data, or local databases.
- Live Hermes homes, live Brain contents, raw captures, session transcripts, delivery targets, or private profile identity files.
- Absolute user-home paths or personal names from a live deployment.

## Required before PR/commit

```bash
python3 tests/validate_repo.py
git diff --cached --name-only
```

If the validation scan flags a file, rewrite the commit before publishing. Do not add a follow-up cleanup commit that leaves leaked history intact.
