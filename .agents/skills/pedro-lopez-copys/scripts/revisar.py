#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""QA del documento de copys de Pedro López.

Uso: revisar.py <copys.md> [--esperar N] [--permitir-pendiente] [--fotos DIR]

Cada bloque: `### PL-NNA · …`, línea `- Foto: ruta`, línea `- Texto en la imagen: TITULAR "…" · APOYO "…"`
y `- COPY` seguido de un bloque ```text con el copy (cuerpo + contacto + hashtags).
Sale con código 1 si hay fallos.
"""
import argparse
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[4]
CONTACTO_MD = Path(__file__).resolve().parents[1] / "references" / "contacto.md"
FIJOS = ["#PedroLópezAsesorEnSeguros", "#TuTranquilidadEsNuestraPrioridad", "#SegurosMéxico"]
PROHIBIDAS = [
    r"gratis", r"gratuit", r"descuento", r"ahorr", r"el mejor", r"la mejor", r"n[uú]mero uno", r"mejor precio",
    r"oferta", r"promoci[oó]n", r"garantiz", r"el m[aá]s barato", r"sin costo",
    r"\bvos\b", r"\btenés\b", r"\bpodés\b", r"\bsos\b", r"\bquerés\b",
    r"\bgnp\b", r"qu[aá]litas", r"potos[ií]", r"metlife", r"\bana seguros\b",
    r"accidente", r"choque", r"incendio", r"robo", r"hospital", r"muerte", r"luto", r"tragedia",
]
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿⭐✅]️?")


def norm(t):
    t = t.lower()
    for a, b in zip("áéíóúü", "aeiouu"):
        t = t.replace(a, b)
    return re.sub(r"[^a-zñ0-9 ]+", " ", t).split()


def leer_contacto():
    txt = CONTACTO_MD.read_text(encoding="utf-8")
    m = re.search(r"\|\s*DIRECCION\s*\|\s*(.+?)\s*\|", txt)
    direccion = m.group(1).strip() if m else "[DIRECCIÓN PENDIENTE]"
    bloque = f"Contáctanos:\n📍 {direccion}\n📲 375 107 2477 (llamada o WhatsApp)\n🌐 www.plseguros.mx"
    return direccion, bloque


def bloques(md):
    partes = re.split(r"(?m)^### (?=PL-)", md)[1:]
    for p in partes:
        cab = p.splitlines()[0]
        idm = re.match(r"(PL-\d{2}[A-Z])", cab)
        foto = re.search(r"- Foto:\s*`?([^\s`]+)`?", p)
        tit = re.search(r'TITULAR\s+"([^"]+)"', p)
        copy = re.search(r"- COPY[^\n]*\n+```text\n(.*?)```", p, re.S)
        yield dict(id=idm.group(1) if idm else cab, foto=foto.group(1) if foto else None,
                   titular=tit.group(1) if tit else "", copy=copy.group(1).strip() if copy else None)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("md")
    ap.add_argument("--esperar", type=int, default=20)
    ap.add_argument("--permitir-pendiente", action="store_true")
    ap.add_argument("--fotos", default="fotos-creada")
    a = ap.parse_args()

    direccion, contacto = leer_contacto()
    fallos = []
    def f(i, msg): fallos.append(f"{i}: {msg}")

    if "PENDIENTE" in direccion.upper() and not a.permitir_pendiente:
        f("contacto.md", "la dirección sigue como [DIRECCIÓN PENDIENTE]")

    bs = list(bloques(Path(a.md).read_text(encoding="utf-8")))
    if len(bs) != a.esperar:
        f("documento", f"se esperaban {a.esperar} bloques y hay {len(bs)}")

    prev = None
    for b in bs:
        i = b["id"]
        if b["copy"] is None:
            f(i, "no tiene bloque COPY en ```text"); prev = None; continue
        if b["foto"] and not (RAIZ / b["foto"]).exists():
            f(i, f"la foto {b['foto']} no existe")
        c = b["copy"]
        k = c.find("Contáctanos:")
        if k < 0:
            f(i, "falta el bloque de contacto"); prev = None; continue
        cuerpo, resto = c[:k].strip(), c[k:]
        bloque_c, _, tags = resto.partition("\n\n")
        if bloque_c.strip() != contacto:
            f(i, "el bloque de contacto no coincide exactamente con contacto.md")
        hashtags = re.findall(r"#\S+", tags)
        if tags.strip() != " ".join(hashtags):
            f(i, "después del contacto solo deben ir los hashtags")
        if not (4 <= len(hashtags) <= 8):
            f(i, f"hashtags {len(hashtags)} (deben ser 4–8)")
        for h in FIJOS:
            if h not in hashtags:
                f(i, f"falta el hashtag fijo {h}")
        emojis = EMOJI.findall(cuerpo)
        if not (1 <= len(emojis) <= 3):
            f(i, f"{len(emojis)} emojis en el cuerpo (deben ser 1–3)")
        low = cuerpo.lower()
        for pat in PROHIBIDAS:
            if re.search(pat, low):
                f(i, f"palabra/tema prohibido: /{pat}/")
        if re.search(r"[$%]|\d", cuerpo):
            f(i, "el cuerpo no debe llevar cifras, $ ni %")
        palabras = len(cuerpo.split())
        if palabras > 90:
            f(i, f"cuerpo de {palabras} palabras (máx. 90)")
        if b["titular"]:
            t = " ".join(norm(b["titular"])); cu = " ".join(norm(cuerpo))
            if t and t in cu:
                f(i, "repite el titular de la imagen palabra por palabra")
        lineas = [l for l in cuerpo.splitlines() if l.strip()]
        primera = norm(lineas[0])[:1] if lineas else []
        cta = " ".join(norm(lineas[-1])) if lineas else ""
        if prev:
            if primera and primera == prev[0]:
                f(i, "empieza con la misma palabra que la pieza anterior")
            if cta and cta == prev[1]:
                f(i, "repite el CTA de la pieza anterior")
        prev = (primera, cta)

    if fallos:
        print(f"{len(fallos)} fallo(s):")
        for x in fallos:
            print(" -", x)
        sys.exit(1)
    print(f"OK: {len(bs)} bloques sin fallos")


if __name__ == "__main__":
    main()
