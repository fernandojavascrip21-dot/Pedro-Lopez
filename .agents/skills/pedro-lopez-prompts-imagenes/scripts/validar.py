#!/usr/bin/env python3
"""Reescala una imagen a 1080x1350 (4:5) y detecta dónde hay espacio libre para el logo.

Uso: validar.py <imagen> [A|B|C|D] [--salida RUTA] [--json] [--no-guardar]

- Recorta al centro a 4:5 si hace falta y reescala a 1080x1350 (sobrescribe la imagen
  salvo que se use --salida o --no-guardar).
- Desliza una ventana del tamaño de la zona del logo por toda la imagen y puntúa cada
  posición por lisura (desviación de luminancia y bordes Canny). El texto del titular
  y los objetos cuentan como "ocupado" porque generan bordes.
- Prefiere lugares estratégicos: bordes superior/inferior y esquinas, lejos del centro.
- El layout (A|B|C|D) es solo una pista de lo que se pidió en el prompt: se informa si
  esa zona quedó libre, pero la propuesta sale de la detección.
Salida: código 0 si hay al menos un candidato libre, 1 si no.
"""
import argparse
import json
import sys

import cv2
import numpy as np
from PIL import Image

W, H = 1080, 1350
BW, BH = 380, 170          # ventana: cabe logo horizontal (~324x85) y apilado (~238x162)
PASO = 30
MAX_STD, MAX_BORDES = 14.0, 0.015
HINT = {  # layout del prompt -> franja/posición pedida (solo informativo)
    "A": "arriba", "B": "arriba", "C": "abajo", "D": "arriba",
}


def a_lienzo(img):
    ancho, alto = img.size
    objetivo = W / H
    if abs(ancho / alto - objetivo) > 0.005:
        if ancho / alto > objetivo:
            nuevo = round(alto * objetivo)
            x = (ancho - nuevo) // 2
            img = img.crop((x, 0, x + nuevo, alto))
        else:
            nuevo = round(ancho / objetivo)
            y = (alto - nuevo) // 2
            img = img.crop((0, y, ancho, y + nuevo))
    return img.resize((W, H), Image.LANCZOS)


def force_pos(x, y):
    cx, cy = x + BW / 2, y + BH / 2
    v = "arriba" if cy < H / 2 else "abajo"
    h = "izq" if cx < W / 3 else ("der" if cx > 2 * W / 3 else "centro")
    return f"{v}-{h}"


def variante(media):
    if media < 0.35:
        return "blanco"
    if media > 0.60:
        return "color"
    return "revisar (blanco/color/negro)"


def candidatos(gris, bordes):
    """Ventanas puntuadas, de mejor a peor. score menor = más libre y más estratégico."""
    # Imágenes integrales: media y varianza por ventana en O(1).
    g = gris.astype(np.float64)
    s1 = cv2.integral(g)
    s2 = cv2.integral(g * g)
    se = cv2.integral(bordes.astype(np.float64))

    def suma(ii, x, y):
        return ii[y + BH, x + BW] - ii[y, x + BW] - ii[y + BH, x] + ii[y, x]

    n = BW * BH
    res = []
    for y in range(0, H - BH + 1, PASO):
        for x in range(0, W - BW + 1, PASO):
            m = suma(s1, x, y) / n
            std = max(suma(s2, x, y) / n - m * m, 0.0) ** 0.5
            ed = suma(se, x, y) / n
            limpio = std / MAX_STD + ed / MAX_BORDES          # <= 2 cuando pasa ambos umbrales
            dist_borde = min(y, H - (y + BH)) / (H / 2)       # 0 en el borde, 1 en el centro
            score = limpio + 1.5 * dist_borde                  # preferir bordes y esquinas
            res.append(dict(x=x, y=y, std=std, bordes=ed, luma=m / 255.0, limpio=limpio, score=score))
    res.sort(key=lambda r: r["score"])
    return res


def top_sin_solape(res, k=3):
    elegidos = []
    for r in res:
        if all(abs(r["x"] - e["x"]) >= BW // 2 or abs(r["y"] - e["y"]) >= BH for e in elegidos):
            elegidos.append(r)
        if len(elegidos) == k:
            break
    return elegidos


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("imagen")
    ap.add_argument("layout", nargs="?", choices=sorted(HINT))
    ap.add_argument("--salida")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--no-guardar", action="store_true")
    a = ap.parse_args()

    img = a_lienzo(Image.open(a.imagen).convert("RGB"))
    destino = a.salida or a.imagen
    if not a.no_guardar:
        img.save(destino)

    gris = cv2.cvtColor(np.asarray(img), cv2.COLOR_RGB2GRAY)
    bordes = (cv2.Canny(gris, 60, 150) > 0)
    res = candidatos(gris, bordes)
    libres = [r for r in res if r["std"] <= MAX_STD and r["bordes"] <= MAX_BORDES]
    top = top_sin_solape(libres or res)

    out = []
    for r in top:
        out.append(dict(
            force_pos=force_pos(r["x"], r["y"]),
            caja=[r["x"], r["y"], r["x"] + BW, r["y"] + BH],
            desv_luma=round(r["std"], 1), bordes_pct=round(r["bordes"] * 100, 2),
            luminancia=round(r["luma"], 2), variante_logo=variante(r["luma"]),
            libre=r["std"] <= MAX_STD and r["bordes"] <= MAX_BORDES,
        ))

    ok = bool(libres)
    nota = ""
    if a.layout:
        esperada = HINT[a.layout]
        cumple = any(c["libre"] and c["force_pos"].startswith(esperada) for c in out)
        nota = (f"layout {a.layout}: franja '{esperada}' " + ("libre" if cumple else "NO quedó libre; se propone otro lugar"))

    if a.json:
        print(json.dumps(dict(archivo=destino, tamano=[W, H], ok=ok, nota=nota, candidatos=out),
                         ensure_ascii=False, indent=2))
    else:
        print(f"archivo : {destino}  ({W}x{H})")
        if nota:
            print(f"pista   : {nota}")
        for i, c in enumerate(out, 1):
            x0, y0, x1, y1 = c["caja"]
            print(f"{i}. {c['force_pos']:<14} caja x{x0}-{x1}, y{y0}-{y1} · desv {c['desv_luma']} · "
                  f"bordes {c['bordes_pct']} % · luma {c['luminancia']} · logo {c['variante_logo']}"
                  f"{'' if c['libre'] else '  (ocupado)'}")
        print("ESPACIO LIBRE ENCONTRADO" if ok else "SIN ESPACIO LIBRE: regenerar o editar el fondo")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
