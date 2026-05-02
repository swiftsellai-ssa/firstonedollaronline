import sys

with open('index.html', 'r', encoding='utf-8') as f:
    idx_content = f.read()

# Extract <head> inclusive CSS
head_start = idx_content.find('<head>')
head_end = idx_content.find('</head>') + 7
head_html = idx_content[head_start:head_end]

# Extract Particle Script & Confetti
nav_start = idx_content.find('<nav>')
nav_end = idx_content.find('</nav>') + 6
nav_html = idx_content[nav_start:nav_end]

footer_start = idx_content.find('<footer>')
footer_end = idx_content.find('</footer>') + 9
footer_html = idx_content[footer_start:footer_end]

particles_script_start = idx_content.find('<!-- Confetti Library -->')
particles_script_end = idx_content.find('</body>')
particles_script = idx_content[particles_script_start:particles_script_end]

# Add specific CSS for the ideas list
extra_css = '''
  <style>
    .idea-card {
      background: var(--white);
      padding: 1.5rem 2rem;
      border-radius: 12px;
      margin-bottom: 1.5rem;
      border: 1px solid #1e293b;
      box-shadow: var(--shadow);
    }
    .idea-card h3 {
      color: var(--primary);
      margin-bottom: 0.5rem;
      font-size: 1.4rem;
    }
    .idea-card p {
      color: var(--text-light);
      font-size: 1.05rem;
    }
    .idea-meta {
      display: flex;
      gap: 1rem;
      margin-bottom: 1rem;
      font-size: 0.9rem;
      font-weight: 600;
    }
    .tag {
      background: rgba(16, 185, 129, 0.1);
      color: var(--accent);
      padding: 0.2rem 0.6rem;
      border-radius: 4px;
    }
    .paywall-container {
      position: relative;
      margin-top: 1.5rem;
      border-radius: 12px;
      overflow: hidden;
    }
    .blurred-content {
      filter: blur(6px);
      opacity: 0.4;
      pointer-events: none;
      user-select: none;
    }
    .paywall-overlay {
      position: absolute;
      top: 0; left: 0; width: 100%; height: 100%;
      display: flex;
      flex-direction: column;
      align-items: center;
      justify-content: center;
      background: linear-gradient(to bottom, rgba(10,14,31,0.2), var(--bg) 90%);
      text-align: center;
      padding: 2rem 1rem;
      z-index: 10;
    }
  </style>
'''

head_html = head_html.replace('</head>', extra_css + '</head>')
head_html = head_html.replace('<title>First$1online – Make Your First $1 Online</title>', '<title>First$1online – $1 Ideas</title>')
# Force 'index.html#' links to not be broken since we are on 1-idea.html
nav_html = nav_html.replace('href="#what-you-get"', 'href="index.html#what-you-get"')
nav_html = nav_html.replace('href="#preview"', 'href="index.html#preview"')

body_html = f'''
<body>
  <!-- === PARTICLE BACKGROUND === -->
  <div id="particles-bg" style="position: fixed; top: 0; left: 0; width: 100%; height: 100%; pointer-events: none; z-index: -1; overflow: hidden;">
    <canvas id="particle-canvas" style="display: block; width: 100%; height: 100%;"></canvas>
  </div>

  {nav_html}

  <section class="hero" style="padding: 4rem 1.5rem 1rem; background: transparent;">
    <h1>The <span>$1 Idea</span> Vault</h1>
    <p>A curated list of micro-services, digital products, and tiny actions that people are actually buying for $1.</p>
  </section>

  <section class="section" style="background: transparent; padding-top: 0; max-width: 800px; margin: 0 auto;">
    
    <div class="idea-card">
      <div class="idea-meta">
        <span class="tag">Writing</span>
        <span class="tag" style="background: #1e293b; color: var(--text);">15 mins</span>
      </div>
      <h3>The Profile Bio Audit</h3>
      <p>Offer to rewrite someone's Twitter or LinkedIn bio for exactly $1. You'll be surprised how many people hate writing about themselves. Position it as a "Roast & Fix" to increase conversion.</p>
    </div>

    <div class="idea-card">
      <div class="idea-meta">
        <span class="tag">Design</span>
        <span class="tag" style="background: #1e293b; color: var(--text);">30 mins</span>
      </div>
      <h3>Notion Workspace Icons</h3>
      <p>Design a very specific, niche set of 10 Notion icons (e.g., "Dark Mode Finance Icons") and drop them in Notion communities. Keep the friction non-existent by pricing it at a single dollar.</p>
    </div>
    
    <!-- PAYWALL -->
    <div class="paywall-container">
      <div class="blurred-content">
        <div class="idea-card">
          <div class="idea-meta"><span class="tag">Tech</span><span class="tag">60 mins</span></div>
          <h3>Hidden Idea #3</h3>
          <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam nec magna non arcu gravida accumsan a at erat. Sed dignissim justo non libero fringilla congue.</p>
        </div>
        <div class="idea-card">
          <div class="idea-meta"><span class="tag">Video</span><span class="tag">15 mins</span></div>
          <h3>Hidden Idea #4</h3>
          <p>Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Vestibulum in finibus orci. Class aptent taciti.</p>
        </div>
        <div class="idea-card">
          <div class="idea-meta"><span class="tag">Data</span><span class="tag">Weekend</span></div>
          <h3>Hidden Idea #5</h3>
          <p>Morbi tincidunt iaculis justo, nec dictum arcu eleifend eget. In tristique est et tincidunt iaculis. Nunc pulvinar mi in massa commodo aliquet.</p>
        </div>
      </div>
      
      <div class="paywall-overlay">
        <i class="fas fa-lock" style="font-size: 3rem; color: var(--accent); margin-bottom: 1rem;"></i>
        <h3 style="font-size: 1.8rem; margin-bottom: 0.5rem; color: var(--text);">Unlock 20+ More Proven Ideas</h3>
        <p style="color: var(--text-light); margin-bottom: 2rem; max-width: 400px; margin-left: auto; margin-right: auto;">Get instant access to the full list, the Notion Blueprint, and our builder community.</p>
        <a href="https://buy.stripe.com/cNi00jcgkcLx4A092k8N201" class="main-cta">Unlock Full List & Blueprint for $1</a>
      </div>
    </div>
    
  </section>

  {footer_html}
  {particles_script}
</body>
</html>
'''

full_html = '<!DOCTYPE html>\n<html lang="en">\n' + head_html + '\n' + body_html
with open('c:/projapp/first$1online/1-idea.html', 'w', encoding='utf-8') as f:
    f.write(full_html)
