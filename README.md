# Subreddit Gallery

A clean, minimal image gallery for browsing any subreddit with sorting options, keyword filtering, and keyboard navigation. Built with **Python / Flask**.

**Live App:** [Reddit Media Gallery](https://subreddit-gallery.onrender.com)

<picture><img width="1050" height="200" alt="Image" src="https://github.com/user-attachments/assets/eca11229-f3d5-4ee4-ac54-4c7018826596" /></picture>

---

## Features

- **Subreddit browsing** — Enter any subreddit name to load its images quickly
- **Sorting options** — Sort posts by Hot, New, or Top
- **Custom image count** — Choose how many images to load at once
- **Keyword filtering** — Optionally filter results by keyword (e.g. a character name or "cosplay")
- **Full-page gallery view** — Images are displayed in a clean, dark-background gallery
- **Keyboard & click navigation** — Select any image and navigate with arrow keys or by clicking through them
- **View Post** — Opens the original Reddit post for the currently displayed image in a new tab

---

## Requirements

- Python 3.x
- Flask

---

## Installation & Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/Reddit-Media-Gallery.git
   cd Reddit-Media-Gallery
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the app**
   ```bash
   python app.py
   ```

4. **Open in your browser**
   ```
   http://localhost:5000
   ```

---

## Usage

1. Enter a subreddit name (e.g. `cats`, `EarthPorn`, `itookapicture`)
2. Select a sorting method: **Hot**, **New**, or **Top**
3. Enter the number of images to load
4. *(Optional)* Enter a keyword to filter results
5. Browse the gallery — click any image to open it, then use **arrow keys** or **click** to navigate

---

## Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript

---

## Why I Built This

I wanted a way to browse through image Subreddits like a gallery with keyboard navigation.
