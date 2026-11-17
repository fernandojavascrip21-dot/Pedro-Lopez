# Prompts de imágenes — Pedro López Seguros · Noviembre 2026

Estrategia: AXIS · Nueva estrategia de publicidad para Pedro López Seguros (dueños de negocios, empresarios y emprendedores).
Skill: `pedro-lopez-prompts-imagenes` · Formato de salida: **1080 × 1350 px** · Destino: `foto-sin-logo/` (sin logo; se coloca después con `pedro-lopez-logo-branding`).

> **Alcance vigente: SOLO PROPUESTA A.** Las 20 imágenes A están generadas y verificadas. Las B quedan excluidas por instrucción posterior del usuario; se detuvo su generación. Los prompts B se conservan como referencia; las imágenes B se eliminaron de `foto-sin-logo/` por instrucción del usuario.

## Supuestos
- 20 piezas (lun–vie, 2–27 nov 2026), una imagen por pieza (versión A) = 20 imágenes.
- Titular + apoyo impresos en la imagen; teléfono y web solo en el caption: `Contáctanos: 375 107 2477 · www.plseguros.mx`.
- El asesor no se muestra con rostro identificable; el protagonista es el empresario.
- Sin precios, descuentos, testimonios, aseguradoras ni coberturas nombradas.
- Generación de las variaciones A autorizada por la indicación del usuario. Los 6 mensajes del PDF están como literales (piezas 01, 05, 06, 13, 16, 17).
- Los giros y personas son ficticios. Los layouts A–D reservan una franja completa (superior o inferior, 16 % del alto) para el logo; la posición final se detecta con `scripts/validar.py` (ver `references/zona-logo.md`).

## Calendario y seguimiento
| ID | Fecha | Enfoque · Tipo | Giro | Layout | Archivo | Generada |
|---|---|---|---|---|---|---|
| PL-01A | lun 2 nov 2026 | E1 Mala atención · Problema | Ferretería de barrio | A (arriba (franja superior)) | `foto-sin-logo/PL-01A_agente-solo-renovar.png` | [ ] |
| PL-02A | mar 3 nov 2026 | E2 Precios y comparación · Solución | Despacho contable | B (arriba (franja superior)) | `foto-sin-logo/PL-02A_comparar-opciones.png` | [ ] |
| PL-03A | mié 4 nov 2026 | E3 Seguimiento y soluciones · Confianza | Taller mecánico ordenado | C (abajo (franja inferior)) | `foto-sin-logo/PL-03A_seguimiento-despues-firma.png` | [ ] |
| PL-04A | jue 5 nov 2026 | E4 Patrimonio empresarial · Beneficio | Panadería al amanecer | D (arriba (franja superior)) | `foto-sin-logo/PL-04A_negocio-equipo-patrimonio.png` | [ ] |
| PL-05A | vie 6 nov 2026 | E5 Atención personalizada y confianza · Problema | Restaurante antes de abrir | A (arriba (franja superior)) | `foto-sin-logo/PL-05A_hace-cuanto-revisa.png` | [ ] |
| PL-06A | lun 9 nov 2026 | E1 Mala atención · Solución | Oficina pyme | B (arriba (franja superior)) | `foto-sin-logo/PL-06A_negocio-no-puede-esperar.png` | [ ] |
| PL-07A | mar 10 nov 2026 | E2 Precios y comparación · Confianza | Distribuidora | C (abajo (franja inferior)) | `foto-sin-logo/PL-07A_punto-por-punto.png` | [ ] |
| PL-08A | mié 11 nov 2026 | E3 Seguimiento y soluciones · Beneficio | Carpintería | D (arriba (franja superior)) | `foto-sin-logo/PL-08A_soluciones-claras.png` | [ ] |
| PL-09A | jue 12 nov 2026 | E4 Patrimonio empresarial · Problema | Minisúper | A (arriba (franja superior)) | `foto-sin-logo/PL-09A_tu-negocio-crecio.png` | [ ] |
| PL-10A | vie 13 nov 2026 | E5 Atención personalizada y confianza · Solución | Estética / barbería | B (arriba (franja superior)) | `foto-sin-logo/PL-10A_asesor-que-te-escucha.png` | [ ] |
| PL-11A | lun 16 nov 2026 | E1 Mala atención · Confianza | Tienda de telas | C (abajo (franja inferior)) | `foto-sin-logo/PL-11A_antes-durante-despues.png` | [ ] |
| PL-12A | mar 17 nov 2026 | E2 Precios y comparación · Beneficio | Transportista | D (arriba (franja superior)) | `foto-sin-logo/PL-12A_cobertura-adecuada.png` | [ ] |
| PL-13A | mié 18 nov 2026 | E3 Seguimiento y soluciones · Problema | Oficina al final del día | A (arriba (franja superior)) | `foto-sin-logo/PL-13A_soluciones-no-excusas.png` | [ ] |
| PL-14A | jue 19 nov 2026 | E4 Patrimonio empresarial · Solución | Manufactura ligera | B (arriba (franja superior)) | `foto-sin-logo/PL-14A_protege-local-equipo.png` | [ ] |
| PL-15A | vie 20 nov 2026 | E5 Atención personalizada y confianza · Confianza | Cafetería | C (abajo (franja inferior)) | `foto-sin-logo/PL-15A_confianza-con-atencion.png` | [ ] |
| PL-16A | lun 23 nov 2026 | E1 Mala atención · Beneficio | Taller de costura | D (arriba (franja superior)) | `foto-sin-logo/PL-16A_mas-que-una-poliza.png` | [ ] |
| PL-17A | mar 24 nov 2026 | E2 Precios y comparación · Problema | Escritorio de pequeña empresa | A (arriba (franja superior)) | `foto-sin-logo/PL-17A_pagando-demasiado.png` | [ ] |
| PL-18A | mié 25 nov 2026 | E3 Seguimiento y soluciones · Solución | Bodega | B (arriba (franja superior)) | `foto-sin-logo/PL-18A_entender-tu-poliza.png` | [ ] |
| PL-19A | jue 26 nov 2026 | E4 Patrimonio empresarial · Confianza | Estudio creativo | C (abajo (franja inferior)) | `foto-sin-logo/PL-19A_tu-equipo-patrimonio.png` | [ ] |
| PL-20A | vie 27 nov 2026 | E5 Atención personalizada y confianza · Beneficio | Vivero | D (arriba (franja superior)) | `foto-sin-logo/PL-20A_tranquilidad-enfocarte.png` | [ ] |

## Prompts

### PL-01A · lun 2 nov 2026 · E1 Mala atención · Problema · Layout A
- Giro y escena: Ferretería de barrio. Ramo interno (no se imprime): PyME / daños.
- Texto impreso: TITULAR "¿Tu agente de seguros solo aparece cuando toca renovar?" · APOYO "Revisa tu póliza con un asesor que te acompaña." · Origen: PDF literal.
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: blanco. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: ¿Cuándo fue la última vez que tu asesor te buscó sin que tuvieras que pedirlo? Tu negocio merece acompañamiento todo el año, no solo en la renovación. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-01A_agente-solo-renovar.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: una dueña de ferretería de unos 50 años, delantal azul grisáceo, de pie tras un mostrador de madera; sostiene su celular con la pantalla en espera (sin texto) y mira hacia la puerta con gesto sereno y pensativo; estantes ordenados de herramientas al fondo, muy desenfocados. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 35 mm, f/2.8, a la altura de los ojos; luz natural cálida y lateral de la tarde. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en la mitad derecha del encuadre, por debajo de la franja; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro lateral liso pintado en azul marino #1E3A6E, ligeramente desenfocado). La composición se organiza en capas verticales: 0–16 % franja libre; 28–48 % bloque de texto a la izquierda; 30–84 % sujeto a la derecha y al centro. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "¿Tu agente de seguros solo aparece cuando toca renovar?" en tipografía serif bold tipo Bitter, color blanco #FFFFFF, máximo 3 líneas, colocado a la izquierda, entre el 28 % y el 48 % de la altura, con ancho máximo del 55 % del lienzo; apoyo "Revisa tu póliza con un asesor que te acompaña." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie oscura, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-02A · mar 3 nov 2026 · E2 Precios y comparación · Solución · Layout B
- Giro y escena: Despacho contable. Ramo interno (no se imprime): Vida / GMM colectivo.
- Texto impreso: TITULAR "Comparar opciones también es cuidar tu empresa." · APOYO "Te ayudamos a revisar tu póliza." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: color. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Comparar coberturas y condiciones te da claridad para decidir. Te ayudamos a revisar tu póliza actual y a encontrar la protección adecuada para tu empresa. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-02A_comparar-opciones.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano por encima del hombro: un contador de unos 45 años y un asesor de espaldas, fuera de foco en primer plano, revisan dos carpetas crema abiertas sobre un escritorio claro; ventana luminosa al fondo. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 50 mm, f/2.8; luz de mañana difusa por la ventana. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal centrado entre el 22 % y el 64 % de la altura; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro crema #F4E9D6 liso y luminoso). La composición se organiza en capas verticales: 0–16 % franja libre; 22–64 % sujeto centrado; 68–86 % bloque de texto. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Comparar opciones también es cuidar tu empresa." en tipografía serif bold tipo Bitter, color azul navy profundo #12244A, máximo 3 líneas, colocado centrado en el tercio inferior, entre el 68 % y el 86 % de la altura; apoyo "Te ayudamos a revisar tu póliza." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie clara, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-03A · mié 4 nov 2026 · E3 Seguimiento y soluciones · Confianza · Layout C
- Giro y escena: Taller mecánico ordenado. Ramo interno (no se imprime): Auto / flotilla.
- Texto impreso: TITULAR "Seguimiento también después de firmar." · APOYO "Revisa tu seguro con un asesor que responde." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada inferior 84–100 % (lienzo 1080×1350) · posición esperada: abajo (franja inferior) · variante sugerida: blanco. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Contratar es solo el primer paso. Contigo antes, durante y después: seguimiento real para que tu póliza siga siendo la adecuada. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-03A_seguimiento-despues-firma.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: el dueño de un taller mecánico, de unos 55 años, overol azul limpio, estrecha la mano de un asesor visto de espaldas con camisa clara; taller impecable y ordenado al fondo. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 35 mm, f/2.8; luz cálida de media mañana. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en el lado izquierdo y la franja media, sin bajar del 82 % de la altura; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja inferior completa (del 84 % de la altura al borde inferior, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (el piso de concreto pulido, liso y de tono medio-oscuro). La composición se organiza en capas verticales: 8–28 % bloque de texto a la izquierda; 30–82 % sujeto; 84–100 % franja libre. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Seguimiento también después de firmar." en tipografía serif bold tipo Bitter, color blanco #FFFFFF, máximo 3 líneas, colocado arriba a la izquierda, entre el 8 % y el 28 % de la altura, con ancho máximo del 60 % del lienzo; apoyo "Revisa tu seguro con un asesor que responde." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie oscura, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-04A · jue 5 nov 2026 · E4 Patrimonio empresarial · Beneficio · Layout D
- Giro y escena: Panadería al amanecer. Ramo interno (no se imprime): PyME + vida de grupo.
- Texto impreso: TITULAR "Tu negocio, tu equipo, tu patrimonio." · APOYO "Cotiza la protección que tu negocio necesita." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: color. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: En Pedro López Seguros no solo buscamos ofrecerte una póliza. Queremos acompañarte, atenderte y ayudarte a encontrar la protección que tu negocio necesita. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-04A_negocio-equipo-patrimonio.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: el dueño de una panadería de unos 48 años y dos empleados (una mujer joven y un hombre mayor), delantales claros, acomodan pan sobre una mesa de acero; luz de amanecer cálida. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 35 mm, f/2.8; luz dorada baja entrando por la ventana. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en el centro-izquierda del encuadre, por debajo de la franja; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro blanco liso de azulejo mate sin juntas visibles). La composición se organiza en capas verticales: 0–16 % franja libre; 24–68 % sujeto al centro-izquierda; 72–88 % bloque de texto. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Tu negocio, tu equipo, tu patrimonio." en tipografía serif bold tipo Bitter, color azul navy profundo #12244A, máximo 3 líneas, colocado abajo a la izquierda, entre el 72 % y el 88 % de la altura, con ancho máximo del 60 % del lienzo; apoyo "Cotiza la protección que tu negocio necesita." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie clara, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-05A · vie 6 nov 2026 · E5 Atención personalizada y confianza · Problema · Layout A
- Giro y escena: Restaurante antes de abrir. Ramo interno (no se imprime): General.
- Texto impreso: TITULAR "¿Hace cuánto que tu agente no revisa si tu seguro sigue siendo adecuado?" · APOYO (ninguno) · Origen: PDF literal.
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: blanco. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Tu negocio cambia, tus necesidades también. Revisa si tu seguro sigue siendo el adecuado. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-05A_hace-cuanto-revisa.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: el dueño de un restaurante, de unos 52 años, sentado en una mesa del comedor vacío con una carpeta crema cerrada frente a él, mirada pensativa y serena; mesas puestas y luz cálida. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 50 mm, f/2.2; luz de ventana cálida. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en la mitad derecha del encuadre, por debajo de la franja; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro liso azul marino #1E3A6E). La composición se organiza en capas verticales: 0–16 % franja libre; 28–48 % bloque de texto a la izquierda; 30–84 % sujeto a la derecha y al centro. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "¿Hace cuánto que tu agente no revisa si tu seguro sigue siendo adecuado?" en tipografía serif bold tipo Bitter, color blanco #FFFFFF, máximo 4 líneas, colocado a la izquierda, entre el 28 % y el 48 % de la altura, con ancho máximo del 55 % del lienzo. Sin texto de apoyo. La zona del titular es una superficie oscura, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-06A · lun 9 nov 2026 · E1 Mala atención · Solución · Layout B
- Giro y escena: Oficina pyme. Ramo interno (no se imprime): General.
- Texto impreso: TITULAR "Tu negocio no puede esperar días para recibir una respuesta." · APOYO (ninguno) · Origen: PDF literal.
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: color. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Cuando surge un tema con tu seguro necesitas una respuesta, no una espera. Atención que escucha, responde y acompaña. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-06A_negocio-no-puede-esperar.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: una empresaria de unos 38 años en una oficina pyme luminosa, atiende una llamada con auricular y gesto sereno mientras mira su laptop (pantalla no visible). Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 35 mm, f/2.8; luz natural suave de ventana. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal centrado entre el 22 % y el 64 % de la altura; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro crema liso y luminoso). La composición se organiza en capas verticales: 0–16 % franja libre; 22–64 % sujeto centrado; 68–86 % bloque de texto. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Tu negocio no puede esperar días para recibir una respuesta." en tipografía serif bold tipo Bitter, color azul navy profundo #12244A, máximo 4 líneas, colocado centrado en el tercio inferior, entre el 68 % y el 86 % de la altura. Sin texto de apoyo. La zona del titular es una superficie clara, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-07A · mar 10 nov 2026 · E2 Precios y comparación · Confianza · Layout C
- Giro y escena: Distribuidora. Ramo interno (no se imprime): Flotilla.
- Texto impreso: TITULAR "Revisamos tu póliza contigo, punto por punto." · APOYO "Compara opciones con claridad." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada inferior 84–100 % (lienzo 1080×1350) · posición esperada: abajo (franja inferior) · variante sugerida: blanco. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Una buena cobertura se entiende. Revisamos tu póliza contigo, punto por punto, y comparamos opciones con claridad. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-07A_punto-por-punto.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano general: patio de una distribuidora con tres camionetas blancas sin rotular y sin placas legibles; el encargado con una tablet (pantalla sin contenido legible) y un asesor de espaldas conversan en primer plano. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 35 mm, f/4; luz de mañana clara. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en el lado izquierdo y la franja media, sin bajar del 82 % de la altura; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja inferior completa (del 84 % de la altura al borde inferior, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (el piso de concreto liso y de tono medio, uniforme). La composición se organiza en capas verticales: 8–28 % bloque de texto a la izquierda; 30–82 % sujeto; 84–100 % franja libre. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Revisamos tu póliza contigo, punto por punto." en tipografía serif bold tipo Bitter, color blanco #FFFFFF, máximo 3 líneas, colocado arriba a la izquierda, entre el 8 % y el 28 % de la altura, con ancho máximo del 60 % del lienzo; apoyo "Compara opciones con claridad." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie oscura, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-08A · mié 11 nov 2026 · E3 Seguimiento y soluciones · Beneficio · Layout D
- Giro y escena: Carpintería. Ramo interno (no se imprime): PyME / daños.
- Texto impreso: TITULAR "Soluciones claras para seguir trabajando." · APOYO "Revisa tu seguro sin complicaciones." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: color. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Para que tú sigas trabajando, tu seguro debe ser claro y estar bien atendido. Si tienes dudas con tu póliza, aquí hay soluciones. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-08A_soluciones-claras.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: un carpintero de unos 55 años lija con calma una pieza de madera, concentrado y tranquilo; virutas finas en el aire, taller ordenado. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 50 mm, f/2.5; luz de ventana lateral cálida. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en el centro-izquierda del encuadre, por debajo de la franja; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (una pared clara y lisa de taller, pintada en crema). La composición se organiza en capas verticales: 0–16 % franja libre; 24–68 % sujeto al centro-izquierda; 72–88 % bloque de texto. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Soluciones claras para seguir trabajando." en tipografía serif bold tipo Bitter, color azul navy profundo #12244A, máximo 3 líneas, colocado abajo a la izquierda, entre el 72 % y el 88 % de la altura, con ancho máximo del 60 % del lienzo; apoyo "Revisa tu seguro sin complicaciones." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie clara, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-09A · jue 12 nov 2026 · E4 Patrimonio empresarial · Problema · Layout A
- Giro y escena: Minisúper. Ramo interno (no se imprime): PyME.
- Texto impreso: TITULAR "Tu negocio creció. ¿Tu seguro también?" · APOYO "Revisa si tu póliza sigue siendo adecuada." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: blanco. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Más productos, más equipo, más metros: tu patrimonio crece y tu protección debe crecer con él. Revisa si tu póliza sigue siendo la adecuada. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-09A_tu-negocio-crecio.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: el dueño de un minisúper, de unos 42 años, de pie frente a sus anaqueles ordenados, mira su local con orgullo pensativo; productos genéricos sin etiquetas legibles. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 35 mm, f/2.8; luz cálida de interior. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en la mitad derecha del encuadre, por debajo de la franja; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro liso azul marino #1E3A6E). La composición se organiza en capas verticales: 0–16 % franja libre; 28–48 % bloque de texto a la izquierda; 30–84 % sujeto a la derecha y al centro. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Tu negocio creció. ¿Tu seguro también?" en tipografía serif bold tipo Bitter, color blanco #FFFFFF, máximo 3 líneas, colocado a la izquierda, entre el 28 % y el 48 % de la altura, con ancho máximo del 55 % del lienzo; apoyo "Revisa si tu póliza sigue siendo adecuada." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie oscura, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-10A · vie 13 nov 2026 · E5 Atención personalizada y confianza · Solución · Layout B
- Giro y escena: Estética / barbería. Ramo interno (no se imprime): General.
- Texto impreso: TITULAR "Un asesor que te escucha y te acompaña." · APOYO "Cotiza con atención personalizada." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: color. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Cada negocio es distinto. Te escuchamos primero y te acompañamos después para encontrar el seguro que sí te conviene. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-10A_asesor-que-te-escucha.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano por encima del hombro: la dueña de una estética, de unos 35 años, conversa relajada con un asesor de espaldas, desenfocado en primer plano; local luminoso y limpio. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 50 mm, f/2.2; luz natural cálida. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal centrado entre el 22 % y el 64 % de la altura; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro crema liso y luminoso). La composición se organiza en capas verticales: 0–16 % franja libre; 22–64 % sujeto centrado; 68–86 % bloque de texto. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Un asesor que te escucha y te acompaña." en tipografía serif bold tipo Bitter, color azul navy profundo #12244A, máximo 3 líneas, colocado centrado en el tercio inferior, entre el 68 % y el 86 % de la altura; apoyo "Cotiza con atención personalizada." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie clara, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-11A · lun 16 nov 2026 · E1 Mala atención · Confianza · Layout C
- Giro y escena: Tienda de telas. Ramo interno (no se imprime): PyME.
- Texto impreso: TITULAR "Atención antes, durante y después de contratar." · APOYO "Revisa tu seguro con nosotros." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada inferior 84–100 % (lienzo 1080×1350) · posición esperada: abajo (franja inferior) · variante sugerida: blanco. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Tu asesor no debería desaparecer después de la firma. Atención antes, durante y después de contratar. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-11A_antes-durante-despues.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: un asesor visto de espaldas visita una tienda de telas; la dueña, de unos 58 años, le muestra un rollo de tela y sonríe con calidez. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 35 mm, f/2.8; luz cálida de ventana. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en el lado izquierdo y la franja media, sin bajar del 82 % de la altura; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja inferior completa (del 84 % de la altura al borde inferior, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (el piso de madera oscura, liso y uniforme). La composición se organiza en capas verticales: 8–28 % bloque de texto a la izquierda; 30–82 % sujeto; 84–100 % franja libre. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Atención antes, durante y después de contratar." en tipografía serif bold tipo Bitter, color blanco #FFFFFF, máximo 3 líneas, colocado arriba a la izquierda, entre el 8 % y el 28 % de la altura, con ancho máximo del 60 % del lienzo; apoyo "Revisa tu seguro con nosotros." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie oscura, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-12A · mar 17 nov 2026 · E2 Precios y comparación · Beneficio · Layout D
- Giro y escena: Transportista. Ramo interno (no se imprime): Transporte / camión.
- Texto impreso: TITULAR "La cobertura adecuada a un precio competitivo." · APOYO "Compara y cotiza para tu empresa." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: color. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Compara opciones y encuentra una cobertura adecuada a un precio competitivo para tus unidades y tu empresa. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-12A_cobertura-adecuada.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: un transportista de unos 50 años junto a un camión de caja blanco, limpio y sin rotular, mira con serenidad hacia el frente en un andén; luz de mañana. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 35 mm, f/2.8; luz de mañana clara. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en el centro-izquierda del encuadre, por debajo de la franja; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro de andén liso, claro y uniforme). La composición se organiza en capas verticales: 0–16 % franja libre; 24–68 % sujeto al centro-izquierda; 72–88 % bloque de texto. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "La cobertura adecuada a un precio competitivo." en tipografía serif bold tipo Bitter, color azul navy profundo #12244A, máximo 3 líneas, colocado abajo a la izquierda, entre el 72 % y el 88 % de la altura, con ancho máximo del 60 % del lienzo; apoyo "Compara y cotiza para tu empresa." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie clara, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-13A · mié 18 nov 2026 · E3 Seguimiento y soluciones · Problema · Layout A
- Giro y escena: Oficina al final del día. Ramo interno (no se imprime): General.
- Texto impreso: TITULAR "Cuando tienes un problema, necesitas soluciones, no excusas." · APOYO (ninguno) · Origen: PDF literal.
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: blanco. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Si tienes un problema con tu seguro, lo importante es que alguien te ayude a resolverlo. Soluciones, no excusas. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-13A_soluciones-no-excusas.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: un empresario de unos 46 años en su oficina al atardecer, un celular con llamada en altavoz sobre el escritorio, manos entrelazadas y mirada serena. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 50 mm, f/2.2; luz dorada cálida de ventana. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en la mitad derecha del encuadre, por debajo de la franja; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro liso azul marino #1E3A6E). La composición se organiza en capas verticales: 0–16 % franja libre; 28–48 % bloque de texto a la izquierda; 30–84 % sujeto a la derecha y al centro. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Cuando tienes un problema, necesitas soluciones, no excusas." en tipografía serif bold tipo Bitter, color blanco #FFFFFF, máximo 4 líneas, colocado a la izquierda, entre el 28 % y el 48 % de la altura, con ancho máximo del 55 % del lienzo. Sin texto de apoyo. La zona del titular es una superficie oscura, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-14A · jue 19 nov 2026 · E4 Patrimonio empresarial · Solución · Layout B
- Giro y escena: Manufactura ligera. Ramo interno (no se imprime): PyME / daños.
- Texto impreso: TITULAR "Protege tu local, tu equipo y tus vehículos." · APOYO "Cotiza una protección a la medida." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: color. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Local, equipo, colaboradores y vehículos: tu empresa tiene mucho que cuidar. Cotiza una protección a la medida. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-14A_protege-local-equipo.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano general: recorrido por una planta de manufactura ligera, ordenada y luminosa; una dueña de unos 50 años y un asesor de espaldas caminan entre mesas de trabajo. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 28 mm, f/4; luz amplia y difusa. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal centrado entre el 22 % y el 64 % de la altura; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro claro y liso, uniforme). La composición se organiza en capas verticales: 0–16 % franja libre; 22–64 % sujeto centrado; 68–86 % bloque de texto. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Protege tu local, tu equipo y tus vehículos." en tipografía serif bold tipo Bitter, color azul navy profundo #12244A, máximo 3 líneas, colocado centrado en el tercio inferior, entre el 68 % y el 86 % de la altura; apoyo "Cotiza una protección a la medida." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie clara, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-15A · vie 20 nov 2026 · E5 Atención personalizada y confianza · Confianza · Layout C
- Giro y escena: Cafetería. Ramo interno (no se imprime): General.
- Texto impreso: TITULAR "Confianza que se construye con atención." · APOYO "Cotiza con un asesor cercano." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada inferior 84–100 % (lienzo 1080×1350) · posición esperada: abajo (franja inferior) · variante sugerida: blanco. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: La confianza se gana con atención constante. Cercanía, claridad y seguimiento para ti y tu negocio. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-15A_confianza-con-atencion.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: la barra de una cafetería; el dueño, de unos 44 años, y un asesor de hombro conversan relajados con un café en la mano. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 35 mm, f/2.2; luz cálida de interior. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en el lado izquierdo y la franja media, sin bajar del 82 % de la altura; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja inferior completa (del 84 % de la altura al borde inferior, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (la madera oscura y lisa de la barra en la esquina inferior derecha). La composición se organiza en capas verticales: 8–28 % bloque de texto a la izquierda; 30–82 % sujeto; 84–100 % franja libre. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Confianza que se construye con atención." en tipografía serif bold tipo Bitter, color blanco #FFFFFF, máximo 3 líneas, colocado arriba a la izquierda, entre el 8 % y el 28 % de la altura, con ancho máximo del 60 % del lienzo; apoyo "Cotiza con un asesor cercano." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie oscura, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-16A · lun 23 nov 2026 · E1 Mala atención · Beneficio · Layout D
- Giro y escena: Taller de costura. Ramo interno (no se imprime): General.
- Texto impreso: TITULAR "Tu empresa necesita más que una póliza." · APOYO "Necesita un asesor que responda." · Origen: PDF literal.
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: color. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Tu empresa necesita más que una póliza: necesita un asesor que responda. Revisa tu seguro con quien te acompaña. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-16A_mas-que-una-poliza.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: la dueña de un taller de costura, de unos 52 años, trabaja en su máquina con mirada tranquila; telas en tonos suaves. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 50 mm, f/2.5; luz de ventana lateral. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en el centro-izquierda del encuadre, por debajo de la franja; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (una pared clara, lisa y cálida). La composición se organiza en capas verticales: 0–16 % franja libre; 24–68 % sujeto al centro-izquierda; 72–88 % bloque de texto. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Tu empresa necesita más que una póliza." en tipografía serif bold tipo Bitter, color azul navy profundo #12244A, máximo 3 líneas, colocado abajo a la izquierda, entre el 72 % y el 88 % de la altura, con ancho máximo del 60 % del lienzo; apoyo "Necesita un asesor que responda." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie clara, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-17A · mar 24 nov 2026 · E2 Precios y comparación · Problema · Layout A
- Giro y escena: Escritorio de pequeña empresa. Ramo interno (no se imprime): General.
- Texto impreso: TITULAR "¿Estás pagando demasiado por el seguro de tu empresa?" · APOYO "Compara antes de renovar." · Origen: PDF literal + apoyo variación (autorizada para generar A).
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: blanco. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Antes de renovar, compara. Una cobertura adecuada y un precio competitivo no tienen por qué estar peleados. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-17A_pagando-demasiado.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: un dueño de empresa de unos 50 años sentado ante su escritorio con una calculadora y una hoja borrosa sin cifras legibles; mirada pensativa y serena. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 50 mm, f/2.2; luz de ventana cálida. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en la mitad derecha del encuadre, por debajo de la franja; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro liso azul marino #1E3A6E). La composición se organiza en capas verticales: 0–16 % franja libre; 28–48 % bloque de texto a la izquierda; 30–84 % sujeto a la derecha y al centro. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "¿Estás pagando demasiado por el seguro de tu empresa?" en tipografía serif bold tipo Bitter, color blanco #FFFFFF, máximo 3 líneas, colocado a la izquierda, entre el 28 % y el 48 % de la altura, con ancho máximo del 55 % del lienzo; apoyo "Compara antes de renovar." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie oscura, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-18A · mié 25 nov 2026 · E3 Seguimiento y soluciones · Solución · Layout B
- Giro y escena: Bodega. Ramo interno (no se imprime): PyME.
- Texto impreso: TITULAR "Te ayudamos a entender tu póliza." · APOYO "Revisa tus coberturas con nosotros." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: color. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Una póliza debe entenderse. Te ayudamos a revisar tus coberturas y a resolver tus dudas con claridad. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-18A_entender-tu-poliza.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano general de una bodega ordenada; el encargado, de unos 40 años, y un asesor de espaldas revisan un portapapeles sin texto legible. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 28 mm, f/4; luz amplia y difusa. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal centrado entre el 22 % y el 64 % de la altura; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un muro claro y liso, uniforme). La composición se organiza en capas verticales: 0–16 % franja libre; 22–64 % sujeto centrado; 68–86 % bloque de texto. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Te ayudamos a entender tu póliza." en tipografía serif bold tipo Bitter, color azul navy profundo #12244A, máximo 3 líneas, colocado centrado en el tercio inferior, entre el 68 % y el 86 % de la altura; apoyo "Revisa tus coberturas con nosotros." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie clara, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-19A · jue 26 nov 2026 · E4 Patrimonio empresarial · Confianza · Layout C
- Giro y escena: Estudio creativo. Ramo interno (no se imprime): Vida / GMM colectivo.
- Texto impreso: TITULAR "Tu equipo también es parte de tu patrimonio." · APOYO "Cotiza protección para tus colaboradores." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada inferior 84–100 % (lienzo 1080×1350) · posición esperada: abajo (franja inferior) · variante sugerida: blanco. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: Quienes trabajan contigo son parte de lo que has construido. Cotiza protección para tus colaboradores. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-19A_tu-equipo-patrimonio.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: un equipo de cuatro personas diversas trabaja alrededor de una mesa con laptops (pantallas sin contenido legible) en un estudio creativo cálido. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 35 mm, f/2.8; luz natural cálida. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en el lado izquierdo y la franja media, sin bajar del 82 % de la altura; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja inferior completa (del 84 % de la altura al borde inferior, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (el piso liso de tono oscuro en la esquina inferior derecha). La composición se organiza en capas verticales: 8–28 % bloque de texto a la izquierda; 30–82 % sujeto; 84–100 % franja libre. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Tu equipo también es parte de tu patrimonio." en tipografía serif bold tipo Bitter, color blanco #FFFFFF, máximo 3 líneas, colocado arriba a la izquierda, entre el 8 % y el 28 % de la altura, con ancho máximo del 60 % del lienzo; apoyo "Cotiza protección para tus colaboradores." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie oscura, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

### PL-20A · vie 27 nov 2026 · E5 Atención personalizada y confianza · Beneficio · Layout D
- Giro y escena: Vivero. Ramo interno (no se imprime): PyME.
- Texto impreso: TITULAR "Tranquilidad para enfocarte en tu negocio." · APOYO "Cotiza tu seguro con atención personalizada." · Origen: Variación (autorizada para generar A).
- Logo: franja reservada superior 0–16 % (lienzo 1080×1350) · posición esperada: arriba (franja superior) · variante sugerida: color. La posición final y el `force_pos` los da `scripts/validar.py` tras generar.
- Caption: En Pedro López Seguros no solo buscamos ofrecerte una póliza. Queremos acompañarte, atenderte y ayudarte a encontrar la protección que tu negocio necesita. Contáctanos: 375 107 2477 · www.plseguros.mx
  #PedroLópezAsesorEnSeguros #TuTranquilidadEsNuestraPrioridad #SegurosMéxico #SegurosParaEmpresas
- Archivo: `foto-sin-logo/PL-20A_tranquilidad-enfocarte.png`
- Estado: [ ] generada  [ ] 1080×1350  [ ] zona OK  [ ] texto OK

```text
Imagen publicitaria vertical 4:5 (1080 x 1350 px), una sola escena fotográfica continua, sin paneles, sin cuadrícula y sin collage.
ESCENA: fotografía editorial realista, México; plano medio: el dueño de un vivero, de unos 55 años, con una regadera entre plantas al atardecer y sonrisa serena. Personas adultas ficticias y no reconocibles, piel con textura real, manos naturales, ropa cotidiana de trabajo, ambiente tranquilo y cálido. Cualquier asesor aparece sin rostro identificable.
CÁMARA Y LUZ: lente 50 mm, f/2.5; luz dorada de atardecer. Acabado profesional y humano, color natural.
COMPOSICIÓN: sujeto principal en el centro-izquierda del encuadre, por debajo de la franja; alrededor del 45 % del encuadre es respiro visual; márgenes de al menos 6 %; el 9 % inferior sin elementos importantes.
ZONA RESERVADA (crítica): la franja superior completa (del borde superior al 16 % de la altura, a todo lo ancho) es una continuación lisa, uniforme y sin detalle del fondo (un cielo claro y liso o una pared de invernadero clara, uniforme). La composición se organiza en capas verticales: 0–16 % franja libre; 24–68 % sujeto al centro-izquierda; 72–88 % bloque de texto. Nada entra en la franja libre, ni siquiera parcialmente: ni personas, objetos, estantes, plantas, ventanas, puertas, texto, líneas, bordes, sombras duras ni brillos; solo superficie lisa con, como mucho, un degradado muy suave de luz. El titular y el apoyo nunca invaden la franja. No dibujar ningún logotipo, marco, recuadro ni leyenda.
TEXTO IMPRESO (solo este, ortografía exacta con acentos y signos de apertura): titular "Tranquilidad para enfocarte en tu negocio." en tipografía serif bold tipo Bitter, color azul navy profundo #12244A, máximo 3 líneas, colocado abajo a la izquierda, entre el 72 % y el 88 % de la altura, con ancho máximo del 60 % del lienzo; apoyo "Cotiza tu seguro con atención personalizada." en sans-serif tipo Montserrat, más pequeño, debajo del titular. La zona del titular es una superficie clara, lisa y de poco detalle, lejos de rostros y manos. Ningún otro texto en la imagen: pantallas, papeles, cajas, letreros y vehículos sin texto legible ni marcas.
PALETA: azul marino #1E3A6E como ancla, dorado #E8A33D solo en un acento muy pequeño (menos del 5 %), crema #F4E9D6 y blancos cálidos.
EVITAR: choques, daños, incendios, hospitales, luto, enojo o angustia; iconos, escudos, destellos, tarjetas, botones o marcos; rojo, morado o neón; estilo 3D, ilustración o stock frío; logotipos de marcas o aseguradoras; personas famosas; manos deformes.
```

