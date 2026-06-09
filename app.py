import streamlit as st
from datetime import datetime
from urllib.parse import urlparse

# ============================================================
# APP MADRE - PORTAL CLINICO IA DR. OLANO
# ============================================================
# Autor/Desarrollador: Dr. Ricardo Daniel Olano
# Especialidad: Cardiologia e Hipertension Arterial
# Objetivo: Portal madre para ingresar a diferentes apps web
# desarrolladas en Streamlit.
# ============================================================

st.set_page_config(
    page_title="Portal Clinico IA - Dr. Olano",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ============================================================
# CSS GENERAL
# ============================================================

CUSTOM_CSS = """
<style>
:root {
    --primary: #0f172a;
    --secondary: #1e3a8a;
    --accent: #0369a1;
    --bg-soft: #f8fafc;
    --border: #e2e8f0;
    --text-soft: #475569;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 2.35rem;
    font-weight: 900;
    color: var(--primary);
    letter-spacing: -0.03em;
    margin-bottom: 0.25rem;
}

.subtitle {
    font-size: 1.05rem;
    color: var(--text-soft);
    margin-bottom: 1.4rem;
}

.section-title {
    font-size: 1.35rem;
    font-weight: 800;
    color: var(--primary);
    margin-top: 0.5rem;
    margin-bottom: 0.8rem;
}

.hero-box {
    background: linear-gradient(135deg, #f8fafc 0%, #e0f2fe 100%);
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 26px;
    margin-bottom: 22px;
    box-shadow: 0 8px 26px rgba(15, 23, 42, 0.06);
}

.metric-box {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 18px;
    padding: 18px;
    text-align: center;
    box-shadow: 0 4px 14px rgba(15, 23, 42, 0.05);
}

.metric-value {
    font-size: 2rem;
    font-weight: 900;
    color: var(--secondary);
}

.metric-label {
    font-size: 0.92rem;
    color: #64748b;
}

.app-card {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 22px;
    min-height: 285px;
    margin-bottom: 18px;
    box-shadow: 0 5px 18px rgba(15, 23, 42, 0.055);
}

.app-title {
    font-size: 1.18rem;
    font-weight: 850;
    color: var(--primary);
    margin-bottom: 0.35rem;
}

.app-description {
    color: var(--text-soft);
    font-size: 0.94rem;
    line-height: 1.45;
    min-height: 88px;
    margin-top: 12px;
}

.badge {
    display: inline-block;
    padding: 4px 10px;
    border-radius: 999px;
    font-size: 0.76rem;
    font-weight: 800;
    margin-right: 5px;
    margin-top: 5px;
}

.badge-category {
    background: #e0f2fe;
    color: #075985;
}

.badge-active {
    background: #dcfce7;
    color: #166534;
}

.badge-dev {
    background: #fef9c3;
    color: #854d0e;
}

.badge-paused {
    background: #fee2e2;
    color: #991b1b;
}

.footer {
    color: #64748b;
    font-size: 0.86rem;
    margin-top: 28px;
    padding-top: 16px;
    border-top: 1px solid var(--border);
}

.login-box {
    background: #ffffff;
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 24px;
    box-shadow: 0 8px 24px rgba(15, 23, 42, 0.08);
}

.small-note {
    font-size: 0.85rem;
    color: #64748b;
}
</style>
"""

st.markdown(CUSTOM_CSS, unsafe_allow_html=True)

# ============================================================
# DATOS POR DEFECTO DE APPS HIJAS
# Se pueden editar desde .streamlit/secrets.toml
# ============================================================

DEFAULT_APPS = [
    {
        "id": "mapa",
        "nombre": "MAPA 24 horas",
        "descripcion": "Analisis de monitoreo ambulatorio de presion arterial, depuracion estadistica, fenotipo hipertensivo, patron circadiano e informe PDF.",
        "url": "https://TU-APP-MAPA.streamlit.app",
        "categoria": "Hipertension arterial",
        "estado": "Activa",
        "icono": "📈",
    },
    {
        "id": "cgi",
        "nombre": "Cardiografia de Impedancia",
        "descripcion": "Evaluacion hemodinamica no invasiva, patron circulatorio, ortostatismo, embarazo, volemia, contractilidad y acoplamiento ventriculo-arterial.",
        "url": "https://TU-APP-CGI.streamlit.app",
        "categoria": "Mecanica vascular",
        "estado": "Activa",
        "icono": "🫀",
    },
    {
        "id": "presion_central",
        "nombre": "Presion Central Olano",
        "descripcion": "Digitalizacion de curva de presion aortica central, calibracion, separacion de ondas, energia relativa, analisis espectral y edad vascular.",
        "url": "https://TU-APP-PRESION-CENTRAL.streamlit.app",
        "categoria": "Presion central",
        "estado": "En desarrollo",
        "icono": "〰️",
    },
    {
        "id": "vop",
        "nombre": "Velocidad de Onda de Pulso",
        "descripcion": "Analisis de rigidez arterial, VOP carotideofemoral, percentiles, edad vascular e integracion clinica.",
        "url": "https://TU-APP-VOP.streamlit.app",
        "categoria": "Rigidez arterial",
        "estado": "Activa",
        "icono": "⚡",
    },
    {
        "id": "ia_mv",
        "nombre": "Proceso IA MV",
        "descripcion": "Informe integrado de mecanica vascular con PAC, VOP y cardiografia de impedancia, graficos comparativos, fenotipo y sugerencia clinica.",
        "url": "https://TU-APP-IA-MV.streamlit.app",
        "categoria": "Integracion clinica",
        "estado": "En desarrollo",
        "icono": "🧠",
    },
    {
        "id": "riesgo_cv",
        "nombre": "Riesgo Cardiovascular",
        "descripcion": "Evaluacion preventiva con escalas de riesgo, dislipemia, objetivos terapeuticos y semaforizacion clinica.",
        "url": "https://TU-APP-RIESGO-CV.streamlit.app",
        "categoria": "Prevencion cardiovascular",
        "estado": "Activa",
        "icono": "🛡️",
    },
    {
        "id": "obesidad",
        "nombre": "Manejo Clinico de Obesidad",
        "descripcion": "Guia clinica para evaluacion de obesidad, IMC, indice cintura/talla, riesgo cardiometabolico y recomendaciones terapeuticas.",
        "url": "https://TU-APP-OBESIDAD.streamlit.app",
        "categoria": "Cardiometabolismo",
        "estado": "Activa",
        "icono": "⚖️",
    },
    {
        "id": "fa",
        "nombre": "Fibrilacion Auricular",
        "descripcion": "Manejo clinico y terapeutico de fibrilacion auricular, estratificacion de riesgo, anticoagulacion y control de frecuencia/ritmo.",
        "url": "https://TU-APP-FA.streamlit.app",
        "categoria": "Arritmias",
        "estado": "Activa",
        "icono": "💓",
    },
    {
        "id": "amiloidosis",
        "nombre": "Amiloidosis Cardiaca",
        "descripcion": "App de apoyo para sospecha, diagnostico, fenotipado y manejo clinico-terapeutico de amiloidosis cardiaca.",
        "url": "https://TU-APP-AMILOIDOSIS.streamlit.app",
        "categoria": "Cardiologia clinica",
        "estado": "Activa",
        "icono": "🧬",
    },
    {
        "id": "miocardiopatia_hipertrofica",
        "nombre": "Miocardiopatia Hipertrofica",
        "descripcion": "Evaluacion clinica y terapeutica de miocardiopatia hipertrofica, riesgo, seguimiento, estudios complementarios y conducta.",
        "url": "https://TU-APP-MCH.streamlit.app",
        "categoria": "Cardiologia clinica",
        "estado": "Activa",
        "icono": "🫀",
    },
]

# ============================================================
# FUNCIONES DE ESTADO Y SEGURIDAD
# ============================================================

def init_state():
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "usuario" not in st.session_state:
        st.session_state.usuario = None


def get_secret(section: str, key: str, default=None):
    try:
        return st.secrets.get(section, {}).get(key, default)
    except Exception:
        return default


def app_url_is_valid(url: str) -> bool:
    try:
        parsed = urlparse(url)
        return parsed.scheme in ["http", "https"] and parsed.netloc != ""
    except Exception:
        return False


def login_screen():
    st.markdown(
        """
        <div class="hero-box">
            <div class="main-title">Portal Clinico IA - Dr. Olano</div>
            <div class="subtitle">
                App madre para acceder a las herramientas web de hipertension arterial, mecanica vascular,
                cardiografia de impedancia, presion central, VOP y prevencion cardiovascular.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    col1, col2, col3 = st.columns([1, 1.15, 1])
    with col2:
        st.markdown('<div class="login-box">', unsafe_allow_html=True)
        st.subheader("Ingreso profesional")
        usuario = st.text_input("Usuario", placeholder="Ingrese usuario")
        password = st.text_input("Contrasena", type="password", placeholder="Ingrese contrasena")

        if st.button("Ingresar", use_container_width=True):
            admin_user = get_secret("auth", "admin_user", "admin")
            admin_password = get_secret("auth", "admin_password", "1234")

            if usuario == admin_user and password == admin_password:
                st.session_state.logged_in = True
                st.session_state.usuario = usuario
                st.rerun()
            else:
                st.error("Usuario o contrasena incorrectos.")

        st.markdown(
            "<div class='small-note'>Usuario inicial de prueba: admin / 1234. Cambiarlo en secrets.toml antes de publicar.</div>",
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
# CARGA DE APPS
# ============================================================

def load_apps():
    """
    Carga apps desde .streamlit/secrets.toml.
    Si no hay configuracion, usa DEFAULT_APPS.
    """
    apps_from_secrets = []

    try:
        apps_section = st.secrets.get("apps", {})
        for key, data in apps_section.items():
            apps_from_secrets.append(
                {
                    "id": key,
                    "nombre": data.get("nombre", key),
                    "descripcion": data.get("descripcion", ""),
                    "url": data.get("url", "#"),
                    "categoria": data.get("categoria", "General"),
                    "estado": data.get("estado", "Activa"),
                    "icono": data.get("icono", "🧩"),
                }
            )
    except Exception:
        apps_from_secrets = []

    return apps_from_secrets if apps_from_secrets else DEFAULT_APPS


def status_badge_class(estado: str) -> str:
    estado_l = estado.lower().strip()
    if estado_l in ["activa", "activo", "online", "produccion"]:
        return "badge badge-active"
    if estado_l in ["en desarrollo", "beta", "prototipo", "demo"]:
        return "badge badge-dev"
    return "badge badge-paused"


def render_app_card(app: dict):
    url = app.get("url", "#")
    url_ok = app_url_is_valid(url)

    st.markdown(
        f"""
        <div class="app-card">
            <div class="app-title">{app.get("icono", "🧩")} {app.get("nombre", "App")}</div>
            <span class="badge badge-category">{app.get("categoria", "General")}</span>
            <span class="{status_badge_class(app.get("estado", "Activa"))}">{app.get("estado", "Activa")}</span>
            <div class="app-description">{app.get("descripcion", "")}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if url_ok:
        st.link_button("Abrir app", url, use_container_width=True)
    else:
        st.button("URL pendiente", use_container_width=True, disabled=True)


# ============================================================
# DASHBOARD PRINCIPAL
# ============================================================

def dashboard():
    apps = load_apps()

    with st.sidebar:
        st.title("🫀 Portal IA")
        st.caption("Dr. Ricardo Daniel Olano")
        st.caption("Cardiologo Hipertensologo")
        st.divider()

        categorias = sorted(set(app.get("categoria", "General") for app in apps))
        categoria_sel = st.selectbox("Categoria", ["Todas"] + categorias)
        estado_sel = st.selectbox("Estado", ["Todos"] + sorted(set(app.get("estado", "Activa") for app in apps)))
        buscar = st.text_input("Buscar", placeholder="MAPA, VOP, presion central...")

        st.divider()
        st.caption(f"Usuario: {st.session_state.usuario}")
        if st.button("Cerrar sesion", use_container_width=True):
            st.session_state.logged_in = False
            st.session_state.usuario = None
            st.rerun()

    # Filtros
    filtered_apps = apps

    if categoria_sel != "Todas":
        filtered_apps = [app for app in filtered_apps if app.get("categoria") == categoria_sel]

    if estado_sel != "Todos":
        filtered_apps = [app for app in filtered_apps if app.get("estado") == estado_sel]

    if buscar:
        q = buscar.lower().strip()
        filtered_apps = [
            app for app in filtered_apps
            if q in app.get("nombre", "").lower()
            or q in app.get("descripcion", "").lower()
            or q in app.get("categoria", "").lower()
        ]

    # Hero
    st.markdown(
        """
        <div class="hero-box">
            <div class="main-title">Portal Clinico IA - Mecanica Vascular</div>
            <div class="subtitle">
                Ecosistema de apps inteligentes para evaluacion hemodinamica, hipertension arterial,
                presion central, rigidez arterial, riesgo cardiovascular y apoyo a la decision clinica.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{len(apps)}</div>
                <div class="metric-label">Apps registradas</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c2:
        activas = sum(1 for app in apps if app.get("estado", "").lower() in ["activa", "activo", "online", "produccion"])
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{activas}</div>
                <div class="metric-label">Apps activas</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c3:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{len(categorias)}</div>
                <div class="metric-label">Categorias</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with c4:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{datetime.now().year}</div>
                <div class="metric-label">Version</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    st.markdown('<div class="section-title">Apps disponibles</div>', unsafe_allow_html=True)

    if not filtered_apps:
        st.warning("No se encontraron apps con los filtros seleccionados.")
        return

    cols = st.columns(3)
    for i, app in enumerate(filtered_apps):
        with cols[i % 3]:
            render_app_card(app)

    st.markdown(
        """
        <div class="footer">
            <b>Desarrollador:</b> Dr. Ricardo Daniel Olano, Cardiologo Hipertensologo.<br>
            <b>Concepto:</b> Plataforma madre para organizar apps clinicas inteligentes desarrolladas en Streamlit.<br>
            <b>Uso previsto:</b> docencia, investigacion, presentacion institucional y apoyo estructurado a la decision clinica.
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# MAIN
# ============================================================

init_state()

if st.session_state.logged_in:
    dashboard()
else:
    login_screen()
