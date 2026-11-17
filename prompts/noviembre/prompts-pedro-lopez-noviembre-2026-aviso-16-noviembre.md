# Pedro López — aviso de suspensión de labores · lunes 16 de noviembre de 2026

## Alcance y supuestos
- Una sola pieza (A). Aviso operativo independiente del calendario mensual; no es variación publicitaria de los mensajes del PDF.
- Datos del usuario: no se labora el lunes 16 de noviembre; se retoman actividades el martes 17. Días de la semana verificados (16 = lunes, 17 = martes).
- Temática: Revolución Mexicana (20 de noviembre; el lunes 16 es su día de descanso). Se interpreta de forma sobria y sin violencia: textiles tradicionales y sombrero de palma, con tricolor **atenuado** (salvia, crema, terracota) para respetar la paleta (sin rojo ni verde brillante). Sin armas, soldados, banderas, escudos ni texto.
- Texto impreso: titular + apoyo literales (12 palabras en total). No se imprime el año, motivo, teléfono ni web (el contacto va en el caption).
- Layout B (franja superior para el logo, fondo crema claro → logo en color). Salida 1080×1350 en `foto-sin-logo/`, sin logo.
- Sin variaciones pendientes de aprobación: el texto es el del usuario.

## Seguimiento
| ID | Archivo | Generada | Validada |
|---|---|---|---|
| PL-AV03A | `foto-sin-logo/PL-AV03A_aviso-no-laboramos-16-noviembre-2026.png` | [ ] | [ ] |

### PL-AV03A · lun 16 nov 2026 · Aviso operativo · Temática 20 de noviembre · Layout B
- Giro y escena: oficina empresarial mexicana tranquila y vacía con detalles de temática revolucionaria sobria. Ramo interno: no aplica.
- Texto impreso: TITULAR "No laboraremos el lunes 16 de noviembre" · APOYO "Retomamos actividades el martes 17" · Origen: texto del usuario.
- Logo: franja reservada superior · posición y variante finales: las da `validar.py` (se espera color sobre crema).
- Caption: «El lunes 16 de noviembre no laboraremos. Retomamos actividades el martes 17.\nGracias por tu comprensión.\nContáctanos: 375 107 2477 · www.plseguros.mx». CTA comercial y hashtags omitidos por ser aviso operativo.
- Archivo: `foto-sin-logo/PL-AV03A_aviso-no-laboramos-16-noviembre-2026.png`
- Estado: [ ] generada [ ] 1080×1350 [ ] zona OK [ ] texto OK

## PROMPT
```text
Uso: ads-marketing. Aviso de servicio para clientes de una asesoría de seguros mexicana.
FORMATO: una sola imagen vertical 4:5, destino final 1080 × 1350 px. Una única escena fotográfica editorial con tipografía integrada profesional y muy legible.
ESCENA: rincón de una oficina empresarial mexicana genérica, tranquila y ordenada, sin personas, con ambiente de pausa. Un único punto focal en el centro: un escritorio de madera cálida, despejado, con una silla de madera junto a él. Sobre el respaldo de la silla, un rebozo de algodón doblado con rayas finas en salvia #4A6B52, crema y terracota #A85C32; sobre el escritorio, un sombrero de palma tejido de ala ancha, sencillo y artesanal. Un pequeño jarrón de cerámica crema con ramas verdes discretas. Es un guiño cultural sobrio a la tradición mexicana del 20 de noviembre, sin armas, soldados, banderas, escudos ni símbolos políticos. Pared lisa crema cálido #F4E9D6 con textura de yeso muy sutil, sin detalles arquitectónicos identificables.
CÁMARA Y LUZ: plano medio editorial a la altura de los ojos, luz cálida de mañana entrando lateral desde fuera de cuadro, sombras suaves; materiales y texturas reales, fotografía sobria y cercana, sin aspecto de render.
COMPOSICIÓN: layout B, 40–50 % de aire visual. Capas verticales claras: franja superior lisa entre 0 % y 16 % del alto; escena (escritorio, silla, rebozo, sombrero, jarrón) centrada entre 22 % y 64 %; titular y apoyo entre 68 % y 86 %, centrados. Márgenes laterales de al menos 8 %. El 9 % inferior completamente libre de elementos críticos. Ningún objeto toca ni invade el texto ni la franja superior. El fondo detrás del texto es continuación uniforme de la pared crema, sin objetos.
ZONA RESERVADA: el 16 % superior del lienzo, a todo el ancho, es crema #F4E9D6 liso y uniforme, continuación natural de la pared, sin objetos, texto, sombras marcadas, ventanas, puertas, estantes ni líneas (un degradado muy suave de luz es aceptable). Separar al menos 4 % del alto cualquier elemento de esta franja. No dibujar nada que indique para qué se utilizará.
TEXTO IMPRESO: solo estos dos bloques literales, conservando exactamente su escritura, acentos y números:
TITULAR: "No laboraremos el lunes 16 de noviembre"
En serif Bitter Bold de gran tamaño, azul marino #1E3A6E, centrado, en dos líneas: "No laboraremos" y "el lunes 16 de noviembre".
APOYO: "Retomamos actividades el martes 17"
En sans Montserrat, azul marino #1E3A6E, centrado, debajo del titular con separación generosa, de tamaño suficiente para leerse en un teléfono. No añadir año ni más texto.
PALETA: crema #F4E9D6 como fondo dominante, azul marino #1E3A6E para el texto, madera cálida; acentos de textil en salvia #4A6B52 y terracota #A85C32 muy discretos; dorado #E8A33D opcional en un detalle mínimo (≤5 %). Sin rojo intenso, verde brillante, morado ni neón.
EVITAR: logos, nombre de marca, marcos, recuadros, tarjetas, botones, sellos, iconos, calendarios, relojes, flechas, destellos, adornos, banderas, escudos, armas, soldados, personas, fuego, humo, confeti. Sin teléfono, web, dirección, horarios, aseguradoras, coberturas ni explicaciones. Ningún texto legible adicional en muebles, objetos, paredes o pantallas. No collage ni cuadrícula. Una sola imagen terminada.
```

## Generación y entrega
Pendiente de generar en Codex (`image_gen`) con el PROMPT literal; luego:
`python3 .agents/skills/pedro-lopez-prompts-imagenes/scripts/validar.py foto-sin-logo/PL-AV03A_aviso-no-laboramos-16-noviembre-2026.png B --json`
y pasar `force_pos`, caja y variante de logo a `pedro-lopez-logo-branding`. Revisar el texto carácter por carácter: "No laboraremos", "el lunes 16 de noviembre", "Retomamos actividades el martes 17".


## Adaptación solicitada a historia 9:16 · 13 de noviembre de 2026
El usuario solicita generar esta pieza en formato historia 9:16. Esta entrega sustituye el tamaño 4:5 por **1080×1920 px**. Se conservan escena, texto literal, paleta y salida sin logo; se adapta la distribución para las zonas seguras de historias.

- Archivo previsto: `foto-sin-logo/PL-AV03A_aviso-no-laboramos-16-noviembre-2026-historia-1080x1920.png`.
- Estado: [x] generada [x] 1080×1920 [x] zona OK [x] texto OK.
- No usar el validador 4:5 con guardado: recortaría el formato solicitado.

### Prompt de historia
```text
Uso: ads-marketing. Aviso de servicio para clientes de una asesoría de seguros mexicana.
FORMATO: una sola imagen vertical de historia 9:16, destino final 1080 × 1920 px. Una única escena fotográfica editorial con tipografía integrada profesional y muy legible.
ESCENA: rincón de una oficina empresarial mexicana genérica, tranquila y ordenada, sin personas, con ambiente de pausa. Un único punto focal en el centro: un escritorio de madera cálida, despejado, con una silla de madera junto a él. Sobre el respaldo de la silla, un rebozo de algodón doblado con rayas finas en salvia #4A6B52, crema y terracota #A85C32; sobre el escritorio, un sombrero de palma tejido de ala ancha, sencillo y artesanal. Un pequeño jarrón de cerámica crema con ramas verdes discretas. Es un guiño cultural sobrio a la tradición mexicana del 20 de noviembre, sin armas, soldados, banderas, escudos ni símbolos políticos. Pared lisa crema cálido #F4E9D6 con textura de yeso muy sutil, sin detalles arquitectónicos identificables.
CÁMARA Y LUZ: plano medio editorial a la altura de los ojos, luz cálida de mañana entrando lateral desde fuera de cuadro, sombras suaves; materiales y texturas reales, fotografía sobria y cercana, sin aspecto de render.
COMPOSICIÓN: layout B adaptado a historia 9:16, 40–50 % de aire visual. Capas verticales claras: franja superior lisa entre 0 % y 24 % del alto; escena (escritorio, silla, rebozo, sombrero, jarrón) centrada entre 28 % y 60 %; titular y apoyo entre 65 % y 83 %, centrados. Márgenes laterales de al menos 8 %. Dejar los 240 px superiores y los 260 px inferiores sin texto importante para las interfaces de historias. Ningún objeto toca ni invade el texto ni la franja superior. El fondo detrás del texto es continuación uniforme de la pared crema, sin objetos. No estirar letras ni objetos.
ZONA RESERVADA: el 24 % superior del lienzo, a todo el ancho, es crema #F4E9D6 liso y uniforme, continuación natural de la pared, sin objetos, texto, sombras marcadas, ventanas, puertas, estantes ni líneas (un degradado muy suave de luz es aceptable). Permitir una futura colocación del logo entre y=260 e y=430, dentro de la zona segura. Separar al menos 4 % del alto cualquier elemento de esta franja. No dibujar nada que indique para qué se utilizará ni colocar un logo.
TEXTO IMPRESO: solo estos dos bloques literales, conservando exactamente su escritura, acentos y números:
TITULAR: "No laboraremos el lunes 16 de noviembre"
En serif Bitter Bold de gran tamaño, azul marino #1E3A6E, centrado, en dos líneas: "No laboraremos" y "el lunes 16 de noviembre".
APOYO: "Retomamos actividades el martes 17"
En sans Montserrat, azul marino #1E3A6E, centrado, debajo del titular con separación generosa, de tamaño suficiente para leerse en un teléfono. No añadir año ni más texto.
PALETA: crema #F4E9D6 como fondo dominante, azul marino #1E3A6E para el texto, madera cálida; acentos de textil en salvia #4A6B52 y terracota #A85C32 muy discretos; dorado #E8A33D opcional en un detalle mínimo (≤5 %). Sin rojo intenso, verde brillante, morado ni neón.
EVITAR: logos, nombre de marca, marcos, recuadros, tarjetas, botones, sellos, iconos, calendarios, relojes, flechas, destellos, adornos, banderas, escudos, armas, soldados, personas, fuego, humo, confeti. Sin teléfono, web, dirección, horarios, aseguradoras, coberturas ni explicaciones. Ningún texto legible adicional en muebles, objetos, paredes o pantallas. No collage ni cuadrícula. Una sola imagen terminada.
```

### Resultado de historia
Generada con `image_gen` y el prompt de historia anterior. Original conservado en `/Users/fernandomorales/.codex/generated_images/01a1d56b-8491-71a3-aa2f-f8289de5c892/exec-6de7e603-f319-4815-8308-49fb18e5975f.png`. Copiada a la ruta prevista y ajustada con `sips` a **1080×1920**, sin recortar. Revisión visual: una escena, ambos textos literales completos y correctos, sin logo ni palabras adicionales.

Validación del espacio sobre el lienzo 9:16, usando los mismos umbrales de luminancia y bordes del validador, sin su recorte 4:5:

| Archivo | force_pos | Caja px (x0,y0,x1,y1) | Variante de logo |
|---|---|---|---|
| `foto-sin-logo/PL-AV03A_aviso-no-laboramos-16-noviembre-2026-historia-1080x1920.png` | `arriba-centro` | `[350,260,730,430]` | color |

Zona libre: desviación 1.1, bordes 0.0 %, luminancia 0.85. Coordenadas referidas al lienzo de historia 1080×1920; la caja queda fuera de los 240 px superiores de interfaz. Logo pendiente de colocación.


## Edición solicitada: mayor temática de la Revolución Mexicana
El usuario pide un poco más de temática del día. Se autoriza añadir papel picado con locomotoras históricas y caballos, y un pequeño camino de mesa artesanal. Se mantiene el texto literal, la paleta atenuada y el formato historia sin logo. Esta edición conserva la imagen anterior.

- Archivo: `foto-sin-logo/PL-AV03A_aviso-no-laboramos-16-noviembre-2026-historia-tematica-1080x1920.png`.
- Original de `image_gen`: `/Users/fernandomorales/.codex/generated_images/01a1d56b-8491-71a3-aa2f-f8289de5c892/exec-00154cc8-725e-425f-a02e-da3e8d1ac8c4.png`.
- Estado: [x] generada [x] 1080×1920 [x] texto literal correcto [x] zona libre [x] revisión visual.
- Ajuste con `sips`: recorte centrado mínimo del fondo para 9:16 y escalado final, conservando los textos y objetos.

| Archivo | force_pos | Caja px | Variante de logo |
|---|---|---|---|
| `PL-AV03A_aviso-no-laboramos-16-noviembre-2026-historia-tematica-1080x1920.png` | `arriba-centro` | `[350,350,730,520]` | color |

Espacio medido sobre el lienzo de historia: desviación 0.8, bordes 0.0 %, luminancia 0.86. La caja queda debajo del papel picado y fuera de la interfaz superior.

### Prompt de edición temática
```text
Uso: ads-marketing. Edita la imagen adjunta para reforzar moderadamente la temática de la conmemoración de la Revolución Mexicana, manteniendo un aviso empresarial elegante y cálido.
IMAGEN OBJETIVO: el aviso vertical crema adjunto. Conservar la misma escena fotográfica, escritorio y silla de madera, sombrero de palma artesanal, rebozo, jarrón, luz natural, fondo crema y diseño. Una sola imagen final de historia 9:16, destino 1080×1920 px.
CAMBIO TEMÁTICO: añadir una guirnalda artesanal de papel picado a lo largo del borde superior, concentrada entre y=50 e y=220 a tamaño final. Papeles pequeños en azul marino, crema, salvia y terracota atenuados; calados tradicionales con siluetas de una locomotora de vapor histórica y un caballo sin jinete, alternados con patrones geométricos mexicanos. Sin letras ni cifras en el papel. Los motivos deben evocar de manera amable la época de la Revolución Mexicana. Añadir sobre un extremo del escritorio un pequeño camino de mesa de tejido artesanal mexicano, con franjas discretas en crema, salvia y terracota, en armonía con el rebozo ya presente. Mantener el sombrero de palma como protagonista. Integrar la decoración con materiales reales, sin aspecto de iconos superpuestos. Cantidad moderada: ambiente un poco más conmemorativo y claramente mexicano, sin saturación.
PRESERVAR EXACTAMENTE los dos únicos bloques de texto, su ortografía, posición, tamaño, azul marino y legibilidad:
"No laboraremos el lunes 16 de noviembre"
"Retomamos actividades el martes 17"
Titular serif bold, apoyo sans. Ninguna letra añadida, omitida o duplicada. No agregar el motivo ni el año.
ZONA PARA LOGO FUTURO: conservar completamente lisa, crema y sin ningún elemento la caja x=350 a 730, y=260 a 430 del lienzo final 1080×1920. No dibujar el logo ni un marcador. No colocar decoración sobre el texto. Mantener libres los 260 px inferiores.
Paleta crema #F4E9D6 dominante, texto azul marino #1E3A6E, madera cálida, salvia #4A6B52 y terracota #A85C32 discretos. Fotografía editorial realista, sombras suaves.
EVITAR: Día de Muertos, calaveras, cempasúchil, altares, pan de muerto, Halloween, banderas, escudos, símbolos políticos, armas, municiones, soldados, violencia, fuego, humo, personas, rojo intenso, verde brillante, morado, neón, confeti, marcos, tarjetas, sellos, botones, slogans, contacto, teléfonos, web, fechas adicionales o texto sobre objetos. No collage. Una sola imagen acabada.
```


## Edición solicitada: temática histórica más marcada
Solicitud del usuario: reforzar aún más la temática. Se incorpora un mural sepia integrado a la pared con una locomotora histórica, un caballo y dos figuras de época desarmadas. Papel picado, sombrero y textiles conservados; ramas del jarrón reducidas. Se conservan el aviso literal, el formato historia y las ediciones anteriores.

- Archivo: `foto-sin-logo/PL-AV03A_aviso-no-laboramos-16-noviembre-2026-historia-revolucion-1080x1920.png`.
- Herramienta: `image_gen`, edición de la historia temática anterior.
- Original: `/Users/fernandomorales/.codex/generated_images/01a1d56b-8491-71a3-aa2f-f8289de5c892/exec-51667a3c-4b14-4081-9e9c-eec8db21cd65.png`.
- Estado: [x] generada [x] 1080×1920 [x] texto literal completo y correcto [x] sin logo [x] revisión visual.
- Ajuste dimensional mínimo con `sips`, sin recorte; original conservado.

| Archivo | force_pos | Caja px | Variante de logo |
|---|---|---|---|
| `PL-AV03A_aviso-no-laboramos-16-noviembre-2026-historia-revolucion-1080x1920.png` | `arriba-izq` | `[90,310,470,480]` | color |

Espacio medido directamente sobre el lienzo de historia: desviación 4.2, bordes 0.0 %, luminancia 0.83. La caja libre final se sitúa a la izquierda, entre el papel picado y el mural; no colocar el logo sobre el tren.

### Prompt de edición histórica
```text
Uso: ads-marketing. Edita la imagen adjunta para que la conmemoración de la Revolución Mexicana se perciba mucho más claramente. Mantener el diseño profesional y cálido del aviso.
OBJETIVO DE EDICIÓN: la imagen adjunta de historia 9:16 con oficina rústica, sombrero y papel picado. Una sola imagen final vertical de historia, destino exacto 1080×1920 px.
CAMBIO PRINCIPAL: transformar la pared detrás del escritorio en una ambientación histórica conmemorativa de la Revolución Mexicana. Integrar sobre el yeso crema un mural pictórico realista en sepia cálido, con bordes suaves y acabado envejecido sutil, como una pintura que existe físicamente en la pared. El mural muestra de forma prominente una locomotora de vapor mexicana de principios del siglo XX, de tres cuartos, y al costado pequeñas siluetas históricas de un campesino con sombrero de ala ancha sosteniendo las riendas de un caballo, y una adelita con falda larga y rebozo, ambos desarmados y sin rostros identificables. Composición histórica serena y digna; nada bélico. Tren como motivo principal, claramente reconocible, con ruedas y frente visibles, sin letras, números, humo ni marcas. El mural queda en la zona media, aproximadamente x=100–1000, y=550–1000 en el lienzo final, detrás de los muebles, separado del texto y del área superior limpia. No una foto rectangular, no marco, no panel, no collage: pintura integrada a la pared real en una sola escena.
REFORZAR LA DECORACIÓN: conservar el papel picado superior de locomotoras y caballos, darle un poco más de presencia en azul marino, crema, salvia y terracota. Conservar el sombrero de palma grande sobre la mesa, el rebozo de la silla y el camino de mesa artesanal; hacer más visibles sus rayas tradicionales. Reducir la altura del jarrón y sus ramas para que no tapen el tren del mural. Luz cálida suave y texturas fotográficas reales. El resultado debe evocar la época revolucionaria mexicana más que una decoración mexicana genérica, con buen gusto empresarial.
PRESERVAR EXACTAMENTE los únicos textos impresos, sin cambiar escritura, números, tamaño, tipografías, posición ni legibilidad:
"No laboraremos el lunes 16 de noviembre"
"Retomamos actividades el martes 17"
Titular serif bold azul marino en la zona inferior, apoyo sans debajo. No añadir el nombre del día festivo, fechas históricas, año, horarios ni otros textos.
Mantener el fondo crema, la madera y los colores de marca: azul marino #1E3A6E, crema #F4E9D6, salvia #4A6B52 y terracota #A85C32. Mural en sepia apagado, con contraste suficiente para identificar el tren sin competir con el aviso.
Mantener lisa y totalmente libre la caja superior x=350–730, y=350–520 para un futuro logo; no dibujar logo ni marcador. Conservar al menos 260 px inferiores libres de elementos importantes, márgenes laterales amplios.
EVITAR armas, cartucheras, municiones, combate, violencia, fuego, humo, banderas, escudos, personajes políticos identificables, rostros detallados, personas reales dentro de la oficina, rojo intenso, verde brillante, morado y neón. Nada de Día de Muertos, calaveras, cempasúchil, altares, Halloween, confeti, slogans, contactos, teléfono, web, logos, marcos, tarjetas, botones ni texto adicional. No reinterpretar las palabras del aviso. Una sola escena final 9:16, no comparativa.
```


## Edición solicitada: mensaje más cálido
El usuario solicita que el mensaje no se sienta tan golpeado. Se suavizan la redacción y el peso tipográfico del aviso operativo, conservando la temática histórica aprobada y las fechas. Texto nuevo:

> Este lunes 16 de noviembre
> haremos una pausa
>
> Retomamos actividades el martes 17.
> Gracias por tu comprensión.

- Archivo: `foto-sin-logo/PL-AV03A_aviso-16-noviembre-2026-historia-mensaje-calido-1080x1920.png`.
- Herramienta: `image_gen`. Referencia de edición: original histórico `exec-51667a3c-4b14-4081-9e9c-eec8db21cd65.png`, recuperado de la carpeta de imágenes generadas.
- Nuevo original: `/Users/fernandomorales/.codex/generated_images/01a1d56b-8491-71a3-aa2f-f8289de5c892/exec-7e1d5e93-049a-4c67-916e-90c0c1b27ec7.png`.
- Estado: [x] generada [x] 1080×1920 [x] texto completo correcto [x] temática conservada [x] sin logo [x] revisión visual.
- Titular de menor tamaño y peso, apoyo con mayor aire y agradecimiento. Ajuste dimensional mínimo con `sips`, sin recorte; original conservado.

| Archivo | force_pos | Caja px | Variante de logo |
|---|---|---|---|
| `PL-AV03A_aviso-16-noviembre-2026-historia-mensaje-calido-1080x1920.png` | `arriba-izq` | `[90,310,470,480]` | color |

Zona libre verificada en el lienzo de historia: desviación 3.8, bordes 0.0 %, luminancia 0.83.

### Prompt de edición del mensaje
```text
Uso: ads-marketing. Edición precisa de texto y jerarquía tipográfica de un aviso.
IMAGEN OBJETIVO: la imagen histórica adjunta. Conservar exactamente su diseño y ambientación de la Revolución Mexicana: mural sepia con locomotora, caballo y figuras de época, papel picado, sombrero, muebles de madera, textiles, jarrón, luz cálida, fondo crema. No añadir ni quitar objetos. Una sola historia vertical 9:16, destino 1080×1920 px.
OBJETIVO: que el mensaje se perciba cálido, amable y sereno, con menor peso visual y más espacio entre líneas.
CAMBIO ÚNICO: reemplazar por completo el aviso inferior anterior por estos dos bloques literales:
TITULAR:
"Este lunes 16 de noviembre
haremos una pausa"
APOYO:
"Retomamos actividades el martes 17.
Gracias por tu comprensión."
No imprimir las comillas ni las etiquetas TITULAR y APOYO. Eliminar totalmente el texto "No laboraremos". No añadir más palabras.
TIPOGRAFÍA: título centrado en serif tipo Bitter Semibold, azul marino #1E3A6E, de peso moderado y tamaño aproximadamente 20 % menor al titular original, sin negritas excesivas. Las dos líneas del titular tienen una jerarquía equilibrada, sin agrandar una palabra aislada. Cuerpo centrado en sans tipo Montserrat Regular; la primera oración puede ocupar dos líneas si es necesario, y el agradecimiento en su propia línea debajo con un espacio generoso. Texto grande y cómodo de leer en móvil, con márgenes laterales de mínimo 9 %, amplio interlineado, acabado editorial delicado.
COMPOSICIÓN: conservar la escena en su sitio, con suave transición al fondo crema detrás del aviso. Organizar todos los textos aproximadamente entre y=1370 e y=1655 al tamaño final, dejando al menos 260 px inferiores libres de texto importante. Ajustar con cuidado el tamaño sin apretar las líneas. No colocar texto sobre los muebles ni el mural.
Conservar el área lisa para futuro logo en x=90–470, y=310–480. No colocar logo, marcos ni recuadros.
VERIFICAR carácter por carácter: "Este lunes 16 de noviembre", "haremos una pausa", "Retomamos actividades el martes 17.", "Gracias por tu comprensión." Acento correcto en comprensión. No cambiar fechas ni añadir año, motivo, teléfono, web, horarios o promesas. No alterar el mural ni agregar símbolos. Una sola imagen terminada.
```


## Edición solicitada: explicar el motivo del puente
El usuario solicita mencionar el puente del 16 de noviembre y acomodar mejor el mensaje. Se autoriza ampliar el aviso operativo para explicar el motivo; se mantiene el tono amable y el diseño histórico. Texto final:

> Con motivo del puente por la Revolución Mexicana, haremos una pausa el lunes 16 de noviembre.
>
> Retomamos actividades el martes 17.
>
> Gracias por tu comprensión.

- Archivo: `foto-sin-logo/PL-AV03A_aviso-puente-16-noviembre-2026-historia-1080x1920.png`.
- Herramienta: `image_gen`, edición del aviso cálido anterior.
- Original: `/Users/fernandomorales/.codex/generated_images/01a1d56b-8491-71a3-aa2f-f8289de5c892/exec-04c83526-658f-41d9-8a73-f9e883677a1b.png`.
- Estado: [x] generada [x] 1080×1920 [x] texto y acentos correctos [x] fechas conservadas [x] sin logo [x] revisión visual.
- Escena reducida y desplazada hacia arriba para dar espacio al motivo, la fecha y el regreso; jerarquía tipográfica moderada, agradecimiento separado. Ajuste dimensional mínimo con `sips`, sin recorte. Original conservado.

| Archivo | force_pos | Caja px | Variante de logo |
|---|---|---|---|
| `PL-AV03A_aviso-puente-16-noviembre-2026-historia-1080x1920.png` | `arriba-izq` | `[90,260,470,430]` | color |

Zona libre medida sobre el lienzo de historia: desviación 10.7, bordes 0.33 %, luminancia 0.8.

### Prompt del aviso con motivo del puente
```text
Uso: ads-marketing. Edición de texto y distribución para un aviso de atención al cliente.
IMAGEN OBJETIVO: la historia adjunta con mural sepia de locomotora de la Revolución Mexicana, papel picado, sombrero y muebles de madera. Conservar ese concepto aprobado y su ambiente cálido. Una sola imagen vertical de historia 9:16, destino 1080×1920 px.
SOLICITUD: explicar amablemente que la pausa se debe al puente por la Revolución Mexicana. Sustituir por completo el texto anterior por los siguientes tres párrafos literales. No omitir ni añadir palabras:
"Con motivo del puente por la
Revolución Mexicana,
haremos una pausa el
lunes 16 de noviembre."
"Retomamos actividades el martes 17."
"Gracias por tu comprensión."
No imprimir comillas ni números de párrafo. No conservar la oración anterior "Este lunes 16 de noviembre haremos una pausa".
JERARQUÍA Y TONO: aviso cálido, sereno, elegante, con tipografía de peso moderado y aire entre párrafos. Primer párrafo en serif tipo Bitter Medium de aproximadamente 43–48 px al tamaño final, centrado; destacar con semibold suave solo "Revolución Mexicana" y "lunes 16 de noviembre", sin cambiar su tamaño. Segundo y tercer párrafos en sans tipo Montserrat Regular de aproximadamente 36–40 px, centrados. El regreso puede distribuirse en dos líneas si hace falta. No usar negritas pesadas ni una palabra gigante. Azul marino #1E3A6E sobre crema #F4E9D6, máximo 82 % del ancho. Texto nítido, muy legible en un teléfono.
RECOMPOSICIÓN: ajustar la escena hacia arriba y reducir ligeramente su altura para liberar una zona crema uniforme para el texto aproximadamente entre y=1250 e y=1655. Mantener el tren completo y reconocible, los personajes históricos, el caballo, el sombrero y los textiles. Separar la escena del texto con un desvanecido natural y sutil, sin líneas ni cajas. Primer párrafo entre y=1250 y y=1490, regreso entre y=1530 y y=1580, agradecimiento entre y=1620 y y=1655. Dejar 260 px inferiores libres para la interfaz. No apretar ni sobreponer líneas. Márgenes laterales de al menos 90 px.
Conservar papel picado en el borde superior y espacio liso en x=90–470, y=310–480 para futuro logo. Sin logo ni marcador.
PALETA Y ESCENA: crema, azul marino, sepia cálido, madera, salvia y terracota discretos. Mantener el estilo fotográfico editorial y el mural pintado en la pared, sin marcos.
VERIFICAR exactamente: "Con motivo del puente por la", "Revolución Mexicana,", "haremos una pausa el", "lunes 16 de noviembre.", "Retomamos actividades el martes 17.", "Gracias por tu comprensión." Acentos en Revolución y comprensión.
No añadir año, horarios, datos históricos, teléfono, web, nombres de marca ni otros textos. Sin armas, violencia, banderas, símbolos políticos, personas reales en la oficina ni elementos de Día de Muertos. No collage ni comparativa. Una sola imagen acabada en formato 9:16.
```


## Corrección solicitada: puente en lugar de pausa
Texto final autorizado por la solicitud de sustituir pausa por puente:

> Con motivo de la Revolución Mexicana, tomaremos el puente del lunes 16 de noviembre.
>
> Retomamos actividades el martes 17.
>
> Gracias por tu comprensión.

- Archivo: `foto-sin-logo/PL-AV03A_aviso-puente-16-noviembre-2026-historia-1080x1920-v2.png`.
- Herramienta: `image_gen`, edición del aviso con motivo del puente anterior.
- Original: `/Users/fernandomorales/.codex/generated_images/01a1d56b-8491-71a3-aa2f-f8289de5c892/exec-c6cd854a-ad31-4f28-a32e-064cc37b80ed.png`.
- Estado: [x] generada [x] 1080×1920 verificado [x] texto literal revisado [x] diseño conservado [x] sin logo.
- Ajuste dimensional mínimo con `sips`, sin recorte. Original y edición anterior conservados.

### Prompt de corrección
```text
Uso: ads-marketing. Edición mínima de texto en el aviso adjunto.
La imagen adjunta es el objetivo de edición. Conservar exactamente toda la imagen: mural sepia de locomotora, caballo y figuras históricas, papel picado, sombrero, muebles, textiles, jarrón, colores, luz, fondo crema, márgenes, encuadre y distribución. Mantener una sola historia vertical 9:16, destino 1080×1920 px, sin logo.
CAMBIAR ÚNICAMENTE EL PRIMER PÁRRAFO. Sustituir el texto "Con motivo del puente por la Revolución Mexicana, haremos una pausa el lunes 16 de noviembre." por este texto literal, con los siguientes saltos de línea:
"Con motivo de la
Revolución Mexicana,
tomaremos el puente del
lunes 16 de noviembre."
No imprimir las comillas. Palabra solicitada: "puente". No usar la palabra "pausa" en ninguna parte. Imprimir "puente" una sola vez. Conservar el azul marino y el peso moderado del texto, serif tipo Bitter, centrado; mantener en semibold solo "Revolución Mexicana" y "lunes 16 de noviembre", con el mismo tamaño que antes. Conservar los cuatro renglones del primer párrafo, el interlineado y su posición.
PRESERVAR EXACTAMENTE LOS OTROS DOS PÁRRAFOS:
"Retomamos actividades el martes 17."
"Gracias por tu comprensión."
Conservar su tipografía sans, tamaño, posición y separación. No añadir ni eliminar palabras. Acentos correctos en Revolución y comprensión. No cambiar fechas. No añadir año, horario, contacto, motivo adicional ni elementos nuevos. Mantener la zona superior libre para futuro logo y el amplio margen inferior.
Una sola imagen final, sin marcos, recuadros, collage ni comparativa.
```
