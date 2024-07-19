from typing import List, Optional, Union
from .ProdusAbstract import ProdusAbstract
from .IPackageable import IPackageable


class Pachet(ProdusAbstract):
    
    def __init__(self, id: int, nume: Optional[str], cod_intern: Optional[str], pret: Optional[int], categorie: Optional[str]):
        super().__init__(id, nume, cod_intern, pret, categorie)
        self.nr_elem: Optional[int] = None
        self.elem_pachet: List[ProdusAbstract] = []

    def can_add_to_package(self, pachet):
        return True

    def __eq__(self, other):
        if not isinstance(other, Pachet):
            return False
        return (self.nume == other.nume and self.cod_intern == other.cod_intern and
                self.pret == other.pret and self.categorie == other.categorie)

    def afisare(self):
        string_afis = f"Pachet: {self.nume} [{self.cod_intern}] Pret: {self.pret} Categorie: {self.categorie}"
        if self.nr_elem and self.nr_elem > 0:
            string_afis += f"\nPachetul {self.nume} contine urmatoarele elemente:"
            string_afis += "\n====================================="
            elem_afisare = "\n".join([elem.afisare() for elem in self.elem_pachet if elem is not None])
            string_afis += f"\n{elem_afisare}"
            string_afis += "\n====================================="
        else:
            string_afis += f"\nPachetul {self.nume} nu contine nici un element"
        return string_afis

    def adaugare(self, elem: IPackageable):
        if elem.can_add_to_package(self):
            self.elem_pachet.append(elem)
