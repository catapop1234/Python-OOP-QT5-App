import xml.etree.ElementTree as ET
from typing import Optional
from .abstract_mgr import AbstractMGR
from entitati.produs import Produs
from Form import FormWindow


class ProdusMGR(AbstractMGR[Produs]):

    def __init__(self):
        super().__init__()

    def read_produse(self):
        self.form_window = FormWindow(self)
        self.form_window.show()

        #self.elements.append(self.create_element(cnt, nume, cod_intern, pret, categorie))

    def add_element(self, nume, cod_intern, pret, categorie, prod):
        cnt = len(self.elements)+1
        new_element = self.create_element(cnt, nume, cod_intern, pret, categorie, prod)
        self.elements.append(new_element)
        print(f"Element added: {new_element}")
        print(f"All elements: {self.elements}")

    def write_produse(self):
        self.write_elements()

    def create_element(self, id: int, nume: str, cod_intern: str, pret: int, categorie: str, producator: str) -> Optional[Produs]:
        prod = Produs(id, nume, cod_intern, pret, categorie, producator)
        if not self.search_element(prod):
            return prod
            print("Saluttttttt")
        print("Sallllll")
        return None

    def afisare_element(self, produs: Produs):
        #print(produs.afisare())
        return produs.afisare()

    def search_element(self, element_to_search: Produs) -> bool:
        return any(element is not None and element == element_to_search for element in self.elements)

    def return_element_dupa_nume(self, nume: str) -> Optional[Produs]:
        for element in self.elements:
            if element is not None and element.nume == nume:
                return element
        return None

    def init_lista_from_xml(self, file_path: str):
        tree = ET.parse(file_path)
        root = tree.getroot()

        for produs_node in root.findall('Produs'):
            nume = produs_node.find('Nume').text
            cod_intern = produs_node.find('CodIntern').text
            producator = produs_node.find('Producator').text
            pret = int(produs_node.find('Pret').text)
            categorie = produs_node.find('Categorie').text

            self.elements.append(Produs(len(self.elements) + 1, nume, cod_intern, pret, categorie, producator))

