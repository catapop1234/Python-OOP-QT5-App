from typing import Optional
import functools
from .ProdusAbstract import ProdusAbstract

class Produs(ProdusAbstract):
    
    def __init__(self, id: int, nume: Optional[str], cod_intern: Optional[str], pret: Optional[int], categorie: Optional[str], producator: Optional[str] = None):
        super().__init__(id, nume, cod_intern, pret, categorie)
        self.producator = producator

    def __eq__(self, other):
        if not isinstance(other, Produs):
            return False
        return (self.nume == other.nume and self.cod_intern == other.cod_intern and
                self.pret == other.pret and self.categorie == other.categorie and
                self.producator == other.producator)

    def __hash__(self):
        return hash((self.nume, self.cod_intern, self.pret, self.categorie, self.producator))

    def afisare(self):
        return f"Produs: {self.nume} [{self.cod_intern}] {self.producator} Pret: {self.pret} Categorie: {self.categorie}"

    def can_add_to_package(self, pachet):
        return True
