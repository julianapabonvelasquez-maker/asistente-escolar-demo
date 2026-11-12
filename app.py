
# PASO 57 - Incorporar resumen del domingo a Streamlit
# Asistente Escolar IA V0.0
# Datos ficticios y sin conexión a Phidias

from pathlib import Path
import ast
import shutil

proyecto_p57 = Path(
    "/content/drive/MyDrive/Asistente_Escolar_IA"
)

archivo_p57 = proyecto_p57 / "demo_publica/app.py"

respaldo_p57 = (
    proyecto_p57 /
    "copias_seguridad/app_antes_resumen_p57.py.bak"
)

if not archivo_p57.is_file():
    print("⚠️ No se encontró app.py.")

else:
    codigo_p57 = archivo_p57.read_text(
        encoding="utf-8"
    )

    marcador_p57 = 'st.divider()'

    bloque_p57 = '''
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

'''

    if 'st.subheader("✨ Tu resumen del domingo")' in codigo_p57:
        print("ℹ️ El resumen ya existe en app.py.")
        print("No se duplicó el código.")
        print("✅ PASO 57 COMPLETADO")

    elif marcador_p57 not in codigo_p57:
        print("⚠️ No encontramos el punto de inserción.")
        print("No se modificó app.py.")

    else:
        # Guardar respaldo fuera de la carpeta pública
        respaldo_p57.parent.mkdir(
            parents=True, exist_ok=True
        )

        if not respaldo_p57.exists():
            shutil.copy2(archivo_p57, respaldo_p57)

        # Insertar antes del primer separador
        codigo_nuevo_p57 = codigo_p57.replace(
            marcador_p57,
            bloque_p57 + marcador_p57,
            1
        )

        # Validar sintaxis antes de guardar
        ast.parse(codigo_nuevo_p57)

        archivo_p57.write_text(
            codigo_nuevo_p57,
            encoding="utf-8"
        )

        print("🏫 ASISTENTE ESCOLAR IA V0.0")
        print("✨ RESUMEN DEL DOMINGO INCORPORADO")
        print("=" * 45)
        print("✅ Código Python validado")
        print("✅ Respaldo creado")
        print("✅ Tarjetas y filtros conservados")
        print("✅ Archivo actualizado:", archivo_p57.name)
        print("✅ PASO 57 COMPLETADO")
