import importlib.util
from pathlib import Path


ARQUIVO = Path(__file__).resolve().parents[1] / "projetos" / "inventario-ti" / "inventario.py"
ESPECIFICACAO = importlib.util.spec_from_file_location("inventario", ARQUIVO)
assert ESPECIFICACAO is not None and ESPECIFICACAO.loader is not None
modulo = importlib.util.module_from_spec(ESPECIFICACAO)
import sys
sys.modules["inventario"] = modulo
ESPECIFICACAO.loader.exec_module(modulo)


def test_listar_online():
    computadores = [modulo.Computador("A", "10.0.0.1", True), modulo.Computador("B", "10.0.0.2")]
    assert [pc.nome for pc in modulo.listar_online(computadores)] == ["A"]
