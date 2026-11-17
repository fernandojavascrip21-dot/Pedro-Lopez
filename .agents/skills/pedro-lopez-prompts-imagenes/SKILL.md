---
name: pedro-lopez-prompts-imagenes
description: Redacta prompts profesionales de imagen (escenarios realistas, enfoque empresarial) para el contenido mensual de Pedro López — Asesor en Seguros según la estrategia AXIS, los reúne en un solo .md y, al ejecutarlo en Codex, genera cada imagen 1080×1350 con zona limpia reservada para el logo y la guarda en foto-sin-logo/. Usar cuando pidan prompts o imágenes de Pedro López, su calendario de contenido, publicaciones para empresarios o "foto sin logo".
---

# Prompts de imágenes — Pedro López Seguros (AXIS)

## Qué hace
1. Escribe **un solo documento** `prompts/prompts-pedro-lopez-<mes>-<año>.md` con todos los prompts del periodo.
2. Si se pide generar (Codex), crea cada imagen, la valida y la guarda en `foto-sin-logo/`.

No coloca el logo: eso lo hace `pedro-lopez-logo-branding` después. Cada imagen deja una zona lisa para él.

## Antes de escribir
Leer solo estos archivos (no la Referencia completa; **nunca sus anexos**, línea 435 en adelante):
- `references/marca.md` · reglas vigentes de marca.
- `references/estrategia-axis.md` · público, problemas, mensajes literales, enfoques.
- `references/escenarios.md` · giros, planos, luz, anti-repetición.
- `references/zona-logo.md` · franjas A–D y uso del detector de espacio libre.
Si hay duda de marca, leer `references/Pedro_Lopez_Asesor_de_Seguros_Referencia_Integral.md` líneas 29–415.

## Entrada (con defaults, sin interrogar)
Periodo (default: mes siguiente) · piezas (20, lun–vie) · propuestas por pieza (1: solo la A; 2 A/B si se piden) · texto impreso (sí: titular + apoyo) · rango a generar. Anotar supuestos al inicio del `.md`.

## Calendario
Semana w=0..3, día d=0..4. Enfoque = E(d+1) (E1 mala atención, E2 precios/comparación, E3 seguimiento/soluciones, E4 patrimonio empresarial, E5 atención personalizada/confianza). Tipo = [Problema, Solución, Confianza, Beneficio][(d+w) mod 4]. Cada enfoque×tipo sale una vez. Los 6 mensajes del PDF van literales; lo demás son variaciones que **requieren aprobación**: tras escribir el `.md`, detenerse y pedirla antes de generar imágenes.

## Reglas duras
- Una idea, un punto focal, 40–50 % de aire. Sin iconos, escudos, destellos, tarjetas, botones ni sellos.
- El problema vive en el titular; la imagen transmite calma (nunca choques, incendios, hospitales, luto, enojo, alarma).
- Sin precios, "ahorra", descuentos, tiempos de respuesta, testimonios, cifras, aseguradoras ni coberturas nombradas. El ramo es dato interno.
- Escenarios mexicanos genéricos; sin ciudad ni monumentos; no deducir ubicación del teléfono.
- El asesor nunca con rostro identificable; protagonista = empresario.
- Texto impreso: solo titular + apoyo (≤10 palabras), literal, con acentos y ¿ ? . Sin teléfono ni web (van en el caption). Titular en serif bold tipo Bitter; apoyo en sans tipo Montserrat.
- Paleta: azul marino #1E3A6E ancla, dorado #E8A33D ≤5 %, crema/blancos. Nada de rojo, morado, neón.
- Pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
- Nunca dibujar logo, marco, recuadro ni leyenda de placeholder; la zona es una franja de fondo liso (sin estantes, plantas, ventanas ni puertas) y el titular nunca la invade.
- En el prompt **nunca** escribir "propuesta", "opción", "versión A/B", "variante" ni pedir comparar o mostrar juntas: causa collages. Cada prompt describe una sola imagen terminada.
- Por defecto una sola imagen por pieza (A). Si se piden dos, A y B difieren en layout, plano y tono de fondo.

## Bloque de cada pieza en el .md
```
### PL-01A · lun 2 nov 2026 · E1 Mala atención · Problema · Layout A
- Giro y escena · Ramo interno (no se imprime)
- Texto impreso: TITULAR "…" · APOYO "…" · Origen: PDF literal | variación (requiere aprobación)
- Logo: franja reservada (superior/inferior) · posición y variante finales: las da `validar.py`
- Caption: 2–4 líneas + CTA + "Contáctanos: 375 107 2477 · www.plseguros.mx" + 4–6 hashtags
- Archivo: foto-sin-logo/PL-01A_<tema>.png
- Estado: [ ] generada [ ] 1080×1350 [ ] zona OK [ ] texto OK
```
Seguido del PROMPT en bloque `text` con: formato 4:5 de una sola escena · ESCENA · CÁMARA Y LUZ · COMPOSICIÓN (9 % inferior libre) · ZONA RESERVADA (franja de 16 % de alto y ancho completo, con capas verticales de franja / texto / sujeto) · TEXTO IMPRESO · PALETA · EVITAR. Al inicio del `.md`, tabla de seguimiento (ID, archivo, `[ ]`) para poder reanudar.

## Generar en Codex (solo si se pide)
Lotes de hasta 5 imágenes por mensaje. Para cada pieza:
1. Una llamada a la herramienta de imagen (`image_gen`) con el PROMPT literal, sin añadir nada.
2. Copiar el archivo más reciente de `$CODEX_HOME/generated_images/` (por defecto `~/.codex/generated_images/`) a `foto-sin-logo/PL-NNX_<tema>.png`. Nunca sobrescribir: un reintento se guarda `-v2` (máx. 2).
3. `python3 .agents/skills/pedro-lopez-prompts-imagenes/scripts/validar.py <archivo> <A|B|C|D> --json` → recorta a 4:5, reescala a **1080×1350** y **detecta el espacio libre real** para el logo (hasta 3 candidatos con `force_pos`, caja en px y variante de logo). La posición final es la detectada, no la del layout.
4. Revisar la imagen a ojo: texto carácter por carácter, una sola escena, sin logos inventados ni texto basura, legible en móvil, y que el candidato elegido sea un lugar razonable (esquina o borde, lejos de rostros y texto).
5. Si falla un solo aspecto (o el detector sale con código 1: sin espacio libre), corregir ese aspecto y regenerar; ante falta de espacio, cambiar de layout o editar la franja (ver `references/zona-logo.md`). Si el texto falla dos veces, generar sin texto y anotarlo en el `.md`.
6. Marcar `[x]` en el `.md`.
Primero 2 piezas de prueba y verificarlas con `pedro-lopez-logo-branding` (pasar `force_pos` y variante detectados); luego el resto de las A.

## Entrega final
Tabla `archivo → force_pos → caja px → variante de logo` (del detector) lista para el skill del logo, más aviso de piezas con texto omitido o variaciones sin aprobar.
