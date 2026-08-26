"""
The goal of this task is to convert source code like:
<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
Extracts its src contents and change to the format of https://youtu.be/xvFZjo5PgG0 by using regex patterns.
"""

import re

def main():
    print(parse(input('HTML: ')))

def parse(s):
    url = re.search(r'<iframe.*src="https?://(?:www\.)?youtube\.com/embed/(.+)".*</iframe>', s)
    if url:
        return f"https://youtu.be/{url.group(1)}"
    else:
        return None

if __name__ == '__main__':
    main()