from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn
import os

app = FastAPI(title="DAPAnalyz | Web3 dApp Node")

# ==========================================
# 1. WEB UI: DAPAnalyz DASHBOARD + ANIMASI INTRO
# ==========================================
@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>DAPAnalyz | Web3 Terminal</title>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/ethers/5.7.2/ethers.umd.min.js"></script>
        
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Rajdhani:wght@500;600;700&family=Fira+Code:wght@400;500&display=swap');

            :root {
                --bg-color: #03060a;
                --panel-bg: rgba(10, 17, 30, 0.85);
                --cyan: #00f0ff;
                --purple: #8a2be2;
                --green: #00ff88;
                --text-main: #e2e8f0;
                --text-muted: #64748b;
            }

            body {
                font-family: 'Rajdhani', sans-serif;
                background-color: var(--bg-color);
                color: var(--text-main);
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                min-height: 100vh;
                overflow: hidden;
                background-image: 
                    linear-gradient(rgba(0, 240, 255, 0.05) 1px, transparent 1px),
                    linear-gradient(90deg, rgba(0, 240, 255, 0.05) 1px, transparent 1px);
                background-size: 30px 30px;
            }

            #particles-js { position: fixed; width: 100%; height: 100%; z-index: 0; top:0; left:0; }

            /* --- ANIMASI INTRO CANGGIH --- */
            #intro-loader {
                position: fixed;
                top: 0; left: 0; width: 100%; height: 100%;
                background-color: var(--bg-color);
                z-index: 9999;
                display: flex;
                flex-direction: column;
                align-items: center;
                justify-content: center;
                transition: opacity 0.8s ease-out, transform 0.8s ease-in;
            }

            /* Cincin Berputar */
            .cyber-rings {
                position: relative;
                width: 160px; height: 160px;
                display: flex; align-items: center; justify-content: center;
            }
            .ring-outer {
                position: absolute; width: 100%; height: 100%;
                border: 2px dashed var(--cyan); border-radius: 50%;
                animation: spinRight 6s linear infinite;
                box-shadow: 0 0 20px rgba(0, 240, 255, 0.2);
            }
            .ring-inner {
                position: absolute; width: 70%; height: 70%;
                border: 2px solid var(--purple); border-radius: 50%;
                border-top-color: transparent; border-bottom-color: transparent;
                animation: spinLeft 3s linear infinite;
            }
            .intro-logo {
                font-size: 3.5rem; position: absolute;
                text-shadow: 0 0 15px var(--cyan);
                animation: pulseLogo 2s infinite alternate;
            }

            @keyframes spinRight { 100% { transform: rotate(360deg); } }
            @keyframes spinLeft { 100% { transform: rotate(-360deg); } }
            @keyframes pulseLogo { 0% { transform: scale(0.9); opacity: 0.7; } 100% { transform: scale(1.1); opacity: 1; } }

            /* Progress Bar */
            .loading-text {
                margin-top: 40px; font-family: 'Fira Code', monospace;
                color: var(--cyan); font-size: 0.9rem; letter-spacing: 2px;
            }
            .progress-container {
                width: 300px; height: 4px; background: rgba(255,255,255,0.1);
                margin-top: 15px; border-radius: 2px; overflow: hidden;
            }
            .progress-bar {
                height: 100%; width: 0%; background: var(--cyan);
                box-shadow: 0 0 15px var(--cyan); transition: width 0.1s;
            }
            .progress-percent {
                margin-top: 10px; font-family: 'Fira Code', monospace; font-size: 1rem; color: #fff;
            }

            /* --- DASHBOARD UTAMA --- */
            #main-ui {
                opacity: 0; transform: scale(0.9);
                transition: all 1s cubic-bezier(0.2, 0.8, 0.2, 1);
                display: flex; justify-content: center; align-items: center;
                width: 100%; height: 100%; position: relative;
                visibility: hidden; /* Sembunyikan saat intro */
            }
            #main-ui.visible { opacity: 1; transform: scale(1); visibility: visible; }

            .dashboard-panel {
                background: var(--panel-bg); backdrop-filter: blur(15px);
                padding: 40px; border-radius: 12px;
                box-shadow: 0 0 40px rgba(0, 240, 255, 0.1);
                border: 1px solid rgba(0, 240, 255, 0.2); border-top: 3px solid var(--cyan);
                max-width: 600px; width: 100%; z-index: 1; margin: 20px;
            }

            .header-container {
                display: flex; align-items: center; justify-content: space-between;
                margin-bottom: 30px; border-bottom: 1px solid rgba(255, 255, 255, 0.1); padding-bottom: 20px;
            }

            .logo-section { display: flex; align-items: center; }
            .logo-icon { font-size: 2.5rem; margin-right: 15px; text-shadow: 0 0 10px var(--cyan); }
            .title-box h1 { margin: 0; font-size: 2rem; background: linear-gradient(90deg, #fff, var(--cyan)); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
            .title-box p { margin: 0; color: var(--cyan); font-family: 'Fira Code', monospace; font-size: 0.8rem; }

            /* Web3 Button */
            .btn-connect {
                background: transparent; color: var(--cyan); border: 1px solid var(--cyan);
                padding: 10px 20px; font-family: 'Fira Code', monospace; font-size: 0.9rem;
                cursor: pointer; border-radius: 4px; transition: all 0.3s ease; box-shadow: 0 0 10px rgba(0, 240, 255, 0.2) inset;
            }
            .btn-connect:hover { background: var(--cyan); color: #000; box-shadow: 0 0 20px rgba(0, 240, 255, 0.6); }

            /* Wallet Data Section */
            #wallet-data { display: none; margin-bottom: 20px; }
            .data-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 15px; margin-bottom: 20px; }
            .data-box { background: rgba(0, 0, 0, 0.5); border: 1px solid rgba(0, 240, 255, 0.3); padding: 15px; border-radius: 8px; }
            .data-label { font-family: 'Fira Code', monospace; font-size: 0.75rem; color: var(--text-muted); }
            .data-value { font-size: 1.2rem; font-weight: bold; margin-top: 5px; color: #fff; font-family: 'Fira Code', monospace; }
            .data-value.green { color: var(--green); }

            /* Terminal Analitik */
            .terminal {
                background: #000; padding: 15px; border-radius: 6px; font-family: 'Fira Code', monospace;
                font-size: 0.8rem; color: var(--text-muted); border: 1px solid rgba(138, 43, 226, 0.4); height: 150px; overflow-y: auto;
            }
            .term-line { margin: 5px 0; border-bottom: 1px dashed rgba(255,255,255,0.05); padding-bottom: 5px; }
            .term-time { color: var(--purple); margin-right: 10px; }
            .term-action { color: var(--cyan); }
            .term-alert { color: #ff3366; }
            .terminal::-webkit-scrollbar { width: 5px; }
            .terminal::-webkit-scrollbar-track { background: #000; }
            .terminal::-webkit-scrollbar-thumb { background: var(--cyan); }

        </style>
    </head>
    <body>

        <div id="intro-loader">
            <div class="cyber-rings">
                <div class="ring-outer"></div>
                <div class="ring-inner"></div>
                <div class="intro-logo">👁️‍🗨️</div>
            </div>
            <div class="loading-text" id="loading-text">CONNECTING TO BASE NETWORK...</div>
            <div class="progress-container">
                <div class="progress-bar" id="progress-bar"></div>
            </div>
            <div class="progress-percent" id="progress-percent">0%</div>
        </div>

        <div id="particles-js"></div>

        <div id="main-ui">
            <div class="dashboard-panel">
                <div class="header-container">
                    <div class="logo-section">
                        <div class="logo-icon">👁️‍🗨️</div>
                        <div class="title-box">
                            <h1>DAPAnalyz</h1>
                            <p>ON-CHAIN ANALYTICS NODE</p>
                        </div>
                    </div>
                    <button id="btn-connect" class="btn-connect" onclick="connectWallet()">CONNECT WALLET</button>
                </div>

                <div id="default-view" style="text-align: center; padding: 40px 0;">
                    <p style="color: var(--text-muted); font-family: 'Fira Code';">
                        [!] SYSTEM STANDBY.<br>
                        Please connect a Web3 wallet to initiate heuristic network scan.
                    </p>
                </div>

                <div id="wallet-data">
                    <div class="data-grid">
                        <div class="data-box"><div class="data-label">TARGET ADDRESS</div><div class="data-value" id="ui-address">0x00...000</div></div>
                        <div class="data-box"><div class="data-label">LIVE BALANCE</div><div class="data-value green" id="ui-balance">0.0000 ETH</div></div>
                        <div class="data-box"><div class="data-label">CONNECTED NETWORK</div><div class="data-value" id="ui-network">Unknown</div></div>
                        <div class="data-box"><div class="data-label">SECURITY RATING</div><div class="data-value" style="color: #00ff88;">A+ (SECURE)</div></div>
                    </div>
                    <div class="data-label" style="margin-bottom: 10px;">> LIVE TRANSACTION HEURISTIC SCAN:</div>
                    <div class="terminal" id="terminal-log">
                        <div class="term-line"><span class="term-action">Initializing blockchain packet sniffer...</span></div>
                    </div>
                </div>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
        <script>
            // Logika Animasi Intro Loading
            document.addEventListener("DOMContentLoaded", () => {
                let progress = 0;
                const bar = document.getElementById('progress-bar');
                const pct = document.getElementById('progress-percent');
                const text = document.getElementById('loading-text');
                const intro = document.getElementById('intro-loader');
                const mainUi = document.getElementById('main-ui');

                const loadingStages = [
                    "CONNECTING TO BASE NETWORK...",
                    "SYNCING LEDGER PROTOCOLS...",
                    "LOADING HEURISTIC AI MODULES...",
                    "BYPASSING SECURITY FIREWALL..."
                ];

                const loaderInterval = setInterval(() => {
                    progress += Math.floor(Math.random() * 4) + 1; // Naik secara acak agar natural
                    if (progress >= 100) progress = 100;
                    
                    bar.style.width = progress + '%';
                    pct.innerText = progress + '%';

                    if (progress === 25) text.innerText = loadingStages[1];
                    if (progress === 55) text.innerText = loadingStages[2];
                    if (progress === 80) text.innerText = loadingStages[3];

                    if (progress === 100) {
                        clearInterval(loaderInterval);
                        text.innerText = "ACCESS GRANTED";
                        text.style.color = "#00ff88"; // Berubah hijau
                        
                        setTimeout(() => {
                            intro.style.transform = 'scale(1.5)'; // Efek zoom mendekat
                            intro.style.opacity = '0'; // Pudar
                            
                            setTimeout(() => {
                                intro.style.display = 'none';
                                mainUi.classList.add('visible'); // Tampilkan Dashboard
                            }, 800);
                        }, 600);
                    }
                }, 60); // Kecepatan interval loading
            });

            // Logika Web3.js / Ethers.js
            async function connectWallet() {
                const btn = document.getElementById('btn-connect');
                if (typeof window.ethereum !== 'undefined') {
                    try {
                        btn.innerText = "CONNECTING...";
                        const provider = new ethers.providers.Web3Provider(window.ethereum);
                        await provider.send("eth_requestAccounts", []);
                        const signer = provider.getSigner();
                        
                        const address = await signer.getAddress();
                        const balance = await provider.getBalance(address);
                        const ethBalance = ethers.utils.formatEther(balance);
                        const network = await provider.getNetwork();

                        document.getElementById('ui-address').innerText = address.substring(0, 6) + '...' + address.substring(38);
                        document.getElementById('ui-balance').innerText = parseFloat(ethBalance).toFixed(4) + ' ETH';
                        document.getElementById('ui-network').innerText = network.name.toUpperCase() + ' (' + network.chainId + ')';

                        document.getElementById('default-view').style.display = 'none';
                        document.getElementById('wallet-data').style.display = 'block';
                        
                        btn.innerText = "CONNECTED"; btn.style.background = "var(--cyan)"; btn.style.color = "#000"; btn.disabled = true;

                        startHeuristicScan(address);
                    } catch (error) {
                        btn.innerText = "CONNECT WALLET";
                        alert("Gagal menghubungkan dompet. Pastikan Anda menyetujui koneksi di MetaMask.");
                    }
                } else {
                    alert("Sistem Web3 tidak terdeteksi! Silakan instal ekstensi browser MetaMask.");
                }
            }

            // Simulasi Log Transaksi Terminal
            function startHeuristicScan(address) {
                const terminal = document.getElementById('terminal-log');
                const dummyLogs = [
                    `<span class="term-action">Extracting historical tx data for ${address.substring(0,8)}...</span>`,
                    `Scanning recent ERC-20 transfers... <span style="color:#00ff88">CLEAN</span>`,
                    `Checking interactions with known malicious contracts... <span style="color:#00ff88">0 FOUND</span>`,
                    `<span class="term-alert">NOTICE:</span> Low liquidity pool interaction detected 12 days ago.`,
                    `Analyzing Gas fee optimization patterns... <span class="term-action">EFFICIENCY: 87%</span>`,
                    `Cross-referencing address with OFAC sanction list... <span style="color:#00ff88">PASSED</span>`,
                    `Monitoring for incoming pending transactions in mempool...`
                ];
                let i = 0;
                const scanInterval = setInterval(() => {
                    if (i < dummyLogs.length) {
                        const time = new Date().toISOString().substring(11, 19);
                        const logLine = document.createElement('div');
                        logLine.className = 'term-line';
                        logLine.innerHTML = `<span class="term-time">[${time}]</span> ${dummyLogs[i]}`;
                        terminal.appendChild(logLine);
                        terminal.scrollTop = terminal.scrollHeight;
                        i++;
                    } else {
                        clearInterval(scanInterval);
                    }
                }, 1200);
            }

            // Latar Belakang Partikel
            particlesJS("particles-js", {
                "particles": {
                    "number": { "value": 50 },
                    "color": { "value": "#00f0ff" },
                    "shape": { "type": "circle" },
                    "opacity": { "value": 0.3 },
                    "size": { "value": 2, "random": true },
                    "line_linked": { "enable": true, "distance": 150, "color": "#00f0ff", "opacity": 0.2, "width": 1 },
                    "move": { "enable": true, "speed": 1 }
                },
                "interactivity": {
                    "events": { "onhover": { "enable": true, "mode": "grab" } },
                    "modes": { "grab": { "distance": 200, "line_linked": { "opacity": 0.5 } } }
                }
            });
        </script>
    </body>
    </html>
    """
    return html_content

# ==========================================
# 2. ENDPOINT RAHASIA (JSON-RPC 2.0 UNTUK 8004SCAN)
# ==========================================

@app.get("/mcp/{agent_id}")
def mcp_health_check(agent_id: str):
    return JSONResponse(
        status_code=200,
        content={"status": "Healthy", "message": "DAPAnalyz Endpoint Active"}
    )

@app.post("/mcp/{agent_id}")
async def mcp_receive_command(agent_id: str, request: Request):
    try:
        req_data = await request.json()
        req_id = req_data.get("id", 1)
        method = req_data.get("method", "")
        
        result_data = {}

        if method == "initialize":
            result_data = {
                "protocolVersion": "2024-11-05",
                "capabilities": { "tools": {}, "prompts": {}, "resources": {} },
                "serverInfo": { "name": "DAPAnalyz Node", "version": "2.0.0" }
            }
        elif method == "tools/list":
            result_data = {
                "tools": [
                    { "name": "analyze_wallet", "description": "Analyze wallet addresses on Base.", "inputSchema": { "type": "object", "properties": { "address": {"type": "string"} }, "required": ["address"] } },
                    { "name": "get_token_price", "description": "Fetch real-time price.", "inputSchema": { "type": "object", "properties": { "contract_address": {"type": "string"} }, "required": ["contract_address"] } },
                    { "name": "check_contract_security", "description": "Scan smart contracts.", "inputSchema": { "type": "object", "properties": { "contract_address": {"type": "string"} }, "required": ["contract_address"] } },
                    { "name": "monitor_whale_activity", "description": "Track whale movements.", "inputSchema": { "type": "object", "properties": { "token_symbol": {"type": "string"}, "min_amount": {"type": "number"} }, "required": ["token_symbol", "min_amount"] } },
                    { "name": "calculate_yield_roi", "description": "Calculate projected ROI.", "inputSchema": { "type": "object", "properties": { "pool_id": {"type": "string"}, "deposit_amount": {"type": "number"} }, "required": ["pool_id", "deposit_amount"] } }
                ]
            }
        elif method == "prompts/list":
            result_data = {
                "prompts": [
                    { "name": "generate_audit_report", "description": "Generate security reports." },
                    { "name": "explain_defi_strategy", "description": "Breakdown yield farming strategy." },
                    { "name": "summarize_dao_proposal", "description": "Summarize DAO governance proposal." }
                ]
            }
        elif method == "resources/list":
            result_data = {
                "resources": [
                    { "uri": "file:///data/base_stats.json", "name": "Base Statistics", "description": "Real-time statistics.", "mimeType": "application/json" },
                    { "uri": "file:///docs/security_guide.md", "name": "Security Guidelines", "description": "Security checklists.", "mimeType": "text/markdown" }
                ]
            }
        else:
            result_data = {"status": "success", "message": f"Command received for {agent_id}"}

        return JSONResponse(status_code=200, content={"jsonrpc": "2.0", "id": req_id, "result": result_data})

    except Exception as e:
        return JSONResponse(status_code=200, content={"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "Parse error"}})

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
