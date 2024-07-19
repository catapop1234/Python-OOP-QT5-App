from abc import ABC, abstractmethod
from typing import Optional
from .IPackageable import IPackageable

class ProdusAbstract(IPackageable, ABC):
    
    def __init__(self, id: int, nume: Optional[str], cod_intern: Optional[str], pret: Optional[int], categorie: Optional[str]):
        self.id = id
        self.nume = nume
        self.cod_intern = cod_intern
        self.pret = pret
        self.categorie = categorie

    @abstractmethod
    def can_add_to_package(self, pachet):
        pass

    @abstractmethod
    def afisare(self):
        pass
