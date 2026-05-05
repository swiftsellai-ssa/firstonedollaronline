import os
import glob
import pathlib

seo_tags = """
  <!-- SEO & Social Meta Tags -->
  <link rel="icon" href="/favicon.ico">
  <link rel="apple-touch-icon" href="/apple-touch-icon.png">
  <link rel="manifest" href="/site.webmanifest">
  <meta name="robots" content="index,follow">
  <meta property="og:title" content="First$1online | Make Your First $1 Online">
  <meta property="og:description" content="A dead-simple $1 Notion kit designed to help complete beginners cross the scariest threshold: making your literal first $1 online.">
  <meta property="og:image" content="https://firstonedollaronline.com/og-image.jpg">
  <meta property="og:url" content="https://firstonedollaronline.com/">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="First$1online | Make Your First $1 Online">
  <meta name="twitter:description" content="A dead-simple $1 Notion kit designed to help complete beginners cross the scariest threshold: making your literal first $1 online.">
  <meta name="twitter:image" content="https://firstonedollaronline.com/og-image.jpg">
  <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "name": "First$1online",
    "url": "https://firstonedollaronline.com/",
    "description": "Make your first $1 online with proven micro-ideas."
  }
  </script>
"""

tap_target_css = """
    /* Tap Target Enhancements */
    a.logo { min-height: 48px; display: inline-flex; align-items: center; }
    .cta-button, button, .newsletter button { min-height: 48px; }
"""

os.chdir(r"c:\projapp\first$1online")

html_files = glob.glob('*.html')

for filepath in html_files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Inject SEO tags
    if 'og:title' not in content:
        content = content.replace('</head>', seo_tags + '\n</head>')

    # Inject Tap Target CSS
    if 'Tap Target Enhancements' not in content:
        content = content.replace('</style>', tap_target_css + '\n</style>')

    # Add Landmarks
    if '<header>' not in content and '<nav>' in content and '<footer>' in content:
        content = content.replace('<nav>', '<header>\n  <nav>')
        content = content.replace('</nav>', '</nav>\n</header>\n<main>')
        content = content.replace('<footer>', '</main>\n<footer>')

    # Fix ARIA Labels
    content = content.replace('id="skill-select"', 'id="skill-select" aria-label="Select your skill"')
    content = content.replace('id="time-select"', 'id="time-select" aria-label="Select your time commitment"')
    content = content.replace('type="email"', 'type="email" aria-label="Email address"')

    # Fix Empty Links
    content = content.replace('href="#" class="logo"', 'href="/" class="logo"')

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

# Create robots.txt
robots_txt = """User-agent: *
Allow: /
Sitemap: https://firstonedollaronline.com/sitemap.xml
"""
with open('robots.txt', 'w', encoding='utf-8') as f:
    f.write(robots_txt)

# Create sitemap.xml
sitemap_xml = """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>https://firstonedollaronline.com/</loc>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>https://firstonedollaronline.com/1-idea.html</loc>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>
  <url>
    <loc>https://firstonedollaronline.com/1-idea-unlocked.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.5</priority>
  </url>
  <url>
    <loc>https://firstonedollaronline.com/the-dollar-game.html</loc>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>
</urlset>
"""
with open('sitemap.xml', 'w', encoding='utf-8') as f:
    f.write(sitemap_xml)

manifest_json = """{
  "name": "First$1online",
  "short_name": "First$1",
  "start_url": "/",
  "display": "standalone",
  "background_color": "#0a0e1f",
  "theme_color": "#10b981",
  "icons": [
    {
      "src": "/apple-touch-icon.png",
      "sizes": "192x192",
      "type": "image/png"
    }
  ]
}"""
with open('site.webmanifest', 'w', encoding='utf-8') as f:
    f.write(manifest_json)

pathlib.Path("favicon.ico").touch(exist_ok=True)
pathlib.Path("apple-touch-icon.png").touch(exist_ok=True)
pathlib.Path("og-image.jpg").touch(exist_ok=True)

print("Finished applying SEO and accessibility fixes.")
