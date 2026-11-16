# Python Discord Bot

An asynchronous Discord bot built with `discord.py` featuring slash commands (`app_commands`), interactive mention parsing, and secure environment-based secret management.

## Overview

This project explores event-driven asynchronous programming (`asyncio`), Discord's Gateway API, and secure credential handling without hardcoding API tokens.

### Key Features
* **Slash Commands (`app_commands`):** Includes `/hello`, `/cba`, and `/roll` (with input validation and follow-up responses).
* **Mention-Based Calculator:** Parses direct bot mentions to dynamically evaluate basic arithmetic (`+`, `-`, `*`, `/`).
* **Secure Secret Management:** Loads the bot token strictly from environment variables (`os.environ["DISCORD_TOKEN"]`).

## Project Structure

```text
python-discord-bot/
├── src/              # Bot source code
├── pyproject.toml    # Project metadata and dependencies managed with uv
├── uv.lock           # Locked dependency versions for reproducible builds
└── README.md
```

## Prerequisites

* Python 3.10+
* [uv](https://github.com)
* A Discord Bot Token from the [Discord Developer Portal](https://discord.com)

## How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com
   cd python-discord-bot
   ```

2. **Install dependencies with `uv`:**
   ```bash
   uv sync
   ```

3. **Set your bot token and run:**
   ```bash
   export DISCORD_TOKEN="your_token_here"
   uv run src/main.py
   ```
   *(Replace `main.py` with your script's exact filename inside `src/`.)*

## Planned Improvements (Roadmap)

* [ ] Add `try...except` error handling for invalid calculator inputs and division by zero.
* [ ] Add ChatOps network diagnostic slash commands (`/ping`, `/dns`, `/subnet`).
* [ ] Containerise with Docker using `uv` and automate image builds with GitHub Actions.
