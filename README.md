# Bracket
A simple tool that analyizes your source code for correct bracket and quotation mark usage.

## Usage
Currently, the "correct" way to use this utiltity is to run it through `pytest`.

On lines 16 and 17, update the `pytest.fixture()` to point to your source file:
```python
@pytest.fixture()
def source_code_file():
    proj_dir = os.path.abspath("</project/dir>")
    return os.path.join(proj_dir, "<source_file>")
```

then, in your terminal:

```bash
cd bracket  # (project root directory)
pytest -v
```

If test(s) pass, then your file was successfully analyzed.

A proper CLI will come later.