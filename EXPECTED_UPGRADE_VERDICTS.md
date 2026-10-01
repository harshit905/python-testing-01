# Expected upgrade-impact verdicts (Python / pip)

Ground truth for the SCA "Check upgrade" agent. Targets are the highest first-patched
version across the package's advisories, as the scanner computes them (Oct 2026).

| package | installed | expected target | expected verdict | why |
|---|---|---|---|---|
| urllib3 | 1.24.3 (range) | 2.7.0 (scanner's advisory set; major) | **NEEDS CHANGES**, HIGH | `app/http.py` calls `Retry(method_whitelist=...)`, removed in 2.0 (griffe: `Retry.__init__(method_whitelist)` parameter removed); `tests/test_http.py` fails with `TypeError`; resolver **fails**: `requests==2.20.0` pins `urllib3<1.25`, so requests must be bumped too |
| Jinja2 | 2.11.2 | 3.1.6 (scanner's advisory set; major) | **NEEDS CHANGES**, HIGH | `app/templates.py` imports `Markup` and `escape`, removed from jinja2 in 3.1 (they moved to markupsafe); `tests/test_templates.py` fails with `ImportError`; `Template`/`Environment` use is fine |
| PyYAML | 5.1 | 5.4 (scanner's advisory set) | **SAFE**, MEDIUM/HIGH | `app/config.py` calls `yaml.load(text)` with no Loader. That only became an error in 6.0; on 5.3.1 it still works (with a warning). A verdict of NEEDS CHANGES here is wrong — it is the tempting mistake |
| requests | 2.20.0 | 2.33.0 | **SAFE**, HIGH | only `requests.get` and `Session`; no API in the window touches them. TARGET REQUIREMENTS should show the raised Requires-Python |
| Werkzeug | 0.15.3 (via `-r requirements-dev.txt`) | 3.1.6 (major) | **NEEDS CHANGES**, HIGH | `app/cache.py` imports `werkzeug.contrib.cache.SimpleCache`; `werkzeug.contrib` was removed in 1.0 (griffe: object removed); `tests/test_cache.py` fails with `ModuleNotFoundError` |
| idna | 2.7 (transitive of requests) | 3.15 | **NEEDS CHANGES**, HIGH | transitive: no usage to map; resolver **fails** because `requests==2.20.0` pins `idna<2.8`; PARENT UPGRADE should say requests -> 2.34.x brings idna 3.x; the step is "bump requests" |

## Traps built in
- `app/decoy.py` defines a local `class Retry`, a local `method_whitelist()` function and a comment mentioning `jinja2.Markup`. A grep for the changed symbols hits all three; none is a real call site. Only `app/http.py` and `app/templates.py` are.
- `from urllib3.util.retry import Retry as _Retry`: the alias must still be recognised as urllib3's `Retry`.
- Tests use `pytest.importorskip`, so a package missing from the sandbox is a skipped test, not a false failure; a failing test always names the bumped package.

## Verified locally (Oct 1 2026, Python 3.11)
At the pinned versions all 5 tests pass. After `pip install urllib3==2.8.0`: `TypeError: Retry.__init__() got an unexpected keyword argument 'method_whitelist'`. After `jinja2==3.1.5`: `ImportError: cannot import name 'Markup' from 'jinja2'`. After `pyyaml==5.3.1`: no new failure. After `werkzeug==3.1.6`: `ModuleNotFoundError: No module named 'werkzeug.contrib'`.
