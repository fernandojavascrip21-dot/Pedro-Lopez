import contextlib
import io
import json
from pathlib import Path
import runpy
import sys

import numpy as np

original_default = json.JSONEncoder.default
def numpy_default(self, obj):
    if isinstance(obj, np.generic):
        return obj.item()
    return original_default(self, obj)
json.JSONEncoder.default = numpy_default

jobs = json.loads(Path('tmp/imagegen/diciembre-2026-jobs.json').read_text())
selected = set(sys.argv[1:])
reports = Path('tmp/imagegen/validacion-diciembre')
reports.mkdir(exist_ok=True)
for job in jobs:
    if selected and job['id'] not in selected:
        continue
    if not Path(job['file']).exists():
        continue
    sys.argv = ['validar.py', job['file'], job['layout'], '--json']
    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        try:
            runpy.run_path('.agents/skills/pedro-lopez-prompts-imagenes/scripts/validar.py', run_name='__main__')
        except SystemExit as exc:
            if exc.code not in (0, 1):
                raise
    result = json.loads(buffer.getvalue())
    (reports / (job['id'] + '.json')).write_text(json.dumps(result, ensure_ascii=False, indent=2))
    print(json.dumps({'id': job['id'], 'ok': result['ok'], 'nota': result['nota'], 'candidato': result['candidatos'][0]}, ensure_ascii=False))
