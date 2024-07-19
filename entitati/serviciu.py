from .ProdusAbstract import ProdusAbstract
from typing import Optional


class Serviciu(ProdusAbstract):
    
    def __init__(self, id: int, nume: Optional[str], cod_intern: Optional[str], pret: Optional[int], categorie: Optional[str]):
        super().__init__(id, nume, cod_intern, pret, categorie)

    def __eq__(self, other):
        if not isinstance(other, Serviciu):
            return False
        return (self.nume == other.nume and self.cod_intern == other.cod_intern and
                self.pret == other.pret and self.categorie == other.categorie)

    def __hash__(self):
        return hash((self.nume, self.cod_intern, self.pret, self.categorie))

    def afisare(self):
        return f"Serviciu: {self.nume} [{self.cod_intern}] Pret: {self.pret} Categorie: {self.categorie}"

    def can_add_to_package(self, pachet):
        return True
