
app.py
100%
import json
from pathlib import Path
from datetime import date
from html import escape

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Mi semana escolar",
    page_icon="📚",
    layout="wide"
)

CARPETA = Path(__file__).resolve().parent
ARCHIVO = CARPETA / "datos_demo.json"

st.markdown("""
<style>
.stApp {
    background-color: #FCFBFF;
}
h1, h2, h3 {
    color: #463D69;
}
div[data-testid="stMetric"] {
    background: #F0ECFA;
    padding: 18px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

st.title("📚 Mi semana escolar")
st.markdown("**Tu familia, organizada en un solo lugar.**")
st.caption("Asistente Escolar IA V0.0 · Datos ficticios")
st.info("Demostración sin conexión a Phidias.")

with ARCHIVO.open("r", encoding="utf-8") as archivo:
    actividades = json.load(archivo)

datos = pd.DataFrame(actividades)

estudiantes = ["Todos"] + sorted(
    datos["estudiante"].unique().tolist()
)

estudiante = st.selectbox(
    "¿De quién quieres consultar las actividades?",
    estudiantes
)

if estudiante == "Todos":
    filtrados = datos.copy()
else:
    filtrados = datos[
        datos["estudiante"] == estudiante
    ].copy()

filtrados = filtrados.sort_values("fecha")

col1, col2, col3 = st.columns(3)

col1.metric("📚 Actividades", len(filtrados))
col2.metric(
    "📝 Exámenes",
    int((filtrados["tipo"] == "Examen").sum())
)
col3.metric(
    "📦 Entregas",
    int((filtrados["tipo"] == "Entrega").sum())
)


# PASO 57 - Resumen automático del domingo

st.subheader("✨ Tu resumen del domingo")

for nombre in sorted(filtrados["estudiante"].unique()):

    actividades_hijo = filtrados[
        filtrados["estudiante"] == nombre
    ].sort_values("fecha")

    examenes = actividades_hijo[
        actividades_hijo["tipo"] == "Examen"
    ]

    entregas = actividades_hijo[
        actividades_hijo["tipo"] == "Entrega"
    ]

    partes = [
        f"Tiene {len(examenes)} exámenes y "
        f"{len(entregas)} entregas esta semana."
    ]

    if not examenes.empty:
        primero = examenes.iloc[0]
        fecha = date.fromisoformat(primero["fecha"])

        partes.append(
            f"Su primer examen es de "
            f"{primero['materia']} el "
            f"{fecha.strftime('%d/%m/%Y')}. "
            "Conviene preparar el repaso con anticipación."
        )

    if not entregas.empty:
        primera = entregas.iloc[0]
        fecha = date.fromisoformat(primera["fecha"])

        partes.append(
            f"Su primera entrega es de "
            f"{primera['materia']} el "
            f"{fecha.strftime('%d/%m/%Y')}. "
            "Es importante revisar que esté terminada."
        )

    with st.container(border=True):
        st.markdown(f"**👤 {nombre}**")
        st.write(" ".join(partes))

st.caption(
    "Resumen automático basado en datos ficticios. "
    "No interpreta todavía publicaciones completas."
)

st.divider()

st.subheader("📅 Actividades de la semana")
st.caption("16 al 22 de noviembre de 2026")

for _, actividad in filtrados.iterrows():

    fecha = date.fromisoformat(actividad["fecha"])
    fecha_legible = fecha.strftime("%d/%m/%Y")

    if actividad["tipo"] == "Examen":
        icono = "📝"
        etiqueta = "EXAMEN"
    else:
        icono = "📦"
        etiqueta = "ENTREGA"

    with st.container(border=True):
        st.markdown(
            f"### {icono} {escape(str(actividad['actividad']))}"
        )

        st.write(
            f"**{etiqueta}** · "
            f"{escape(str(actividad['materia']))}"
        )

        st.write(
            f"📅 {fecha_legible} · "
            f"👤 {escape(str(actividad['estudiante']))}"
        )

        st.caption(
            "Fuente de prueba: " +
            str(actividad["seccion"])
        )

st.divider()

st.caption(
    "La aplicación organiza actividades. "
    "No resuelve tareas ni presenta evaluaciones."
)
Mostrando app.py
