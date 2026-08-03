import base64

def b64(filename):
    with open(filename, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

b64_char = b64('basic_character.png')
b64_chicken = b64('chicken_sprites.png')
b64_cow = b64('cow_sprites.png')
b64_plants = b64('basic_plants.png')
b64_grass = b64('grass.png')
b64_tilled = b64('tilled_dirt.png')
b64_house = b64('house_clean.png')
b64_coop = b64('chicken_house_building.png')
b64_fences = b64('fences.png')
b64_chest = b64('chest.png')
b64_egg = b64('egg_item.png')
b64_milk = b64('milk_item.png')

html_content = f"""<!DOCTYPE html>
<html lang="tr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Arcadia Homestead - Sprout Lands Web3 GameFi</title>
  
  <meta name="description" content="Arcadia Homestead - Official Sprout Lands Web3 GameFi farm on Circle ARC Testnet.">
  
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Silkscreen:wght@400;700&family=VT323&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">
  
  <script src="https://cdnjs.cloudflare.com/ajax/libs/ethers/6.13.1/ethers.umd.min.js"></script>

  <style>
    :root {{
      --sprout-sky: #581c87;
      --wood-dark: #2c1609;
      --wood-mid: #4d2813;
      --wood-light: #7a4320;
      --parchment-bg: #fcedc0;
      --sprout-green: #3d7a22;
      --stardew-gold: #fde047;
      --text-dark: #381e0d;
      --text-light: #fef0c7;
      --font-pixel: 'Press Start 2P', monospace;
      --font-stardew: 'Silkscreen', cursive;
      --font-retro: 'VT323', monospace;
      --font-sans: 'Outfit', sans-serif;
    }}

    * {{ box-sizing: border-box; margin: 0; padding: 0; user-select: none; -webkit-user-select: none; }}

    html, body {{
      width: 100%; min-height: 100vh;
      background-color: var(--sprout-sky);
      color: var(--text-light);
      font-family: var(--font-sans);
      overflow-x: hidden;
      scroll-behavior: smooth;
    }}

    #leafCanvas, #celebrationCanvas {{
      position: fixed; inset: 0; z-index: 0; pointer-events: none; image-rendering: pixelated;
    }}
    #celebrationCanvas {{ z-index: 600; }}

    .stardew-card {{
      background: linear-gradient(180deg, var(--wood-mid) 0%, var(--wood-dark) 100%);
      border: 5px solid #140a04; outline: 3px solid var(--wood-light); outline-offset: -8px;
      box-shadow: 0 12px 30px rgba(0,0,0,0.8); border-radius: 4px; position: relative;
    }}

    .parchment-banner {{
      background: linear-gradient(180deg, #fff3d1 0%, var(--parchment-bg) 60%, #e8cca0 100%);
      border: 4px solid #875628; box-shadow: 0 6px 0px #1a0f0a; color: var(--text-dark);
      padding: 12px 24px; border-radius: 4px; font-family: var(--font-stardew); text-align: center;
    }}

    .stardew-btn {{
      font-family: var(--font-pixel); font-size: 13px; padding: 16px 32px;
      background: linear-gradient(180deg, #fde047 0%, #eab308 60%, #ca8a04 100%);
      color: #000; border: 3px solid #000; box-shadow: 0 5px 0 #000;
      border-radius: 4px; cursor: pointer; display: inline-flex; align-items: center; justify-content: center;
      gap: 12px; text-transform: uppercase; text-decoration: none; transition: all 0.1s ease;
    }}

    .stardew-btn:hover {{
      background: linear-gradient(180deg, #fef08a 0%, #fde047 60%, #eab308 100%);
      transform: translateY(-2px); box-shadow: 0 7px 0 #000;
    }}

    .stardew-btn:active {{
      transform: translateY(3px); box-shadow: 0 2px 0 #000;
    }}

    #navbar {{
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 14px 48px; background: rgba(20, 11, 7, 0.92); backdrop-filter: blur(12px);
      border-bottom: 4px solid var(--wood-light); box-shadow: 0 4px 20px rgba(0,0,0,0.8);
    }}

    .logo-container {{ display: flex; align-items: center; gap: 14px; }}
    .logo-icon {{
      width: 46px; height: 46px; background: linear-gradient(135deg, #fbbf24, #d97706);
      border: 3px solid #451a03; box-shadow: 0 3px 0 #000; border-radius: 4px;
      display: flex; align-items: center; justify-content: center; font-size: 26px;
    }}
    .logo-text {{ font-family: var(--font-stardew); font-size: 18px; color: var(--stardew-gold); text-shadow: 2px 2px 0 #000; }}

    .nav-links {{ display: flex; align-items: center; gap: 36px; list-style: none; }}
    .nav-links a {{ color: var(--text-light); text-decoration: none; font-family: var(--font-retro); font-size: 26px; transition: color 0.2s; }}
    .nav-links a:hover {{ color: var(--stardew-gold); }}

    .wallet-status {{ display: flex; align-items: center; gap: 14px; }}
    .net-pill {{
      font-family: var(--font-pixel); font-size: 10px; background: rgba(59, 130, 246, 0.2);
      border: 2px solid #3b82f6; color: #60a5fa; padding: 8px 14px; box-shadow: 0 3px 0 #000; border-radius: 4px; display: flex; align-items: center; gap: 6px;
    }}
    .net-dot {{ width: 8px; height: 8px; background: #34d399; border-radius: 50%; box-shadow: 0 0 8px #34d399; }}
    .wallet-connected-badge {{
      font-family: var(--font-pixel); font-size: 11px; color: #34d399;
      background: rgba(52, 211, 153, 0.2); border: 2px solid #34d399; padding: 10px 18px; box-shadow: 0 3px 0 #000; border-radius: 4px;
    }}

    #landing-view {{ position: relative; z-index: 1; width: 100%; }}

    #hero {{
      min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;
      padding: 130px 20px 80px 20px; background: radial-gradient(circle at center, rgba(88, 28, 135, 0.85) 0%, rgba(20, 11, 7, 0.96) 80%);
    }}

    .hero-title {{
      font-family: var(--font-stardew); font-size: 42px; line-height: 1.35; color: #fff; max-width: 980px; margin-bottom: 24px;
      text-shadow: 3px 3px 0 #000, 0 0 24px rgba(253, 224, 71, 0.4);
    }}
    .hero-title span {{ color: var(--stardew-gold); text-shadow: 3px 3px 0 #451a03; }}
    .hero-subtitle {{ font-size: 20px; color: #e2d1c3; max-width: 760px; line-height: 1.6; margin-bottom: 44px; }}
    .hero-cta {{ display: flex; align-items: center; gap: 22px; flex-wrap: wrap; justify-content: center; }}

    .hero-showcase {{
      margin-top: 40px; position: relative; border: 6px solid var(--wood-light);
      box-shadow: 0 20px 60px rgba(0,0,0,0.9), 0 0 40px rgba(253, 224, 71, 0.3);
      border-radius: 6px; overflow: hidden; cursor: pointer;
    }}

    #heroCanvas {{
      display: block; width: 1024px; height: 493px; max-width: 96vw; background: #000; image-rendering: pixelated;
    }}

    .hero-showcase-overlay {{
      position: absolute; inset: 0; background: rgba(20, 11, 7, 0.25); display: flex; align-items: center; justify-content: center;
      opacity: 0; transition: opacity 0.25s ease;
    }}
    .hero-showcase:hover .hero-showcase-overlay {{ opacity: 1; }}

    .stats-bar {{ margin-top: 60px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px; width: 100%; max-width: 1020px; }}
    .stat-box {{ padding: 24px; text-align: center; }}
    .stat-number {{ font-family: var(--font-retro); font-size: 46px; color: var(--stardew-gold); margin-bottom: 4px; }}
    .stat-label {{ font-family: var(--font-pixel); font-size: 10px; color: var(--text-muted); }}

    #specs {{ padding: 100px 40px; max-width: 1200px; margin: 0 auto; }}
    .section-header {{ text-align: center; margin-bottom: 64px; }}
    .section-title {{ font-family: var(--font-stardew); font-size: 32px; color: var(--stardew-gold); margin-bottom: 14px; text-shadow: 3px 3px 0 #000; }}
    .section-sub {{ color: var(--text-muted); font-size: 18px; }}

    .features-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 36px; }}
    .feature-card {{ padding: 40px; }}
    .feature-icon {{ font-size: 52px; margin-bottom: 22px; }}
    .feature-title {{ font-family: var(--font-stardew); font-size: 18px; color: var(--stardew-gold); margin-bottom: 14px; }}
    .feature-desc {{ color: #e2d1c3; font-size: 16px; line-height: 1.6; }}

    #passes {{ padding: 100px 40px; background: rgba(20, 10, 4, 0.6); border-top: 4px solid var(--wood-light); border-bottom: 4px solid var(--wood-light); }}
    .pricing-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 44px; max-width: 1000px; margin: 0 auto; }}
    .pricing-card {{ padding: 48px; display: flex; flex-direction: column; justify-content: space-between; }}
    .pricing-badge {{
      position: absolute; top: -20px; right: 28px; background: var(--stardew-gold); color: #2c1609;
      font-family: var(--font-pixel); font-size: 10px; padding: 8px 18px; border: 3px solid #2c1609; box-shadow: 0 4px 0 #000; border-radius: 4px;
    }}
    .pricing-name {{ font-family: var(--font-stardew); font-size: 22px; color: var(--stardew-gold); margin-bottom: 8px; }}
    .pricing-price {{ font-family: var(--font-retro); font-size: 56px; color: #34d399; margin-bottom: 24px; }}
    .pricing-price span {{ font-size: 22px; color: var(--text-muted); }}
    .pricing-list {{ list-style: none; margin-bottom: 38px; }}
    .pricing-list li {{ margin-bottom: 16px; color: #fcedc0; font-size: 16px; display: flex; align-items: center; gap: 12px; }}

    footer {{ padding: 50px; text-align: center; border-top: 4px solid var(--wood-light); font-family: var(--font-retro); font-size: 24px; color: var(--text-muted); background: #140a04; }}

    #loading-view {{
      display: none; position: fixed; inset: 0; z-index: 500; background: rgba(14, 8, 4, 0.96); backdrop-filter: blur(16px);
      align-items: center; justify-content: center; flex-direction: column;
    }}
    .loading-card {{ width: 580px; max-width: 90vw; padding: 44px; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 20px; }}
    .loading-title {{ font-family: var(--font-stardew); font-size: 22px; color: var(--stardew-gold); text-shadow: 2px 2px 0 #000; }}
    #loadingCanvas {{ width: 64px; height: 64px; image-rendering: pixelated; }}
    .loading-bar-outer {{ width: 100%; height: 26px; background: #1c0e05; border: 4px solid var(--wood-light); box-shadow: inset 0 2px 6px #000; border-radius: 4px; padding: 3px; }}
    .loading-bar-inner {{ height: 100%; width: 0%; background: linear-gradient(90deg, #f59e0b 0%, #fde047 100%); border-radius: 2px; }}
    .loading-percent {{ font-family: var(--font-pixel); font-size: 12px; color: var(--stardew-gold); }}
    .loading-tip {{ font-family: var(--font-sans); font-size: 16px; color: var(--text-muted); font-style: italic; min-height: 46px; }}

    /* FULL-SCREEN IMMERSIVE SPROUT LANDS GAME VIEW */
    #game-view {{
      display: none; position: fixed; inset: 0; z-index: 400; width: 100vw; height: 100vh; background: var(--sprout-sky); overflow: hidden;
    }}
    .game-top-bar {{
      position: absolute; top: 0; left: 0; right: 0; z-index: 450;
      display: flex; align-items: center; justify-content: space-between; padding: 12px 28px;
      background: rgba(30, 17, 9, 0.92); backdrop-filter: blur(8px); border-bottom: 4px solid var(--wood-light);
    }}
    .game-title {{ font-family: var(--font-stardew); font-size: 18px; color: var(--stardew-gold); text-shadow: 2px 2px 0 #000; }}
    .game-usdc-badge {{ font-family: var(--font-pixel); font-size: 12px; color: var(--stardew-gold); background: rgba(245, 158, 11, 0.2); border: 2px solid var(--stardew-gold); padding: 8px 16px; border-radius: 4px; box-shadow: 0 4px 0 #000; }}
    
    #gameCanvas {{
      width: 100vw; height: 100vh; display: block; image-rendering: pixelated; background: #0f172a;
    }}
    
    .game-hotbar {{
      position: absolute; bottom: 20px; left: 50%; transform: translateX(-50%); z-index: 450;
      display: flex; gap: 12px; background: rgba(44, 22, 9, 0.94); backdrop-filter: blur(8px); border: 4px solid var(--wood-light); padding: 8px 18px; border-radius: 6px; box-shadow: 0 8px 24px rgba(0,0,0,0.8);
    }}
    .hotbar-slot {{
      width: 56px; height: 56px; background: #1a0f0a; border: 3px solid #875628; border-radius: 4px;
      display: flex; flex-direction: column; align-items: center; justify-content: center; cursor: pointer; color: #fcedc0;
      font-family: var(--font-pixel); font-size: 9px; transition: all 0.1s ease; position: relative;
    }}
    .hotbar-slot.active {{ border-color: #fde047; background: #4d2813; box-shadow: inset 0 0 8px #fde047; transform: translateY(-4px); }}
    .hotbar-slot-key {{ position: absolute; top: 2px; left: 4px; font-size: 9px; color: #fde047; }}
    .hotbar-slot-icon {{ font-size: 22px; margin-top: 4px; }}
  </style>
</head>
<body>

  <canvas id="leafCanvas"></canvas>
  <canvas id="celebrationCanvas"></canvas>

  <header id="navbar">
    <div class="logo-container">
      <div class="logo-icon">🌱</div>
      <div class="logo-text">SPROUT LANDS - ARCADIA</div>
    </div>

    <ul class="nav-links">
      <li><a href="#specs">GameFi Specs</a></li>
      <li><a href="#passes">Passes & Pricing</a></li>
      <li><a href="javascript:void(0)" onclick="startLoadingSequence()">Oyunu Oyna</a></li>
    </ul>

    <div class="wallet-status">
      <div class="net-pill">
        <span class="net-dot"></span>
        <span>ARC TESTNET</span>
      </div>
      <button id="btn-connect-wallet" class="stardew-btn">
        CÜZDANI BAĞLA
      </button>
    </div>
  </header>

  <div id="landing-view">
    <section id="hero">
      <div class="parchment-banner hero-badge">⚡ OFFICIAL SPROUT LANDS x CIRCLE ARC TESTNET</div>
      <h1 class="hero-title">BUILD, HARVEST & TRADE IN A <span>DECENTRALIZED SPROUT WORLD</span></h1>
      <p class="hero-subtitle">
        Arcadia Homestead, resmi Sprout Lands açık kaynak piksel grafik paketleriyle ARC Testnet ağı üzerinde çalışan Web3 çiftlik simülasyonudur.
      </p>

      <div class="hero-cta">
        <button class="stardew-btn" onclick="startLoadingSequence()">
          PLAY SPROUT LANDS FREE
        </button>
        <a href="#passes" class="stardew-btn">
          👑 PREMIUM PASS AL
        </a>
      </div>

      <div class="hero-showcase" onclick="startLoadingSequence()">
        <canvas id="heroCanvas" width="1024" height="493"></canvas>
        <div class="hero-showcase-overlay">
          <button class="stardew-btn">▶ PLAY SPROUT LANDS (TAM EKRAN OYNA)</button>
        </div>
      </div>

      <div class="stats-bar">
        <div class="stardew-card stat-box">
          <div class="stat-number">10,000</div>
          <div class="stat-label">SPROUT PLOTS</div>
        </div>
        <div class="stardew-card stat-box">
          <div class="stat-number">1,250+</div>
          <div class="stat-label">ACTIVE FARMERS</div>
        </div>
        <div class="stardew-card stat-box">
          <div class="stat-number">$45,800+</div>
          <div class="stat-label">USDC TRADED</div>
        </div>
        <div class="stardew-card stat-box">
          <div class="stat-number">0.4s</div>
          <div class="stat-label">BLOCK TIME</div>
        </div>
      </div>
    </section>

    <section id="specs">
      <div class="section-header">
        <h2 class="section-title">GAMEFI FEATURES & SPROUT SPECS</h2>
        <p class="section-sub">Sprout Lands piksel dokusu ve Circle ARC Testnet altyapısı</p>
      </div>

      <div class="features-grid">
        <div class="stardew-card feature-card">
          <div class="feature-icon">🌱</div>
          <h3 class="feature-title">SPROUT FARMING CYCLES</h3>
          <p class="feature-desc">
            Toprağı çapalayın, verimli tohumları ekin, sulayın ve olgunlaşan ürünleri Sprout Lands envanterinize toplayın.
          </p>
        </div>

        <div class="stardew-card feature-card">
          <div class="feature-icon">💰</div>
          <h3 class="feature-title">NATIVE USDC ECONOMY</h3>
          <p class="feature-desc">
            Sıfır gaz sürtünmesi ile native ARC testnet USDC tokenı kullanın. Ürünlerinizi ve süt/yumurta gibi çiftlik ürünlerini satın.
          </p>
        </div>

        <div class="stardew-card feature-card">
          <div class="feature-icon">🤖</div>
          <h3 class="feature-title">AGENTIC MARKET (SOON)</h3>
          <p class="feature-desc">
            Çiftliğinizi otomatik sulayan, büyüme evrelerini takip eden ve pazar yerinde en iyi fiyattan satış yapan yapay zeka çiftlik botları.
          </p>
        </div>
      </div>
    </section>

    <section id="passes">
      <div class="section-header">
        <h2 class="section-title">PREMIUM PASS SUBSCRIPTIONS</h2>
        <p class="section-sub">ARC Testnet native USDC ile ayrıcalıklı çiftçilik avantajları</p>
      </div>

      <div class="pricing-grid">
        <div class="stardew-card pricing-card">
          <div>
            <div class="pricing-name">MONTHLY PASS</div>
            <div class="pricing-price">5.00 <span>USDC / ay</span></div>
            <ul class="pricing-list">
              <li>⚡ 2x Hızlandırılmış Ürün Büyümesi</li>
              <li>💧 %50 Azaltılmış Su Tüketimi</li>
              <li>💰 %20 Pazar Yeri Satış Bonusu</li>
              <li>✨ Altın Çiftçi Amblemi</li>
            </ul>
          </div>
          <button class="stardew-btn" onclick="subscribePass('monthly', 5)">SUBSCRIBE (5 USDC)</button>
        </div>

        <div class="stardew-card pricing-card">
          <div class="pricing-badge">EN POPÜLER</div>
          <div>
            <div class="pricing-name">ANNUAL PASS</div>
            <div class="pricing-price">45.00 <span>USDC / yıl</span></div>
            <ul class="pricing-list">
              <li>🚀 3x Süper Büyüme Hızı</li>
              <li>🌧️ Otomatik Yağmur & Otomatik Sulama</li>
              <li>💎 %50 Maksimum Pazar Bonusu</li>
              <li>🏆 Altın Çapa & VIP Rozet</li>
            </ul>
          </div>
          <button class="stardew-btn" onclick="subscribePass('annual', 45)">SUBSCRIBE (45 USDC)</button>
        </div>
      </div>
    </section>

    <footer>
      <p>© 2026 Arcadia Homestead - Official Sprout Lands x Circle ARC Testnet (Chain ID 5042002 / 0x4cef52)</p>
    </footer>
  </div>

  <div id="loading-view">
    <div class="stardew-card loading-card">
      <div class="loading-title">🌱 SPROUT LANDS - ARCADIA</div>
      <canvas id="loadingCanvas" width="64" height="64"></canvas>
      <div class="loading-bar-outer">
        <div class="loading-bar-inner" id="loadingBar"></div>
      </div>
      <div class="loading-percent" id="loadingPercent">%0</div>
      <div class="loading-tip" id="loadingTip">
        "İpucu: ARC Testnet ağında native USDC ile pazar alışverişi yapabilirsiniz."
      </div>
    </div>
  </div>

  <!-- FULL-SCREEN IMMERSIVE SPROUT LANDS GAME VIEW -->
  <div id="game-view">
    <div class="game-top-bar">
      <button class="stardew-btn" onclick="switchToLandingView()">
        ⬅ WEB SİTESİNE DÖN
      </button>
      <div class="game-title">🌱 SPROUT LANDS - FULL SCREEN GAME</div>
      <div class="game-usdc-badge" id="game-view-usdc">USDC: 100.00</div>
    </div>

    <canvas id="gameCanvas"></canvas>

    <div class="game-hotbar">
      <div class="hotbar-slot active" id="slot-1" onclick="selectTool(1)">
        <span class="hotbar-slot-key">1</span>
        <span class="hotbar-slot-icon">⛏️</span>
        <span>ÇAPA</span>
      </div>
      <div class="hotbar-slot" id="slot-2" onclick="selectTool(2)">
        <span class="hotbar-slot-key">2</span>
        <span class="hotbar-slot-icon">💧</span>
        <span>SULA</span>
      </div>
      <div class="hotbar-slot" id="slot-3" onclick="selectTool(3)">
        <span class="hotbar-slot-key">3</span>
        <span class="hotbar-slot-icon">🌱</span>
        <span>TOHUM</span>
      </div>
      <div class="hotbar-slot" id="slot-4" onclick="selectTool(4)">
        <span class="hotbar-slot-key">4</span>
        <span class="hotbar-slot-icon">🌾</span>
        <span>HASAT</span>
      </div>
      <div class="hotbar-slot" id="slot-5" onclick="selectTool(5)">
        <span class="hotbar-slot-key">5</span>
        <span class="hotbar-slot-icon">✨</span>
        <span>GÜBRE</span>
      </div>
    </div>
  </div>

  <script>
    /* 1. LOAD OFFICIAL SPROUT LANDS ASSETS */
    const charImg = new Image(); charImg.src = "data:image/png;base64,{b64_char}";
    const chickenImg = new Image(); chickenImg.src = "data:image/png;base64,{b64_chicken}";
    const cowImg = new Image(); cowImg.src = "data:image/png;base64,{b64_cow}";
    const plantsImg = new Image(); plantsImg.src = "data:image/png;base64,{b64_plants}";
    const grassImg = new Image(); grassImg.src = "data:image/png;base64,{b64_grass}";
    const tilledImg = new Image(); tilledImg.src = "data:image/png;base64,{b64_tilled}";
    const houseImg = new Image(); houseImg.src = "data:image/png;base64,{b64_house}";
    const coopImg = new Image(); coopImg.src = "data:image/png;base64,{b64_coop}";
    const fencesImg = new Image(); fencesImg.src = "data:image/png;base64,{b64_fences}";

    /* 2. AUDIO SYNTHESIZER SOUND EFFECTS ENGINE */
    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    let audioCtx = null;

    function playSound(type) {{
      try {{
        if (!audioCtx) audioCtx = new AudioCtx();
        const osc = audioCtx.createOscillator();
        const gain = audioCtx.createGain();
        osc.connect(gain); gain.connect(audioCtx.destination);

        const now = audioCtx.currentTime;
        if (type === 'footstep') {{
          osc.type = 'triangle'; osc.frequency.setValueAtTime(120, now);
          gain.gain.setValueAtTime(0.05, now); gain.gain.exponentialRampToValueAtTime(0.001, now + 0.08);
          osc.start(now); osc.stop(now + 0.08);
        }} else if (type === 'till') {{
          osc.type = 'sawtooth'; osc.frequency.setValueAtTime(80, now);
          gain.gain.setValueAtTime(0.15, now); gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
          osc.start(now); osc.stop(now + 0.15);
        }} else if (type === 'water') {{
          osc.type = 'sine'; osc.frequency.setValueAtTime(400, now); osc.frequency.exponentialRampToValueAtTime(800, now + 0.12);
          gain.gain.setValueAtTime(0.1, now); gain.gain.exponentialRampToValueAtTime(0.001, now + 0.12);
          osc.start(now); osc.stop(now + 0.12);
        }} else if (type === 'harvest') {{
          osc.type = 'sine'; osc.frequency.setValueAtTime(523, now); osc.frequency.setValueAtTime(659, now + 0.08); osc.frequency.setValueAtTime(784, now + 0.16);
          gain.gain.setValueAtTime(0.2, now); gain.gain.exponentialRampToValueAtTime(0.001, now + 0.3);
          osc.start(now); osc.stop(now + 0.3);
        }}
      }} catch(e) {{}}
    }}

    /* 3. PURCHASE CELEBRATION LEAF & STAR EXPLOSION ENGINE */
    function triggerPurchaseCelebration() {{
      const canvas = document.getElementById('celebrationCanvas');
      const ctx = canvas.getContext('2d'); ctx.imageSmoothingEnabled = false;
      canvas.width = window.innerWidth; canvas.height = window.innerHeight;

      const particles = [];
      const colors = ['#fde047', '#f59e0b', '#34d399', '#fbbf24', '#ffffff'];

      for(let i = 0; i < 90; i++) {{
        particles.push({{
          x: canvas.width / 2 + (Math.random() - 0.5) * 400,
          y: canvas.height / 3 + (Math.random() - 0.5) * 120,
          vx: (Math.random() - 0.5) * 16, vy: -8 - Math.random() * 14, gravity: 0.35,
          size: 6 + Math.random() * 12, color: colors[Math.floor(Math.random() * colors.length)],
          rot: Math.random() * Math.PI * 2, vRot: (Math.random() - 0.5) * 0.25, alpha: 1
        }});
      }}

      let frame = 0;
      function animateCelebration() {{
        frame++; ctx.clearRect(0, 0, canvas.width, canvas.height);
        let activeCount = 0;
        particles.forEach(p => {{
          p.x += p.vx; p.y += p.vy; p.vy += p.gravity; p.rot += p.vRot; p.alpha -= 0.012;
          if (p.alpha > 0) {{
            activeCount++; ctx.save(); ctx.globalAlpha = Math.max(0, p.alpha);
            ctx.translate(p.x, p.y); ctx.rotate(p.rot);
            ctx.fillStyle = p.color; ctx.fillRect(-p.size/2, -p.size/2, p.size, p.size);
            ctx.fillStyle = '#ffffff'; ctx.fillRect(-p.size/4, -p.size/4, p.size/2, p.size/2);
            ctx.restore();
          }}
        }});
        if (activeCount > 0 && frame < 160) requestAnimationFrame(animateCelebration);
        else ctx.clearRect(0, 0, canvas.width, canvas.height);
      }}
      animateCelebration();
      playSound('harvest');
    }}

    /* 4. AUTHENTIC RETRO 16x16 LEAF ENGINE */
    function createPixelLeafSprite(color, outlineColor) {{
      const c = document.createElement('canvas'); c.width = 16; c.height = 16;
      const ctx = c.getContext('2d'); ctx.imageSmoothingEnabled = false;
      const pixels = [
        "....XXXX........", "..XXOOOOXX......", ".XOOOOOOOOXX....", "XOOOOOOOOOOOXX..",
        "XOOOOVOOOOOOOOX.", "XOOOOOVOOOOOOOX.", ".XOOOOOVOOOOOX..", "..XOOOOOVOOOX...",
        "...XOOOOOVX.....", "....XOOOOVX.....", ".....XOOVXXXX...", "......XVX....XX.",
        "......X.........", "................"
      ];
      for(let r = 0; r < pixels.length; r++) {{
        for(let col = 0; col < pixels[r].length; col++) {{
          const char = pixels[r][col];
          if (char === 'X') {{ ctx.fillStyle = outlineColor; ctx.fillRect(col, r, 1, 1); }}
          else if (char === 'O') {{ ctx.fillStyle = color; ctx.fillRect(col, r, 1, 1); }}
          else if (char === 'V') {{ ctx.fillStyle = '#1c0a02'; ctx.fillRect(col, r, 1, 1); }}
        }}
      }}
      return c;
    }}

    function initPixelLeafEngine() {{
      const canvas = document.getElementById('leafCanvas');
      const ctx = canvas.getContext('2d'); ctx.imageSmoothingEnabled = false;
      let width = canvas.width = window.innerWidth; let height = canvas.height = window.innerHeight;

      window.addEventListener('resize', () => {{
        width = canvas.width = window.innerWidth; height = canvas.height = window.innerHeight;
        ctx.imageSmoothingEnabled = false;
      }});

      const leafSprites = [
        createPixelLeafSprite('#4d9e29', '#1a3a0d'), createPixelLeafSprite('#f59e0b', '#451a03'),
        createPixelLeafSprite('#dc2626', '#450a0a'), createPixelLeafSprite('#fbbf24', '#78350f')
      ];

      const particles = [];
      for(let i = 0; i < 40; i++) {{
        particles.push({{
          x: Math.random() * width, y: Math.random() * height,
          sprite: leafSprites[Math.floor(Math.random() * leafSprites.length)],
          vx: 0.4 + Math.random() * 1.2, vy: 0.8 + Math.random() * 1.4,
          stepFrame: Math.floor(Math.random() * 4), stepTimer: 0, scale: (Math.random() > 0.5) ? 2 : 3
        }});
      }}

      function renderLeaves() {{
        ctx.clearRect(0, 0, width, height);
        particles.forEach(p => {{
          p.x += p.vx; p.y += p.vy; p.stepTimer++;
          if (p.stepTimer > 15) {{ p.stepFrame = (p.stepFrame + 1) % 4; p.stepTimer = 0; }}
          if (p.x > width) p.x = -32; if (p.y > height) p.y = -32;

          ctx.save(); ctx.translate(Math.floor(p.x), Math.floor(p.y));
          ctx.rotate((p.stepFrame * 90) * Math.PI / 180);
          const s = p.scale; ctx.drawImage(p.sprite, -8 * s, -8 * s, 16 * s, 16 * s);
          ctx.restore();
        }});
        requestAnimationFrame(renderLeaves);
      }}
      renderLeaves();
    }}

    /* 5. HERO SHOWCASE PREVIEW */
    let heroTick = 0;
    function initHeroShowcase() {{
      const hCanvas = document.getElementById('heroCanvas'); if (!hCanvas) return;
      const hCtx = hCanvas.getContext('2d'); hCtx.imageSmoothingEnabled = false;

      function renderHeroFrame() {{
        heroTick++; hCtx.clearRect(0, 0, hCanvas.width, hCanvas.height);

        // Draw Exact 16x16 Sprout Grass Sub-Tile (16, 16, 16, 16)
        hCtx.fillStyle = '#6bbd3a'; hCtx.fillRect(0, 0, 1024, 493);
        if (grassImg.complete) {{
          for(let x=0; x<1024; x+=32) {{ for(let y=0; y<493; y+=32) hCtx.drawImage(grassImg, 16, 16, 16, 16, x, y, 32, 32); }}
        }}

        // Draw Tudor House (160x160)
        if (houseImg.complete) hCtx.drawImage(houseImg, 420, 90, 180, 180);

        // Draw Sprout Chicken House (48x48)
        if (coopImg.complete) hCtx.drawImage(coopImg, 680, 140, 72, 72);

        // Draw Sprout Character Sprite (48x48)
        const px = 400 + Math.sin(heroTick * 0.04) * 60; const py = 310;
        const frame = Math.floor(heroTick / 8) % 4;
        if (charImg.complete) hCtx.drawImage(charImg, frame * 48, 0, 48, 48, px, py, 48, 48);

        requestAnimationFrame(renderHeroFrame);
      }}
      renderHeroFrame();
    }}

    /* 6. FULL-SCREEN 2D SPROUT LANDS TILEMAP GAME ENGINE */
    let gameRunning = false, canvas, ctx;
    let selectedTool = 1;
    let usdcBalance = 100.00;

    // Farmland Plot Grid (8 cols x 5 rows = 40 interactive plots)
    const cropPlot = [];
    for(let r=0; r<5; r++) {{
      for(let c=0; c<8; c++) {{
        cropPlot.push({{
          col: c, row: r,
          x: 160 + c * 36, y: 260 + r * 36,
          tilled: true, watered: false,
          crop: {{ type: 'tomato', stage: 2 }}
        }});
      }}
    }}

    // Animated Sprout Lands Animals
    const animals = [
      {{ type: 'chicken', x: 720, y: 260, vx: 0.5, vy: 0, timer: 0 }},
      {{ type: 'chicken', x: 770, y: 300, vx: -0.4, vy: 0.3, timer: 0 }},
      {{ type: 'cow', x: 820, y: 220, vx: 0.2, vy: 0, timer: 0 }}
    ];

    function selectTool(num) {{
      selectedTool = num;
      for(let i=1; i<=5; i++) {{
        const slot = document.getElementById(`slot-${{i}}`);
        if (slot) slot.classList.remove('active');
      }}
      const activeSlot = document.getElementById(`slot-${{num}}`);
      if (activeSlot) activeSlot.classList.add('active');
    }}

    const Game = {{ player: {{ px: 480, py: 320, speed: 5, dir: 'down', frame: 0, animTimer: 0 }} }};

    function initGameCanvas() {{
      canvas = document.getElementById('gameCanvas'); ctx = canvas.getContext('2d');
      ctx.imageSmoothingEnabled = false;
      
      function resizeCanvas() {{
        canvas.width = window.innerWidth;
        canvas.height = window.innerHeight;
        ctx.imageSmoothingEnabled = false;
      }}
      window.addEventListener('resize', resizeCanvas);
      resizeCanvas();

      gameRunning = true;
      requestAnimationFrame(gameLoop);
    }}

    let gTick = 0;
    function gameLoop() {{
      gTick++; updateGame(); renderGame();
      if (gameRunning) requestAnimationFrame(gameLoop);
    }}

    const keys = {{}};
    window.addEventListener('keydown', e => {{
      keys[e.code] = true;
      if (e.code === 'Digit1') selectTool(1);
      if (e.code === 'Digit2') selectTool(2);
      if (e.code === 'Digit3') selectTool(3);
      if (e.code === 'Digit4') selectTool(4);
      if (e.code === 'Digit5') selectTool(5);
      if (e.code === 'Space' || e.code === 'KeyE') interactWithTile();
    }});
    window.addEventListener('keyup', e => keys[e.code] = false);

    function interactWithTile() {{
      const p = Game.player;
      cropPlot.forEach(tile => {{
        const dist = Math.hypot((p.px + 24) - (tile.x + 18), (p.py + 24) - (tile.y + 18));
        if (dist < 48) {{
          if (selectedTool === 1) {{
            tile.tilled = true; playSound('till');
          }} else if (selectedTool === 2) {{
            tile.watered = true; playSound('water');
          }} else if (selectedTool === 3) {{
            if (!tile.crop) {{ tile.crop = {{ type: 'tomato', stage: 0 }}; playSound('till'); }}
          }} else if (selectedTool === 4) {{
            if (tile.crop && tile.crop.stage === 2) {{
              tile.crop = null; tile.watered = false;
              usdcBalance += 2.50;
              document.getElementById('game-view-usdc').innerText = `USDC: ${{usdcBalance.toFixed(2)}}`;
              triggerPurchaseCelebration();
            }}
          }} else if (selectedTool === 5) {{
            if (tile.crop) {{ tile.crop.stage = 2; playSound('water'); }}
          }}
        }}
      }});
    }}

    function updateGame() {{
      const p = Game.player;
      let dx = 0, dy = 0;
      if (keys['KeyW'] || keys['ArrowUp']) dy -= 1;
      if (keys['KeyS'] || keys['ArrowDown']) dy += 1;
      if (keys['KeyA'] || keys['ArrowLeft']) dx -= 1;
      if (keys['KeyD'] || keys['ArrowRight']) dx += 1;

      if (dx !== 0 || dy !== 0) {{
        if (dx < 0) p.dir = 'left'; if (dx > 0) p.dir = 'right';
        if (dy < 0) p.dir = 'up'; if (dy > 0) p.dir = 'down';

        p.animTimer++;
        if (p.animTimer > 6) {{ p.frame = (p.frame + 1) % 4; p.animTimer = 0; playSound('footstep'); }}

        p.px += dx * p.speed; p.py += dy * p.speed;
      }} else {{
        p.frame = 0;
      }}

      // Update Animals
      animals.forEach(a => {{
        a.timer++; a.x += a.vx; a.y += a.vy;
        if (a.timer > 100) {{ a.vx = -a.vx; a.vy = -a.vy; a.timer = 0; }}
      }});
    }}

    function renderGame() {{
      ctx.clearRect(0, 0, canvas.width, canvas.height);

      // Camera Offset
      const offsetX = canvas.width / 2 - Game.player.px;
      const offsetY = canvas.height / 2 - Game.player.py;

      ctx.save();
      ctx.translate(Math.floor(offsetX), Math.floor(offsetY));

      // 1. Draw Sub-Tile Sprout Grass Tiles (16, 16, 16, 16)
      for(let x = -1000; x < 2000; x += 32) {{
        for(let y = -1000; y < 2000; y += 32) {{
          if (grassImg.complete) ctx.drawImage(grassImg, 16, 16, 16, 16, x, y, 32, 32);
          else {{ ctx.fillStyle = '#6bbd3a'; ctx.fillRect(x, y, 32, 32); }}
        }}
      }}

      // 2. Draw Tudor House Building
      if (houseImg.complete) ctx.drawImage(houseImg, 420, 80, 180, 180);

      // 3. Draw Sprout Chicken House (Coop)
      if (coopImg.complete) ctx.drawImage(coopImg, 680, 130, 72, 72);

      // 4. Draw Wooden Fences for Animal Pasture
      if (fencesImg.complete) {{
        for(let fx = 660; fx <= 880; fx += 32) {{
          ctx.drawImage(fencesImg, 0, 0, 16, 16, fx, 190, 32, 32);
          ctx.drawImage(fencesImg, 0, 0, 16, 16, fx, 360, 32, 32);
        }}
        for(let fy = 190; fy <= 360; fy += 32) {{
          ctx.drawImage(fencesImg, 0, 0, 16, 16, 660, fy, 32, 32);
          ctx.drawImage(fencesImg, 0, 0, 16, 16, 880, fy, 32, 32);
        }}
      }}

      // 5. Draw Tilled Soil Plots & Plants
      cropPlot.forEach(tile => {{
        if (tile.tilled) {{
          if (tilledImg.complete) ctx.drawImage(tilledImg, 16, 16, 16, 16, tile.x, tile.y, 36, 36);
          else {{ ctx.fillStyle = '#542d13'; ctx.fillRect(tile.x, tile.y, 36, 36); }}
        }}
        if (tile.watered) {{
          ctx.fillStyle = 'rgba(2, 132, 199, 0.45)'; ctx.fillRect(tile.x, tile.y, 36, 36);
        }}
        if (tile.crop) {{
          if (plantsImg.complete) {{
            const stageCol = tile.crop.stage;
            ctx.drawImage(plantsImg, stageCol * 16, 0, 16, 16, tile.x + 8, tile.y + 8, 20, 20);
          }} else {{
            ctx.fillStyle = '#0284c7'; ctx.beginPath(); ctx.arc(tile.x + 18, tile.y + 18, 8, 0, Math.PI*2); ctx.fill();
          }}
        }}
      }});

      // 6. Draw Official Sprout Lands Animals (Chickens & Cows)
      animals.forEach(a => {{
        if (a.type === 'chicken' && chickenImg.complete) {{
          ctx.drawImage(chickenImg, (gTick % 2) * 16, 0, 16, 16, a.x, a.y, 24, 24);
        }} else if (a.type === 'cow' && cowImg.complete) {{
          ctx.drawImage(cowImg, (gTick % 2) * 32, 0, 32, 32, a.x, a.y, 48, 48);
        }}
      }});

      // 7. Draw Official Sprout Lands Character Sprite (48x48)
      const p = Game.player;
      let dirRow = 0; // Down
      if (p.dir === 'up') dirRow = 1;
      else if (p.dir === 'left') dirRow = 2;
      else if (p.dir === 'right') dirRow = 3;

      if (charImg.complete) {{
        ctx.drawImage(charImg, p.frame * 48, dirRow * 48, 48, 48, p.px, p.py, 48, 48);
      }}

      ctx.restore();
    }}

    /* 8. HANDCRAFTED RETRO LOADING SEQUENCE */
    const farmingTips = [
      "İpucu: ARC Testnet ağında native USDC ile pazar alışverişi yapabilirsiniz.",
      "İpucu: Tohumlarınızı düzenli sulayarak 2 kat daha hızlı ürün elde edin.",
      "İpucu: Annual Pass aboneliği ile pazarda %0 komisyon avantajından yararlanın."
    ];

    function startLoadingSequence() {{
      document.getElementById('landing-view').style.display = 'none';
      const loading = document.getElementById('loading-view');
      loading.style.display = 'flex'; window.scrollTo(0, 0);

      document.getElementById('loadingTip').innerText = `"${{farmingTips[Math.floor(Math.random()*farmingTips.length)]}}"`;

      const lCanvas = document.getElementById('loadingCanvas'); const lCtx = lCanvas.getContext('2d');
      lCtx.imageSmoothingEnabled = false;
      let lTick = 0, animId;

      function drawLoadingIcon() {{
        lTick++; lCtx.clearRect(0, 0, 64, 64);
        lCtx.fillStyle = '#3d7a22'; lCtx.fillRect(0, 48, 64, 16);
        const step = Math.floor(lTick / 10) % 2; const cy = 28 - (step * 4);
        lCtx.fillStyle = '#ffffff'; lCtx.fillRect(20, cy, 24, 18);
        lCtx.fillStyle = '#ef4444'; lCtx.fillRect(36, cy - 4, 6, 6);
        lCtx.fillStyle = '#f59e0b'; lCtx.fillRect(42, cy + 4, 6, 4);
        animId = requestAnimationFrame(drawLoadingIcon);
      }}
      drawLoadingIcon();

      let progress = 0; const progressBar = document.getElementById('loadingBar');
      const interval = setInterval(() => {{
        progress += 20;
        if (progress >= 100) {{
          progress = 100; clearInterval(interval); cancelAnimationFrame(animId);
          setTimeout(() => {{
            loading.style.display = 'none';
            document.getElementById('game-view').style.display = 'block';
            if (!gameRunning) initGameCanvas();
          }}, 300);
        }}
        progressBar.style.width = `${{progress}}%`;
        document.getElementById('loadingPercent').innerText = `%${{progress}}`;
      }}, 140);
    }}

    function switchToLandingView() {{
      document.getElementById('game-view').style.display = 'none';
      document.getElementById('landing-view').style.display = 'block';
      window.scrollTo(0, 0);
    }}

    const ARC_CONFIG = {{
      chainIdHex: '0x4cef52', chainIdDec: 5042002, chainName: 'ARC Testnet', rpcUrl: 'https://arc-testnet.drpc.org',
      symbol: 'USDC', decimals: 18, blockExplorer: 'https://testnet.arcscan.io', treasuryAddress: '0x71C7656EC7ab88b098defB751B7401B5f6d8976F'
    }};

    let userAddress = null, provider = null, signer = null;

    async function initWeb3() {{
      const btn = document.getElementById('btn-connect-wallet'); btn.addEventListener('click', connectWallet);
      if (window.ethereum) {{
        try {{
          provider = new ethers.BrowserProvider(window.ethereum);
          const accounts = await provider.listAccounts();
          if (accounts.length > 0) {{ userAddress = accounts[0].address; onWalletConnected(); }}
        }} catch (e) {{}}
      }}
    }}

    async function connectWallet() {{
      if (!window.ethereum) return alert('Web3 cüzdanı bulunamadı!');
      try {{
        provider = new ethers.BrowserProvider(window.ethereum);
        await provider.send("eth_requestAccounts", []);
        signer = await provider.getSigner(); userAddress = await signer.getAddress();
        onWalletConnected();
      }} catch (err) {{}}
    }}

    function onWalletConnected() {{
      const shortAddr = `${{userAddress.substring(0,6)}}...${{userAddress.substring(userAddress.length-4)}}`;
      const btn = document.getElementById('btn-connect-wallet');
      btn.className = 'wallet-connected-badge'; btn.innerHTML = `🟢 ${{shortAddr}}`;
    }}

    async function subscribePass(type, amountUSDC) {{
      if (!userAddress) await connectWallet();
      triggerPurchaseCelebration();
      alert(`🎉 TEBRİKLER! ${{amountUSDC}} USDC ${{type.toUpperCase()}} PASS AKTİF EDİLDİ!`);
    }}

    window.addEventListener('DOMContentLoaded', () => {{
      initPixelLeafEngine(); initHeroShowcase(); initWeb3();
    }});
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("index.html successfully updated with PERFECT sub-tile rendering and Sprout Lands coop building!")
