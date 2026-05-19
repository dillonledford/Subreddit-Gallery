from flask import Flask, request, jsonify, render_template
import praw
import logging
import threading
import requests
import time
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)

# Configure Reddit API using environment variables
reddit = praw.Reddit(
    client_id=os.getenv('REDDIT_CLIENT_ID'),
    client_secret=os.getenv('REDDIT_CLIENT_SECRET'),
    user_agent='MyRedditApp/0.1 by Dillon Ledford'
)

@app.route('/')
def index():
    return render_template('index.html')

if not app.view_functions.get('fetch_media'):
    @app.route('/fetch_media', methods=['POST'])
    def fetch_media():
        try:
            data = request.json
            subreddit_name = data.get('subreddit')
            search_term = data.get('search_term')
            num_images = int(data.get('num_images', 10))
            sort_order = data.get('sort_order')
            if subreddit_name.startswith('r/'):
                subreddit_name = subreddit_name[2:]
            logging.info(f"Fetching {num_images} media for subreddit: {subreddit_name} with search term: {search_term if search_term else 'None'} and sort order: {sort_order}")
            subreddit = reddit.subreddit(subreddit_name)
            media_posts = []
            count = 0
            after = None

            while count < num_images:
                if search_term:
                    submissions = subreddit.search(query=search_term, sort='new', time_filter='all', params={'after': after})
                else:
                    submissions = getattr(subreddit, sort_order)(params={'after': after})

                new_count = 0
                for submission in submissions:
                    if submission.url.endswith(('jpg', 'jpeg', 'png', 'gif')):
                        if hasattr(submission, 'preview'):
                            thumbnail_url = submission.preview['images'][0]['resolutions'][0]['url']
                            full_image_url = submission.url
                            media_posts.append({
                            'thumbnail': thumbnail_url,
                            'full': full_image_url,
                            'post_url': f"https://reddit.com{submission.permalink}"
                            })
                            count += 1
                            new_count += 1
                            if count >= num_images:
                                break

                if new_count == 0:
                    break

                after = submission.fullname if new_count > 0 else None

            logging.info(f"Fetched {len(media_posts)} media posts")
            return jsonify(media_posts)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            return jsonify({"error": str(e)}), 500

## Keep Render Site Alive - No Spindown --- Script Start ---

def keep_alive():
    time.sleep(30)  # wait for server to start
    while True:
        try:
            requests.get('https://subreddit-gallery.onrender.com/')
        except:
            pass
        time.sleep(14 * 60)  # ping every 14 minutes

if os.getenv('FLASK_ENV') != 'development':
    thread = threading.Thread(target=keep_alive, daemon=True)
    thread.start()

## Keep Render Site Alive - No Spindown --- Script End ---

if __name__ == '__main__':
    app.run()
    
    # Enable for debugging
    #app.run(debug=True)