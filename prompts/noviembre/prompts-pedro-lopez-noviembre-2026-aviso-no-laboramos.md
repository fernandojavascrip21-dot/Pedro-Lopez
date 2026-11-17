# Pedro López — aviso de suspensión de labores

## Alcance y supuestos
- Una sola pieza para el lunes 2 de noviembre de 2026; fecha y suspensión de labores indicadas por el usuario. El día de la semana corresponde a la fecha.
- Texto literal del usuario, dividido en titular y apoyo, con mayúscula inicial. No es una variación publicitaria de los mensajes del PDF.
- Aviso operativo independiente del calendario mensual; no se inventa motivo, horario, fecha de regreso ni atención alternativa.
- Generación con la herramienta integrada de imagen. Salida 1080×1350 en `foto-sin-logo/`, sin logo. Layout C.

## Seguimiento
| ID | Archivo | Generada | Validada |
|---|---|---|---|
| PL-AV01A | `foto-sin-logo/PL-AV01A_aviso-no-laboramos-02-noviembre-2026.png` | [x] | [x] |
| PL-AV01A (segunda generación solicitada) | `foto-sin-logo/PL-AV01A_aviso-no-laboramos-02-noviembre-2026-v2.png` | [x] | [x] |

### PL-AV01A · lun 2 nov 2026 · Aviso operativo · Layout C
- Giro y escena: oficina empresarial tranquila y vacía. Ramo interno: no aplica.
- Texto impreso: TITULAR "No vamos a laborar" · APOYO "Lunes 2 de noviembre" · Origen: texto indicado por el usuario.
- Logo: franja inferior detectada; `force_pos=abajo-izq`, caja `[150,1170,530,1340]`, variante blanca.
- Caption de acompañamiento: «El lunes 2 de noviembre no vamos a laborar.\nGracias por tu comprensión.\nContáctanos: 375 107 2477 · www.plseguros.mx».
- CTA comercial y hashtags omitidos por tratarse de un aviso operativo.
- Archivo: `foto-sin-logo/PL-AV01A_aviso-no-laboramos-02-noviembre-2026.png`.
- Estado: [x] generada [x] 1080×1350 [x] zona OK [x] texto OK

## PROMPT
```text
Uso: ads-marketing. Aviso de servicio para clientes de una asesoría de seguros mexicana.
FORMATO: una sola imagen vertical 4:5, destino final 1080 × 1350 px. Una única escena fotográfica editorial con tipografía integrada profesional y muy legible.
ESCENA: oficina empresarial mexicana genérica, tranquila y ordenada, sin personas. Un único punto focal discreto en el tercio medio-inferior derecho: una silla de oficina color azul marino junto a un escritorio de madera clara despejado. La escena sugiere una pausa en las actividades. Fondo de pared lisa azul marino profundo, con amplitud y serenidad, sin detalles arquitectónicos identificables.
CÁMARA Y LUZ: plano general editorial, perspectiva natural a la altura de los ojos, luz lateral cálida y suave fuera de cuadro; materiales reales, fotografía sobria y cercana, sin aspecto de render.
COMPOSICIÓN: layout C, 45–50 % de aire visual. Capas verticales claras: texto en el tercio superior entre 9 % y 34 % del alto; escena y silla discretas entre 40 % y 77 %; franja inferior lisa entre 84 % y 100 %. Mantener al menos 6 % de margen lateral. Dejar el 9 % inferior completamente libre de elementos críticos. La silla y el escritorio no invaden el texto ni la franja inferior. El fondo inferior es continuación natural uniforme del azul marino del fondo, sin borde ni separación.
ZONA RESERVADA: el 16 % inferior del lienzo a todo el ancho es azul marino #1E3A6E liso y uniforme, sin objetos, texto, sombras marcadas, ventanas, puertas ni líneas. Separar por al menos 4 % del alto cualquier elemento de esta franja. No dibujar nada que indique para qué se utilizará.
TEXTO IMPRESO: solo estos dos bloques literales, conservando exactamente su escritura:
TITULAR: "No vamos a laborar"
En serif Bitter Bold de gran tamaño, blanco crema, alineado a la izquierda, dos líneas como máximo. Distribuir "No vamos" en una línea y "a laborar" en la siguiente si hace falta.
APOYO: "Lunes 2 de noviembre"
En sans Montserrat, blanco crema, debajo del titular, con una separación generosa, de tamaño suficiente para leerlo en un teléfono. No añadir año ni más texto.
PALETA: azul marino #1E3A6E como ancla y fondo dominante, crema #F4E9D6 y blanco para texto y luz; madera cálida discreta. Sin necesidad de acento dorado.
EVITAR: logos, nombre de marca, marcos, recuadros, tarjetas, botones, sellos, iconos, calendarios, relojes, flechas, destellos, adornos, flores, velas, calaveras, motivos funerarios o festivos, rojo, morado o neón. Sin personas, teléfonos, web, direcciones, horarios, fecha de regreso, aseguradoras, coberturas ni explicaciones legales. Ningún texto legible adicional en muebles, documentos, paredes o pantallas. No collage ni cuadrícula. Una sola imagen terminada.
```

## Validación y entrega para logo
Generada con la herramienta integrada `image_gen`; original conservado en `/Users/fernandomorales/.codex/generated_images/01a18df8-8976-7c00-9732-81558503da61/exec-dbdbb866-8b57-4974-9de5-1b648110e9a7.png`.

Validación: 1080×1350 px, una escena, texto literal completo y legible, sin logo ni texto adicional. Espacio inferior apto para logo, sin colocarlo en esta etapa.

| Archivo | force_pos | Caja px (x0,y0,x1,y1) | Variante de logo |
|---|---|---|---|
| `foto-sin-logo/PL-AV01A_aviso-no-laboramos-02-noviembre-2026.png` | `abajo-izq` | `[150,1170,530,1340]` | blanco |

Detector: desviación de luminancia 1.0, bordes 0.0 %, luminancia 0.22; código de salida 0. La salida `--json` presentó un error de serialización de booleanos NumPy; se verificó con la salida normal del mismo validador y `--no-guardar`, sin modificar el script.

Sin texto omitido ni variaciones publicitarias pendientes de aprobar. La fecha y el aviso proceden de la solicitud del usuario.

## Segunda generación solicitada
Generada nuevamente con el mismo PROMPT literal y la herramienta integrada `image_gen`. Original: `/Users/fernandomorales/.codex/generated_images/01a18df8-8976-7c00-9732-81558503da61/exec-eeb35fb7-b251-45c4-a869-a53bc51648c2.png`.

Archivo nuevo conservando el anterior: `foto-sin-logo/PL-AV01A_aviso-no-laboramos-02-noviembre-2026-v2.png`.

Estado: [x] generada [x] 1080×1350 [x] zona OK [x] texto OK. Inspección visual: texto completo y correcto, legible, una sola escena, sin logo. Validador en salida normal: código 0.

| Archivo | force_pos | Caja px (x0,y0,x1,y1) | Variante de logo |
|---|---|---|---|
| `PL-AV01A_aviso-no-laboramos-02-noviembre-2026-v2.png` | `abajo-izq` | `[0,1170,380,1340]` | blanco |

Detector: desviación 1.9, bordes 0.0 %, luminancia 0.23. Zona libre inferior verificada; al colocar el logo se deben respetar los márgenes de marca.

## Imágenes finales con logo
Se añadió el logo horizontal blanco y dorado de `Logo/Pedro_Logo_blanco_v2.png` a ambos avisos mediante composición con la herramienta integrada `image_gen`, usando cada aviso como imagen de edición y el archivo original del logo como referencia. Ubicación: esquina inferior izquierda, sobre azul. El skill `pedro-lopez-logo-branding` no está instalado en las carpetas de skills disponibles; se usaron las reglas vigentes de marca y el logo existente.

Archivos finales, ambos a 1080×1350 px:
- `fotos-creada/PL-AV01A_aviso-no-laboramos-02-noviembre-2026.png`
- `fotos-creada/PL-AV01A_aviso-no-laboramos-02-noviembre-2026-v2.png`

Instrucción de edición: colocar una sola copia del logo original horizontal blanco y dorado en la franja inferior izquierda, manteniendo la transparencia, la proporción, el monograma PL y las leyendas «PEDRO LÓPEZ» y «ASESOR EN SEGUROS»; conservar el titular «No vamos a laborar» y el apoyo «Lunes 2 de noviembre», sin agregar contacto ni otros elementos. Una llamada independiente por imagen.

Revisión final: texto completo y correcto en ambos avisos, logo legible sobre azul, sin cajas ni fondo blanco, sin recortes del logo. Originales sin logo conservados en `foto-sin-logo/`. Los PNG editados originales se conservan en la carpeta de imágenes generadas con nombres `exec-8e2a6b4c-b052-4efe-b122-ce2bed5b8a86.png` y `exec-4d55d5b0-980d-481b-90a2-96ded9720c35.png`.

## Adaptación solicitada: Día de Muertos
El usuario solicita expresamente la temática de Día de Muertos. Se incorporan cempasúchil y papel picado como adaptación cultural autorizada, conservando el aviso, el logo y la paleta base. Esta instrucción sustituye las exclusiones de flores y motivos festivos del prompt inicial para estas dos ediciones.

Salidas previstas, conservando las imágenes anteriores:
- `fotos-creada/PL-AV01A_aviso-dia-de-muertos-02-noviembre-2026.png`
- `fotos-creada/PL-AV01A_aviso-dia-de-muertos-02-noviembre-2026-v2.png`

### Prompt de edición para cada aviso
```text
Uso: ads-marketing. Edición temática precisa de una imagen existente.
IMAGEN DE ENTRADA: aviso de oficina con el logo ya colocado. Mantén la misma escena, muebles, encuadre y diseño.
CAMBIO SOLICITADO: incorporar una temática mexicana de Día de Muertos, cálida, elegante y sobria, sin saturación.
ESCENA: sustituye únicamente la pequeña planta sobre el escritorio por un arreglo compacto natural de flores de cempasúchil naranja cálido en un recipiente sencillo de cerámica crema. Coloca unos pocos pétalos junto al arreglo sobre la madera. Añade una sola guirnalda ligera de papel picado artesanal en color crema y ámbar, con recortes florales tradicionales, a lo largo del borde superior en el espacio vacío por encima del titular. Los papeles deben ser discretos, pequeños, sin letras, sin tapar ni rozar el texto. El arreglo floral y el papel picado deben identificar claramente Día de Muertos con buen gusto profesional.
PRESERVAR EXACTAMENTE: el texto literal "No vamos a laborar" y "Lunes 2 de noviembre", su tamaño, tipografías, color crema, posición y legibilidad; el fondo azul marino; el escritorio y silla; y el logo completo original blanco y dorado abajo a la izquierda con su monograma PL, arcos y leyendas "PEDRO LÓPEZ" y "ASESOR EN SEGUROS", sin redibujarlo, cambiarlo ni moverlo. No añadir palabras, slogans, teléfonos, web ni fechas adicionales.
COMPOSICIÓN: una sola fotografía editorial vertical 4:5, salida final 1080×1350 px. Conservar abundante espacio negativo; decoración limitada al borde superior vacío y al pequeño arreglo sobre el escritorio. Mantener despejada la zona del logo y márgenes de seguridad. Luz natural cálida y suave, materiales reales.
PALETA: azul marino #1E3A6E dominante, crema y blanco; naranja cempasúchil y ámbar como acentos culturales mesurados. Sin morado, rojo ni neón.
EVITAR: Halloween, calabazas, murciélagos, telarañas, terror, cementerios, ataúdes, luto, personas, disfraces, altares recargados, efectos brillantes, iconos, tarjetas, recuadros, botones, collage y texto adicional. Una sola imagen terminada.
```

Estado de adaptación: [x] ambas generadas con `image_gen` [x] ambas 1080×1350 [x] texto correcto [x] logo legible [x] revisión visual final.

Resultado: cempasúchil naranja sobre el escritorio, pocos pétalos y papel picado crema/ámbar en la parte superior; fondo azul, aviso y logo conservados. Archivos guardados en las dos rutas previstas de `fotos-creada/`. Validador con código 0 para ambos. No se coloca un logo adicional: ya está integrado.

Originales de las ediciones en `/Users/fernandomorales/.codex/generated_images/01a18df8-8976-7c00-9732-81558503da61/`: `exec-ad201ee7-c02d-4514-9109-9ed1f57c3112.png` y `exec-1ffaf067-f243-4efd-93ac-a53e774e05a1.png`.

## Edición con mayor festividad
Solicitud: añadir un poco más de festividad. Se toma como base la última imagen entregada (`PL-AV01A_aviso-dia-de-muertos-02-noviembre-2026-v2.png`) y se conserva como archivo independiente.

Salida: `fotos-creada/PL-AV01A_aviso-dia-de-muertos-02-noviembre-2026-festiva.png`.

### Prompt de edición
```text
Uso: ads-marketing. Edita la imagen adjunta para aumentar moderadamente la festividad del Día de Muertos mexicano, conservando su calidad fotográfica profesional y su diseño.
La imagen adjunta es el objetivo de edición. Conserva exactamente el aviso "No vamos a laborar" y "Lunes 2 de noviembre", toda su ortografía, tamaño, posición, color y legibilidad. Conserva exactamente el logo original abajo a la izquierda, el monograma PL y los textos "PEDRO LÓPEZ" y "ASESOR EN SEGUROS", sin alteración. Mantén el fondo azul marino, el encuadre vertical, el escritorio y la silla de la oficina.
AUMENTAR FESTIVIDAD: haz el ramo de cempasúchil del escritorio un poco más abundante y exuberante; coloca a su lado una pequeña calaverita de azúcar artesanal blanca con detalles florales naranja, ámbar y teal apagado, expresión alegre y amable, nunca macabra, sin palabras. Añade un pequeño pan de muerto artesanal sobre un platito de barro claro junto al arreglo y unos pocos pétalos sobre la madera. Enriquece la guirnalda superior de papel picado con recortes tradicionales de flores y calaveritas amables en crema y naranja cempasúchil, manteniéndola estrictamente en el espacio del borde superior y sin tocar el titular. Incorpora al costado derecho de la escena un pequeño tramo vertical de guirnalda de cempasúchil, fuera de las letras y sin obstruir la silla. Que los nuevos elementos se sientan parte real y cuidada de la decoración temporal de una oficina mexicana.
Composición equilibrada con abundante aire; centro y fondo detrás del texto permanecen despejados. El ambiente es cálido, alegre, cultural y respetuoso. Luz natural de tarde suave, texturas reales. Paleta azul marino dominante con crema, naranja cempasúchil, ámbar y diminutos detalles teal apagado. No morado, rojo ni neón.
No añadas otros textos, contactos, slogans, personas, marcos, botones, etiquetas, confeti flotante ni efectos brillantes. No Halloween, terror, calabazas, murciélagos ni escenas funerarias. No saturar la composición ni cubrir el logo. Una sola imagen final vertical 4:5, 1080×1350 px.
```

Estado: [x] generada con `image_gen` [x] 1080×1350 [x] texto correcto [x] logo completo y legible [x] revisión visual final. Se incorporaron un ramo más abundante, una calaverita de azúcar, pan de muerto, pétalos y guirnaldas, conservando el espacio del aviso. Imagen anterior conservada.

Original generado: `/Users/fernandomorales/.codex/generated_images/01a18df8-8976-7c00-9732-81558503da61/exec-4e3ab228-a6f8-42f1-a64f-0a7fafd35f41.png`. Archivo final guardado en la ruta prevista de `fotos-creada/`.

## Aviso completo: excepción de texto autorizada
El usuario solicita expresamente más texto solo para esta pieza y proporciona el motivo y la fecha de regreso. Se adapta la redacción a futuro y se mantienen todos los datos: suspensión el lunes 2 de noviembre de 2026 y regreso el martes 3 de noviembre. Días de la semana verificados con el calendario. Esta autorización puntual sustituye el límite de titular y apoyo para esta edición.

Texto final:
> Aviso a nuestros clientes
>
> Con motivo de la celebración del Día de Muertos,
>
> suspenderemos nuestros servicios el lunes 2 de noviembre de 2026.
>
> Reanudaremos actividades el martes 3 de noviembre.

Base: `fotos-creada/PL-AV01A_aviso-dia-de-muertos-02-noviembre-2026-festiva.png`.
Salida: `fotos-creada/PL-AV01A_aviso-dia-de-muertos-2026-completo.png`.

### Prompt de edición
```text
Uso: ads-marketing. Edición de texto y composición de un aviso de servicio ya diseñado.
La imagen adjunta es el objetivo. Conserva el estilo fotográfico profesional de la oficina, el fondo azul marino #1E3A6E, la festividad mexicana del Día de Muertos con cempasúchil, papel picado, calaverita de azúcar y pan de muerto. Conserva intacto el logo horizontal original blanco y dorado abajo a la izquierda, incluyendo monograma PL y leyendas "PEDRO LÓPEZ" y "ASESOR EN SEGUROS", sin recrearlo ni moverlo.
CAMBIO PRINCIPAL: sustituye por completo el texto anterior "No vamos a laborar" y "Lunes 2 de noviembre" por el siguiente aviso completo, exactamente como se indica y sin repetir ningún bloque. Se autoriza más texto solo en esta imagen.
TEXTO IMPRESO LITERAL Y JERARQUÍA:
1. Encabezado grande serif bold tipo Bitter, crema, dos líneas:
"Aviso a nuestros
clientes"
2. Texto de introducción en sans Montserrat, crema, con buena separación:
"Con motivo de la celebración
del Día de Muertos,"
3. Mensaje de suspensión en sans Montserrat, crema, destacando en semibold la fecha:
"suspenderemos nuestros servicios
el lunes 2 de noviembre de 2026."
4. Mensaje de regreso en sans Montserrat, crema, con la fecha en semibold:
"Reanudaremos actividades
el martes 3 de noviembre."
No imprimir las comillas ni los números de esta lista. No añadir otras palabras.
COMPOSICIÓN: una sola imagen vertical 4:5, salida final 1080×1350 px. Texto alineado a la izquierda con margen de al menos 8 % del ancho. Encabezado en la zona 12–26 % del alto; introducción 30–36 %; suspensión 40–47 %; regreso 51–58 %. Tamaño de cuerpo de aproximadamente 35–40 px a tamaño final, fecha muy clara y legible en móvil. Interlineado amplio y espacios entre los tres párrafos. Jerarquía sobria y limpia, sin cajas ni botones. Mantener el papel picado dentro del 0–9 % superior, separado de las letras. Adaptar si es necesario la escena hacia abajo: escritorio a partir de 68 % del alto y arreglo de flores, calaverita y pan alrededor de 62–76 %, dejando completamente despejado y uniforme el fondo detrás de todo el texto. Las flores del borde derecho quedan confinadas al margen derecho, lejos de las letras. El logo permanece abajo a la izquierda, completo y legible, separado de los objetos. Mantener los muebles y las decoraciones como una sola escena natural.
PALETA: azul marino dominante, crema/blanco para el texto, naranja cempasúchil y dorado con pequeños detalles teal. Luz cálida natural. Acabado limpio, cercano, festivo y respetuoso.
VERIFICAR CARÁCTER POR CARÁCTER: "celebración", "Día de Muertos", "suspenderemos", "lunes 2 de noviembre de 2026", "Reanudaremos", "martes 3 de noviembre". No omitir ni duplicar palabras. No errores ortográficos. No texto sobre objetos ni sobre decoraciones. No contacto, teléfono, web, horario ni promesas adicionales. No Halloween, terror, luto ni personas. No collage. Una sola imagen terminada.
```

Estado del aviso completo: [x] generado con `image_gen` [x] 1080×1350 [x] texto completo revisado carácter por carácter [x] fechas correctas [x] logo legible [x] temática conservada. La suspensión y el regreso están destacados en negritas; composición reorganizada para admitir el texto adicional autorizado. Imagen previa conservada.

Original de la edición: `/Users/fernandomorales/.codex/generated_images/01a18df8-8976-7c00-9732-81558503da61/exec-3a979a9c-998c-4531-817d-e6dbcede8edc.png`.

## Diseño adicional: crema y bodegón festivo
Solicitud del usuario: otro diseño. Se conserva el aviso completo autorizado, las fechas y la temática. Nueva dirección: composición centrada, fondo crema, tipografía azul marino y bodegón cultural en el tercio inferior, con logo original a color. Se conserva la edición anterior.

Salida: `fotos-creada/PL-AV02A_aviso-dia-de-muertos-2026-crema.png`.
Referencias: aviso completo anterior (contenido) y `Logo/Pedro_Logo_sin_fondo_v2.png` (logo original).

### Prompt
```text
Uso: ads-marketing. Crea un diseño completamente nuevo de un aviso de Día de Muertos para clientes de Pedro López, Asesor en Seguros.
REFERENCIAS: Imagen 1 sirve exclusivamente para el contenido literal del aviso, el tono festivo mexicano y los datos. No conservar su composición de oficina. Imagen 2 es el logo original horizontal azul y dorado sobre transparencia: usar ese logo exacto sin reinterpretarlo, conservar monograma PL, arcos, tipografía y leyendas "PEDRO LÓPEZ" y "ASESOR EN SEGUROS".
DIRECCIÓN VISUAL: composición editorial cálida y elegante, fondo crema claro #F4E9D6 con textura de papel de algodón muy sutil. Tipografía azul marino #1E3A6E. Diseño centrado, equilibrado y con aire, radicalmente distinto del aviso de oficina azul. Un solo lienzo vertical 4:5, 1080×1350 px, profesional y perfectamente legible en un teléfono.
DECORACIÓN: una guirnalda pequeña de papel picado azul marino y ámbar en el borde superior, con recortes tradicionales de flores y pequeñas calaveritas amables, sin letras. En el tercio inferior, un bodegón fotográfico realista sobre superficie crema: un pequeño jarrón artesanal con cempasúchil naranja a la izquierda, una calaverita de azúcar blanca con finos detalles naranja y azul en el centro y un pan de muerto sobre barro claro a la derecha. Unos pocos pétalos sobre la superficie. Luz cálida natural lateral, sombras suaves, ambiente alegre y respetuoso. Nada de escritorio, silla, computadora ni oficina. La escena debe integrarse naturalmente en el fondo sin recuadros ni divisiones.
TEXTO LITERAL, imprimir solo estos bloques y el logo:
Encabezado serif bold tipo Bitter, azul marino, centrado en dos líneas:
"Aviso a nuestros
clientes"
Introducción sans Montserrat, centrada:
"Con motivo de la celebración
del Día de Muertos,"
Suspensión sans Montserrat, centrada, fecha en negritas:
"suspenderemos nuestros servicios
el lunes 2 de noviembre de 2026."
Regreso sans Montserrat, centrado, fecha en negritas:
"Reanudaremos actividades
el martes 3 de noviembre."
JERARQUÍA: papel picado dentro del 0–8 % superior; encabezado 12–25 %; introducción 29–36 %; suspensión 40–47 %; regreso 51–58 %. Texto de cuerpo equivalente a 35–40 px al tamaño final, máximo 84 % del ancho, líneas generosamente separadas y fechas muy claras. El bodegón se concentra entre 64–82 %. Área inferior 85–100 % limpia en crema. Coloca el logo original de imagen 2 centrado en el área inferior alrededor del 90 % del alto, ancho visible aproximado 340 px, sin fondo blanco añadido y con margen mínimo de 60 px al borde inferior. Conservar azul y dorado exactos y la proporción del logo. No repetir el nombre fuera del logo.
RESTRICCIONES: texto completo sin errores, no omitir el año 2026 ni las fechas de cierre y regreso. No añadir horarios, teléfono, web, agradecimientos ni otros textos. No comillas ni etiquetas de instrucciones. No tarjetas, botones, sellos, líneas de marco ni collage. Sin personas. Sin Halloween, terror, cementerios, luto, calabazas, murciélagos, morado, rojo ni neón. Mantener aire y un estilo de marca profesional. Una sola imagen terminada, no comparativa.
```

Estado del diseño adicional: [x] generado con `image_gen` [x] 1080×1350 [x] texto completo correcto [x] fechas correctas [x] logo legible [x] revisión visual final. Fondo crema y texto azul marino centrado, papel picado superior y bodegón de cempasúchil, calaverita y pan en la parte inferior. Todas las ediciones anteriores se conservan.

Original generado: `/Users/fernandomorales/.codex/generated_images/01a18df8-8976-7c00-9732-81558503da61/exec-0ffcb943-cab9-4dc1-bb01-11465cca5756.png`.

## Adaptación a historia 9:16
El usuario solicita expresamente el mismo diseño en formato historia 9:16. Se adapta el diseño crema más reciente a 1080×1920 px; esta instrucción sustituye el formato habitual 1080×1350 para esta entrega. Se conserva el texto completo, la temática y el logo autorizado. Destino `fotos-creada/` al tratarse de una adaptación del arte final con logo.

Base: `fotos-creada/PL-AV02A_aviso-dia-de-muertos-2026-crema.png`.
Salida: `fotos-creada/PL-AV02A_aviso-dia-de-muertos-2026-historia-1080x1920.png`.

### Prompt de adaptación
```text
Uso: ads-marketing. Adaptación precisa de formato para historia de Instagram/Facebook.
La imagen adjunta es el diseño original aprobado. ADAPTAR EL MISMO DISEÑO a un lienzo vertical 9:16, destino exacto 1080×1920 px. No crear un concepto diferente: conservar el fondo crema con textura de papel, tipografía azul marino, guirnalda de papel picado azul y naranja, cempasúchil en jarrón artesanal, calaverita blanca decorada y pan de muerto sobre plato de barro. Mantener el mismo estilo fotográfico cálido y editorial, colores, objetos y calidad.
Recomponer y extender verticalmente el fondo crema para aprovechar el formato de historia, sin deformar ni estirar objetos ni letras. Conservar completamente cada texto y el logo, sin recortarlos.
ZONAS SEGURAS: dejar aproximadamente 240 px superiores y 260 px inferiores libres de texto importante y del logo para las interfaces de historias. La guirnalda puede adornar la parte superior, pero todo el aviso y el logo deben permanecer entre y=260 e y=1620. Márgenes laterales de mínimo 80 px.
COMPOSICIÓN SUGERIDA: papel picado en la parte alta, encabezado centrado entre 15 y 26 % del alto; introducción entre 29 y 35 %; suspensión entre 38 y 45 %; regreso entre 48 y 54 %. Bodegón festivo entre 59 y 76 %. Logo centrado aproximadamente entre 78 y 85 %, manteniendo amplio margen inferior. Extender fondo crema natural hasta el borde inferior. No añadir más objetos. Mucho aire, lectura cómoda en teléfono.
TEXTO LITERAL, conservar sin omitir ni duplicar:
Encabezado en serif bold azul marino:
"Aviso a nuestros
clientes"
Introducción en sans:
"Con motivo de la celebración
del Día de Muertos,"
Suspensión en sans, fecha en negritas:
"suspenderemos nuestros servicios
el lunes 2 de noviembre de 2026."
Regreso en sans, fecha en negritas:
"Reanudaremos actividades
el martes 3 de noviembre."
Preservar exactamente el logo original de la imagen: monograma PL con arcos azul y dorado, "PEDRO LÓPEZ", "ASESOR EN SEGUROS", horizontal, sin redibujar ni alterar. Logo proporcional y legible, ancho visible aproximado de 400 px. No añadir un segundo logo.
Nada de otros textos, teléfono, web, horarios, slogans, botones, marcos o etiquetas. No imprimir estas instrucciones ni comillas. Sin Halloween, terror ni personas. Una sola imagen final vertical de historia 9:16, no collage ni comparativa.
```

Estado de historia: [x] generada con `image_gen` [x] 1080×1920 verificado con `sips` [x] proporción 9:16 [x] texto completo y fechas correctas [x] logo completo y legible [x] revisión visual final. Se conserva el diseño crema y sus elementos, distribuidos verticalmente. Arte previo conservado. No se usó el validador de 4:5, ya que cambiaría la proporción solicitada.

Original generado: `/Users/fernandomorales/.codex/generated_images/01a18df8-8976-7c00-9732-81558503da61/exec-40749423-e868-4125-b734-2dafc795fa28.png` (941×1672). Ajuste final mínimo con `sips` a 1080×1920, sin recortar texto ni logo.

## Nueva ejecución de historia · 13 de noviembre de 2026
- Solicitud confirmada: ejecutar el último prompt en formato historia 9:16.
- Herramienta: `image_gen`, con el prompt de adaptación literal y el original crema como referencia de edición.
- Referencia recuperada: `/Users/fernandomorales/.codex/generated_images/01a18df8-8976-7c00-9732-81558503da61/exec-0ffcb943-cab9-4dc1-bb01-11465cca5756.png`.
- Nuevo original: `/Users/fernandomorales/.codex/generated_images/01a1d56b-8491-71a3-aa2f-f8289de5c892/exec-79cd55d4-250c-44f8-8f77-5581e13c1c9a.png`.
- Archivo guardado: `fotos-creada/PL-AV02A_aviso-dia-de-muertos-2026-historia-1080x1920.png`.
- Estado: [x] generada [x] 1080×1920 verificado con `sips` [x] texto literal completo [x] fechas revisadas [x] logo legible [x] revisión visual.
- Se ajustaron únicamente las dimensiones con `sips`, sin recortar; el original generado se conserva. No se ejecutó el validador 4:5 para conservar el formato historia.
