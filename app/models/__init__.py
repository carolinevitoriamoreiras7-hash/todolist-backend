"""Modelos de domínio: as entidades do sistema, com seus dados e suas regras.

Cada entidade é responsável por manter o próprio estado válido: o `Usuário`
normaliza o próprio e-mail e só aceita a senha em forma de hash
"""

# Importar as entidades aqui registra as tabelas no SQLalchemy (é o que 
# `criar tabelas()` e usa) e permite escrever `from app.models import Usuário`.
from app.models.usuario import Usuario

__all__ = ["Usuario"]
