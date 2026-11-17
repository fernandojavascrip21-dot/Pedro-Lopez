# Zona reservada para el logo

Lienzo final 1080 × 1350. El logo lo coloca después `pedro-lopez-logo-branding` (logo horizontal ≈30 % del ancho ≈324×85 px, apilado ≈22 % ≈238×162 px, margen ≈49 px).

## Cómo se garantiza el espacio
1. **En el prompt** se reserva una **franja completa** (16 % del alto, todo el ancho), arriba o abajo, no una esquina. El generador respeta mejor una franja que una caja pequeña, y titular y sujeto se organizan en capas verticales que nunca la tocan.
2. **Después de generar**, `scripts/validar.py` busca el espacio libre real: desliza una ventana de 380×170 px por toda la imagen y puntúa lisura (desviación de luminancia ≤14 y bordes Canny ≤1.5 %), prefiriendo bordes y esquinas lejos del centro. El layout del prompt es solo la intención; la posición final es la detectada.

| Layout | Franja pedida | Titular | Sujeto |
|---|---|---|---|
| A | superior 0–16 % | izquierda, 28–48 % | derecha, 30–84 % |
| B | superior 0–16 % | centrado, 68–86 % | centrado, 22–64 % |
| C | inferior 84–100 % | arriba-izq, 8–28 % | izquierda/centro, 30–82 % |
| D | superior 0–16 % | abajo-izq, 72–88 % | centro-izq, 24–68 % |

## Uso del detector
```
python3 .agents/skills/pedro-lopez-prompts-imagenes/scripts/validar.py <imagen> [A|B|C|D] [--json] [--no-guardar] [--salida RUTA]
```
- Recorta a 4:5 y reescala a 1080×1350 (sobrescribe salvo `--no-guardar`/`--salida`).
- Devuelve hasta 3 candidatos sin solape: `force_pos` (arriba/abajo-izq/centro/der), caja en px, desviación, bordes, luminancia y variante de logo.
- Variante: luminancia < 0.35 → blanco (`Pedro_Logo_blanco_transparente_HD.png`); > 0.60 → color (`pedro-lopez-logo-fondo-transparente.png`); intermedio → revisar (negro `Pedro_Logo_negro_sinfondo.png`).
- Código de salida 0 si hay candidato libre, 1 si no. Con `--json` entrega los datos para el skill del logo.

## Qué hacer si no hay espacio
1. Regenerar una vez cambiando el layout (de franja superior a inferior o al revés).
2. Editar en Codex: "deja lisa y uniforme la franja [superior/inferior]; no muevas nada más"; guardar `-v2`.
3. Si aun así falla, anotarlo en el `.md` y avisar.

## Reglas
- La franja es continuación lisa del fondo: sin personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos (un degradado muy suave está bien).
- Titular, apoyo y sujeto quedan fuera de la franja con al menos 4 % de margen.
- Nunca pedir al generador que dibuje un logo, marco, recuadro, leyenda o "espacio para logo".
- Fondo oscuro → logo blanco; claro → color o negro.
- Si un recorte posterior a 4:5 se come la franja, validar de nuevo.
- El 9 % inferior sin elementos críticos, por si luego se superpone el contacto.
