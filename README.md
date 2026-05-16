# SSG
A SSG for documentation. Used for all my projects. 

## Start
Install dependencies
```Bash
python install -r requirements.txt
```
Then
```Bash
python main.py
```
to start the wizard. 

### Content
Doesn't matter, everyhting gets copied. 
#### .md
Should have a heading e.g: (minimum = title)
```yaml
---
title: Welcome
sitemap:
  lastmod: "YYYY-MM-DD"
  changefreq: "monthly"
  priority: "0.5"
---
```
Then the rest of the .md file. 



## Features
- Generates sitemap
- Generates robots.txt
- Supports all filetypes (.ico, .jpeg...)
- Code highlighting

## Working on (never going to happen)
- Warning before generation of site if not configured
- More templates
- Better error handling
- Code refactoring (it's bad)
- Images
- Nav bar positioning (now it's alphabetical)
- Next/back button
- Python 3.13 and older support (.copy isn't a thing there)
- A way to directly push the website to a server?
- Export function (.zip, .tar...)

## Examples
### Working example
[FlanOS Documentation](https://flanos.forageek.com/)
### Code + Screenshot
```Markdown
---
title: Welcome
sitemap:
  lastmod: "YYYY-MM-DD"
  changefreq: "monthly"
  priority: "0.5"
---

# Welcome to the documentation of FlanOS!

```Python
display print "Hello there!" #It's Flanlang code
\`\`\`


## Features

| Month    | Savings |
| -------- | ------- |
| January  | $250    |
| February | $80     |
| March    | $420    |
```
<img width="1407" height="1523" alt="image" src="https://github.com/user-attachments/assets/74a7d856-9b25-4cf2-b6df-f15e1106b186" />

# License
Free for personal, educational, research, and non-commercial use.
Commercial use requires written permission or a separate commercial license.


