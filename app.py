
import json
from pathlib import Path

import pandas as pd
import streamlit as st

st.set_page_config(
    page_title="Mi semana escolar",
    page_icon="📚",
    layout="wide"
)

CARPETA = Path(__file__).resolve().parent
ARCHIVO = CARPETA / "datos_demo.json"

st.title("📚 Mi semana escolar")
st.caption("Asistente Escolar IA V0.0")
st.info("Demostración con datos ficticios. Sin conexión a Phidias.")

with ARCHIVO.open("r", encoding="utf-8") as archivo:
    actividades = json.load(archivo)

datos = pd.DataFrame(actividades)

estudiantes = ["Todos"] + sorted(
    datos["estudiante"].unique().tolist()
)

estudiante = st.selectbox(
    "Selecciona un estudiante",
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

st.subheader("📅 Agenda de la semana")
st.caption("16 al 22 de noviembre de 2026")

tabla = filtrados[
    ["fecha", "estudiante", "materia", "tipo",
     "actividad", "seccion"]
].rename(columns={
    "fecha": "Fecha",
    "estudiante": "Estudiante",
    "materia": "Materia",
    "tipo": "Tipo",
    "actividad": "Actividad",
    "seccion": "Sección"
})

st.dataframe(
    tabla,
    use_container_width=True,
    hide_index=True
)

st.caption(
    "La aplicación organiza actividades; "
    "no resuelve tareas ni presenta evaluaciones."
)
