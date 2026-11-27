# Plan de versionado

**Proyecto:** ValorGol. **Integrantes:** Carlos Andrés Herrera Benavides, Cristian Daniel Ramos Rivas.


## 1. Convención de versiones

Se usa una numeración simple `vX.Y`:

- `X` cambia cuando se entrega una versión completa y estable (`v1.0` es la entrega final).
- `Y` aumenta con cada procedimiento relevante: un componente terminado, una prueba importante o un ajuste mayor.

Cada versión se registra en GitHub como una *release* con su etiqueta (*tag*), por ejemplo `v0.2`, con un mensaje corto que resume el avance.

## 2. Versiones del software

| Versión | Fecha | Día del proyecto | Procedimiento relevante | Avance acumulado | Estado |
|---|---|---|---|---|---|
| v0.1 | 8 nov 2026 | 6 | Creación del repositorio en GitHub, actas de entendimiento, colaboración y responsabilidad | 10 % | Completada |
| v0.2 | 12 nov 2026 | 10 | Dataset original en `data/raw/`, cuaderno `limpieza.ipynb` y archivo limpio `data/datos.csv` | 25 % | Pendiente |
| v0.3 | 15 nov 2026 | 13 | Documentación inicial: README, licencia, requisitos, cronograma y presupuesto | 40 % | Completada |
| v0.4 | 20 nov 2026 | 18 | Carga de datos (`src/data.py`) y página Explorar con filtros, detalle, estadísticas y gráficos | 55 % | Pendiente |
| v0.5 | 20 nov 2026 | 18 | Juego «¿Cuánto vale?»: clase `Partida` (`src/juego.py`) y página Jugar | 70 % | Pendiente |
| v0.6 | 22 nov 2026 | 20 | Páginas Mis datos e Inicio, identidad visual y `st.session_state` | 85 % | Pendiente |
| v0.7 | 24 nov 2026 | 22 | Integración de las cuatro páginas, pruebas y manejo de errores | 92 % | Pendiente |
| v0.8 | 27 nov 2026 | 25 | Ajustes tras la asesoría con la docente y manual de usuario | 97 % | Pendiente |
| v1.0 | 29 nov 2026 | 27 | Entrega final: código fuente, plan de versionado y manual de usuario | 100 % | Pendiente |

> Las fechas de las versiones pendientes son las planeadas en el cronograma. Cuando una versión se complete, el equipo actualiza la columna «Estado» y, si cambió, la fecha real.

## 3. Detalle del avance por versión

### v0.1: Repositorio y actas
- Repositorio público `valorgol` creado con la cuenta institucional.
- Actas subidas a la carpeta `actas/`.
- Docente y compañero vinculados como colaboradores.

### v0.2: Datos
- Archivo original descargado de *Transfermarkt datasets* y guardado en `data/raw/`.
- Limpieza documentada: duplicados, jugadores activos, valores faltantes, edad calculada, textos y traducciones.
- Exportación a `data/datos.csv`.

### v0.3: Documentación inicial
- `README.md` con integrantes, logo, descripción y reporte de visión.
- `docs/LICENSE.md` (CC BY-NC 4.0) y `docs/requisitos.md`.
- `docs/cronograma.xlsx` con diagrama de Gantt y `docs/presupuesto.xlsx`.

### v0.4: Explorar
- Tabla interactiva con selección de registro.
- Cinco filtros: posición, país, edad, valor de mercado y nombre.
- Cuatro indicadores y dos gráficos que se actualizan con los filtros.

### v0.5: Jugar
- Partidas de 10 rondas con dos jugadores reales del conjunto de datos.
- Puntaje con bono por racha y retroalimentación después de cada respuesta.
- Reinicio sin perder las estadísticas de la sesión.

### v0.6: Mis datos e Inicio
- Resumen de actividad, historial, gráfico de progreso y mensaje cuando no hay actividad.
- Inicio con indicadores, funcionalidades, equipo, créditos y licencias.

### v0.7: Integración
- Prueba de las cuatro páginas con los datos reales.
- Revisión de casos límite: filtros sin resultados, archivo inexistente y columnas faltantes.

### v0.8: Ajustes
- Correcciones sugeridas por la docente en la asesoría.
- Manual de usuario (`docs/manual_usuario.md`).

### v1.0: Entrega final
- Todo el código fuente, el plan de versionado y el manual de usuario en el repositorio.
- Aplicación ejecutable con `streamlit run app.py`.

## 4. Cómo registrar una versión en GitHub

1. Abrir el repositorio y pulsar **Releases → Create a new release**.
2. En **Choose a tag**, escribir el número de versión (por ejemplo `v0.4`) y crear la etiqueta.
3. Poner un título y una descripción corta del avance.
4. Pulsar **Publish release**.
