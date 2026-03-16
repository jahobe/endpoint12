from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse, HTMLResponse
import uvicorn
import os

app = FastAPI(title="MasterDAO | Advanced Control Panel")

# ==========================================
# 1. WEB UI ANIMASI FULL (BOOT-UP & HOLOGRAM)
# ==========================================
@app.get("/", response_class=HTMLResponse)
def read_root():
    html_content = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>MasterDAO | System Terminal</title>
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Orbitron:wght@500;700&family=Space+Mono&display=swap');

            body {
                font-family: 'Space Mono', monospace;
                background-color: #030406;
                color: #b0bec5;
                margin: 0;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
                overflow: hidden;
            }

            /* --- ANIMASI BOOT-UP TERMINAL --- */
            #boot-screen {
                position: absolute;
                top: 0; left: 0; width: 100%; height: 100%;
                background-color: #030406;
                z-index: 9999;
                display: flex;
                flex-direction: column;
                justify-content: center;
                padding-left: 10%;
                color: #4ADE80;
                font-size: 1.2rem;
                transition: opacity 1s ease-out;
            }

            .typewriter-text {
                overflow: hidden;
                white-space: nowrap;
                border-right: .15em solid #4ADE80;
                margin: 0;
                width: 0;
            }

            @keyframes typing {
                from { width: 0 }
                to { width: 100% }
            }
            @keyframes blink-caret {
                from, to { border-color: transparent }
                50% { border-color: #4ADE80; }
            }

            /* --- UI UTAMA --- */
            #main-ui {
                opacity: 0;
                transform: scale(0.9);
                transition: all 1.5s cubic-bezier(0.16, 1, 0.3, 1);
                display: flex;
                justify-content: center;
                align-items: center;
                width: 100%; height: 100%;
                position: relative;
            }

            #main-ui.visible {
                opacity: 1;
                transform: scale(1);
            }

            #particles-js { position: absolute; width: 100%; height: 100%; z-index: 0; }

            /* Panel Mengambang */
            .panel {
                background: rgba(15, 23, 42, 0.6);
                backdrop-filter: blur(12px);
                padding: 50px;
                border-radius: 24px;
                box-shadow: 0 0 50px rgba(56, 189, 248, 0.1);
                text-align: center;
                border: 1px solid rgba(56, 189, 248, 0.4);
                max-width: 450px;
                width: 100%;
                z-index: 1;
                position: relative;
                overflow: hidden;
                animation: float 6s ease-in-out infinite;
            }

            @keyframes float {
                0% { transform: translateY(0px); }
                50% { transform: translateY(-15px); }
                100% { transform: translateY(0px); }
            }

            /* Garis Scanner Hologram */
            .scanline {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 5px;
                background: linear-gradient(to bottom, rgba(56, 189, 248, 0), rgba(56, 189, 248, 0.8), rgba(56, 189, 248, 0));
                box-shadow: 0 0 15px rgba(56, 189, 248, 0.8);
                opacity: 0.6;
                animation: scanning 3s linear infinite;
                z-index: 10;
                pointer-events: none;
            }

            @keyframes scanning {
                0% { top: -10%; }
                100% { top: 110%; }
            }

            .logo-container { position: relative; display: inline-block; margin-bottom: 20px; }
            .logo { font-size: 4.5rem; }
            .logo-glow {
                position: absolute; top: 0; left: 0; width: 100%; height: 100%;
                background: radial-gradient(circle, rgba(56, 189, 248, 0.6) 0%, rgba(56, 189, 248, 0) 70%);
                border-radius: 50%;
                animation: pulseGlow 2s infinite alternate;
                z-index: -1;
            }

            @keyframes pulseGlow {
                0% { transform: scale(1); opacity: 0.5; }
                100% { transform: scale(1.3); opacity: 0.9; }
            }

            h1 {
                font-family: 'Orbitron', sans-serif;
                color: #e0f2fe;
                margin: 15px 0;
                font-size: 2.2rem;
                letter-spacing: 3px;
                text-shadow: 0 0 15px #38bdf8;
            }

            p { color: #94a3b8; letter-spacing: 1px; }

            .status-container { display: flex; justify-content: center; align-items: center; margin-top: 25px; }
            .status-indicator {
                width: 14px; height: 14px; background-color: #4ade80; border-radius: 50%; margin-right: 12px;
                box-shadow: 0 0 15px #4ade80;
                animation: blink 1s infinite alternate;
            }

            @keyframes blink {
                0% { opacity: 0.4; box-shadow: 0 0 5px #4ade80; }
                100% { opacity: 1; box-shadow: 0 0 20px #4ade80; }
            }

            .status-text { color: #4ade80; font-weight: bold; letter-spacing: 2px; }
            .info-line { height: 1px; background: linear-gradient(to right, transparent, rgba(56, 189, 248, 0.5), transparent); margin: 30px 0; }
            .footer { font-size: 0.75rem; color: #64748b; }
        </style>
    </head>
    <body>

        <div id="boot-screen">
            <p class="typewriter-text" style="animation: typing 1s steps(30, end) forwards;">> INITIATING MASTERDAO PROTOCOL...</p>
            <p class="typewriter-text" style="animation: typing 1s steps(30, end) 1s forwards; width: 0;">> ESTABLISHING SECURE CONNECTION TO BASE NETWORK...</p>
            <p class="typewriter-text" style="animation: typing 1s steps(30, end) 2s forwards, blink-caret .75s step-end infinite; width: 0;">> BYPASSING FIREWALL... SUCCESS!</p>
        </div>

        <div id="main-ui">
            <div id="particles-js"></div>
            <div class="panel">
                <div class="scanline"></div>
                <div class="logo-container">
                    <div class="logo">🛰️</div>
                    <div class="logo-glow"></div>
                </div>
                <h1>MasterDAO</h1>
                <p>Advanced MCP Node</p>
                <div class="info-line"></div>
                <div class="status-container">
                    <div class="status-indicator"></div>
                    <div class="status-text">NODE ONLINE // SYNCED</div>
                </div>
                <div class="info-line"></div>
                <div class="footer">
                    AWAITING INSTRUCTIONS FROM ERC-8004 SMART CONTRACT
                </div>
            </div>
        </div>

        <script src="https://cdn.jsdelivr.net/particles.js/2.0.0/particles.min.js"></script>
        <script>
            // Logika transisi Boot-up ke Main UI
            setTimeout(() => {
                const bootScreen = document.getElementById('boot-screen');
                const mainUi = document.getElementById('main-ui');
                
                bootScreen.style.opacity = '0';
                setTimeout(() => {
                    bootScreen.style.display = 'none';
                    mainUi.classList.add('visible');
                }, 1000);
            }, 3500);

            // Efek Partikel
            particlesJS("particles-js", {
                "particles": {
                    "number": { "value": 60, "density": { "enable": true, "value_area": 800 } },
                    "color": { "value": "#38bdf8" },
                    "shape": { "type": "circle" },
                    "opacity": { "value": 0.5, "random": true },
                    "size": { "value": 3, "random": true },
                    "line_linked": { "enable": true, "distance": 150, "color": "#38bdf8", "opacity": 0.2, "width": 1 },
                    "move": { "enable": true, "speed": 1.5, "direction": "top", "random": true, "out_mode": "out" }
                },
                "interactivity": {
                    "detect_on": "canvas",
                    "events": { "onhover": { "enable": true, "mode": "repulse" }, "onclick": { "enable": true, "mode": "push" } },
                    "modes": { "repulse": { "distance": 100, "duration": 0.4 } }
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
        content={"status": "Healthy", "message": "MCP Endpoint Active"}
    )

@app.post("/mcp/{agent_id}")
async def mcp_receive_command(agent_id: str, request: Request):
    try:
        req_data = await request.json()
        
        req_id = req_data.get("id", 1)
        method = req_data.get("method", "")
        
        print(f"[*] Agent {agent_id} received request method: {method}")

        result_data = {}

        if method == "initialize":
            result_data = {
                "protocolVersion": "2024-11-05",
                "capabilities": {
                    "tools": {},
                    "prompts": {},
                    "resources": {}
                },
                "serverInfo": {
                    "name": "MasterDAO Node",
                    "version": "1.0.0"
                }
            }
            
        elif method == "tools/list":
            result_data = {
                "tools": [
                    {
                        "name": "analyze_wallet",
                        "description": "Analyze wallet addresses and transaction history on the Base network.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "address": {"type": "string", "description": "Target 0x wallet address"}
                            },
                            "required": ["address"]
                        }
                    },
                    {
                        "name": "get_token_price",
                        "description": "Fetch real-time price and liquidity data for ERC-20 tokens on decentralized exchanges.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "contract_address": {"type": "string", "description": "Token smart contract address"}
                            },
                            "required": ["contract_address"]
                        }
                    },
                    {
                        "name": "check_contract_security",
                        "description": "Scan smart contracts for common vulnerabilities such as reentrancy or overflow.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "contract_address": {"type": "string", "description": "Smart contract address to audit"}
                            },
                            "required": ["contract_address"]
                        }
                    },
                    {
                        "name": "monitor_whale_activity",
                        "description": "Track large transactions and whale movements for specific assets.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "token_symbol": {"type": "string", "description": "Token symbol (e.g., ETH, USDC)"},
                                "min_amount": {"type": "number", "description": "Minimum transaction value in USD"}
                            },
                            "required": ["token_symbol", "min_amount"]
                        }
                    },
                    {
                        "name": "calculate_yield_roi",
                        "description": "Calculate projected Return on Investment (ROI) and Impermanent Loss for DeFi staking pools.",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "pool_id": {"type": "string", "description": "Identifier of the liquidity pool"},
                                "deposit_amount": {"type": "number", "description": "Amount to deposit"}
                            },
                            "required": ["pool_id", "deposit_amount"]
                        }
                    }
                ]
            }
            
        elif method == "prompts/list":
            result_data = {
                "prompts": [
                    {
                        "name": "generate_audit_report",
                        "description": "Generate comprehensive Web3 smart contract audit and security reports."
                    },
                    {
                        "name": "explain_defi_strategy",
                        "description": "Provide a step-by-step breakdown of a specific yield farming strategy on the Base network."
                    },
                    {
                        "name": "summarize_dao_proposal",
                        "description": "Summarize the key points, risks, and potential impact of an active DAO governance proposal."
                    }
                ]
            }
            
        # 4. KITA TAMBAHKAN RESOURCES DI SINI!
        elif method == "resources/list":
            result_data = {
                "resources": [
                    {
                        "uri": "file:///data/base_network_stats.json",
                        "name": "Base Network Statistics",
                        "description": "Real-time statistics of the Base blockchain including TPS, gas fees, and active addresses.",
                        "mimeType": "application/json"
                    },
                    {
                        "uri": "file:///docs/masterdao_security_guidelines.md",
                        "name": "MasterDAO Security Guidelines",
                        "description": "Standard operating procedures and security checklists for DeFi smart contract audits.",
                        "mimeType": "text/markdown"
                    }
                ]
            }
            
        else:
            result_data = {"status": "success", "message": f"Command received for {agent_id}"}

        response_payload = {
            "jsonrpc": "2.0",
            "id": req_id,
            "result": result_data
        }
        
        return JSONResponse(status_code=200, content=response_payload)

    except Exception as e:
        return JSONResponse(status_code=200, content={
            "jsonrpc": "2.0",
            "id": None,
            "error": {"code": -32700, "message": "Parse error"}
        })

if __name__ == "__main__":
    import os
    port = int(os.environ.get("PORT", 8000))
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=port)
