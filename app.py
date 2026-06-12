import streamlit as st
from datetime import datetime


# ============================================================
# CONFIGURACIÓN GENERAL DE LA PÁGINA
# ============================================================

st.set_page_config(
    page_title="Portal Clínico IA - Dr. Olano",
    page_icon="🫀",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ============================================================
# CONFIGURACIÓN DE USUARIOS
# ============================================================

USUARIOS = {
    "admin": {
        "password": "1234",
        "nombre": "Dr. Ricardo Daniel Olano",
        "rol": "Administrador",
    },
    "usuario": {
        "password": "1234",
        "nombre": "Usuario invitado",
        "rol": "Usuario",
    },
}


# ============================================================
# CONFIGURACIÓN DE APPS HIJAS
# Reemplazar las URL por las URL reales de tus apps Streamlit
# ============================================================

APPS = [
    {
        "nombre": "MAPA 24 horas",
        "descripcion": (
            "Aplicación para análisis de monitoreo ambulatorio de presión arterial, "
            "fenotipo hipertensivo, carga presora, patrón circadiano e informe PDF."
        ),
        "url": "https://informe-mapa.streamlit.app/",
        "categoria": "Hipertensión arterial",
        "estado": "Activa",
        "icono": "📈",
    },
    {
        "nombre": "Cardiografía de Impedancia",
        "descripcion": (
            "Evaluación hemodinámica no invasiva, índice cardíaco, resistencias vasculares, "
            "volemia, contractilidad, ortostatismo y embarazo."
        ),
        "url": "https://app-cgi-hemodinamia.streamlit.app/",
        "categoria": "Mecánica vascular",
        "estado": "Activa",
        "icono": "🫀",
    },
    {
        "nombre": "Presión Central",
        "descripcion": (
            "Digitalización y análisis de presión aórtica central, separación de ondas, "
            "índice de aumento, presión reflejada y análisis armónico."
        ),
        "url": "https://presion-central.streamlit.app/",
        "categoria": "Presión central",
        "estado": "Activa",
        "icono": "📊",
    },
    {
        "nombre": "Velocidad de Onda de Pulso",
        "descripcion": (
            "Análisis de VOP carótido-femoral, rigidez arterial, edad vascular, "
            "riesgo vascular e informe clínico."
        ),
        "url": "https://rigidez-vascular-vop.streamlit.app/",
        "categoria": "Rigidez arterial",
        "estado": "Activa",
        "icono": "🧬",
    },
    {
        "nombre": "Riesgo Cardiovascular",
        "descripcion": (
            "Evaluación de riesgo cardiovascular, prevención primaria/secundaria, "
            "dislipemia, objetivos terapéuticos y recomendaciones."
        ),
        "url": "https://TU-APP-RIESGO-CV.streamlit.app",
        "categoria": "Prevención cardiovascular",
        "estado": "Activa",
        "icono": "🛡️",
    },
    {
        "nombre": "App Embarazo y Preeclampsia",
        "descripcion": (
            "Evaluación hemodinámica materna, índice cardíaco, resistencias vasculares, "
            "riesgo de preeclampsia y patrón circulatorio según edad gestacional."
        ),
        "url": "https://TU-APP-EMBARAZO.streamlit.app",
        "categoria": "Embarazo",
        "estado": "Beta",
        "icono": "🤰",
    },
    {
        "nombre": "Obesidad y Riesgo Metabólico",
        "descripcion": (
            "Guía clínica para evaluación de obesidad, IMC, índice cintura/talla, "
            "riesgo cardiometabólico y orientación terapéutica."
        ),
        "url": "https://TU-APP-OBESIDAD.streamlit.app",
        "categoria": "Riesgo metabólico",
        "estado": "En desarrollo",
        "icono": "⚖️",
    },
    {
        "nombre": "Fibrilación Auricular",
        "descripcion": (
            "Manejo clínico de fibrilación auricular, estratificación de riesgo, "
            "anticoagulación, control de ritmo y control de frecuencia."
        ),
        "url": "https://TU-APP-FA.streamlit.app",
        "categoria": "Cardiología clínica",
        "estado": "En desarrollo",
        "icono": "💓",
    },
    {
        "nombre": "Amiloidosis Cardíaca",
        "descripcion": (
            "App de apoyo para sospecha, diagnóstico, estratificación y tratamiento "
            "de la amiloidosis cardíaca."
        ),
        "url": "https://TU-APP-AMILOIDOSIS.streamlit.app",
        "categoria": "Cardiología clínica",
        "estado": "En desarrollo",
        "icono": "🧪",
    },
    {
        "nombre": "Miocardiopatía Hipertrófica",
        "descripcion": (
            "Guía de evaluación clínica, riesgo arrítmico, indicación de estudios, "
            "tratamiento y seguimiento de miocardiopatía hipertrófica."
        ),
        "url": "https://TU-APP-MCH.streamlit.app",
        "categoria": "Cardiología clínica",
        "estado": "En desarrollo",
        "icono": "🫁",
    },
    {
        "nombre": "Repositorio IA Mecánica Vascular",
        "descripcion": (
            "Repositorio general de herramientas, informes, algoritmos y módulos "
            "de inteligencia artificial aplicados a hipertensión y mecánica vascular."
        ),
        "url": "https://TU-APP-REPOSITORIO-IA.streamlit.app",
        "categoria": "Repositorio IA",
        "estado": "Beta",
        "icono": "🧠",
    },
]


# ============================================================
# ESTILOS CSS
# ============================================================

st.markdown(
    """
    <style>
    .main-title {
        font-size: 2.5rem;
        font-weight: 900;
        color: #0f172a;
        margin-bottom: 0.1rem;
    }

    .subtitle {
        font-size: 1.05rem;
        color: #475569;
        margin-bottom: 1.5rem;
    }

    .section-title {
        font-size: 1.5rem;
        font-weight: 800;
        color: #0f172a;
        margin-top: 1.2rem;
        margin-bottom: 0.8rem;
    }

    .app-card {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 20px;
        padding: 22px;
        box-shadow: 0px 4px 16px rgba(15, 23, 42, 0.07);
        min-height: 265px;
        margin-bottom: 18px;
    }

    .app-card:hover {
        border: 1px solid #0f766e;
        box-shadow: 0px 6px 22px rgba(15, 118, 110, 0.12);
    }

    .app-title {
        font-size: 1.22rem;
        font-weight: 850;
        color: #0f172a;
        margin-bottom: 0.5rem;
    }

    .app-description {
        color: #475569;
        font-size: 0.92rem;
        line-height: 1.45;
        min-height: 95px;
        margin-top: 0.8rem;
        margin-bottom: 0.8rem;
    }

    .badge-category {
        display: inline-block;
        background: #e0f2fe;
        color: #075985;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 0.76rem;
        font-weight: 800;
        margin-right: 5px;
    }

    .badge-active {
        display: inline-block;
        background: #dcfce7;
        color: #166534;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 0.76rem;
        font-weight: 800;
    }

    .badge-beta {
        display: inline-block;
        background: #fef9c3;
        color: #854d0e;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 0.76rem;
        font-weight: 800;
    }

    .badge-dev {
        display: inline-block;
        background: #fee2e2;
        color: #991b1b;
        padding: 4px 10px;
        border-radius: 999px;
        font-size: 0.76rem;
        font-weight: 800;
    }

    .metric-box {
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        padding: 18px;
        text-align: center;
        box-shadow: 0px 3px 12px rgba(15, 23, 42, 0.04);
    }

    .metric-value {
        font-size: 2rem;
        font-weight: 900;
        color: #0f172a;
    }

    .metric-label {
        font-size: 0.9rem;
        color: #64748b;
        font-weight: 600;
    }

    .footer-box {
        margin-top: 30px;
        padding: 18px;
        background: #f8fafc;
        border: 1px solid #e2e8f0;
        border-radius: 18px;
        color: #475569;
        font-size: 0.9rem;
    }

    .login-box {
        background: #ffffff;
        border: 1px solid #e2e8f0;
        border-radius: 22px;
        padding: 26px;
        box-shadow: 0px 4px 20px rgba(15, 23, 42, 0.08);
    }

    .small-text {
        color: #64748b;
        font-size: 0.85rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FUNCIONES DE SESIÓN
# ============================================================

def inicializar_sesion():
    if "logueado" not in st.session_state:
        st.session_state.logueado = False

    if "usuario" not in st.session_state:
        st.session_state.usuario = None

    if "nombre_usuario" not in st.session_state:
        st.session_state.nombre_usuario = None

    if "rol" not in st.session_state:
        st.session_state.rol = None


def cerrar_sesion():
    st.session_state.logueado = False
    st.session_state.usuario = None
    st.session_state.nombre_usuario = None
    st.session_state.rol = None
    st.rerun()


# ============================================================
# LOGIN
# ============================================================

def pantalla_login():
    col_izq, col_centro, col_der = st.columns([1, 1.15, 1])

    with col_centro:
        st.markdown("<br><br>", unsafe_allow_html=True)
        st.markdown(
            """
            <div class="login-box">
                <div class="main-title">🫀 Portal Clínico IA</div>
                <div class="subtitle">
                    Ecosistema de apps clínicas inteligentes en hipertensión arterial,
                    cardiografía de impedancia y mecánica vascular.
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        st.markdown("### Ingreso profesional")

        usuario = st.text_input("Usuario")
        password = st.text_input("Contraseña", type="password")

        ingresar = st.button("Ingresar", use_container_width=True)

        if ingresar:
            if usuario in USUARIOS and password == USUARIOS[usuario]["password"]:
                st.session_state.logueado = True
                st.session_state.usuario = usuario
                st.session_state.nombre_usuario = USUARIOS[usuario]["nombre"]
                st.session_state.rol = USUARIOS[usuario]["rol"]
                st.success("Ingreso correcto.")
                st.rerun()
            else:
                st.error("Usuario o contraseña incorrectos.")

        st.info("Usuario inicial: admin | Contraseña inicial: 1234")

        st.markdown(
            """
            <div class="small-text">
            Recomendación: luego de subir la app a Streamlit Cloud, cambiar usuario y contraseña.
            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# BADGE DE ESTADO
# ============================================================

def badge_estado(estado):
    estado_lower = estado.lower()

    if estado_lower == "activa":
        return f'<span class="badge-active">{estado}</span>'

    if estado_lower == "beta":
        return f'<span class="badge-beta">{estado}</span>'

    return f'<span class="badge-dev">{estado}</span>'


# ============================================================
# TARJETA DE APP
# ============================================================

def renderizar_tarjeta_app(app):
    st.markdown(
        f"""
        <div class="app-card">
            <div class="app-title">{app["icono"]} {app["nombre"]}</div>
            <span class="badge-category">{app["categoria"]}</span>
            {badge_estado(app["estado"])}
            <div class="app-description">{app["descripcion"]}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.link_button(
        label="Abrir app",
        url=app["url"],
        use_container_width=True,
    )


# ============================================================
# PANEL PRINCIPAL
# ============================================================

def pantalla_principal():
    # Sidebar
    with st.sidebar:
        st.title("🫀 Portal IA")
        st.caption("Dr. Ricardo Daniel Olano")
        st.divider()

        st.markdown(f"**Usuario:** {st.session_state.nombre_usuario}")
        st.markdown(f"**Rol:** {st.session_state.rol}")

        st.divider()

        categorias = sorted(set(app["categoria"] for app in APPS))
        estados = sorted(set(app["estado"] for app in APPS))

        categoria_seleccionada = st.selectbox(
            "Filtrar por categoría",
            ["Todas"] + categorias,
        )

        estado_seleccionado = st.selectbox(
            "Filtrar por estado",
            ["Todos"] + estados,
        )

        busqueda = st.text_input("Buscar app")

        st.divider()

        if st.button("Cerrar sesión", use_container_width=True):
            cerrar_sesion()

    # Encabezado
    st.markdown(
        """
        <div class="main-title">Portal Clínico IA - Mecánica Vascular</div>
        <div class="subtitle">
            Panel madre para ingresar a las diferentes apps web clínicas, docentes y de investigación.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Métricas
    total_apps = len(APPS)
    apps_activas = sum(1 for app in APPS if app["estado"].lower() == "activa")
    apps_beta = sum(1 for app in APPS if app["estado"].lower() == "beta")
    apps_desarrollo = total_apps - apps_activas - apps_beta

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{total_apps}</div>
                <div class="metric-label">Apps registradas</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c2:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{apps_activas}</div>
                <div class="metric-label">Activas</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c3:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{apps_beta}</div>
                <div class="metric-label">Beta</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with c4:
        st.markdown(
            f"""
            <div class="metric-box">
                <div class="metric-value">{apps_desarrollo}</div>
                <div class="metric-label">En desarrollo</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.divider()

    # Filtrado
    apps_filtradas = APPS.copy()

    if categoria_seleccionada != "Todas":
        apps_filtradas = [
            app for app in apps_filtradas
            if app["categoria"] == categoria_seleccionada
        ]

    if estado_seleccionado != "Todos":
        apps_filtradas = [
            app for app in apps_filtradas
            if app["estado"] == estado_seleccionado
        ]

    if busqueda:
        texto = busqueda.lower()
        apps_filtradas = [
            app for app in apps_filtradas
            if texto in app["nombre"].lower()
            or texto in app["descripcion"].lower()
            or texto in app["categoria"].lower()
            or texto in app["estado"].lower()
        ]

    st.markdown('<div class="section-title">Aplicaciones disponibles</div>', unsafe_allow_html=True)

    if not apps_filtradas:
        st.warning("No se encontraron apps con los filtros seleccionados.")
    else:
        columnas = st.columns(3)

        for i, app in enumerate(apps_filtradas):
            with columnas[i % 3]:
                renderizar_tarjeta_app(app)

    # Área administrador
    if st.session_state.rol == "Administrador":
        st.divider()
        st.markdown('<div class="section-title">Panel administrador</div>', unsafe_allow_html=True)

        with st.expander("Ver configuración actual de apps"):
            st.dataframe(APPS, use_container_width=True)

        st.info(
            "Para agregar o modificar apps, editar la lista APPS dentro de app.py. "
            "También se puede migrar luego a una base Excel, Google Sheets o SQLite."
        )

    # Footer
    st.markdown(
        f"""
        <div class="footer-box">
            <b>Desarrollador:</b> Dr. Ricardo Daniel Olano, Cardiólogo Hipertensólogo.<br>
            <b>Proyecto:</b> Ecosistema de Apps Clínicas Inteligentes para Hipertensión Arterial,
            Cardiografía de Impedancia, Presión Central, VOP y Mecánica Vascular.<br>
            <b>Año:</b> {datetime.now().year}
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# EJECUCIÓN PRINCIPAL
# ============================================================

def main():
    inicializar_sesion()

    if not st.session_state.logueado:
        pantalla_login()
    else:
        pantalla_principal()


if __name__ == "__main__":
    main()
