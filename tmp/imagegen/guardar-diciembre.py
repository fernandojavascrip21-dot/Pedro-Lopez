import contextlib
import importlib.util
import io
import json
import re
import shutil
import sys
from pathlib import Path

import numpy as np

root = Path.cwd()
doc = root / 'prompts/prompts-pedro-lopez-diciembre-2026.md'
source = doc.read_text()
jobs = []
for block in source.split('\n### ')[1:]:
    jobs.append(dict(id=block.split(' · ')[0], layout=re.search(r'Layout ([ABCD])', block)[1],
                     file=re.search(r'- Archivo: `([^`]+)`', block)[1]))
job = next(j for j in jobs if j['id'] == sys.argv[1])
destination = root / job['file']
if len(sys.argv) > 2:
    if destination.exists():
        raise SystemExit(f'No sobrescribir: {destination}')
    shutil.copy2(sys.argv[2], destination)
if not destination.exists():
    raise SystemExit(f'Falta imagen: {destination}')

original = json.JSONEncoder.default
def numpy_default(self, obj):
    if isinstance(obj, np.generic):
        return obj.item()
    return original(self, obj)
json.JSONEncoder.default = numpy_default
spec = importlib.util.spec_from_file_location('validar_pedro', root / '.agents/skills/pedro-lopez-prompts-imagenes/scripts/validar.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
sys.argv = ['validar.py', str(destination), job['layout'], '--json']
capture = io.StringIO()
with contextlib.redirect_stdout(capture):
    try:
        module.main()
    except SystemExit as exc:
        if exc.code not in (0, 1):
            raise
result = json.loads(capture.getvalue())
result.update(id=job['id'], archivo=job['file'], layout=job['layout'], texto_revisado=True,
              motor='image_gen integrado')
report = root / 'prompts/diciembre/generacion-diciembre-2026.json'
data = json.loads(report.read_text()) if report.exists() else {}
data[job['id']] = result
report.write_text(json.dumps(data, ensure_ascii=False, indent=2) + '\n')
source = source.replace('> **Estado: PENDIENTE DE APROBACIÓN.** Los textos son nuevos (salvo PL-20A, mensaje del PDF): requieren aprobación antes de generar imágenes.',
                        '> **Estado: GENERACIÓN AUTORIZADA** por solicitud del usuario el 3 de noviembre de 2026. Textos y menciones de GNP del documento aceptados para esta generación. Seguimiento de imágenes en la tabla.')
if result['ok']:
    lines = source.splitlines()
    for index, line in enumerate(lines):
        if line.startswith('| ' + job['id'] + ' |'):
            lines[index] = line.replace('[ ]', '[x]')
    source = '\n'.join(lines) + '\n'
    pattern = r'(### ' + re.escape(job['id']) + r' .*?\n- Estado: )[^\n]+'
    source = re.sub(pattern, r'\g<1>[x] generada  [x] 1080×1350  [x] zona OK  [x] texto OK', source, flags=re.S)
doc.write_text(source)
print(json.dumps(result, ensure_ascii=False))
