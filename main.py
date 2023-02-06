import requests
import random
import json
import yt_dlp
def save_meme(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/random/.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    response = requests.get(url, headers=headers)
    data = json.loads(response.text)
    if data[0]["kind"] == "Listing":
        if data[0]["data"]["children"]!=[]:
            random_post = data[0]["data"]["children"][0]["data"]
            if "url" in random_post and random_post["url"].endswith(("jpg", "jpeg", "png")): #add .mp4 extension to include video posts
                url= random_post["url"]
                post_caption = random_post["title"]
                ydl_opts_start = {
                    'format': 'bv+ba/b',        #set 'format': 'wv+wa/w` to get lowest filesize
                    'outtmpl': f'videos/%(title)s.%(ext)s',
                    'no_warnings': False,
                    'logtostderr': False,
                    'ignoreerrors': False,
                    'noplaylist': True,
                    'writethumbnail': False
                    }
                ydl = yt_dlp.YoutubeDL(ydl_opts_start)
                with ydl:
                    result = ydl.extract_info(url, download=False)
                    title = ydl.prepare_filename(result)
                ydl.download([url])
            else:
                print("Your requested post format not found!")
        else:
            print("Empty subreddit! No posts found!")
    else:
        print("Subreddit doesn't exists!")

subreddit = "fingmemes" # Replace with desired subreddit name
save_meme(subreddit)
