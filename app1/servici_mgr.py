import xml.etree.ElementTree as ET
from typing import Optional
from .abstract_mgr import AbstractMGR
from entitati.serviciu import Serviciu

class ServiciuMGR(AbstractMGR[Serviciu]):

    def __init__(self):
        super().__init__()

    def read_servicii(self, nr_servicii: int):
        self.read_elements(nr_servicii)

    def write_servicii(self):
        self.write_elements()

    def create_element(self, id: int, nume: str, cod_intern: str, pret: int, categorie: str) -> Optional[Serviciu]:
        serv = Serviciu(id, nume, cod_intern, pret, categorie)
        if not self.search_element(serv):
            return serv
        return None

    def afisare_element(self, produs: Serviciu):
        #print(produs.afisare())
        return produs.afisare()

    def search_element(self, element_to_search: Serviciu) -> bool:
        return any(element is not None and element == element_to_search for element in self.elements)

    def return_element_dupa_nume(self, nume: str) -> Optional[Serviciu]:
        for element in self.elements:
            if element is not None and element.nume == nume:
                return element
        return None

    def init_lista_from_xml(self, file_path: str):
        tree = ET.parse(file_path)
        root = tree.getroot()

        for serviciu_node in root.findall('Serviciu'):
            nume = serviciu_node.find('Nume').text
            cod_intern = serviciu_node.find('CodIntern').text
            pret = int(serviciu_node.find('Pret').text)
            categorie = serviciu_node.find('Categorie').text

            self.elements.append(Serviciu(len(self.elements) + 1, nume, cod_intern, pret, categorie))
