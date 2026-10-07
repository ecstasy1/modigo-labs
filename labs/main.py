def all_unique_tags(post):
    tags = set()
    for post in post:
       tags.update(post["tags"])
    return tags