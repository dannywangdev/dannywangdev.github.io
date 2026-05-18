import os
import re

SECONDS_PER_IMAGE = 12

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

articles = []
for item in os.listdir(SCRIPT_DIR):
    item_path = os.path.join(SCRIPT_DIR, item)
    if os.path.isdir(item_path):
        index_path = os.path.join(item_path, "index.html")
        if os.path.isfile(index_path):
            with open(index_path, "r", encoding="utf-8") as f:
                content = f.read()
            # Find the article title inside <main> (skip sidebar h1)
            main_match = re.search(r"<main[^>]*>(.*?)</main>", content, flags=re.DOTALL)
            main_content = main_match.group(1) if main_match else content
            title_match = re.search(r"<h1>(.*?)</h1>", main_content)
            title = title_match.group(1) if title_match else item
            if len(title) > 60:
                title = title[:57] + "..."
            articles.append((title, index_path))

if not articles:
    print("No articles found.")
    exit(1)

print("\nAvailable articles:\n")
for i, (title, path) in enumerate(articles, 1):
    print(f"  {i}. {title}")

print()
while True:
    try:
        choice = input(f"Select article (1-{len(articles)}): ").strip()
        idx = int(choice) - 1
        if 0 <= idx < len(articles):
            break
        print(f"Enter a number between 1 and {len(articles)}.")
    except ValueError:
        print("Enter a valid number.")

path = articles[idx][1]
with open(path, "r", encoding="utf-8") as f:
    content = f.read()

# Count images
img_count = len(re.findall(r"<img[^>]+>", content))

# Strip tags for word count
text = re.sub(r"<script[^>]*>.*?</script>", "", content, flags=re.DOTALL)
text = re.sub(r"<style[^>]*>.*?</style>", "", text, flags=re.DOTALL)
text = re.sub(r"<[^>]+>", " ", text)
text = re.sub(r"\s+", " ", text).strip()

word_count = len(text.split())
base_minutes = word_count / 200
image_seconds = img_count * SECONDS_PER_IMAGE
image_minutes = image_seconds / 60
total_minutes = base_minutes + image_minutes

print(f"\n--- {articles[idx][0]} ---")
print(f"  Word count:      {word_count}")
print(f"  Images:          {img_count} (+{image_seconds}s)")
print(f"  Read time:       {max(1, round(total_minutes))} min")
print(f"  Breakdown:       {max(1, round(base_minutes))} min reading + {image_seconds}s for images\n")
