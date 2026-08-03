# Figma MCP Design System Rules

When using the Figma MCP Server (`https://mcp.figma.com/mcp`) to inspect or convert design frames into code:

1. **Pixel Art & Dark Mode Alignment**:
   - Translate Figma auto-layout frames into clean HTML5 Flexbox/Grid elements.
   - Retain retro pixel fonts (`'Press Start 2P'`, `'VT323'`) and pixelated border shadows (`box-shadow: 4px 4px 0px #000`).

2. **Asset Extraction**:
   - Extract design variables, colors, and typography directly from Figma node IDs.
   - Maintain 100% true alpha transparency for icons and sprites.

3. **Web3 Component Binding**:
   - Connect Figma button nodes directly to Ethers.js wallet triggers (`connectWallet()`, `subscribePass()`).
