import sys
from pathlib import Path

sys.path.append(str(Path().absolute().parent / "pylode"))
try:
    from pylode.ontdoc import OntDoc
except ImportError:
    from ontdoc import OntDoc

EXAMPLES_DIR = Path().absolute() / "ontdoc"

for f in Path(EXAMPLES_DIR).glob("*.ttl"):
    html_file = Path(EXAMPLES_DIR / Path(f.stem + ".html")).absolute()
    print(f"regenerating {html_file}")

    OntDoc(f).make_html(destination=html_file)
