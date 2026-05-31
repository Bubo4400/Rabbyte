# Rabbyte – Wikipedia Pathfinder

A semantic search tool that finds a path between two Wikipedia articles using sentence‑embedding similarity. Instead of traditional graph traversal, Rabbyte uses AI‑powered comparisons to choose the most promising next link at each step.

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue) ![License](https://img.shields.io/badge/license-MIT-green) ![Sentence Transformers](https://img.shields.io/badge/SentenceTransformers-required-orange)

## Features

- **Semantic Link Selection** – Uses `all‑MiniLM‑L6‑v2` embeddings to compare the current page’s links with the target article.
- **Interactive CLI** – Choose start and end pages by name or random selection (`--rand`).
- **Backtracking** – When no link is found, the algorithm steps back to the previous page.
- **Real‑time Feedback** – Displays time spent per page, total visited pages, and current location.
- **No API Keys** – Uses `wikipediaapi` with a custom user agent (requires only an email address).

---

## Installation

### Prerequisites
- Python 3.8 or higher
- Internet connection (to fetch Wikipedia pages and download the embedding model)

### Clone & Setup
```bash
git clone https://github.com/Bubo4400/Rabbyte
cd Rabbyte
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from your terminal:

```bash
python main.py
```

You will be prompted for:
1. **Email address** – Used as part of the Wikipedia user agent (e.g., `Rabbyte your@email.com`).
2. **Start page** – Enter a Wikipedia article title or `--rand` for a random page.
3. **End page** – Enter another title or `--rand`.

The program then attempts to find a path from the start page to the end page by repeatedly:
- Fetching all links on the current page.
- Embedding each link title and comparing it to the target title.
- Choosing the link with the highest cosine similarity.

The search continues until it either reaches the target or gets stuck (and backtracks).

### Example
```txt
Please enter your email: user@example.com

Which page to start on (--rand for random page): Artificial intelligence
Which page to end on (--rand for random page): Philosophy

Rabbyte spent 0.34sec on the last site.
Currently on page: Artificial intelligence and this is page number 1 that has been visited
...
Successfully found path in 24 links by viewing {...} in 12.45sec
The path from Artificial intelligence to Philosophy is:
Artificial intelligence -> History of artificial intelligence -> ...
```

---

## Project Structure
```txt
rabbyte-wikipedia-pathfinder/
├── main.py              # Entry point, search loop, backtracking logic
├── src/
│   ├── compare.py       # Cosine similarity and embedding comparison
│   └── wiki.py          # Wikipedia API wrapper (get page, links, random)
└── README.md
```

---

## How It Works

1. **Embedding Model** – `all-MiniLM-L6-v2` (Sentence Transformers) converts page titles into 384‑dimensional vectors.
2. **Similarity Scoring** – For each link on the current page, we compute cosine similarity between its title embedding and the target page’s title embedding.
3. **Greedy Step** – The link with the highest similarity (and not yet visited) becomes the next page.
4. **Dead‑end Handling** – If a page has no links, only one link (already visited), or none of its links lead towards the target, the algorithm backtracks to the previous page and tries the next‑best alternative.
5. **Termination** – Stops when the target page is reached or after exhaustive backtracking (returns an empty path).

The search is **not** guaranteed to find the shortest path in graph terms, but it often finds a semantically meaningful route.

---

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to improve.

---

**Rabbyte** – Navigate Wikipedia with semantic intelligence. 🐇
