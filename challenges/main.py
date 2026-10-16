def all_unique_tags(posts):
    tags = set()
    for post in posts:
        tags.update(post["tags"])
    return tags