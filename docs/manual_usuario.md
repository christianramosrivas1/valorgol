# Manual de usuario de ValorGol

ValorGol es una aplicación web para explorar datos reales de jugadores de fútbol profesional y jugar a adivinar cuál tiene mayor valor de mercado. ¡Empecemos!

## 1. Requisitos

- Python 3.10 o superior.
- Un navegador web actual (Edge, Chrome o Firefox).
- Conexión a internet para ver las fotos de los jugadores.

## 2. Instalación

1. Descargar o clonar el repositorio desde GitHub (botón **Code → Download ZIP**) y descomprimirlo.
2. Abrir una terminal dentro de la carpeta del proyecto.
3. Instalar las librerías:

```bash
pip install -r requirements.txt
```

## 3. Preparar los datos

La aplicación lee el archivo `data/datos.csv`. Si el repositorio ya lo trae, se puede pasar al paso 4.

Si no existe:
1. Guardar el archivo original `players.csv` de *Transfermarkt datasets* en `data/raw/`.
2. Abrir `data/limpieza.ipynb` con Jupyter y ejecutar todas las celdas, desde la carpeta `data`.
3. Verificar que se creó `data/datos.csv`.

## 4. Ejecución

Desde la carpeta del proyecto:

```bash
streamlit run app.py
```

Se abre una pestaña del navegador con la aplicación. Si no se abre sola, entrar a la dirección que aparece en la terminal, normalmente `http://localhost:8501`.

## 5. Navegación

El menú de la barra lateral izquierda tiene cuatro páginas: **Inicio**, **Explorar**, **Jugar** y **Mis datos**. Se puede pasar de una a otra en cualquier momento sin perder la información de la sesión.

## 6. Página Inicio

Presenta la aplicación y muestra:
- El nombre, el logo y una descripción breve.
- La fuente de los datos y su licencia.
- Cuatro indicadores: jugadores, países, valor medio y partidas jugadas.
- Enlaces a las secciones Explorar, Jugar y Mis datos.
- El equipo desarrollador, los créditos y las licencias.

## 7. Página Explorar

Sirve para consultar y analizar los jugadores.

**Filtros (barra lateral izquierda)**

| Filtro | Cómo usarlo |
|---|---|
| Posición | Elegir una o varias; vacío significa todas |
| País | Elegir uno o varios; vacío significa todos |
| Edad | Mover los extremos del control deslizante |
| Valor de mercado (millones €) | Mover los extremos del control deslizante |
| Nombre contiene | Escribir parte del nombre del jugador |

**Qué se actualiza al filtrar**
- Cuatro indicadores: jugadores encontrados, valor medio, valor mediano y edad promedio.
- La tabla de registros.
- Dos gráficos: valor medio por posición y edad frente a valor de mercado.

**Detalle de un jugador:** hacer clic en una fila de la tabla. Debajo aparece su foto, posición, país, club, edad y valor de mercado.

Si ningún jugador cumple los filtros, la página muestra un aviso para que se amplíen.

## 8. Página Jugar: «¿Cuánto vale?»

**Objetivo:** acertar cuál de dos jugadores tiene mayor valor de mercado.

**Reglas**
- Cada partida tiene 10 rondas.
- Acertar suma 10 puntos.
- Cada acierto consecutivo suma 2 puntos extra (racha).
- Fallar pone la racha en cero.

**Cómo jugar**
1. Pulsar **Nueva partida**.
2. Leer los datos de los dos jugadores (posición, club, país y edad). El valor está oculto.
3. Pulsar **Este vale más** debajo del jugador elegido.
4. Ver el mensaje de resultado, que indica si acertaste y el valor de ambos jugadores.
5. Repetir hasta completar las 10 rondas.

**Al terminar:** se muestran el puntaje, los aciertos, la mejor racha y el mejor puntaje de la sesión. El botón **Jugar de nuevo** inicia otra partida sin borrar las estadísticas acumuladas.

## 9. Página Mis datos

Resume lo que hiciste durante la sesión:
- **Indicadores:** partidas jugadas, puntaje acumulado, mejor resultado y jugadores consultados en Explorar.
- **Estadísticas de juego:** precisión global (porcentaje de aciertos).
- **Gráfico:** evolución del puntaje por partida.
- **Historial:** fecha, puntaje, aciertos, mejor racha y duración de cada partida.
- **Descarga:** el botón **Descargar mi historial (CSV)** guarda el historial en un archivo.
- **Jugadores consultados:** lista de los que seleccionaste en Explorar.

Si todavía no hay actividad, la página muestra un mensaje que invita a jugar o explorar.

> Los datos de Mis datos viven solo mientras la pestaña está abierta. Al cerrar o recargar el navegador, la sesión empieza de cero.

## 10. Mensajes y problemas frecuentes

| Mensaje o situación | Causa | Solución |
|---|---|---|
| «No se encontró `data/datos.csv`» | Falta el archivo de datos | Ejecutar `data/limpieza.ipynb` (sección 3) |
| «El archivo `data/datos.csv` está vacío» | La limpieza dejó el archivo sin filas | Volver a ejecutar el cuaderno y revisar el archivo original |
| «Faltan columnas en datos.csv» | El archivo no tiene la estructura esperada | Regenerarlo con `limpieza.ipynb` |
| «Ningún jugador cumple con los filtros» | Los filtros son demasiado estrictos | Ampliar los rangos o quitar filtros |
| Una foto no aparece | Falta internet o el enlace de la imagen no responde | Verificar la conexión; el juego sigue funcionando |
| `streamlit` no se reconoce como comando | Streamlit no está instalado | Ejecutar `pip install -r requirements.txt` |

## 11. Créditos y licencias

- Datos: *Transfermarkt datasets*, licencia CC0 1.0.
- Software: licencia CC BY-NC 4.0 (ver `docs/LICENSE.md`).
- Autores: Carlos Andrés Herrera Benavides y Cristian Daniel Ramos Rivas, Universidad de Antioquia.
