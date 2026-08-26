# Learnings: CS50P watch.py

- **Objective**: Extract embedded YouTube URLs from HTML `iframe` tags and convert them to short `youtu.be` links (e.g., transforming `<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>` into `https://youtu.be/xvFZjo5PgG0`) by extracting the contents within src.
- **Takeaway 1 (Pattern Matching & Groups)**:
  - Used `re.search(r'<iframe.*src="https?://(?:www\.)?youtube\.com/embed/(.+)".*</iframe>', s)` to scan anywhere in the string.
  - Use non-capturing groups `(?: )` when grouping logic without extracting (e.g., `(?:www\.)?`), and capturing groups `(.+)` to isolate the video ID for retrieval via `url.group(1)`.
- **Takeaway 2 (Escape Characters & Raw Strings)**:
  - Always prefix the pattern with `r''` and use backslashes (`\.`) to ensure literal dots are not misinterpreted as regex wildcards.
- **Takeaway 3 (Alternative Regex Methods)**:
  - `re.match` checks patterns strictly from the very beginning of the string, while `re.findall` returns all matching groups as a list if multiple URLs are present.
