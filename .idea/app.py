from flask import Flask, request, render_template_string, send_file
import io

app = Flask(__name__)

# =========================================================
# HTML COM TODAS AS FUNCIONALIDADES
# =========================================================
HTML = """
<!doctype html>
<html lang="pt-br">
<head>
<meta charset="utf-8">
<title>Mini-CAM Nanxing</title>
<style>
* { box-sizing: border-box; margin: 0; padding: 0; }
body { 
    font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif; 
    background: hsl(220, 20%, 10%); 
    color: hsl(210, 20%, 95%);
    min-height: 100vh;
}
.header {
    background: hsla(220, 18%, 13%, 0.8);
    backdrop-filter: blur(10px);
    border-bottom: 1px solid hsl(220, 14%, 22%);
    padding: 16px 24px;
    position: sticky;
    top: 0;
    z-index: 100;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.header-title {
    display: flex;
    align-items: center;
    gap: 12px;
}
.header-icon {
    width: 40px;
    height: 40px;
    background: hsla(199, 89%, 48%, 0.2);
    border-radius: 8px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: hsl(199, 89%, 48%);
}
.header h1 { font-size: 18px; font-weight: 600; }
.header p { font-size: 12px; color: hsl(215, 15%, 55%); }
.container { 
    max-width: 1600px; 
    margin: 0 auto; 
    padding: 24px;
    display: grid;
    grid-template-columns: 380px 1fr;
    gap: 24px;
}
@media (max-width: 1024px) {
    .container { grid-template-columns: 1fr; }
}
.section {
    background: hsl(220, 18%, 13%);
    border: 1px solid hsl(220, 14%, 22%);
    border-radius: 8px;
    padding: 20px;
    margin-bottom: 16px;
}
.section-title {
    font-size: 14px;
    font-weight: 600;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
    color: hsl(210, 20%, 95%);
}
.section-title svg { color: hsl(199, 89%, 48%); }
label { 
    display: block; 
    font-size: 11px;
    font-weight: 500;
    color: hsl(215, 15%, 55%);
    text-transform: uppercase;
    letter-spacing: 0.5px;
    margin-bottom: 6px;
}
input, select { 
    width: 100%; 
    padding: 10px 12px;
    background: hsl(220, 14%, 18%);
    border: 1px solid hsl(220, 14%, 22%);
    border-radius: 6px;
    color: hsl(210, 20%, 95%);
    font-family: 'JetBrains Mono', monospace;
    font-size: 14px;
    transition: all 0.2s;
}
input:focus, select:focus {
    outline: none;
    border-color: hsl(199, 89%, 48%);
    box-shadow: 0 0 0 3px hsla(199, 89%, 48%, 0.2);
}
.row { 
    display: grid; 
    grid-template-columns: 1fr 1fr; 
    gap: 16px; 
}
.form-group { margin-bottom: 16px; }
.mode-buttons {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 12px;
}
.mode-btn {
    padding: 16px;
    border-radius: 8px;
    border: 2px solid hsl(220, 14%, 22%);
    background: transparent;
    cursor: pointer;
    transition: all 0.2s;
    text-align: left;
}
.mode-btn:hover { border-color: hsl(215, 15%, 55%); }
.mode-btn.active-desbaste { 
    border-color: hsl(0, 72%, 51%); 
    background: hsla(0, 72%, 51%, 0.1);
}
.mode-btn.active-sangramento { 
    border-color: hsl(210, 100%, 50%); 
    background: hsla(210, 100%, 50%, 0.1);
}
.mode-btn-content {
    display: flex;
    align-items: center;
    gap: 12px;
}
.mode-indicator {
    width: 12px;
    height: 12px;
    border-radius: 50%;
}
.mode-indicator.desbaste { background: hsl(0, 72%, 51%); }
.mode-indicator.sangramento { background: hsl(210, 100%, 50%); }
.mode-btn-text { color: hsl(210, 20%, 95%); }
.mode-btn-text span { display: block; font-size: 14px; font-weight: 500; }
.mode-btn-text small { font-size: 12px; color: hsl(215, 15%, 55%); }

/* Controles de visualização */
.slider-container { margin-bottom: 16px; }
.slider-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 8px;
}
.slider-value {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: hsl(215, 15%, 55%);
}
input[type="range"] {
    -webkit-appearance: none;
    width: 100%;
    height: 8px;
    background: hsl(220, 14%, 18%);
    border-radius: 4px;
    border: none;
    padding: 0;
}
input[type="range"]::-webkit-slider-thumb {
    -webkit-appearance: none;
    width: 16px;
    height: 16px;
    background: hsl(199, 89%, 48%);
    border-radius: 50%;
    cursor: pointer;
    box-shadow: 0 2px 8px hsla(199, 89%, 48%, 0.4);
}
.toggle-buttons {
    display: flex;
    gap: 12px;
}
.toggle-btn {
    flex: 1;
    padding: 12px;
    border-radius: 8px;
    border: 1px solid hsl(220, 14%, 22%);
    background: transparent;
    color: hsl(215, 15%, 55%);
    cursor: pointer;
    transition: all 0.2s;
    font-size: 14px;
    font-weight: 500;
}
.toggle-btn.active-margin {
    border-color: hsl(45, 100%, 50%);
    background: hsla(45, 100%, 50%, 0.1);
    color: hsl(45, 100%, 50%);
}
.toggle-btn.active-grid {
    border-color: hsl(199, 89%, 48%);
    background: hsla(199, 89%, 48%, 0.1);
    color: hsl(199, 89%, 48%);
}

/* Botões principais */
.btn-primary {
    background: hsl(199, 89%, 48%);
    color: hsl(220, 20%, 10%);
    border: none;
    padding: 14px 24px;
    border-radius: 8px;
    font-size: 14px;
    font-weight: 600;
    cursor: pointer;
    transition: all 0.2s;
    box-shadow: 0 4px 12px hsla(199, 89%, 48%, 0.3);
}
.btn-primary:hover { opacity: 0.9; transform: translateY(-1px); }
.btn-primary:active { transform: scale(0.98); }

/* Preview */
.preview-container {
    background: hsl(220, 20%, 8%);
    border: 1px solid hsl(220, 14%, 22%);
    border-radius: 8px;
    overflow: hidden;
}
.preview-header {
    padding: 12px 16px;
    border-bottom: 1px solid hsl(220, 14%, 22%);
    display: flex;
    justify-content: space-between;
    align-items: center;
}
.preview-label {
    font-size: 12px;
    font-weight: 500;
    color: hsl(215, 15%, 55%);
}
.badge {
    display: inline-flex;
    padding: 4px 8px;
    border-radius: 4px;
    font-size: 11px;
    font-weight: 600;
}
.badge-desbaste {
    background: hsla(0, 72%, 51%, 0.2);
    color: hsl(0, 72%, 51%);
}
.badge-sangramento {
    background: hsla(210, 100%, 50%, 0.2);
    color: hsl(210, 100%, 50%);
}
.preview-dimensions {
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: hsl(215, 15%, 55%);
}
.preview-svg {
    display: block;
    width: 100%;
    height: 450px;
}
.status-bar {
    background: hsla(220, 14%, 18%, 0.5);
    border-top: 1px solid hsl(220, 14%, 22%);
    padding: 8px 16px;
    display: flex;
    justify-content: space-between;
    font-family: 'JetBrains Mono', monospace;
    font-size: 12px;
    color: hsl(215, 15%, 55%);
}
.status-bar span { margin-right: 16px; }
.status-bar .value { color: hsl(210, 20%, 95%); }

/* XML Preview */
.xml-preview {
    background: hsl(220, 14%, 18%);
    border-radius: 8px;
    padding: 16px;
    max-height: 300px;
    overflow: auto;
}
.xml-preview pre {
    font-family: 'JetBrains Mono', monospace;
    font-size: 11px;
    color: hsl(215, 15%, 55%);
    white-space: pre-wrap;
    word-break: break-all;
}

/* Error */
.error-box {
    background: hsla(0, 72%, 51%, 0.05);
    border: 1px solid hsla(0, 72%, 51%, 0.5);
    border-radius: 8px;
    padding: 16px;
    color: hsl(0, 72%, 51%);
    display: flex;
    align-items: center;
    gap: 12px;
}

/* Footer */
.footer {
    border-top: 1px solid hsl(220, 14%, 22%);
    margin-top: 32px;
    padding: 16px 24px;
}
.footer-content {
    max-width: 1600px;
    margin: 0 auto;
    display: flex;
    justify-content: space-between;
    font-size: 12px;
    color: hsl(215, 15%, 55%);
}
</style>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet">
</head>
<body>

<header class="header">
    <div class="header-title">
        <div class="header-icon">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <rect x="4" y="4" width="16" height="16" rx="2"/>
                <rect x="9" y="9" width="6" height="6"/>
                <line x1="9" y1="1" x2="9" y2="4"/><line x1="15" y1="1" x2="15" y2="4"/>
                <line x1="9" y1="20" x2="9" y2="23"/><line x1="15" y1="20" x2="15" y2="23"/>
                <line x1="20" y1="9" x2="23" y2="9"/><line x1="20" y1="14" x2="23" y2="14"/>
                <line x1="1" y1="9" x2="4" y2="9"/><line x1="1" y1="14" x2="4" y2="14"/>
            </svg>
        </div>
        <div>
            <h1>Mini-CAM Nanxing</h1>
            <p>Gerador de XML para Centro de Usinagem</p>
        </div>
    </div>
    {% if xml %}
    <form method="post" action="/download" style="margin:0;">
        <input type="hidden" name="xml" value="{{xml|e}}">
        {% for k,v in p.items() %}
        <input type="hidden" name="{{k}}" value="{{v}}">
        {% endfor %}
        <button type="submit" class="btn-primary">⬇ Baixar XML</button>
    </form>
    {% endif %}
</header>

<form method="post">
<div class="container">
    <!-- Painel Esquerdo -->
    <div class="left-panel">
        
        <!-- Dimensões da Chapa -->
        <div class="section">
            <div class="section-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/>
                </svg>
                Dimensões da Chapa
            </div>
            <div class="row">
                <div class="form-group">
                    <label>Altura (Y)</label>
                    <input name="altura" type="number" value="{{p.altura or 600}}" required>
                </div>
                <div class="form-group">
                    <label>Largura (X)</label>
                    <input name="largura" type="number" value="{{p.largura or 800}}" required>
                </div>
            </div>
            <div class="row">
                <div class="form-group">
                    <label>Espessura</label>
                    <input name="espessura" type="number" step="0.1" value="{{p.espessura or 18}}" required>
                </div>
                <div class="form-group">
                    <label>Espessura Final</label>
                    <input name="esp_final" type="number" step="0.1" value="{{p.esp_final or 15}}" required>
                </div>
            </div>
        </div>

        <!-- Ferramenta -->
        <div class="section">
            <div class="section-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-2 2 2 2 0 0 1-2-2v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1-2-2 2 2 0 0 1 2-2h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 2-2 2 2 0 0 1 2 2v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 2 2 2 2 0 0 1-2 2h-.09a1.65 1.65 0 0 0-1.51 1z"/>
                </svg>
                Ferramenta
            </div>
            <div class="row">
                <div class="form-group">
                    <label>Diâmetro da Fresa</label>
                    <input name="diametro" type="number" step="0.1" value="{{p.diametro or 12}}" required>
                </div>
                <div class="form-group">
                    <label>Passes Z</label>
                    <input name="passes" type="number" value="{{p.passes or 3}}" min="1" required>
                </div>
            </div>
            <div class="row">
                <div class="form-group">
                    <label>Espaçamento (Sangramento)</label>
                    <input name="espacamento" type="number" step="0.1" value="{{p.espacamento or 5}}">
                </div>
                <div class="form-group">
                    <label>Margem Extra Sangramento</label>
                    <input name="margem_sangra" type="number" step="0.1" value="{{p.margem_sangra or 5}}">
                </div>
            </div>
        </div>

        <!-- Margens de Usinagem -->
        <div class="section">
            <div class="section-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <line x1="3" y1="12" x2="21" y2="12"/><polyline points="8 8 4 12 8 16"/><polyline points="16 16 20 12 16 8"/>
                </svg>
                Margens de Usinagem
            </div>
            <div class="row">
                <div class="form-group">
                    <label>Margem Esquerda</label>
                    <input name="margem_esq" type="number" step="0.1" value="{{p.margem_esq or 20}}">
                </div>
                <div class="form-group">
                    <label>Margem Direita</label>
                    <input name="margem_dir" type="number" step="0.1" value="{{p.margem_dir or 20}}">
                </div>
            </div>
            <div class="row">
                <div class="form-group">
                    <label>Margem Superior</label>
                    <input name="margem_sup" type="number" step="0.1" value="{{p.margem_sup or 20}}">
                </div>
                <div class="form-group">
                    <label>Margem Inferior</label>
                    <input name="margem_inf" type="number" step="0.1" value="{{p.margem_inf or 20}}">
                </div>
            </div>
        </div>

        <!-- Modo de Operação -->
        <div class="section">
            <div class="section-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polygon points="12 2 2 7 12 12 22 7 12 2"/><polyline points="2 17 12 22 22 17"/><polyline points="2 12 12 17 22 12"/>
                </svg>
                Modo de Operação
            </div>
            <div class="mode-buttons">
                <label class="mode-btn {{'active-desbaste' if (p.modo or 'desbaste') == 'desbaste' else ''}}">
                    <input type="radio" name="modo" value="desbaste" style="display:none" {{'checked' if (p.modo or 'desbaste') == 'desbaste' else ''}}>
                    <div class="mode-btn-content">
                        <div class="mode-indicator desbaste"></div>
                        <div class="mode-btn-text">
                            <span>Desbaste</span>
                            <small>Remoção contínua</small>
                        </div>
                    </div>
                </label>
                <label class="mode-btn {{'active-sangramento' if p.modo == 'sangramento' else ''}}">
                    <input type="radio" name="modo" value="sangramento" style="display:none" {{'checked' if p.modo == 'sangramento' else ''}}>
                    <div class="mode-btn-content">
                        <div class="mode-indicator sangramento"></div>
                        <div class="mode-btn-text">
                            <span>Sangramento</span>
                            <small>Cortes espaçados</small>
                        </div>
                    </div>
                </label>
            </div>
        </div>

        <!-- Controles de Visualização -->
        <div class="section">
            <div class="section-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <path d="M1 12s4-8 11-8 11 8 11 8-4 8-11 8-11-8-11-8z"/><circle cx="12" cy="12" r="3"/>
                </svg>
                Controles de Visualização
            </div>
            <div class="slider-container">
                <div class="slider-header">
                    <label style="margin:0">Área da Fresa</label>
                    <span class="slider-value" id="opacity-value">{{(p.toolpath_opacity or 0.25)|float * 100|int}}%</span>
                </div>
                <input type="range" name="toolpath_opacity" min="0" max="1" step="0.05" 
                       value="{{p.toolpath_opacity or 0.25}}" 
                       oninput="document.getElementById('opacity-value').textContent = Math.round(this.value*100)+'%'">
            </div>
            <div class="toggle-buttons">
                <label class="toggle-btn {{'active-margin' if (p.show_margins or 'on') == 'on' else ''}}">
                    <input type="checkbox" name="show_margins" style="display:none" {{'checked' if (p.show_margins or 'on') == 'on' else ''}}>
                    ⬜ Margens
                </label>
                <label class="toggle-btn {{'active-grid' if (p.show_grid or 'on') == 'on' else ''}}">
                    <input type="checkbox" name="show_grid" style="display:none" {{'checked' if (p.show_grid or 'on') == 'on' else ''}}>
                    # Grid
                </label>
            </div>
        </div>

        <button type="submit" class="btn-primary" style="width:100%">▶ Gerar Preview</button>
    </div>

    <!-- Painel Direito -->
    <div class="right-panel">
        {% if error %}
        <div class="error-box">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <circle cx="12" cy="12" r="10"/><line x1="12" y1="8" x2="12" y2="12"/><line x1="12" y1="16" x2="12.01" y2="16"/>
            </svg>
            {{error}}
        </div>
        {% endif %}

        {{preview|safe}}

        {% if xml %}
        <div class="section" style="margin-top:16px;">
            <div class="section-title">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                    <polygon points="5 3 19 12 5 21 5 3"/>
                </svg>
                XML Gerado
            </div>
            <div class="xml-preview">
                <pre>{{xml}}</pre>
            </div>
        </div>
        {% endif %}
    </div>
</div>
</form>

<footer class="footer">
    <div class="footer-content">
        <span>Mini-CAM Nanxing v1.0</span>
        <span>Compatível com Nanxing FCC</span>
    </div>
</footer>

<script>
// Auto-update radio button styles
document.querySelectorAll('input[name="modo"]').forEach(radio => {
    radio.addEventListener('change', function() {
        document.querySelectorAll('.mode-btn').forEach(btn => {
            btn.classList.remove('active-desbaste', 'active-sangramento');
        });
        if (this.checked) {
            this.closest('.mode-btn').classList.add('active-' + this.value);
        }
    });
});

// Toggle buttons
document.querySelectorAll('.toggle-btn input[type="checkbox"]').forEach(cb => {
    cb.addEventListener('change', function() {
        if (this.name === 'show_margins') {
            this.closest('.toggle-btn').classList.toggle('active-margin', this.checked);
        } else if (this.name === 'show_grid') {
            this.closest('.toggle-btn').classList.toggle('active-grid', this.checked);
        }
    });
});
</script>

</body>
</html>
"""

# =========================================================
# SVG PREVIEW COMPLETO
# =========================================================
def gerar_svg_preview(w, h, linhas, params, x_ini, x_fim, y_ini, y_fim):
    modo = params.get('modo', 'desbaste')
    diam = float(params.get('diametro', 12))
    m_esq = float(params.get('margem_esq', 20))
    m_dir = float(params.get('margem_dir', 20))
    m_sup = float(params.get('margem_sup', 20))
    m_inf = float(params.get('margem_inf', 20))
    toolpath_opacity = float(params.get('toolpath_opacity', 0.25))
    show_margins = params.get('show_margins') == 'on'
    show_grid = params.get('show_grid') == 'on'

    # Cores por modo
    if modo == 'sangramento':
        stroke_color = 'hsl(210, 100%, 50%)'
        toolpath_color = f'hsla(210, 100%, 50%, {toolpath_opacity})'
        badge_class = 'badge-sangramento'
        badge_text = 'SANGRAMENTO'
    else:
        stroke_color = 'hsl(0, 72%, 51%)'
        toolpath_color = f'hsla(0, 72%, 51%, {toolpath_opacity})'
        badge_class = 'badge-desbaste'
        badge_text = 'DESBASTE'

    margin_color = 'hsl(45, 100%, 50%)'
    padding = 40

    svg_elements = []

    # Grid
    if show_grid:
        for i in range(0, int(w) + 1, 50):
            svg_elements.append(
                f'<line x1="{i}" y1="0" x2="{i}" y2="{h}" stroke="hsl(220, 14%, 20%)" stroke-width="0.5" stroke-dasharray="4,4"/>'
            )
        for i in range(0, int(h) + 1, 50):
            svg_elements.append(
                f'<line x1="0" y1="{i}" x2="{w}" y2="{i}" stroke="hsl(220, 14%, 20%)" stroke-width="0.5" stroke-dasharray="4,4"/>'
            )

    # Chapa
    svg_elements.append(
        f'<rect x="0" y="0" width="{w}" height="{h}" fill="hsl(220, 18%, 15%)" stroke="hsl(220, 14%, 30%)" stroke-width="2"/>'
    )

    # Margens visuais
    if show_margins:
        # Margem esquerda
        svg_elements.append(
            f'<rect x="0" y="0" width="{m_esq}" height="{h}" fill="hsla(45, 100%, 50%, 0.15)" stroke="{margin_color}" stroke-width="1" stroke-dasharray="4,2"/>'
        )
        # Margem direita
        svg_elements.append(
            f'<rect x="{w - m_dir}" y="0" width="{m_dir}" height="{h}" fill="hsla(45, 100%, 50%, 0.15)" stroke="{margin_color}" stroke-width="1" stroke-dasharray="4,2"/>'
        )
        # Margem superior
        svg_elements.append(
            f'<rect x="{m_esq}" y="0" width="{w - m_esq - m_dir}" height="{m_sup}" fill="hsla(45, 100%, 50%, 0.15)" stroke="{margin_color}" stroke-width="1" stroke-dasharray="4,2"/>'
        )
        # Margem inferior
        svg_elements.append(
            f'<rect x="{m_esq}" y="{h - m_inf}" width="{w - m_esq - m_dir}" height="{m_inf}" fill="hsla(45, 100%, 50%, 0.15)" stroke="{margin_color}" stroke-width="1" stroke-dasharray="4,2"/>'
        )
        # Labels
        svg_elements.append(
            f'<text x="{m_esq/2}" y="{h/2}" fill="{margin_color}" font-size="10" text-anchor="middle" transform="rotate(-90, {m_esq/2}, {h/2})">{int(m_esq)}mm</text>'
        )
        svg_elements.append(
            f'<text x="{w - m_dir/2}" y="{h/2}" fill="{margin_color}" font-size="10" text-anchor="middle" transform="rotate(90, {w - m_dir/2}, {h/2})">{int(m_dir)}mm</text>'
        )
        svg_elements.append(
            f'<text x="{w/2}" y="{m_sup/2 + 3}" fill="{margin_color}" font-size="10" text-anchor="middle">{int(m_sup)}mm</text>'
        )
        svg_elements.append(
            f'<text x="{w/2}" y="{h - m_inf/2 + 3}" fill="{margin_color}" font-size="10" text-anchor="middle">{int(m_inf)}mm</text>'
        )

    # Área de usinagem
    area_x = x_ini - diam/2
    area_y = max(0, y_ini - diam/2)
    area_w = x_fim - x_ini + diam
    area_h = min(h, y_fim) - max(0, y_ini) + diam
    svg_elements.append(
        f'<rect x="{area_x}" y="{h - area_y - area_h}" width="{area_w}" height="{area_h}" fill="none" stroke="hsl(160, 84%, 39%)" stroke-width="1" stroke-dasharray="8,4" opacity="0.5"/>'
    )

    # Toolpath com área da fresa
    if toolpath_opacity > 0:
        for x1, y1, x2, y2 in linhas:
            svg_elements.append(
                f'<line x1="{x1}" y1="{h-y1}" x2="{x2}" y2="{h-y2}" stroke="{toolpath_color}" stroke-width="{diam}" stroke-linecap="round" stroke-linejoin="round"/>'
            )

    # Linha central
    for x1, y1, x2, y2 in linhas:
        svg_elements.append(
            f'<line x1="{x1}" y1="{h-y1}" x2="{x2}" y2="{h-y2}" stroke="{stroke_color}" stroke-width="1.5" stroke-linecap="round"/>'
        )

    # Ponto inicial
    svg_elements.append(
        f'<circle cx="{x_ini}" cy="{h-y_ini}" r="4" fill="hsl(160, 84%, 39%)" stroke="white" stroke-width="1"/>'
    )

    # Dimensões
    svg_elements.append(
        f'<text x="{w/2}" y="-15" fill="hsl(215, 15%, 55%)" font-size="10" text-anchor="middle" font-family="JetBrains Mono, monospace">{int(w)} mm</text>'
    )
    svg_elements.append(
        f'<text x="-15" y="{h/2}" fill="hsl(215, 15%, 55%)" font-size="10" text-anchor="middle" font-family="JetBrains Mono, monospace" transform="rotate(-90, -15, {h/2})">{int(h)} mm</text>'
    )

    # Origem
    svg_elements.append(f'<line x1="-20" y1="{h}" x2="20" y2="{h}" stroke="hsl(160, 84%, 39%)" stroke-width="1"/>')
    svg_elements.append(f'<line x1="0" y1="{h-20}" x2="0" y2="{h+20}" stroke="hsl(160, 84%, 39%)" stroke-width="1"/>')
    svg_elements.append(f'<text x="8" y="{h+15}" fill="hsl(160, 84%, 39%)" font-size="10">0,0</text>')

    # Calcular estatísticas
    esp = float(params.get('espessura', 18))
    esp_final = float(params.get('esp_final', 15))
    passes = int(params.get('passes', 3))
    prof_total = esp - esp_final

    return f"""
<div class="preview-container">
    <div class="preview-header">
        <div style="display:flex;align-items:center;gap:12px;">
            <span class="preview-label">PREVIEW</span>
            <span class="badge {badge_class}">{badge_text}</span>
        </div>
        <span class="preview-dimensions">{int(w)} x {int(h)} mm</span>
    </div>
    <svg viewBox="-{padding} -{padding} {w + padding*2} {h + padding*2}" class="preview-svg">
        {''.join(svg_elements)}
    </svg>
    <div class="status-bar">
        <div>
            <span>Linhas: <span class="value">{len(linhas)}</span></span>
            <span>Passes Z: <span class="value">{passes}</span></span>
            <span>Prof. total: <span class="value">{prof_total:.1f}mm</span></span>
        </div>
        <div>Ferramenta: <span class="value">fr{int(diam)}</span></div>
    </div>
</div>
"""


# =========================================================
# MOTOR CAM (CORRIGIDO)
# =========================================================
def gerar_xml(p):
    altura = float(p['altura'])
    largura = float(p['largura'])
    esp = float(p['espessura'])
    esp_final = float(p['esp_final'])
    diam = float(p['diametro'])
    passes = int(p['passes'])
    espac = float(p.get('espacamento', 5))
    margem_sangra = float(p.get('margem_sangra', 5))
    modo = p.get('modo', 'desbaste')

    m_esq = float(p.get('margem_esq', 20))
    m_dir = float(p.get('margem_dir', 20))
    m_sup = float(p.get('margem_sup', 20))
    m_inf = float(p.get('margem_inf', 20))

    raio = diam / 2

    # Limites de usinagem - CORRIGIDO para cobertura total
    x_ini = m_esq + raio
    x_fim = largura - m_dir - raio

    if modo == "sangramento":
        y_ini = -(raio + margem_sangra)
        y_fim = altura + (raio + margem_sangra)
    else:
        y_ini = m_inf + raio
        y_fim = altura - m_sup - raio

    # Validação de área
    if x_ini >= x_fim or y_ini >= y_fim:
        raise ValueError("Margens inválidas: não sobra área usinável")

    remover = esp - esp_final
    prof = remover / passes
    z_passes = [round(esp - prof * (i + 1), 2) for i in range(passes)]

    preview = []
    machines = []
    lid = 1
    mid = 10

    for z in z_passes:
        lines = []
        x = x_ini
        y = y_ini
        direcao = 1

        # CORRIGIDO: Loop que garante cobertura total
        while x <= x_fim:
            y_dest = y_fim if direcao == 1 else y_ini

            # Linha vertical
            lines.append(f'<Line LineID="{lid}" EndX="{x:.2f}" EndY="{y_dest:.2f}" EndZ="{z}"/>')
            preview.append((x, y, x, y_dest))
            lid += 1
            y = y_dest

            # Calcula próximo X
            if modo == "sangramento":
                x2 = x + diam + espac
            else:
                x2 = x + diam

            # Se próximo ponto está além do limite, para
            if x2 > x_fim + raio:
                break

            # Linha horizontal de conexão
            x2_clamped = min(x2, x_fim)
            lines.append(f'<Line LineID="{lid}" EndX="{x2_clamped:.2f}" EndY="{y:.2f}" EndZ="{z}"/>')
            preview.append((x, y, x2_clamped, y))
            lid += 1
            x = x2

            direcao *= -1

        machines.append(f"""
<Machining ID="{mid}" Type="3" IsArea="false" AreaType="0"
IsGenCode="2" IsGenCodeOld="2" Face="5"
X="{x_ini:.2f}" Y="{y_ini:.2f}" Z="{z}" Depth="{prof:.2f}"
ToolName="fr{int(diam)}" ToolOffset="中" EdgeABThickness="0">
<Lines>
{''.join(lines)}
</Lines>
</Machining>
""")
        mid += 1

    xml = f"""<?xml version="1.0"?>
<Root ApplicationVersion="2.0">
<Project Name="AUTO_NANXING">
<Panels>
<Panel ID="AUTO001" Name="AUTO" Material="MDF"
Thickness="{esp}" Length="{largura}" Width="{altura}"
CutLength="{largura}" CutWidth="{altura}" Qty="1"
MachiningPoint="1" Type="1" Grain="N" Memo="">
<Machines>
{''.join(machines)}
</Machines>

<EdgeGroup X1="0" Y1="0">
<Edge Face="1" Thickness="0" Pre_Milling="0" X="0" Y="0" CentralAngle="0"/>
<Edge Face="2" Thickness="0" Pre_Milling="0" X="0" Y="0" CentralAngle="0"/>
<Edge Face="3" Thickness="0" Pre_Milling="0" X="0" Y="0" CentralAngle="0"/>
<Edge Face="4" Thickness="0" Pre_Milling="0" X="0" Y="0" CentralAngle="0"/>
</EdgeGroup>

</Panel>
</Panels>
</Project>
</Root>
"""

    svg = gerar_svg_preview(largura, altura, preview, p, x_ini, x_fim, y_ini, y_fim)
    return xml, svg


# =========================================================
# NOME AUTOMÁTICO
# =========================================================
def gerar_nome(p):
    nome = f"{p.get('modo', 'desbaste').upper()}_{int(float(p['altura']))}x{int(float(p['largura']))}"
    nome += f"_Z{p['passes']}_F{int(float(p['diametro']))}"
    if p.get('modo') == "sangramento":
        nome += f"_E{int(float(p.get('espacamento', 5)))}"
    return nome + ".xml"


# =========================================================
# ROTAS
# =========================================================
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            # Processar checkboxes
            form_data = request.form.to_dict()
            form_data['show_margins'] = 'on' if 'show_margins' in request.form else 'off'
            form_data['show_grid'] = 'on' if 'show_grid' in request.form else 'off'
            
            xml, svg = gerar_xml(form_data)
            return render_template_string(HTML, preview=svg, xml=xml, p=form_data, error=None)
        except Exception as e:
            form_data = request.form.to_dict()
            form_data['show_margins'] = 'on' if 'show_margins' in request.form else 'off'
            form_data['show_grid'] = 'on' if 'show_grid' in request.form else 'off'
            return render_template_string(HTML, preview="", xml=None, p=form_data, error=str(e))
    
    # Valores padrão
    default_p = {
        'altura': 600, 'largura': 800, 'espessura': 18, 'esp_final': 15,
        'diametro': 12, 'passes': 3, 'espacamento': 5, 'margem_sangra': 5,
        'margem_esq': 20, 'margem_dir': 20, 'margem_sup': 20, 'margem_inf': 20,
        'modo': 'desbaste', 'toolpath_opacity': 0.25, 'show_margins': 'on', 'show_grid': 'on'
    }
    return render_template_string(HTML, preview="", xml=None, p=default_p, error=None)


@app.route("/download", methods=["POST"])
def download():
    xml = request.form["xml"]
    nome = gerar_nome(request.form)
    return send_file(
        io.BytesIO(xml.encode()),
        as_attachment=True,
        download_name=nome,
        mimetype="application/xml"
    )


if __name__ == "__main__":
    app.run(debug=True)
