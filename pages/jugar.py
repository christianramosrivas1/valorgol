"""Página Jugar: '¿Cuánto vale?' - elige qué jugador tiene mayor valor de mercado."""
import streamlit as st
from src.data import obtener_datos
from src.juego import Partida
from src.ui import encabezado, formato_eur, icono_posicion, mostrar_foto
encabezado("¿Cuánto vale?", "Adivina qué jugador tiene el mayor valor de mercado.")
df = obtener_datos()
def iniciar_partida():
    """Crea una partida nueva sin borrar el historial acumulado."""
    st.session_state["partida"] = Partida(df)
    st.session_state["feedback"] = None
    st.session_state["partida_guardada"] = False
def elegir(indice):
    """Registra la respuesta del usuario en la partida actual."""
    st.session_state["feedback"] = st.session_state["partida"].responder(indice)
with st.expander("📖 Instrucciones", expanded=st.session_state["partida"] is None):
    st.markdown(
        "- Verás **dos jugadores reales** del dataset.\n"
        "- Elige cuál tiene **mayor valor de mercado**.\n"
        "- Cada partida tiene **10 rondas**. Acertar suma 10 puntos y cada acierto "
        "seguido suma 2 puntos extra (racha).\n"
        "- Si fallas, la racha vuelve a cero.\n"
        "- Tus partidas quedan guardadas en **Mis datos** mientras dure la sesión."
    )
partida = st.session_state["partida"]
if partida is None:
    st.info("Pulsa el botón para comenzar.")
    st.button("▶️ Nueva partida", on_click=iniciar_partida, type="primary")
    st.stop()
# Retroalimentación de la última respuesta
fb = st.session_state["feedback"]
if fb:
    detalle = (
        f"{fb['nombres'][0]}: {formato_eur(fb['valores'][0])} · "
        f"{fb['nombres'][1]}: {formato_eur(fb['valores'][1])}"
    )
    if fb["acierto"]:
        st.success(f"✅ ¡Correcto! +{fb['puntos']} puntos. {detalle}")
    else:
        st.error(f"❌ Fallaste. {detalle}")
# Fin de la partida
if partida.terminada:
    if not st.session_state["partida_guardada"]:
        registro = partida.resumen()
        registro["partida"] = len(st.session_state["historial"]) + 1
        st.session_state["historial"].append(registro)
        st.session_state["partida_guardada"] = True
    st.header("🏁 Partida terminada")
    m1, m2, m3 = st.columns(3)
    m1.metric("Puntaje", partida.puntaje)
    m2.metric("Aciertos", f"{partida.aciertos}/{partida.rondas}")
    m3.metric("Mejor racha", partida.mejor_racha)
    mejor = max(p["puntaje"] for p in st.session_state["historial"])
    st.caption(f"Tu mejor puntaje en esta sesión: {mejor}")
    st.button("🔄 Jugar de nuevo", on_click=iniciar_partida, type="primary")
    st.stop()
# Ronda en curso
st.progress(
    partida.ronda_actual / partida.rondas,
    text=f"Ronda {partida.ronda_actual + 1} de {partida.rondas} · Puntaje: {partida.puntaje} · Racha: {partida.racha}",
)
columnas = st.columns(2)
for i, jugador in enumerate(partida.par):
    with columnas[i]:
        mostrar_foto(jugador["imagen_url"])
        st.subheader(jugador["nombre"])
        st.write(f"**Posición:** {icono_posicion(jugador['posicion'])} {jugador['posicion']}")
        st.write(f"**Club:** {jugador['club']}")
        st.write(f"**País:** {jugador['pais']} · **Edad:** {jugador['edad']}")
        st.button(
            "Este vale más",
            key=f"opcion_{i}_{partida.ronda_actual}",
            on_click=elegir,
            args=(i,),
        )
