"""HTTP client adapted from the original show tooling; standard library only.

Launch and verify the GUI session first. A port does not identify its show folder.
Set XLIGHTS_API_PORT before import. Mutations are never automatically retried.
"""
import json
import os
from pathlib import Path
import time
import urllib.error
import urllib.request

PORT = int(os.environ.get('XLIGHTS_API_PORT', '49913'))
if PORT not in (49913, 49914):
    raise ValueError('XLIGHTS_API_PORT must be 49913 (A) or 49914 (B).')
BASE = f'http://127.0.0.1:{PORT}/xlDoAutomation'


def xl(cmd, timeout=30, **kwargs):
    if cmd == 'setEffectSettings':
        raise ValueError('setEffectSettings can corrupt settings; remove and re-add effects.')
    body = json.dumps({'cmd': cmd, **kwargs}).encode()
    request = urllib.request.Request(BASE, body, {'Content-Type': 'application/json'})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        result = json.loads(response.read())
    if not isinstance(result, dict):
        raise RuntimeError(f'{cmd} returned an unexpected response: {result!r}')
    if str(result.get('res', 200)) != '200' or str(result.get('worked', True)).lower() == 'false':
        raise RuntimeError(f'{cmd} failed: {result}')
    return result


def wait_ready(timeout=600):
    deadline = time.monotonic() + timeout
    while time.monotonic() < deadline:
        try:
            return xl('getVersion', timeout=min(5, max(.01, deadline-time.monotonic())))
        except (urllib.error.URLError, TimeoutError, RuntimeError):
            time.sleep(max(0, min(3, deadline-time.monotonic())))
    raise TimeoutError('xLights automation API did not become ready')


def add_effect(model, layer, effect, settings, palette, start_ms, end_ms):
    if layer < 0 or start_ms < 0 or end_ms <= start_ms:
        raise ValueError('Require a nonnegative layer/start and end > start.')
    if not isinstance(settings, str) or not isinstance(palette, str):
        raise TypeError('Settings and palette must be key=value strings.')
    return xl('addEffect', target=model, effect=effect, settings=settings,
              palette=palette, layer=layer, startTime=int(start_ms), endTime=int(end_ms))


def import_timings(template_xsq):
    """Import once; caller must verify unique track names and a timing-only template."""
    path = Path(template_xsq).expanduser().resolve(strict=True)
    return xl('importXLightsSequence', filename=str(path), mapmethod='auto',
              importmedia='false', timeout=900)


def save(path):
    path = Path(path).expanduser()
    if not path.is_absolute() or not path.parent.is_dir():
        raise ValueError('save requires an absolute path with an existing parent folder.')
    return xl('saveSequence', seq=str(path), timeout=900)


def render_all():
    return xl('renderAll', timeout=3600)


def export_video_preview(path):
    path = Path(path).expanduser()
    if not path.is_absolute():
        raise ValueError('Preview path must be absolute.')
    path.parent.mkdir(parents=True, exist_ok=True)
    return xl('exportVideoPreview', filename=str(path), timeout=3600)
