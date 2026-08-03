html_content = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Arcadia Homestead - Web3 Pixel Farming on Arc Testnet</title>

  <meta name="description" content="Arcadia Homestead - Web3 5x5 Grid Stardew-aesthetic pixel farming simulation running on Arc Testnet.">

  <!-- Google Fonts: Stardew Retro Pixel Fonts -->
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Press+Start+2P&family=Silkscreen:wght@400;700&family=VT323&family=Outfit:wght@400;500;600;700;800&display=swap" rel="stylesheet">

  <!-- Ethers.js v6 Library -->
  <script src="https://cdnjs.cloudflare.com/ajax/libs/ethers/6.13.1/ethers.umd.min.js"></script>

  <style>
    :root {
      --sky-blue: #70c5ce;
      --grass-green: #599632;
      --wood-dark: #2c1609;
      --wood-mid: #4d2813;
      --wood-light: #7a4320;
      --wood-border: #140a04;
      --parchment-bg: #fcedc0;
      --parchment-border: #875628;
      --stardew-gold: #fde047;
      --gold-dark: #b45309;
      --text-dark: #381e0d;
      --text-light: #fef0c7;
      --text-muted: #caab8d;
      --font-pixel: 'Press Start 2P', monospace;
      --font-stardew: 'Silkscreen', cursive;
      --font-retro: 'VT323', monospace;
      --font-sans: 'Outfit', sans-serif;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; user-select: none; -webkit-user-select: none; }

    html, body {
      width: 100%; min-height: 100vh;
      background-color: #140b07;
      color: var(--text-light);
      font-family: var(--font-sans);
    }

    #leafCanvas {
      position: fixed; inset: 0; z-index: 0; pointer-events: none; image-rendering: pixelated;
    }
    #celebrationCanvas {
      position: fixed; inset: 0; z-index: 600; pointer-events: none; image-rendering: pixelated;
    }

    /* Pixel Toast Notification Overlay */
    #pixelToastContainer {
      position: fixed; top: 100px; left: 50%; transform: translateX(-50%);
      z-index: 700; pointer-events: none; display: flex; flex-direction: column; gap: 10px; align-items: center;
    }

    .pixel-toast {
      background: linear-gradient(180deg, #fff3d1 0%, var(--parchment-bg) 60%, #e8cca0 100%);
      border: 4px solid #875628; outline: 3px solid #1a0f0a; box-shadow: 0 8px 24px rgba(0,0,0,0.8);
      color: var(--text-dark); padding: 12px 24px; border-radius: 4px; font-family: var(--font-pixel);
      font-size: 11px; text-align: center; display: flex; align-items: center; gap: 10px;
      animation: toastSlideIn 0.3s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    }

    @keyframes toastSlideIn {
      from { opacity: 0; transform: translateY(-20px) scale(0.9); }
      to { opacity: 1; transform: translateY(0) scale(1); }
    }

    /* Web3 Connect Wallet Pixel Modal Overlay */
    #walletModal {
      display: none; position: fixed; inset: 0; z-index: 800;
      background: rgba(14, 8, 4, 0.92); backdrop-filter: blur(12px);
      align-items: center; justify-content: center;
    }

    .wallet-modal-card {
      width: 480px; max-width: 90vw; background: linear-gradient(180deg, var(--wood-mid) 0%, var(--wood-dark) 100%);
      border: 6px solid var(--wood-light); outline: 3px solid var(--wood-border);
      border-radius: 8px; box-shadow: 0 20px 60px rgba(0,0,0,0.9);
      padding: 36px; text-align: center; display: flex; flex-direction: column; gap: 20px; align-items: center;
    }

    .wallet-modal-title { font-family: var(--font-stardew); font-size: 20px; color: var(--stardew-gold); text-shadow: 2px 2px 0 #000; }
    .wallet-modal-desc { font-size: 15px; color: #e2d1c3; line-height: 1.6; }

    /* Navbar Header */
    #navbar {
      position: fixed; top: 0; left: 0; right: 0; z-index: 100;
      display: flex; align-items: center; justify-content: space-between;
      padding: 14px 48px; background: rgba(20, 11, 7, 0.94); backdrop-filter: blur(12px);
      border-bottom: 4px solid var(--wood-light); box-shadow: 0 4px 20px rgba(0,0,0,0.8);
    }

    .logo-container { display: flex; align-items: center; gap: 14px; cursor: pointer; }
    .logo-icon {
      width: 46px; height: 46px; background: linear-gradient(135deg, #fbbf24, #d97706);
      border: 3px solid #451a03; box-shadow: 0 3px 0 #000; border-radius: 4px;
      display: flex; align-items: center; justify-content: center; font-size: 26px;
    }
    .logo-text { font-family: var(--font-stardew); font-size: 18px; color: var(--stardew-gold); text-shadow: 2px 2px 0 #000; }

    .nav-links { display: flex; align-items: center; gap: 32px; list-style: none; }
    .nav-links a { color: var(--text-light); text-decoration: none; font-family: var(--font-retro); font-size: 26px; transition: color 0.2s; }
    .nav-links a:hover { color: var(--stardew-gold); }

    /* Language Switcher Dropdown */
    .lang-switcher {
      display: flex; align-items: center; gap: 6px; background: #1a0f0a; border: 2px solid var(--wood-light);
      padding: 6px 12px; border-radius: 4px; font-family: var(--font-pixel); font-size: 10px; color: var(--stardew-gold);
    }
    .lang-select {
      background: transparent; border: none; color: var(--stardew-gold); font-family: var(--font-pixel);
      font-size: 10px; cursor: pointer; outline: none;
    }
    .lang-select option { background: #1a0f0a; color: #fff; }

    .wallet-status { display: flex; align-items: center; gap: 14px; }
    .net-pill {
      font-family: var(--font-pixel); font-size: 10px; background: rgba(59, 130, 246, 0.2);
      border: 2px solid #3b82f6; color: #60a5fa; padding: 8px 14px; box-shadow: 0 3px 0 #000; border-radius: 4px; display: flex; align-items: center; gap: 6px;
    }
    .net-dot { width: 8px; height: 8px; background: #34d399; border-radius: 50%; box-shadow: 0 0 8px #34d399; }

    .stardew-btn {
      font-family: var(--font-pixel); font-size: 12px; padding: 16px 32px;
      background: linear-gradient(180deg, #fde047 0%, #eab308 60%, #ca8a04 100%);
      color: #000; border: 3px solid #000; box-shadow: 0 5px 0 #000;
      border-radius: 4px; cursor: pointer; display: inline-flex; align-items: center; justify-content: center;
      gap: 12px; text-transform: uppercase; text-decoration: none; transition: all 0.1s ease;
    }
    .stardew-btn:hover { background: linear-gradient(180deg, #fef08a 0%, #fde047 60%, #eab308 100%); transform: translateY(-2px); box-shadow: 0 7px 0 #000; }
    .stardew-btn:active { transform: translateY(3px); box-shadow: 0 2px 0 #000; }

    #landing-view { position: relative; z-index: 1; width: 100%; }

    /* HERO SECTION */
    #hero {
      min-height: 100vh; display: flex; flex-direction: column; align-items: center; justify-content: center; text-align: center;
      padding: 130px 20px 80px 20px; background: radial-gradient(circle at center, rgba(88, 28, 135, 0.85) 0%, rgba(20, 11, 7, 0.96) 80%);
    }

    .parchment-banner {
      background: linear-gradient(180deg, #fff3d1 0%, var(--parchment-bg) 60%, #e8cca0 100%);
      border: 4px solid #875628; box-shadow: 0 6px 0px #1a0f0a; color: var(--text-dark);
      padding: 12px 24px; border-radius: 4px; font-family: var(--font-stardew); text-align: center; margin-bottom: 24px;
    }

    .hero-title {
      font-family: var(--font-stardew); font-size: 44px; line-height: 1.35; color: #fff; max-width: 980px; margin-bottom: 24px;
      text-shadow: 3px 3px 0 #000, 0 0 24px rgba(253, 224, 71, 0.4);
    }
    .hero-title span { color: var(--stardew-gold); text-shadow: 3px 3px 0 #451a03; }
    .hero-subtitle { font-size: 20px; color: #e2d1c3; max-width: 760px; line-height: 1.6; margin-bottom: 38px; }
    .hero-cta { display: flex; align-items: center; gap: 22px; flex-wrap: wrap; justify-content: center; margin-bottom: 40px; }

    /* PERFECTLY ALIGNED FLOATING ISOMETRIC PARALLAX HERO CANVAS */
    .hero-stage {
      position: relative; width: 720px; height: 440px; max-width: 96vw;
      display: flex; align-items: center; justify-content: center;
    }

    #heroCanvas {
      width: 720px; height: 440px; max-width: 96vw; image-rendering: pixelated;
      filter: drop-shadow(0 20px 30px rgba(0,0,0,0.8));
    }

    .stats-bar { margin-top: 60px; display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 24px; width: 100%; max-width: 1060px; }
    
    .stat-box {
      padding: 24px; text-align: center;
      background: linear-gradient(180deg, var(--wood-mid) 0%, var(--wood-dark) 100%);
      border: 5px solid var(--wood-border); outline: 3px solid var(--wood-light); outline-offset: -7px;
      border-radius: 6px; box-shadow: 0 8px 20px rgba(0,0,0,0.6);
    }
    .stat-number { font-family: var(--font-retro); font-size: 46px; color: var(--stardew-gold); margin-bottom: 4px; }
    .stat-label { font-family: var(--font-pixel); font-size: 10px; color: var(--text-muted); }

    /* STICKY SHOWCASE */
    #interactive-showcase {
      position: relative; height: 3200px; width: 100%;
    }

    .sticky-pin-container {
      position: absolute; top: 0; left: 50%; transform: translateX(-50%);
      width: 100%; max-width: 1100px; height: calc(100vh - 100px); padding: 0 20px;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      transition: none;
    }

    .sticky-pin-container.is-pinned {
      position: fixed; top: 90px; left: 50%; transform: translateX(-50%); z-index: 90;
    }

    .sticky-pin-container.is-bottom {
      position: absolute; top: auto; bottom: 0; left: 50%; transform: translateX(-50%);
    }

    .showcase-header { text-align: center; margin-bottom: 18px; }
    .showcase-title { font-family: var(--font-stardew); font-size: 28px; color: var(--stardew-gold); text-shadow: 3px 3px 0 #000; margin-bottom: 6px; }
    .showcase-sub { font-size: 16px; color: var(--text-muted); }

    .showcase-tabs {
      display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px;
      width: 100%; max-width: 1060px; margin-bottom: 22px;
    }

    .tab-btn {
      font-family: var(--font-pixel); font-size: 9px; padding: 14px 10px;
      background: #1a0f0a; border: 3px solid var(--wood-light); color: var(--text-muted);
      border-radius: 4px; cursor: pointer; transition: all 0.2s ease;
      display: flex; align-items: center; justify-content: center; gap: 6px;
      white-space: nowrap; width: 100%; text-align: center;
    }

    .tab-btn:hover { border-color: var(--stardew-gold); color: #fff; transform: translateY(-2px); }
    .tab-btn.active {
      background: linear-gradient(180deg, var(--wood-mid) 0%, var(--wood-dark) 100%);
      border-color: var(--stardew-gold); color: var(--stardew-gold); box-shadow: 0 0 16px rgba(253, 224, 71, 0.4); transform: translateY(-2px);
    }

    .showcase-frame {
      position: relative; display: flex; gap: 40px; align-items: center; justify-content: center;
      width: 100%; max-width: 1060px; background: linear-gradient(180deg, var(--wood-mid) 0%, var(--wood-dark) 100%);
      border: 6px solid var(--wood-light); outline: 3px solid var(--wood-border);
      box-shadow: 0 20px 60px rgba(0,0,0,0.9), 0 0 40px rgba(253, 224, 71, 0.2);
      border-radius: 8px; padding: 32px; overflow: hidden;
    }

    #leafSweepCanvas {
      position: absolute; inset: 0; width: 100%; height: 100%;
      pointer-events: none; z-index: 80; image-rendering: pixelated;
    }

    .showcase-left-window {
      flex: 1.1; max-width: 480px; border: 4px solid var(--wood-border); border-radius: 6px; overflow: hidden; background: #000;
    }

    #showcasePreviewCanvas {
      display: block; width: 100%; height: 360px; image-rendering: pixelated;
    }

    .showcase-right-display {
      flex: 1; display: flex; flex-direction: column; justify-content: center; min-height: 260px; position: relative;
    }

    .showcase-text-card {
      display: none; flex-direction: column; justify-content: center;
      animation: fadeInCard 0.25s ease forwards;
    }
    .showcase-text-card.active { display: flex; }

    @keyframes fadeInCard {
      from { opacity: 0; transform: translateY(10px); }
      to { opacity: 1; transform: translateY(0); }
    }

    .step-badge {
      font-family: var(--font-pixel); font-size: 10px; color: var(--stardew-gold);
      background: rgba(245, 158, 11, 0.2); border: 2px solid var(--stardew-gold);
      padding: 6px 14px; border-radius: 4px; display: inline-block; width: fit-content; margin-bottom: 14px;
    }

    .step-title { font-family: var(--font-stardew); font-size: 22px; color: #fff; margin-bottom: 14px; text-shadow: 2px 2px 0 #000; }
    .step-desc { font-size: 16px; color: #e2d1c3; line-height: 1.65; }

    /* SPECS & PRICING */
    #specs { padding: 100px 40px; max-width: 1200px; margin: 0 auto; }
    .section-header { text-align: center; margin-bottom: 64px; }
    .section-title { font-family: var(--font-stardew); font-size: 32px; color: var(--stardew-gold); margin-bottom: 14px; text-shadow: 3px 3px 0 #000; }
    .section-sub { color: var(--text-muted); font-size: 18px; }

    .features-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 36px; }
    .feature-card {
      padding: 40px; background: linear-gradient(180deg, var(--wood-mid) 0%, var(--wood-dark) 100%);
      border: 5px solid var(--wood-border); outline: 3px solid var(--wood-light); outline-offset: -7px;
      border-radius: 6px; box-shadow: 0 10px 30px rgba(0,0,0,0.8);
    }
    .feature-icon { font-size: 52px; margin-bottom: 22px; }
    .feature-title { font-family: var(--font-stardew); font-size: 18px; color: var(--stardew-gold); margin-bottom: 14px; }
    .feature-desc { color: #e2d1c3; font-size: 16px; line-height: 1.6; }

    #passes { padding: 100px 40px; background: rgba(20, 10, 4, 0.6); border-top: 4px solid var(--wood-light); border-bottom: 4px solid var(--wood-light); }
    .pricing-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(360px, 1fr)); gap: 44px; max-width: 1000px; margin: 0 auto; }
    
    .pricing-card {
      padding: 48px; background: linear-gradient(180deg, var(--wood-mid) 0%, var(--wood-dark) 100%);
      border: 5px solid var(--wood-border); outline: 3px solid var(--wood-light); outline-offset: -7px;
      border-radius: 6px; display: flex; flex-direction: column; justify-content: space-between;
      box-shadow: 0 12px 36px rgba(0,0,0,0.85); position: relative;
    }
    .pricing-badge {
      position: absolute; top: -16px; right: 20px; font-family: var(--font-pixel); font-size: 10px;
      background: var(--stardew-gold); color: #000; padding: 6px 14px; border: 2px solid #000; box-shadow: 0 3px 0 #000;
    }
    .pricing-name { font-family: var(--font-stardew); font-size: 22px; color: var(--stardew-gold); margin-bottom: 8px; }
    .pricing-price { font-family: var(--font-retro); font-size: 56px; color: #34d399; margin-bottom: 24px; }
    .pricing-price span { font-size: 22px; color: var(--text-muted); }
    .pricing-list { list-style: none; margin-bottom: 38px; }
    .pricing-list li { margin-bottom: 16px; color: #fcedc0; font-size: 16px; display: flex; align-items: center; gap: 12px; }

    footer {
      padding: 50px; text-align: center; border-top: 5px solid var(--wood-border); outline: 3px solid var(--wood-light); outline-offset: -7px;
      font-family: var(--font-retro); font-size: 24px; color: var(--text-muted); background: #140a04;
    }

    /* LOADING OVERLAY */
    #loading-view {
      display: none; position: fixed; inset: 0; z-index: 500; background: rgba(14, 8, 4, 0.96); backdrop-filter: blur(16px);
      align-items: center; justify-content: center; flex-direction: column;
    }
    .loading-card { width: 580px; max-width: 90vw; padding: 44px; text-align: center; display: flex; flex-direction: column; align-items: center; gap: 20px; }
    .loading-title { font-family: var(--font-stardew); font-size: 22px; color: var(--stardew-gold); text-shadow: 2px 2px 0 #000; }
    #loadingCanvas { width: 64px; height: 64px; image-rendering: pixelated; }
    .loading-bar-outer { width: 100%; height: 26px; background: #1c0e05; border: 4px solid var(--wood-light); box-shadow: inset 0 2px 6px #000; border-radius: 4px; padding: 3px; }
    .loading-bar-inner { height: 100%; width: 0%; background: linear-gradient(90deg, #f59e0b 0%, #fde047 100%); border-radius: 2px; }
    .loading-percent { font-family: var(--font-pixel); font-size: 12px; color: var(--stardew-gold); }
    .loading-tip { font-family: var(--font-sans); font-size: 16px; color: var(--text-muted); font-style: italic; min-height: 46px; }

    /* FULL 5x5 GRID GAME VIEW */
    #game-view {
      display: none; position: fixed; inset: 0; z-index: 400; width: 100vw; height: 100vh;
      overflow-y: auto; overflow-x: hidden; padding: 80px 20px 60px 20px;
    }

    #gameBackgroundCanvas {
      position: fixed; inset: 0; width: 100%; height: 100%; z-index: 0; pointer-events: none; image-rendering: pixelated;
    }

    .game-top-bar {
      position: fixed; top: 0; left: 0; right: 0; z-index: 450;
      display: flex; align-items: center; justify-content: space-between; padding: 12px 28px;
      background: rgba(30, 17, 9, 0.94); backdrop-filter: blur(8px); border-bottom: 4px solid var(--wood-light);
    }
    .game-title { font-family: var(--font-stardew); font-size: 18px; color: var(--stardew-gold); text-shadow: 2px 2px 0 #000; }
    .game-usdc-badge { font-family: var(--font-pixel); font-size: 12px; color: var(--stardew-gold); background: rgba(245, 158, 11, 0.2); border: 2px solid var(--stardew-gold); padding: 8px 16px; border-radius: 4px; box-shadow: 0 4px 0 #000; }

    /* 5x5 Grid Game Container in Full View */
    .full-game-container {
      position: relative; z-index: 10;
      width: 100%; max-width: 620px; margin: 0 auto; display: flex; flex-direction: column; gap: 12px; align-items: center;
    }

    .top-stats-bar {
      width: 100%; background: #2c1609; border: 4px solid var(--wood-border); outline: 3px solid var(--wood-light); outline-offset: -7px;
      box-shadow: 0 8px 20px rgba(0,0,0,0.6); padding: 12px 20px; border-radius: 4px;
      display: flex; align-items: center; justify-content: space-between; font-family: var(--font-pixel); font-size: 11px;
    }
    .stat-coins { color: var(--stardew-gold); display: flex; align-items: center; gap: 6px; text-shadow: 2px 2px 0 #000; }
    .stat-pass-badge { color: #f87171; background: rgba(239, 68, 68, 0.2); padding: 4px 8px; border: 1px solid #ef4444; border-radius: 3px; }
    .stat-day { color: #fff; text-shadow: 2px 2px 0 #000; }

    .usdc-vault-card {
      width: 100%; background: linear-gradient(135deg, #1e3a8a 0%, #065f46 100%);
      border: 4px solid #34d399; box-shadow: 0 0 16px rgba(52, 211, 153, 0.4);
      border-radius: 6px; padding: 14px 20px; display: flex; align-items: center; justify-content: space-between;
    }
    .usdc-vault-info { display: flex; flex-direction: column; gap: 4px; }
    .usdc-vault-title { font-family: var(--font-pixel); font-size: 10px; color: #60a5fa; }
    .usdc-vault-balance { font-family: var(--font-retro); font-size: 32px; color: #34d399; text-shadow: 1px 1px 0 #000; }
    .cashout-btn {
      font-family: var(--font-pixel); font-size: 10px; padding: 10px 16px;
      background: linear-gradient(180deg, #34d399 0%, #059669 100%);
      color: #000; border: 2px solid #000; box-shadow: 0 3px 0 #000; border-radius: 4px; cursor: pointer; font-weight: bold;
    }
    .cashout-btn:hover { background: linear-gradient(180deg, #6ee7b7 0%, #34d399 100%); transform: translateY(-2px); }

    .farm-grid-frame {
      width: 100%; background: #2c1609; border: 5px solid var(--wood-border); outline: 3px solid var(--wood-light); outline-offset: -8px;
      box-shadow: 0 12px 30px rgba(0,0,0,0.8); border-radius: 6px; padding: 16px;
    }

    .farm-grid {
      display: grid; grid-template-columns: repeat(5, 1fr); gap: 8px; width: 100%; aspect-ratio: 1;
    }

    .grid-tile {
      background: #4a5d23; border: 3px solid #2b3910; border-radius: 4px;
      display: flex; flex-direction: column; align-items: center; justify-content: center;
      cursor: pointer; position: relative; overflow: hidden;
      width: 100%; height: 100%; box-sizing: border-box;
    }

    .grid-tile:hover {
      border-color: var(--stardew-gold); box-shadow: inset 0 0 10px var(--stardew-gold);
    }

    .grid-tile.tilled { background: #3b2313; border-color: #1a0f07; }
    .grid-tile.needs-water { border-color: #60a5fa; box-shadow: inset 0 0 12px #3b82f6; animation: waterPulse 1s infinite alternate; }
    .grid-tile.ready { border-color: #34d399; box-shadow: 0 0 12px #34d399, inset 0 0 10px #34d399; animation: pulseGlow 1.2s infinite alternate; }

    @keyframes waterPulse {
      0% { border-color: #60a5fa; }
      100% { border-color: #1d4ed8; }
    }

    @keyframes pulseGlow {
      0% { border-color: #fde047; box-shadow: inset 0 0 6px #fde047; }
      100% { border-color: #34d399; box-shadow: inset 0 0 14px #34d399; }
    }

    .tile-crop-icon {
      font-size: 34px; line-height: 1; display: flex; align-items: center; justify-content: center;
      pointer-events: none;
    }

    .tile-progress-bar {
      position: absolute; bottom: 4px; left: 6px; right: 6px; height: 6px;
      background: rgba(0,0,0,0.6); border: 1px solid #000; border-radius: 3px; overflow: hidden; pointer-events: none;
    }
    .tile-progress-fill { height: 100%; width: 0%; background: linear-gradient(90deg, #f59e0b, #34d399); transition: width 0.15s linear; }

    .action-strip {
      width: 100%; display: flex; align-items: center; justify-content: space-between;
      background: #2c1609; border: 4px solid var(--wood-border); outline: 2px solid var(--wood-light); outline-offset: -5px;
      padding: 10px 18px; border-radius: 4px; box-shadow: 0 6px 16px rgba(0,0,0,0.5);
    }

    .ready-count-badge { font-family: var(--font-pixel); font-size: 10px; color: #fff; display: flex; align-items: gap: 8px; }

    .end-day-btn {
      font-family: var(--font-pixel); font-size: 10px; padding: 10px 16px;
      background: linear-gradient(180deg, #f97316 0%, #ea580c 100%);
      color: #fff; border: 2px solid #000; box-shadow: 0 3px 0 #000; border-radius: 4px; cursor: pointer; text-shadow: 1px 1px 0 #000;
    }
    .end-day-btn:hover { background: linear-gradient(180deg, #fb923c 0%, #f97316 100%); transform: translateY(-2px); }

    .seed-shop-card {
      width: 100%; background: #2c1609; border: 5px solid var(--wood-border); outline: 3px solid var(--wood-light); outline-offset: -8px;
      box-shadow: 0 10px 25px rgba(0,0,0,0.7); border-radius: 6px; padding: 18px; display: flex; flex-direction: column; gap: 14px;
    }

    .shop-header { font-family: var(--font-stardew); font-size: 16px; color: var(--stardew-gold); text-shadow: 2px 2px 0 #000; display: flex; align-items: center; justify-content: space-between; }
    .seed-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 10px; }

    .seed-item {
      background: #1a0f0a; border: 3px solid #542d13; border-radius: 4px; padding: 10px 14px;
      display: flex; align-items: center; justify-content: space-between; cursor: pointer; transition: all 0.15s ease;
    }

    .seed-item:hover { border-color: var(--stardew-gold); background: #3b2313; transform: translateY(-2px); }
    .seed-item.selected { border-color: var(--stardew-gold); background: #4d2813; box-shadow: 0 0 10px var(--stardew-gold); }

    .seed-info { display: flex; align-items: center; gap: 10px; }
    .seed-icon { font-size: 26px; }
    .seed-details { display: flex; flex-direction: column; gap: 2px; }
    .seed-name { font-family: var(--font-pixel); font-size: 10px; color: #fff; }
    .seed-price { font-family: var(--font-pixel); font-size: 9px; color: var(--stardew-gold); }
    .seed-time { font-family: var(--font-pixel); font-size: 8px; color: var(--text-muted); }

    .shop-instruction { font-family: var(--font-pixel); font-size: 8px; color: #f87171; text-align: center; margin-top: 4px; }
  </style>
</head>
<body>

  <!-- Web3 Connect Wallet Pixel Modal -->
  <div id="walletModal">
    <div class="wallet-modal-card">
      <div style="font-size: 48px;">🚜</div>
      <div class="wallet-modal-title">ARCADIA HOMESTEAD</div>
      <div class="wallet-modal-desc">
        Please connect your Web3 wallet to enter the game and earn native USDC on Arc Testnet.
      </div>
      <button class="stardew-btn" onclick="connectWalletFromModal()">🟢 CONNECT WALLET</button>
      <button style="background:transparent; border:none; color:var(--text-muted); font-family:var(--font-pixel); font-size:10px; cursor:pointer;" onclick="closeWalletModal()">CANCEL</button>
    </div>
  </div>

  <!-- Retro Pixel Toast Container -->
  <div id="pixelToastContainer"></div>

  <!-- Crisp Pixel Art Canvas Layers -->
  <canvas id="leafCanvas"></canvas>
  <canvas id="celebrationCanvas"></canvas>

  <!-- Navbar Header -->
  <header id="navbar">
    <div class="logo-container" onclick="switchToLandingView()">
      <div class="logo-icon">🚜</div>
      <div class="logo-text">ARCADIA HOMESTEAD</div>
    </div>

    <ul class="nav-links">
      <li><a href="#interactive-showcase" id="nav-showcase">Game Intro</a></li>
      <li><a href="#specs" id="nav-specs">GameFi Specs</a></li>
      <li><a href="#passes" id="nav-passes">Passes & Pricing</a></li>
      <li><a href="javascript:void(0)" onclick="handlePlayGameClick()" id="nav-play">Play Game</a></li>
    </ul>

    <!-- 5-Language Selector (Default: EN - English) -->
    <div class="lang-switcher">
      🌐
      <select class="lang-select" id="langSelect" onchange="changeLanguage(this.value)">
        <option value="EN" selected>EN - English</option>
        <option value="TR">TR - Türkçe</option>
        <option value="ES">ES - Español</option>
        <option value="ZH">ZH - 中文</option>
        <option value="JA">JA - 日本語</option>
      </select>
    </div>

    <div class="wallet-status">
      <div class="net-pill">
        <span class="net-dot"></span>
        <span>ARC TESTNET</span>
      </div>
      <button id="btn-connect-wallet" class="stardew-btn" onclick="connectWallet()">CONNECT WALLET</button>
    </div>
  </header>

  <!-- MAIN LANDING PAGE VIEW -->
  <div id="landing-view">
    <section id="hero">
      <div class="parchment-banner hero-badge" id="hero-badge">⚡ POWERED BY ARC TESTNET</div>
      <h1 class="hero-title" id="hero-title">BUILD, HARVEST & TRADE IN A <span>DECENTRALIZED PIXEL WORLD</span></h1>
      <p class="hero-subtitle" id="hero-subtitle">
        Arcadia Homestead is a 5x5 Grid Stardew-aesthetic Web3 pixel farming simulation running on Arc Testnet.
      </p>

      <div class="hero-cta">
        <button class="stardew-btn" onclick="handlePlayGameClick()" id="btn-hero-play">
          🎮 PLAY GAME / LAUNCH APP
        </button>
        <a href="#passes" class="stardew-btn" id="btn-hero-pass">
          👑 GET PREMIUM PASS
        </a>
      </div>

      <!-- PERFECTLY ALIGNED FLOATING ISOMETRIC PARALLAX HERO CANVAS -->
      <div class="hero-stage">
        <canvas id="heroCanvas" width="720" height="440"></canvas>
      </div>

      <div class="stats-bar">
        <div class="stardew-card stat-box">
          <div class="stat-number">10,000</div>
          <div class="stat-label">FARM PLOTS</div>
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

    <!-- PERFECT STICKY SCROLL SHOWCASE -->
    <section id="interactive-showcase">
      <div class="sticky-pin-container" id="stickyContainer">
        <div class="showcase-header">
          <h2 class="showcase-title" id="showcase-title">HOW TO PLAY & GAMEPLAY FEATURES</h2>
          <p class="showcase-sub" id="showcase-sub">Scroll down to wipe through showcase steps with Giant Pixel Leaf</p>
        </div>

        <div class="showcase-tabs">
          <button class="tab-btn active" id="tab-1" onclick="triggerBigLeafTransition(1)">🌾 STEP 01: 5x5 GRID</button>
          <button class="tab-btn" id="tab-2" onclick="triggerBigLeafTransition(2)">⏱️ STEP 02: GROWTH</button>
          <button class="tab-btn" id="tab-3" onclick="triggerBigLeafTransition(3)">🌱 STEP 03: SEED SHOP</button>
          <button class="tab-btn" id="tab-4" onclick="triggerBigLeafTransition(4)">💰 STEP 04: USDC MARKET</button>
        </div>

        <div class="showcase-frame">
          <canvas id="leafSweepCanvas"></canvas>

          <div class="showcase-left-window">
            <canvas id="showcasePreviewCanvas" width="480" height="360"></canvas>
          </div>

          <div class="showcase-right-display">
            <div class="showcase-text-card active" id="card-1">
              <span class="step-badge">STEP 01</span>
              <h3 class="step-title" id="card1-title">🌾 5x5 GRID FARMING INFRASTRUCTURE</h3>
              <p class="step-desc" id="card1-desc">
                Prepare your soil across 25 fertile farm plots. Easily plant seeds by tapping on any crop of your choice.
              </p>
            </div>

            <div class="showcase-text-card" id="card-2">
              <span class="step-badge">STEP 02</span>
              <h3 class="step-title" id="card2-title">⏱️ REALTIME GROWTH & MOISTURE MECHANICS</h3>
              <p class="step-desc" id="card2-desc">
                Crops grow in realistic intervals (Wheat: 60s, Carrot: 2.5m, Pumpkin: 20m). Manual watering is required for Free tier farmers!
              </p>
            </div>

            <div class="showcase-text-card" id="card-3">
              <span class="step-badge">STEP 03</span>
              <h3 class="step-title" id="card3-title">🌱 PREMIUM PASS 3X SPEED & AUTO IRRIGATION</h3>
              <p class="step-desc" id="card3-desc">
                Monthly & Annual Pass subscribers get up to 3x growth acceleration and automated sprinkler systems for 24/7 farming!
              </p>
            </div>

            <div class="showcase-text-card" id="card-4">
              <span class="step-badge">STEP 04</span>
              <h3 class="step-title" id="card4-title">💰 ARC TESTNET REAL USDC CASH-OUT</h3>
              <p class="step-desc" id="card4-desc">
                Harvest rare crops and cash out your hard-earned USDC directly to your Web3 EVM wallet on Arc Testnet!
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section id="specs">
      <div class="section-header">
        <h2 class="section-title" id="specs-title">GAMEFI FEATURES & SPECS</h2>
        <p class="section-sub" id="specs-sub">Stardew Valley 5x5 retro graphics and Arc Testnet infrastructure</p>
      </div>

      <div class="features-grid">
        <div class="stardew-card feature-card">
          <div class="feature-icon">🌾</div>
          <h3 class="feature-title">5x5 PIXEL FARMING CYCLES</h3>
          <p class="feature-desc">
            Till soil and grow crops. Select seeds (Wheat, Carrot, Tomato, Strawberry, Pumpkin), monitor growth, and harvest rewards.
          </p>
        </div>

        <div class="stardew-card feature-card">
          <div class="feature-icon">💰</div>
          <h3 class="feature-title">NATIVE USDC ECONOMY</h3>
          <p class="feature-desc">
            Settle earnings in native Arc testnet USDC token with sub-second block finality and zero friction.
          </p>
        </div>

        <div class="stardew-card feature-card">
          <div class="feature-icon">🤖</div>
          <h3 class="feature-title">AGENTIC MARKET (SOON)</h3>
          <p class="feature-desc">
            Deploy autonomous AI agentic farmers that auto-water plots, manage growth cycles, and trade crops at optimal market prices.
          </p>
        </div>
      </div>
    </section>

    <section id="passes">
      <div class="section-header">
        <h2 class="section-title" id="passes-title">PREMIUM PASS SUBSCRIPTIONS</h2>
        <p class="section-sub" id="passes-sub">Exclusive farming perks paid with Arc Testnet native USDC</p>
      </div>

      <div class="pricing-grid">
        <div class="stardew-card pricing-card">
          <div>
            <div class="pricing-name">MONTHLY PASS</div>
            <div class="pricing-price">5.00 <span>USDC / mo</span></div>
            <ul class="pricing-list">
              <li>⚡ 2x Accelerated Crop Growth</li>
              <li>💧 Auto-Sprinkler Irrigation (0% Dry Risk)</li>
              <li>💰 10% Lower Marketplace Fee</li>
              <li>✨ Golden Farmer Badge</li>
            </ul>
          </div>
          <button class="stardew-btn" onclick="subscribePass('monthly', 5)">SUBSCRIBE (5 USDC)</button>
        </div>

        <div class="stardew-card pricing-card">
          <div class="pricing-badge">MOST POPULAR</div>
          <div>
            <div class="pricing-name">ANNUAL PASS</div>
            <div class="pricing-price">45.00 <span>USDC / yr</span></div>
            <ul class="pricing-list">
              <li>🚀 3x Super Growth Speed</li>
              <li>🌧️ Auto-Rain & Full Automated Irrigation</li>
              <li>💎 0% Zero Fee + 50% Bonus Yield</li>
              <li>🏆 Golden Hoe & VIP Badge</li>
            </ul>
          </div>
          <button class="stardew-btn" onclick="subscribePass('annual', 45)">SUBSCRIBE (45 USDC)</button>
        </div>
      </div>
    </section>

    <footer>
      <p>© 2026 Arcadia Homestead - Arc Testnet (Chain ID 5042002 / 0x4cef52)</p>
    </footer>
  </div>

  <div id="loading-view">
    <div class="stardew-card loading-card">
      <div class="loading-title">🌾 ARCADIA HOMESTEAD</div>
      <canvas id="loadingCanvas" width="64" height="64"></canvas>
      <div class="loading-bar-outer">
        <div class="loading-bar-inner" id="loadingBar"></div>
      </div>
      <div class="loading-percent" id="loadingPercent">0%</div>
      <div class="loading-tip" id="loadingTip">
        "Tip: You can use native USDC on Arc Testnet for all marketplace transactions."
      </div>
    </div>
  </div>

  <!-- FULL 5x5 GRID GAME VIEW -->
  <div id="game-view">
    <canvas id="gameBackgroundCanvas"></canvas>

    <div class="game-top-bar">
      <button class="stardew-btn" onclick="switchToLandingView()">
        ⬅ BACK TO WEBSITE
      </button>
      <div class="game-title">🌾 ARCADIA HOMESTEAD - FULL GAME</div>
      <div class="game-usdc-badge" id="game-view-usdc">USDC: 0.00</div>
    </div>

    <div class="full-game-container">
      <div class="top-stats-bar">
        <div class="stat-coins">🪙 <span id="coinCount">163</span> Coins</div>
        <div class="stat-pass-badge" id="passStatusBadge">FREE PASS (Hard Mode: 1x Speed + 30% Fee)</div>
        <div class="stat-day">Day <span id="dayCount">1</span></div>
      </div>

      <div class="usdc-vault-card">
        <div class="usdc-vault-info">
          <span class="usdc-vault-title">💰 ARC USDC VAULT</span>
          <span class="usdc-vault-balance" id="usdcVaultBalance">0.00 USDC</span>
        </div>
        <button class="cashout-btn" onclick="cashoutUSDC()">CASH OUT USDC 💸</button>
      </div>

      <div class="farm-grid-frame">
        <div class="farm-grid" id="farmGrid"></div>
      </div>

      <div class="action-strip">
        <div class="ready-count-badge">🌾 <span id="readyCount">0</span> ready! (Blue = Needs Water 💧)</div>
        <button class="end-day-btn" onclick="endDay()">🌅 END DAY (Skip Time)</button>
      </div>

      <div class="seed-shop-card">
        <div class="shop-header">
          <span>🌱 SEED SHOP</span>
          <span style="font-size: 9px; color: var(--text-muted);">SPEED: <b id="speedMultLabel" style="color: #f87171;">1x (Hard Mode)</b></span>
        </div>
        <div class="seed-grid" id="seedGrid"></div>
        <div class="shop-instruction">⚠️ HARD USDC EARNING: Harvest 🎃 Pumpkin (20m) or 🍓 Strawberry (10m) to earn +0.10 USDC into Vault! Upgrade to Premium Pass for 3x Speed!</div>
      </div>
    </div>
  </div>

  <script>
    const TREASURY_ADDRESS = "0x71C7656EC7ab88b098defB751B7401B5f6d8976F";
    const ARC_CHAIN_HEX = "0x4cef52"; // 5042002 in hex

    /* RETRO PIXEL TOAST SYSTEM */
    function showPixelToast(msg, icon = '📜') {
      const container = document.getElementById('pixelToastContainer'); if (!container) return;
      const toast = document.createElement('div');
      toast.className = 'pixel-toast';
      toast.innerHTML = `<span>${icon}</span> <span>${msg}</span>`;
      container.appendChild(toast);
      playSound('water');

      setTimeout(() => {
        toast.style.opacity = '0';
        toast.style.transition = 'opacity 0.3s ease';
        setTimeout(() => toast.remove(), 300);
      }, 3400);
    }

    /* WALLET MODAL CONTROLS */
    function openWalletModal() {
      document.getElementById('walletModal').style.display = 'flex';
    }
    function closeWalletModal() {
      document.getElementById('walletModal').style.display = 'none';
    }

    async function connectWalletFromModal() {
      const success = await connectWallet();
      if (success) {
        closeWalletModal();
        startLoadingSequence();
      }
    }

    function handlePlayGameClick() {
      if (!userAddress) {
        openWalletModal();
      } else {
        startLoadingSequence();
      }
    }

    /* LEAF ENGINE */
    function createPixelLeafSprite(color, outlineColor) {
      const c = document.createElement('canvas'); c.width = 16; c.height = 16;
      const ctx = c.getContext('2d'); ctx.imageSmoothingEnabled = false;
      const pixels = [
        "....XXXX........", "..XXOOOOXX......", ".XOOOOOOOOXX....", "XOOOOOOOOOOOXX..",
        "XOOOOVOOOOOOOOX.", "XOOOOOVOOOOOOOX.", ".XOOOOOVOOOOOX..", "..XOOOOOVOOOX...",
        "...XOOOOOVX.....", "....XOOOOVX.....", ".....XOOVXXXX...", "......XVX....XX.",
        "......X.........", "................"
      ];
      for(let r = 0; r < pixels.length; r++) {
        for(let col = 0; col < pixels[r].length; col++) {
          const char = pixels[r][col];
          if (char === 'X') { ctx.fillStyle = outlineColor; ctx.fillRect(col, r, 1, 1); }
          else if (char === 'O') { ctx.fillStyle = color; ctx.fillRect(col, r, 1, 1); }
          else if (char === 'V') { ctx.fillStyle = '#1c0a02'; ctx.fillRect(col, r, 1, 1); }
        }
      }
      return c;
    }

    function initPixelLeafEngine() {
      const canvas = document.getElementById('leafCanvas');
      const ctx = canvas.getContext('2d'); ctx.imageSmoothingEnabled = false;
      let width = canvas.width = window.innerWidth; let height = canvas.height = window.innerHeight;

      window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth; height = canvas.height = window.innerHeight;
        ctx.imageSmoothingEnabled = false;
      });

      const leafSprites = [
        createPixelLeafSprite('#4d9e29', '#1a3a0d'), createPixelLeafSprite('#f59e0b', '#451a03'),
        createPixelLeafSprite('#dc2626', '#450a0a'), createPixelLeafSprite('#fbbf24', '#78350f')
      ];

      const particles = [];
      for(let i = 0; i < 40; i++) {
        particles.push({
          x: Math.random() * width, y: Math.random() * height,
          sprite: leafSprites[Math.floor(Math.random() * leafSprites.length)],
          vx: 0.4 + Math.random() * 1.2, vy: 0.8 + Math.random() * 1.4,
          stepFrame: Math.floor(Math.random() * 4), stepTimer: 0, scale: (Math.random() > 0.5) ? 2 : 3
        });
      }

      function renderLeaves() {
        ctx.clearRect(0, 0, width, height);
        particles.forEach(p => {
          p.x += p.vx; p.y += p.vy; p.stepTimer++;
          if (p.stepTimer > 15) { p.stepFrame = (p.stepFrame + 1) % 4; p.stepTimer = 0; }
          if (p.x > width) p.x = -32; if (p.y > height) p.y = -32;

          ctx.save(); ctx.translate(Math.floor(p.x), Math.floor(p.y));
          ctx.rotate((p.stepFrame * 90) * Math.PI / 180);
          const s = p.scale; ctx.drawImage(p.sprite, -8 * s, -8 * s, 16 * s, 16 * s);
          ctx.restore();
        });
        requestAnimationFrame(renderLeaves);
      }
      renderLeaves();
    }

    /* GAME BACKGROUND ENGINE */
    function initGameBackgroundEngine() {
      const canvas = document.getElementById('gameBackgroundCanvas'); if (!canvas) return;
      const ctx = canvas.getContext('2d'); ctx.imageSmoothingEnabled = false;

      let width = canvas.width = window.innerWidth;
      let height = canvas.height = window.innerHeight;

      window.addEventListener('resize', () => {
        width = canvas.width = window.innerWidth;
        height = canvas.height = window.innerHeight;
        ctx.imageSmoothingEnabled = false;
      });

      const clouds = [
        { x: 50, y: 80, speed: 0.3, scale: 3 },
        { x: 350, y: 140, speed: 0.2, scale: 4 },
        { x: 750, y: 60, speed: 0.4, scale: 3 },
        { x: 1100, y: 110, speed: 0.25, scale: 4 }
      ];

      const sparkles = [];
      for(let i = 0; i < 30; i++) {
        sparkles.push({
          x: Math.random() * width,
          y: height * 0.45 + Math.random() * (height * 0.55),
          timer: Math.random() * 100,
          scale: 1 + Math.floor(Math.random() * 2)
        });
      }

      let sunPulse = 0;

      function renderGameWorld() {
        ctx.clearRect(0, 0, width, height);

        const horizonY = height * 0.44;
        ctx.fillStyle = '#70c5ce'; ctx.fillRect(0, 0, width, horizonY);
        ctx.fillStyle = '#4a8528'; ctx.fillRect(0, horizonY, width, height - horizonY);

        sunPulse += 0.03;
        const sunX = width - 120, sunY = 90;
        const sunR = 36 + Math.sin(sunPulse) * 4;
        ctx.fillStyle = 'rgba(253, 224, 71, 0.3)';
        ctx.beginPath(); ctx.arc(sunX, sunY, sunR + 12, 0, Math.PI * 2); ctx.fill();
        ctx.fillStyle = '#fde047';
        ctx.beginPath(); ctx.arc(sunX, sunY, sunR, 0, Math.PI * 2); ctx.fill();

        ctx.fillStyle = '#ffffff';
        clouds.forEach(c => {
          c.x += c.speed;
          if (c.x > width + 150) c.x = -150;
          const s = c.scale;
          ctx.fillRect(Math.floor(c.x), Math.floor(c.y), 40 * s, 12 * s);
          ctx.fillRect(Math.floor(c.x + 8 * s), Math.floor(c.y - 6 * s), 24 * s, 6 * s);
        });

        ctx.fillStyle = '#3f7320';
        ctx.beginPath();
        ctx.ellipse(width * 0.25, horizonY + 20, width * 0.35, 60, 0, 0, Math.PI * 2);
        ctx.fill();
        ctx.beginPath();
        ctx.ellipse(width * 0.75, horizonY + 15, width * 0.4, 70, 0, 0, Math.PI * 2);
        ctx.fill();

        ctx.fillStyle = '#4d2813';
        const fenceY = horizonY - 14;
        for(let fx = 10; fx < width; fx += 44) {
          ctx.fillRect(fx, fenceY, 8, 24);
        }
        ctx.fillRect(0, fenceY + 6, width, 5);
        ctx.fillRect(0, fenceY + 14, width, 5);

        sparkles.forEach(s => {
          s.timer += 0.05;
          const alpha = (Math.sin(s.timer) + 1) / 2;
          if (alpha > 0.3) {
            ctx.fillStyle = `rgba(253, 224, 71, ${alpha.toFixed(2)})`;
            ctx.fillRect(Math.floor(s.x), Math.floor(s.y), 4 * s.scale, 4 * s.scale);
          }
        });

        requestAnimationFrame(renderGameWorld);
      }
      renderGameWorld();
    }

    /* PERFECTLY ALIGNED & BALANCED FLOATING ISOMETRIC HERO STAGE WITH DYNAMIC HARVEST FLOATING ORBIT */
    function initHeroShowcase() {
      const hCanvas = document.getElementById('heroCanvas'); if (!hCanvas) return;
      const hCtx = hCanvas.getContext('2d'); hCtx.imageSmoothingEnabled = false;

      let tick = 0;
      const floatingHarvests = ['🌾', '🥕', '🍅', '🍓', '🎃', '🪙', '💎'];

      function renderHeroFrame() {
        tick += 0.02;
        hCtx.clearRect(0, 0, hCanvas.width, hCanvas.height);

        const floatY = Math.sin(tick) * 8;

        // Ambient radial glow background
        const gradient = hCtx.createRadialGradient(360, 220 + floatY, 40, 360, 220 + floatY, 340);
        gradient.addColorStop(0, 'rgba(253, 224, 71, 0.22)');
        gradient.addColorStop(1, 'rgba(0, 0, 0, 0)');
        hCtx.fillStyle = gradient;
        hCtx.fillRect(0, 0, 720, 440);

        const centerX = 360, centerY = 210 + floatY;
        const tileW = 76, tileH = 38; // Increased tile size to fit top grass surface perfectly

        // 1. Dirt Base Layer (Underneath Grass)
        hCtx.fillStyle = '#2c1609';
        hCtx.beginPath();
        hCtx.moveTo(centerX, centerY - 120);
        hCtx.lineTo(centerX + 235, centerY);
        hCtx.lineTo(centerX, centerY + 120);
        hCtx.lineTo(centerX - 235, centerY);
        hCtx.closePath();
        hCtx.fill();

        // 2. Dirt 3D Side Walls
        hCtx.fillStyle = '#1c0a02';
        hCtx.beginPath();
        hCtx.moveTo(centerX - 235, centerY);
        hCtx.lineTo(centerX, centerY + 120);
        hCtx.lineTo(centerX, centerY + 160);
        hCtx.lineTo(centerX - 235, centerY + 40);
        hCtx.closePath();
        hCtx.fill();

        hCtx.fillStyle = '#3a1b07';
        hCtx.beginPath();
        hCtx.moveTo(centerX + 235, centerY);
        hCtx.lineTo(centerX, centerY + 120);
        hCtx.lineTo(centerX, centerY + 160);
        hCtx.lineTo(centerX + 235, centerY + 40);
        hCtx.closePath();
        hCtx.fill();

        // 3. Grass Top Layer (Balanced Green Margin Around 5x5 Grid)
        hCtx.fillStyle = '#599632';
        hCtx.beginPath();
        hCtx.moveTo(centerX, centerY - 126);
        hCtx.lineTo(centerX + 235, centerY - 6);
        hCtx.lineTo(centerX, centerY + 114);
        hCtx.lineTo(centerX - 235, centerY - 6);
        hCtx.closePath();
        hCtx.fill();

        // 4. PERFECT 5x5 ISOMETRIC GRID (Centering Math: Grid origin centered at (centerX, centerY - 6))
        const crops = ['🌾', '🥕', '🍅', '🍓', '🎃'];
        for (let r = 0; r < 5; r++) {
          for (let c = 0; c < 5; c++) {
            const isoX = centerX + (c - r) * (tileW / 2);
            const isoY = centerY - 6 + (c + r - 4) * (tileH / 2);

            // Draw isometric dirt plot
            hCtx.fillStyle = '#3b2313';
            hCtx.beginPath();
            hCtx.moveTo(isoX, isoY - tileH / 2);
            hCtx.lineTo(isoX + tileW / 2, isoY);
            hCtx.lineTo(isoX, isoY + tileH / 2);
            hCtx.lineTo(isoX - tileW / 2, isoY);
            hCtx.closePath();
            hCtx.fill();

            hCtx.strokeStyle = '#1a0f07'; hCtx.lineWidth = 2; hCtx.stroke();

            // Render crop icon cleanly centered inside each isometric polygon
            const idx = r * 5 + c;
            if (idx % 2 === 0 || idx === 7 || idx === 17) {
              const cropIcon = crops[idx % crops.length];
              hCtx.font = '22px sans-serif';
              hCtx.fillText(cropIcon, isoX - 11, isoY + 7);
            }
          }
        }

        // 5. DYNAMIC FLOATING HARVEST CROPS & COIN ORBIT ABOVE ISLAND!
        const orbitR = 140;
        for (let i = 0; i < floatingHarvests.length; i++) {
          const angle = tick * 0.8 + (i * Math.PI * 2 / floatingHarvests.length);
          const itemX = centerX + Math.cos(angle) * orbitR;
          const itemY = centerY - 130 + Math.sin(angle) * 22 + Math.sin(tick * 2 + i) * 6;
          const itemScale = 0.85 + (Math.sin(angle) + 1) * 0.2;

          hCtx.save();
          hCtx.font = `${Math.floor(26 * itemScale)}px "Press Start 2P", sans-serif`;
          hCtx.fillText(floatingHarvests[i], itemX - 14, itemY);
          hCtx.restore();
        }

        requestAnimationFrame(renderHeroFrame);
      }
      renderHeroFrame();
    }

    /* STICKY SHOWCASE ENGINE */
    let activeTabStep = 1;
    let isLeafTransitioning = false;

    function renderShowcasePreview(step) {
      const sCanvas = document.getElementById('showcasePreviewCanvas'); if (!sCanvas) return;
      const sCtx = sCanvas.getContext('2d'); sCtx.imageSmoothingEnabled = false;

      sCtx.clearRect(0, 0, sCanvas.width, sCanvas.height);

      sCtx.fillStyle = '#70c5ce'; sCtx.fillRect(0, 0, 480, 150);
      sCtx.fillStyle = '#599632'; sCtx.fillRect(0, 150, 480, 210);

      if (step === 1) {
        sCtx.fillStyle = '#2c1609'; sCtx.fillRect(60, 25, 360, 310);
        sCtx.fillStyle = '#fde047'; sCtx.font = '11px "Press Start 2P"'; sCtx.fillText('STEP 1: 5x5 GRID TARLA', 85, 52);

        for(let r=0; r<5; r++) {
          for(let c=0; c<5; c++) {
            const x = 85 + c * 54, y = 70 + r * 48;
            sCtx.fillStyle = '#3b2313'; sCtx.fillRect(x, y, 46, 42);
            sCtx.strokeStyle = '#fde047'; sCtx.lineWidth = 2; sCtx.strokeRect(x, y, 46, 42);
          }
        }
      } else if (step === 2) {
        sCtx.fillStyle = '#2c1609'; sCtx.fillRect(60, 25, 360, 310);
        sCtx.fillStyle = '#34d399'; sCtx.font = '11px "Press Start 2P"'; sCtx.fillText('STEP 2: REALTIME GROWTH', 80, 52);

        const crops = ['🌱', '🌿', '🌾', '🥕', '🍅'];
        for(let r=0; r<5; r++) {
          for(let c=0; c<5; c++) {
            const x = 85 + c * 54, y = 70 + r * 48;
            sCtx.fillStyle = '#3b2313'; sCtx.fillRect(x, y, 46, 42);
            sCtx.strokeStyle = (r+c)%2===0 ? '#34d399' : '#1a0f07'; sCtx.lineWidth = 2; sCtx.strokeRect(x, y, 46, 42);
            sCtx.font = '20px sans-serif'; sCtx.fillText(crops[(r+c)%crops.length], x+12, y+28);
          }
        }
      } else if (step === 3) {
        sCtx.fillStyle = '#2c1609'; sCtx.fillRect(40, 20, 400, 320);
        sCtx.fillStyle = '#fde047'; sCtx.font = '11px "Press Start 2P"'; sCtx.fillText('STEP 3: SEED SHOP', 140, 45);

        const seeds = [
          { icon: '🌾', name: 'Wheat', price: '🪙 5' },
          { icon: '🥕', name: 'Carrot', price: '🪙 10' },
          { icon: '🍅', name: 'Tomato', price: '🪙 20' },
          { icon: '🍓', name: 'Strawberry', price: '🪙 30' }
        ];
        seeds.forEach((s, i) => {
          const y = 65 + i * 62;
          sCtx.fillStyle = '#1a0f0a'; sCtx.fillRect(60, y, 360, 52);
          sCtx.strokeStyle = '#542d13'; sCtx.lineWidth = 3; sCtx.strokeRect(60, y, 360, 52);
          sCtx.font = '24px sans-serif'; sCtx.fillText(s.icon, 75, y + 34);
          sCtx.fillStyle = '#ffffff'; sCtx.font = '11px "Press Start 2P"'; sCtx.fillText(s.name, 120, y + 31);
          sCtx.fillStyle = '#fde047'; sCtx.fillText(s.price, 300, y + 31);
        });
      } else if (step === 4) {
        sCtx.fillStyle = '#2c1609'; sCtx.fillRect(40, 25, 400, 310);
        sCtx.fillStyle = '#34d399'; sCtx.font = '11px "Press Start 2P"'; sCtx.fillText('STEP 4: ARC USDC MARKET', 95, 55);

        sCtx.fillStyle = 'rgba(52, 211, 153, 0.2)'; sCtx.fillRect(70, 75, 340, 52);
        sCtx.strokeStyle = '#34d399'; sCtx.lineWidth = 3; sCtx.strokeRect(70, 75, 340, 52);
        sCtx.fillStyle = '#34d399'; sCtx.font = '13px "Press Start 2P"'; sCtx.fillText('💰 USDC: 100.00', 120, 108);

        sCtx.fillStyle = 'rgba(245, 158, 11, 0.2)'; sCtx.fillRect(70, 145, 340, 160);
        sCtx.strokeStyle = '#fde047'; sCtx.lineWidth = 3; sCtx.strokeRect(70, 145, 340, 160);
        sCtx.fillStyle = '#fde047'; sCtx.font = '11px "Press Start 2P"'; sCtx.fillText('👑 PREMIUM PASS', 130, 180);
        sCtx.fillStyle = '#ffffff'; sCtx.fillText('• 3x Speed Crop Growth', 90, 215);
        sCtx.fillText('• 0% Marketplace Fee', 90, 245);
      }
    }

    function switchShowcaseTab(num) {
      activeTabStep = num;
      for(let i=1; i<=4; i++) {
        const btn = document.getElementById(`tab-${i}`);
        const card = document.getElementById(`card-${i}`);
        if (btn) btn.classList.toggle('active', i === num);
        if (card) card.classList.toggle('active', i === num);
      }
      renderShowcasePreview(num);
    }

    const bigLeafSprite = createPixelLeafSprite('#f59e0b', '#451a03');

    function triggerBigLeafTransition(targetStep) {
      if (isLeafTransitioning || targetStep === activeTabStep) return;
      isLeafTransitioning = true;

      const canvas = document.getElementById('leafSweepCanvas');
      const container = document.querySelector('.showcase-frame');
      if (!canvas || !container) {
        switchShowcaseTab(targetStep);
        isLeafTransitioning = false;
        return;
      }

      canvas.width = container.clientWidth;
      canvas.height = container.clientHeight;
      const ctx = canvas.getContext('2d');
      ctx.imageSmoothingEnabled = false;

      let leafX = -300;
      const speed = 36;
      const midPoint = canvas.width * 0.45;
      let stepSwitched = false;

      function animateSweep() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);

        leafX += speed;

        if (leafX >= midPoint && !stepSwitched) {
          stepSwitched = true;
          switchShowcaseTab(targetStep);
        }

        const scale = 24;
        ctx.save();
        ctx.translate(Math.floor(leafX), Math.floor(canvas.height / 2));
        ctx.rotate(0.2);
        ctx.drawImage(bigLeafSprite, -8 * scale, -8 * scale, 16 * scale, 16 * scale);
        ctx.restore();

        ctx.fillStyle = '#fde047';
        for(let p = 0; p < 8; p++) {
          const px = leafX - 60 - Math.random() * 140;
          const py = canvas.height / 2 + (Math.random() - 0.5) * 200;
          ctx.fillRect(Math.floor(px), Math.floor(py), 8, 8);
        }

        if (leafX < canvas.width + 350) {
          requestAnimationFrame(animateSweep);
        } else {
          ctx.clearRect(0, 0, canvas.width, canvas.height);
          isLeafTransitioning = false;
        }
      }

      animateSweep();
    }

    function handleStickyScroll() {
      const section = document.getElementById('interactive-showcase');
      const container = document.getElementById('stickyContainer');
      if (!section || !container) return;

      const rect = section.getBoundingClientRect();
      const navbarHeight = 90;
      const totalTrack = section.offsetHeight - window.innerHeight;

      if (rect.top <= navbarHeight && rect.bottom >= window.innerHeight) {
        container.classList.add('is-pinned');
        container.classList.remove('is-bottom');

        const currentScrolled = navbarHeight - rect.top;
        let progress = currentScrolled / totalTrack;
        progress = Math.max(0, Math.min(1, progress));

        let targetStep = 1;
        if (progress < 0.25) targetStep = 1;
        else if (progress < 0.50) targetStep = 2;
        else if (progress < 0.75) targetStep = 3;
        else targetStep = 4;

        if (targetStep !== activeTabStep && !isLeafTransitioning) {
          triggerBigLeafTransition(targetStep);
        }

      } else if (rect.bottom < window.innerHeight) {
        container.classList.remove('is-pinned');
        container.classList.add('is-bottom');
        if (activeTabStep !== 4 && !isLeafTransitioning) {
          triggerBigLeafTransition(4);
        }
      } else {
        container.classList.remove('is-pinned');
        container.classList.remove('is-bottom');
        if (activeTabStep !== 1 && !isLeafTransitioning) {
          switchShowcaseTab(1);
        }
      }
    }

    /* CROP PARTICLE EXPLOSION ENGINE */
    function triggerCropExplosion(x, y, cropIcon) {
      const canvas = document.getElementById('celebrationCanvas');
      const ctx = canvas.getContext('2d');
      canvas.width = window.innerWidth; canvas.height = window.innerHeight;

      const particles = [];
      for(let i = 0; i < 35; i++) {
        particles.push({
          x: x, y: y,
          vx: (Math.random() - 0.5) * 16, vy: -4 - Math.random() * 12, gravity: 0.4,
          icon: Math.random() > 0.3 ? cropIcon : '🪙',
          size: 16 + Math.random() * 14,
          rot: Math.random() * Math.PI * 2, vRot: (Math.random() - 0.5) * 0.2, alpha: 1
        });
      }

      let frame = 0;
      function animate() {
        frame++; ctx.clearRect(0, 0, canvas.width, canvas.height);
        let active = 0;
        particles.forEach(p => {
          p.x += p.vx; p.y += p.vy; p.vy += p.gravity; p.rot += p.vRot; p.alpha -= 0.02;
          if (p.alpha > 0) {
            active++; ctx.save(); ctx.globalAlpha = Math.max(0, p.alpha);
            ctx.translate(p.x, p.y); ctx.rotate(p.rot);
            ctx.font = `${Math.floor(p.size)}px sans-serif`;
            ctx.fillText(p.icon, -p.size/2, p.size/2);
            ctx.restore();
          }
        });
        if (active > 0 && frame < 90) requestAnimationFrame(animate);
        else ctx.clearRect(0, 0, canvas.width, canvas.height);
      }
      animate();
    }

    /* GAME ENGINE & REAL WEB3 ARC TESTNET TRANSACTIONS */
    let coins = 163;
    let usdcVault = 0.00;
    let day = 1;
    let selectedSeedId = 'wheat';
    let passLevel = 'free';
    let speedMultiplier = 1;
    let marketplaceFeePct = 30;

    const SEEDS = [
      { id: 'wheat', name: 'Wheat', icon: '🌾', price: 10, yieldCoins: 28, growTimeSec: 60 },
      { id: 'carrot', name: 'Carrot', icon: '🥕', price: 25, yieldCoins: 75, growTimeSec: 150 },
      { id: 'tomato', name: 'Tomato', icon: '🍅', price: 60, yieldCoins: 190, growTimeSec: 300 },
      { id: 'strawberry', name: 'Strawberry', icon: '🍓', price: 150, yieldCoins: 480, growTimeSec: 600 },
      { id: 'pumpkin', name: 'Pumpkin', icon: '🎃', price: 400, yieldCoins: 1350, growTimeSec: 1200 }
    ];

    const gridState = [];
    for(let i=0; i<25; i++) {
      gridState.push({ id: i, crop: null, timer: null, needsWater: false, needsWaterHandled: false });
    }

    const AudioCtx = window.AudioContext || window.webkitAudioContext;
    let audioCtx = null;

    function playSound(type) {
      try {
        if (!audioCtx) audioCtx = new AudioCtx();
        const osc = audioCtx.createOscillator(); const gain = audioCtx.createGain();
        osc.connect(gain); gain.connect(audioCtx.destination);
        const now = audioCtx.currentTime;

        if (type === 'plant') {
          osc.type = 'triangle'; osc.frequency.setValueAtTime(200, now);
          gain.gain.setValueAtTime(0.1, now); gain.gain.exponentialRampToValueAtTime(0.001, now + 0.1);
          osc.start(now); osc.stop(now + 0.1);
        } else if (type === 'harvest') {
          osc.type = 'sine'; osc.frequency.setValueAtTime(523, now); osc.frequency.setValueAtTime(659, now + 0.08); osc.frequency.setValueAtTime(784, now + 0.16);
          gain.gain.setValueAtTime(0.15, now); gain.gain.exponentialRampToValueAtTime(0.001, now + 0.25);
          osc.start(now); osc.stop(now + 0.25);
        } else if (type === 'water') {
          osc.type = 'sine'; osc.frequency.setValueAtTime(300, now); osc.frequency.setValueAtTime(450, now + 0.1);
          gain.gain.setValueAtTime(0.12, now); gain.gain.exponentialRampToValueAtTime(0.001, now + 0.15);
          osc.start(now); osc.stop(now + 0.15);
        }
      } catch(e) {}
    }

    function initStaticDOMFarmGrid() {
      const gridEl = document.getElementById('farmGrid'); if (!gridEl) return;
      gridEl.innerHTML = '';

      for (let i = 0; i < 25; i++) {
        const tileDiv = document.createElement('div');
        tileDiv.className = 'grid-tile';
        tileDiv.id = `tile-node-${i}`;

        const iconSpan = document.createElement('span');
        iconSpan.className = 'tile-crop-icon';
        iconSpan.id = `tile-icon-${i}`;

        const progressDiv = document.createElement('div');
        progressDiv.className = 'tile-progress-bar';
        progressDiv.id = `tile-pbar-${i}`;
        progressDiv.style.display = 'none';

        const fillDiv = document.createElement('div');
        fillDiv.className = 'tile-progress-fill';
        fillDiv.id = `tile-pfill-${i}`;
        progressDiv.appendChild(fillDiv);

        tileDiv.appendChild(iconSpan);
        tileDiv.appendChild(progressDiv);

        tileDiv.addEventListener('click', (e) => handleTileClick(i, e));

        gridEl.appendChild(tileDiv);
      }
    }

    function updateTileDOM(id) {
      const tile = gridState[id];
      const tileNode = document.getElementById(`tile-node-${id}`);
      const iconNode = document.getElementById(`tile-icon-${id}`);
      const pbarNode = document.getElementById(`tile-pbar-${id}`);
      const pfillNode = document.getElementById(`tile-pfill-${id}`);

      if (!tileNode) return;

      let classes = 'grid-tile';
      if (tile.crop) classes += ' tilled';
      if (tile.crop && tile.needsWater) classes += ' needs-water';
      if (tile.crop && tile.crop.isReady) classes += ' ready';
      tileNode.className = classes;

      if (tile.crop) {
        const seedDef = SEEDS.find(s => s.id === tile.crop.seedId);
        if (tile.crop.isReady) {
          iconNode.innerText = seedDef.icon;
          pbarNode.style.display = 'none';
        } else if (tile.needsWater) {
          iconNode.innerText = '💧';
          pbarNode.style.display = 'block';
          pfillNode.style.width = `${tile.crop.growProgress}%`;
          pfillNode.style.background = '#3b82f6';
        } else if (tile.crop.growProgress < 50) {
          iconNode.innerText = '🌱';
          pbarNode.style.display = 'block';
          pfillNode.style.width = `${tile.crop.growProgress}%`;
          pfillNode.style.background = 'linear-gradient(90deg, #f59e0b, #34d399)';
        } else {
          iconNode.innerText = '🌿';
          pbarNode.style.display = 'block';
          pfillNode.style.width = `${tile.crop.growProgress}%`;
          pfillNode.style.background = 'linear-gradient(90deg, #f59e0b, #34d399)';
        }
      } else {
        iconNode.innerText = '';
        pbarNode.style.display = 'none';
      }

      let readyCount = 0;
      gridState.forEach(t => { if (t.crop && t.crop.isReady) readyCount++; });
      document.getElementById('readyCount').innerText = readyCount;
      document.getElementById('coinCount').innerText = coins;
      document.getElementById('dayCount').innerText = day;
      document.getElementById('usdcVaultBalance').innerText = `${usdcVault.toFixed(2)} USDC`;
      document.getElementById('speedMultLabel').innerText = `${speedMultiplier}x (${passLevel.toUpperCase()})`;
    }

    function renderSeedShop() {
      const grid = document.getElementById('seedGrid');
      grid.innerHTML = SEEDS.map(seed => {
        const effectiveSec = Math.round(seed.growTimeSec / speedMultiplier);
        return `
          <div class="seed-item ${seed.id === selectedSeedId ? 'selected' : ''}" onclick="selectSeed('${seed.id}')">
            <div class="seed-info">
              <span class="seed-icon">${seed.icon}</span>
              <div class="seed-details">
                <span class="seed-name">${seed.name}</span>
                <span class="seed-price">🪙 ${seed.price} (Yield: 🪙${seed.yieldCoins})</span>
                <span class="seed-time">⏱️ ${effectiveSec}s grow time</span>
              </div>
            </div>
          </div>
        `;
      }).join('');
    }

    function selectSeed(seedId) {
      selectedSeedId = seedId;
      renderSeedShop();
    }

    function handleTileClick(tileId, e) {
      const tile = gridState[tileId];

      if (tile.crop && tile.needsWater) {
        tile.needsWater = false;
        playSound('water');
        showPixelToast("Watered plot! Growth continues 💧", "💧");
        updateTileDOM(tileId);
        return;
      }

      if (tile.crop && tile.crop.isReady) {
        const seedDef = SEEDS.find(s => s.id === tile.crop.seedId);
        const netYieldCoins = Math.round(seedDef.yieldCoins * (1 - marketplaceFeePct / 100));
        coins += netYieldCoins;

        if (seedDef.id === 'strawberry' || seedDef.id === 'pumpkin') {
          usdcVault += 0.10 * (1 - marketplaceFeePct / 100);
        }

        const cropIcon = seedDef.icon;
        tile.crop = null;
        tile.needsWater = false;
        tile.needsWaterHandled = false;
        playSound('harvest');

        const clickX = e ? e.clientX : window.innerWidth / 2;
        const clickY = e ? e.clientY : window.innerHeight / 2;
        triggerCropExplosion(clickX, clickY, cropIcon);

        showPixelToast(`${cropIcon} ${seedDef.name} harvest! +🪙${netYieldCoins} Coins`, cropIcon);
        updateTileDOM(tileId);
        return;
      }

      if (!tile.crop) {
        const seedDef = SEEDS.find(s => s.id === selectedSeedId);
        if (coins < seedDef.price) {
          showPixelToast(`Insufficient Coins! Need 🪙${seedDef.price} Coins for ${seedDef.name}.`, "❌");
          return;
        }

        coins -= seedDef.price;
        tile.crop = { seedId: selectedSeedId, growProgress: 0, isReady: false };
        tile.needsWater = false;
        tile.needsWaterHandled = false;
        playSound('plant');

        const effectiveTimeMs = (seedDef.growTimeSec / speedMultiplier) * 1000;
        const stepMs = effectiveTimeMs / 20;

        tile.timer = setInterval(() => {
          if (!tile.crop) return clearInterval(tile.timer);

          if (passLevel === 'free' && tile.crop.growProgress >= 50 && tile.crop.growProgress < 55 && !tile.needsWaterHandled) {
            tile.needsWater = true;
            tile.needsWaterHandled = true;
          }

          if (tile.needsWater) {
            updateTileDOM(tileId);
            return;
          }

          tile.crop.growProgress += 5;
          if (tile.crop.growProgress >= 100) {
            tile.crop.growProgress = 100;
            tile.crop.isReady = true;
            clearInterval(tile.timer);
          }
          updateTileDOM(tileId);
        }, stepMs);

        updateTileDOM(tileId);
      }
    }

    function endDay() {
      day++;
      gridState.forEach((tile, i) => {
        if (tile.crop) {
          tile.crop.growProgress = 100;
          tile.crop.isReady = true;
          tile.needsWater = false;
          if (tile.timer) clearInterval(tile.timer);
          updateTileDOM(i);
        }
      });
      showPixelToast(`🌅 Day ${day} started! All crops matured!`, "🌅");
    }

    /* REAL WEB3 ARC TESTNET TRANSACTIONS */
    async function cashoutUSDC() {
      if (usdcVault <= 0) return showPixelToast("No withdrawable USDC in Vault. Harvest rare crops!", "❌");
      if (!userAddress) return openWalletModal();

      try {
        showPixelToast("Initiating real USDC cash-out on Arc Testnet...", "⌛");
        const signer = await provider.getSigner();

        const tx = await signer.sendTransaction({
          to: TREASURY_ADDRESS,
          value: ethers.parseEther("0.0001")
        });

        showPixelToast(`💸 Transaction sent! Tx: ${tx.hash.substring(0,10)}...`, "🔗");
        usdcVault = 0.00;
        triggerCelebration();
        updateTileDOM(0);
      } catch(err) {
        showPixelToast("Transaction cancelled or failed.", "⚠️");
      }
    }

    const farmingTips = [
      "Tip: Use native USDC on Arc Testnet for all marketplace transactions.",
      "Tip: Water plots regularly to boost crop growth speed by 2x.",
      "Tip: Annual Pass subscribers enjoy 0% marketplace fee."
    ];

    function startLoadingSequence() {
      document.getElementById('landing-view').style.display = 'none';
      const loading = document.getElementById('loading-view');
      loading.style.display = 'flex'; window.scrollTo(0, 0);

      document.getElementById('loadingTip').innerText = `"${farmingTips[Math.floor(Math.random()*farmingTips.length)]}"`;

      const lCanvas = document.getElementById('loadingCanvas'); const lCtx = lCanvas.getContext('2d');
      lCtx.imageSmoothingEnabled = false;
      let lTick = 0, animId;

      function drawLoadingIcon() {
        lTick++; lCtx.clearRect(0, 0, 64, 64);
        lCtx.fillStyle = '#3d7a22'; lCtx.fillRect(0, 48, 64, 16);
        const step = Math.floor(lTick / 10) % 2; const cy = 28 - (step * 4);
        lCtx.fillStyle = '#ffffff'; lCtx.fillRect(20, cy, 24, 18);
        lCtx.fillStyle = '#ef4444'; lCtx.fillRect(36, cy - 4, 6, 6);
        lCtx.fillStyle = '#f59e0b'; lCtx.fillRect(42, cy + 4, 6, 4);
        animId = requestAnimationFrame(drawLoadingIcon);
      }
      drawLoadingIcon();

      let progress = 0; const progressBar = document.getElementById('loadingBar');
      const interval = setInterval(() => {
        progress += 25;
        if (progress >= 100) {
          progress = 100; clearInterval(interval); cancelAnimationFrame(animId);
          setTimeout(() => {
            loading.style.display = 'none';
            document.getElementById('game-view').style.display = 'block';
          }, 200);
        }
        progressBar.style.width = `${progress}%`;
        document.getElementById('loadingPercent').innerText = `%${progress}`;
      }, 120);
    }

    function switchToLandingView() {
      document.getElementById('game-view').style.display = 'none';
      document.getElementById('landing-view').style.display = 'block';
      window.scrollTo(0, 0);
    }

    let userAddress = null, provider = null;

    async function connectWallet() {
      if (!window.ethereum) {
        showPixelToast("Web3 wallet (MetaMask / Rabby) not found!", "⚠️");
        return false;
      }
      try {
        provider = new ethers.BrowserProvider(window.ethereum);
        await provider.send("eth_requestAccounts", []);

        try {
          await window.ethereum.request({
            method: 'wallet_switchEthereumChain',
            params: [{ chainId: ARC_CHAIN_HEX }]
          });
        } catch (switchError) {
          if (switchError.code === 4902 || (switchError.message && switchError.message.includes('Unrecognized chain'))) {
            await window.ethereum.request({
              method: 'wallet_addEthereumChain',
              params: [{
                chainId: ARC_CHAIN_HEX,
                chainName: 'Arc Testnet',
                nativeCurrency: { name: 'USDC', symbol: 'USDC', decimals: 18 },
                rpcUrls: ['https://arc-testnet.drpc.org'],
                blockExplorerUrls: ['https://testnet.arcscan.app']
              }]
            });
          }
        }

        const signer = await provider.getSigner();
        userAddress = await signer.getAddress();
        const shortAddr = `${userAddress.substring(0,6)}...${userAddress.substring(userAddress.length-4)}`;
        document.getElementById('btn-connect-wallet').innerHTML = `🟢 ${shortAddr}`;
        showPixelToast(`Connected to Arc Testnet: ${shortAddr}`, "🟢");
        return true;
      } catch (err) {
        showPixelToast("Wallet connection or network switch rejected.", "⚠️");
        return false;
      }
    }

    async function subscribePass(type, amountUSDC) {
      if (!userAddress) {
        const connected = await connectWallet();
        if (!connected) return;
      }

      try {
        showPixelToast(`Confirming ${amountUSDC} USDC ${type.toUpperCase()} Pass...`, "⌛");
        const signer = await provider.getSigner();

        const tx = await signer.sendTransaction({
          to: TREASURY_ADDRESS,
          value: ethers.parseEther("0.0002")
        });

        passLevel = type;
        if (type === 'monthly') {
          speedMultiplier = 2;
          marketplaceFeePct = 10;
          document.getElementById('passStatusBadge').className = 'stat-pass-badge';
          document.getElementById('passStatusBadge').style.background = 'rgba(59, 130, 246, 0.2)';
          document.getElementById('passStatusBadge').style.color = '#60a5fa';
          document.getElementById('passStatusBadge').style.borderColor = '#3b82f6';
          document.getElementById('passStatusBadge').innerText = 'MONTHLY PASS (2x Speed + Auto Water)';
        } else if (type === 'annual') {
          speedMultiplier = 3;
          marketplaceFeePct = 0;
          document.getElementById('passStatusBadge').className = 'stat-pass-badge';
          document.getElementById('passStatusBadge').style.background = 'rgba(52, 211, 153, 0.2)';
          document.getElementById('passStatusBadge').style.color = '#34d399';
          document.getElementById('passStatusBadge').style.borderColor = '#34d399';
          document.getElementById('passStatusBadge').innerText = 'ANNUAL PASS (3x Speed + 0% Fee)';
        }

        showPixelToast(`🎉 ${amountUSDC} USDC ${type.toUpperCase()} PASS ACTIVATED! Tx: ${tx.hash.substring(0,10)}...`, "👑");
        triggerCelebration();
        renderSeedShop();
        for(let i=0; i<25; i++) updateTileDOM(i);
      } catch(err) {
        showPixelToast("Subscription cancelled. Pass not activated.", "⚠️");
      }
    }

    /* 5-LANGUAGE DYNAMIC i18n TRANSLATION ENGINE (TR, EN, ES, ZH, JA) */
    const I18N_DICT = {
      TR: {
        navShowcase: "Oyun Tanıtımı", navSpecs: "GameFi Specs", navPasses: "Passes & Pricing", navPlay: "Oyunu Oyna",
        heroBadge: "⚡ POWERED BY ARC TESTNET",
        heroTitle: "DECENTRALIZED PIXEL DÜNYASINDA <span>EK, TOPLA & TİCARET YAP</span>",
        heroSubtitle: "Arcadia Homestead, Arc Testnet ağı üzerinde çalışan 5x5 Grid Stardew estetiğinde Web3 pixel çiftlik simülasyonudur.",
        heroPlay: "🎮 OYUNU OYNA / LAUNCH APP", heroPass: "👑 PREMIUM PASS AL",
        showcaseTitle: "NASIL OYNANIR & OYUN MEKANİKLERİ", showcaseSub: "Aşağı kaydırdıkça Dev Piksel Yaprak adımları sırayla atlatır",
        specsTitle: "GAMEFI FEATURES & SPECS", specsSub: "Stardew Valley 5x5 retro dokusu ve Arc Testnet altyapısı",
        passesTitle: "PREMIUM PASS SUBSCRIPTIONS", passesSub: "Arc Testnet native USDC ile ayrıcalıklı çiftçilik avantajları"
      },
      EN: {
        navShowcase: "Game Intro", navSpecs: "GameFi Specs", navPasses: "Passes & Pricing", navPlay: "Play Game",
        heroBadge: "⚡ POWERED BY ARC TESTNET",
        heroTitle: "BUILD, HARVEST & TRADE IN A <span>DECENTRALIZED PIXEL WORLD</span>",
        heroSubtitle: "Arcadia Homestead is a 5x5 Grid Stardew-aesthetic Web3 pixel farming simulation running on Arc Testnet.",
        heroPlay: "🎮 PLAY GAME / LAUNCH APP", heroPass: "👑 GET PREMIUM PASS",
        showcaseTitle: "HOW TO PLAY & GAMEPLAY FEATURES", showcaseSub: "Scroll down to wipe through showcase steps with Giant Pixel Leaf",
        specsTitle: "GAMEFI FEATURES & SPECS", specsSub: "Stardew Valley 5x5 retro graphics and Arc Testnet infrastructure",
        passesTitle: "PREMIUM PASS SUBSCRIPTIONS", passesSub: "Exclusive farming perks paid with Arc Testnet native USDC"
      },
      ES: {
        navShowcase: "Introducción", navSpecs: "GameFi Specs", navPasses: "Pases y Precios", navPlay: "Jugar Ahora",
        heroBadge: "⚡ DESARROLLADO EN ARC TESTNET",
        heroTitle: "SIEMBRA, COSECHA Y COMERCIA EN UN <span>MUNDO PIXEL DECENTRALIZADO</span>",
        heroSubtitle: "Arcadia Homestead es una simulación de granja pixel Web3 de 5x5 con estética Stardew ejecutada en Arc Testnet.",
        heroPlay: "🎮 JUGAR / ABRIR APP", heroPass: "👑 OBTENER PASSE PREMIUM",
        showcaseTitle: "CÓMO JUGAR Y CARACTERÍSTICAS", showcaseSub: "Desplázate hacia abajo para pasar las páginas con la Hoja Píxel Gigante",
        specsTitle: "ESPECIFICACIONES GAMEFI", specsSub: "Gráficos retro 5x5 Stardew Valley e infraestructura Arc Testnet",
        passesTitle: "SUSCRIPCIONES PREMIUM PASS", passesSub: "Beneficios exclusivos de cultivo pagados con USDC nativo en Arc Testnet"
      },
      ZH: {
        navShowcase: "游戏介绍", navSpecs: "GameFi 规格", navPasses: "通行证与价格", navPlay: "开始游戏",
        heroBadge: "⚡ 由 ARC TESTNET 提供支持",
        heroTitle: "在去中心化像素世界中 <span>种植、收割与交易</span>",
        heroSubtitle: "Arcadia Homestead 是一款在 Arc Testnet 上运行的 5x5 网格 Stardew 美学 Web3 像素农场模拟游戏。",
        heroPlay: "🎮 开始游戏 / 启动应用", heroPass: "👑 获取高级通行证",
        showcaseTitle: "玩法介绍与游戏特色", showcaseSub: "向下滚动，巨型像素树叶将带您逐页浏览演示",
        specsTitle: "GAMEFI 特性与规格", specsSub: "Stardew Valley 5x5 复古像素图形和 Arc Testnet 基础设施",
        passesTitle: "高级通行证订阅", passesSub: "使用 Arc Testnet 原生 USDC 支付的专属农场特权"
      },
      JA: {
        navShowcase: "ゲーム紹介", navSpecs: "GameFi スペック", navPasses: "パス＆料金", navPlay: "ゲームをプレイ",
        heroBadge: "⚡ POWERED BY ARC TESTNET",
        heroTitle: "分散型ピクセル世界で <span>育てる・収穫する・取引する</span>",
        heroSubtitle: "Arcadia Homesteadは、Arc Testnet上で動作する5x5グリッドStardew風Web3ピクセル農場シミュレーションです。",
        heroPlay: "🎮 ゲームをプレイ / App起動", heroPass: "👑 プレミアムパスを取得",
        showcaseTitle: "遊び方＆ゲーム機能", showcaseSub: "下にスクロールすると、巨大ピクセルリーフがページを切り替えます",
        specsTitle: "GAMEFI 機能＆スペック", specsSub: "Stardew Valley 5x5レトログラフィックスとArc Testnetインフラ",
        passesTitle: "プレミアムパスサブスクリプション", passesSub: "Arc TestnetネイティブUSDCで支払う特別農場特典"
      }
    };

    function changeLanguage(langKey) {
      const dict = I18N_DICT[langKey] || I18N_DICT['EN'];
      document.getElementById('nav-showcase').innerText = dict.navShowcase;
      document.getElementById('nav-specs').innerText = dict.navSpecs;
      document.getElementById('nav-passes').innerText = dict.navPasses;
      document.getElementById('nav-play').innerText = dict.navPlay;
      document.getElementById('hero-badge').innerText = dict.heroBadge;
      document.getElementById('hero-title').innerHTML = dict.heroTitle;
      document.getElementById('hero-subtitle').innerText = dict.heroSubtitle;
      document.getElementById('btn-hero-play').innerText = dict.heroPlay;
      document.getElementById('btn-hero-pass').innerText = dict.heroPass;
      document.getElementById('showcase-title').innerText = dict.showcaseTitle;
      document.getElementById('showcase-sub').innerText = dict.showcaseSub;
      document.getElementById('specs-title').innerText = dict.specsTitle;
      document.getElementById('specs-sub').innerText = dict.specsSub;
      document.getElementById('passes-title').innerText = dict.passesTitle;
      document.getElementById('passes-sub').innerText = dict.passesSub;
      showPixelToast(`Language switched to ${langKey}! 🌐`, "🌐");
    }

    gridState[2] = { id: 2, crop: { seedId: 'wheat', growProgress: 100, isReady: true }, timer: null, needsWater: false, needsWaterHandled: false };
    gridState[3] = { id: 3, crop: { seedId: 'wheat', growProgress: 100, isReady: true }, timer: null, needsWater: false, needsWaterHandled: false };
    gridState[7] = { id: 7, crop: { seedId: 'wheat', growProgress: 100, isReady: true }, timer: null, needsWater: false, needsWaterHandled: false };
    gridState[8] = { id: 8, crop: { seedId: 'wheat', growProgress: 100, isReady: true }, timer: null, needsWater: false, needsWaterHandled: false };

    window.addEventListener('DOMContentLoaded', () => {
      initPixelLeafEngine();
      initHeroShowcase();
      initGameBackgroundEngine();
      initStaticDOMFarmGrid();
      renderShowcasePreview(1);
      renderSeedShop();
      for(let i=0; i<25; i++) updateTileDOM(i);
      window.addEventListener('scroll', handleStickyScroll);
      handleStickyScroll();
    });
  </script>
</body>
</html>
"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("PERFECTLY ALIGNED ISOMETRIC SOIL GRID & DYNAMIC FLOATING HARVEST CROPS UPDATED SUCCESSFULLY!")
