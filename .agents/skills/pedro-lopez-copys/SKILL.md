---
name: pedro-lopez-copys
description: Escribe los copys (textos de publicación para Facebook e Instagram) de Pedro López — Asesor en Seguros, uno por cada foto terminada en fotos-creada/, con la voz de la marca, relacionados con lo que se ve en la imagen y con su bloque del documento de prompts, y con el contacto (dirección, teléfono, web) al final. Usar cuando pidan copys, captions, textos o publicaciones para las imágenes de Pedro López.
---

# Copys de Pedro López — uno por foto

## Qué hace
Para cada imagen de `fotos-creada/` escribe un copy listo para pegar en Facebook e Instagram y los reúne en **un solo documento**: `copys/copys-pedro-lopez-<mes>-<año>.md`. No genera ni modifica imágenes.

## Archivos que se leen (solo estos)
- `references/voz.md` · cómo habla la marca, qué nunca decir, emojis, hashtags, CTA.
- `references/formulas.md` · estructura por tipo (Problema/Solución/Confianza/Beneficio) y enfoque (E1–E5).
- `references/contacto.md` · bloque de contacto (fuente única).
- `prompts/prompts-pedro-lopez-<mes>-<año>.md` · bloque de cada pieza: ID, fecha, enfoque, tipo, titular, apoyo, giro.
- `.agents/skills/pedro-lopez-prompts-imagenes/references/estrategia-axis.md` · ángulo empresarial.
- La **foto final**: `fotos-creada/PL-NNA_*.png`.
Si hay dudas de marca, solo líneas 29–415 de la Referencia Integral; **nunca sus anexos**.

## Flujo
1. **Mira la foto** (abre la imagen) y anota en una línea lo que realmente se ve: giro, persona, gesto, objeto clave, luz y texto impreso. No inventar detalles.
2. Lee su bloque en el documento de prompts (enfoque, tipo, titular, apoyo).
3. Escribe el copy con la estructura de abajo, retomando un detalle visible de la foto.
4. Añade el bloque al `.md` (lotes de 5) y marca la tabla de seguimiento.
5. Corre `python3 -I .agents/skills/pedro-lopez-copys/scripts/revisar.py copys/<archivo>.md` y corrige hasta 0 fallos.
6. Revisión cruzada: ¿el copy concuerda con la foto y con el titular impreso, sin repetirlo?
7. Con piezas nuevas: primero 2 muestras (por ejemplo PL-01A y PL-05A) y pedir visto bueno al tono antes de seguir.

## Estructura del copy (Facebook + Instagram, 1 versión)
1. **Gancho** (1 línea): conecta con la escena y el problema real del empresario.
2. **Desarrollo** (2–3 líneas cortas, 1–2 líneas por párrafo, espacio entre ellos): el valor del tipo de pieza (Atención, Soluciones, Precio).
3. **CTA** (1 línea): revisar, comparar o cotizar; variar entre captación / informativo / cierre suave; no repetir el de la pieza anterior.
4. **Bloque de contacto**, copiado exactamente de `references/contacto.md` (📍 dirección · 📲 teléfono · 🌐 web).
5. **Hashtags** (4–6; fijos `#PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico` + 1–3 temáticos).
Cuerpo ≤ 90 palabras, 1–3 emojis relacionados con el mensaje. No repetir el titular impreso palabra por palabra.

## Reglas duras
- Español de México, tú, nunca voseo. Tono profesional, cálido y directo; protección y tranquilidad, nunca miedo.
- Sin precios, descuentos, "gratis", "ahorra", cifras, testimonios, promociones, tiempos de respuesta, coberturas ni aseguradoras nombradas.
- Mala atención (E1): la pregunta va al lector; jamás se critica a otro agente ni aseguradora.
- Solo datos de contacto documentados. **La dirección no se inventa ni se deduce**: si `references/contacto.md` dice `[DIRECCIÓN PENDIENTE]`, los copys son borradores y se avisa al usuario; no se presentan como finales.
- Cada pieza distinta: variar primera palabra, tipo de apertura, CTA y emoji entre piezas consecutivas.

## Bloque de cada foto en el .md
````
### PL-01A · lun 2 nov 2026 · E1 Mala atención · Problema
- Foto: fotos-creada/PL-01A_agente-solo-renovar.png
- Lo que se ve: <una línea con lo que realmente se ve>
- Texto en la imagen: TITULAR "…" · APOYO "…"
- Ángulo del copy: <qué detalle de la foto y qué valor usa>
- COPY (listo para pegar):

```text
<gancho>

<desarrollo>

<CTA>

Contáctanos:
📍 <dirección>
📲 375 107 2477 (llamada o WhatsApp)
🌐 www.plseguros.mx

#PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #…
```
````
Al inicio del `.md`: título, supuestos y tabla de seguimiento (ID, foto, ángulo, CTA usado, `[ ]`/`[x]`).

## Entrega final
Avisar cuántos copys hay, cuáles no pasaron QA (si alguno), y si la dirección sigue pendiente.
