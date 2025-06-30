# Brawl Stars API Data Loader

[![Check Style](https://github.com/GreetingsEarthling/brawl-stars-seo/actions/workflows/style.yaml/badge.svg)](https://github.com/GreetingsEarthling/brawl-stars-seo/actions/workflows/style.yaml)

[![Tests](https://github.com/GreetingsEarthling/brawl-stars-seo/actions/workflows/tests.yaml/badge.svg)](https://github.com/GreetingsEarthling/brawl-stars-seo/actions/workflows/tests.yaml)

This project fetches Brawler data from the Brawl Stars API and stores it in a local SQLite database.

## Setup Instructions

1. **Install required libraries**

2. **Set up API token**
- Replace the empty string in `HEADERS` with your Brawl Stars API token:
  ```python
  "Authorization": "Bearer YOUR_API_TOKEN"
  ```
## How to Run

Run the script using:

python brawl_post.py

## Overview

- Sends a GET request to the Brawl Stars API `/brawlers` endpoint.
- Converts the JSON response into a pandas DataFrame.
- Saves the data to a SQLite database (`brawl_stars.db`) in a table called `brawlers`.
- Queries and prints the table content.
