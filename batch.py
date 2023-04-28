import random
from glob import glob
import frontmatter
import random


FREQ = 2  # once N days (probabilistic)
COUNT = 1  # (deterministic)


if random.random() <= 1 / FREQ:
    paths = glob("content/posts/*")
    random.shuffle(paths)
    count = 0
    for path in paths:
        post = frontmatter.load(path)
        if "draft" in post and post["draft"]:
            post["draft"] = False
            frontmatter.dump(post, path)
            count += 1
            if count >= COUNT:
                break
