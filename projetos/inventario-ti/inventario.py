"""Aplicação integradora: inventário simples de computadores."""

from dataclasses import dataclass


@dataclass
class Computador:
    nome: str
    ip: str
    online: bool = False


def listar_online(computadores: list[Computador]) -> list[Computador]:
    """Retorna os computadores com status online."""
    return [computador for computador in computadores if computador.online]


def main() -> None:
    computadores = [
        Computador("LAB-01", "192.168.0.10", True),
        Computador("LAB-02", "192.168.0.11", False),
        Computador("LAB-03", "192.168.0.12", True),
    ]
    print("Computadores online:")
    for computador in listar_online(computadores):
        print(f"- {computador.nome} ({computador.ip})")


if __name__ == "__main__":
    main()
