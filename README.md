# Portal Clinico IA - Dr. Olano

App madre desarrollada en Streamlit para acceder a diferentes apps web clinicas del ecosistema del Dr. Ricardo Daniel Olano.

## Objetivo

Centralizar el ingreso a apps de:

- MAPA 24 horas
- Cardiografia de Impedancia
- Presion Central Olano
- Velocidad de Onda de Pulso
- Proceso IA MV
- Riesgo Cardiovascular
- Obesidad
- Fibrilacion Auricular
- Amiloidosis Cardiaca
- Miocardiopatia Hipertrofica

## Estructura

```text
app-madre-olano/
├── app.py
├── requirements.txt
├── README.md
└── .streamlit/
    ├── config.toml
    └── secrets.toml.example
```

## Ejecucion local

1. Crear entorno virtual:

```bash
python -m venv .venv
```

2. Activar entorno:

Windows:

```bash
.venv\Scripts\activate
```

Linux/Mac:

```bash
source .venv/bin/activate
```

3. Instalar dependencias:

```bash
pip install -r requirements.txt
```

4. Copiar secrets de ejemplo:

```bash
cp .streamlit/secrets.toml.example .streamlit/secrets.toml
```

En Windows PowerShell:

```powershell
Copy-Item .streamlit/secrets.toml.example .streamlit/secrets.toml
```

5. Ejecutar:

```bash
streamlit run app.py
```

## Usuario inicial

```text
Usuario: admin
Contrasena: 1234
```

Cambiar estos datos en `.streamlit/secrets.toml` antes de publicar.

## Despliegue en Streamlit Cloud

1. Subir este repositorio a GitHub.
2. Crear nueva app en Streamlit Cloud.
3. Seleccionar:
   - Repository: `app-madre-olano`
   - Branch: `main`
   - Main file path: `app.py`
4. En `App settings > Secrets`, pegar el contenido de `.streamlit/secrets.toml.example` y editar las URLs reales de cada app.

## Edicion de apps hijas

Las apps se configuran desde secrets:

```toml
[apps.nombre_app]
nombre = "Nombre visible"
descripcion = "Descripcion breve"
url = "https://url-real.streamlit.app"
categoria = "Categoria clinica"
estado = "Activa"
icono = "🫀"
```

## Nota de seguridad

Este login es simple y suficiente como barrera inicial para un portal personal/demo. Para uso institucional o datos sensibles, debe implementarse autenticacion robusta con usuarios, roles, registro de accesos y control de permisos.

## Autor

Dr. Ricardo Daniel Olano  
Cardiologo Hipertensologo
