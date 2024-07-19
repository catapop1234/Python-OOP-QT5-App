import json
from abc import ABC, abstractmethod
from PyQt5.QtWidgets import QMessageBox
from typing import List, TypeVar, Generic

T = TypeVar('T')

class AbstractMGR(ABC, Generic[T]):
    
    def __init__(self):
        self.elements: List[T] = []

    def read_elements(self, nr_elements: int):
        for cnt in range(nr_elements):
            print("Introdu un element")
            nume = input("Numele: ")
            cod_intern = input("Codul intern: ")
            pret = int(input("Pretul: "))
            categorie = input("Categoria: ")

            self.elements.append(self.create_element(cnt, nume, cod_intern, pret, categorie))

    def save_elemente_to_xml(self, file_path: str):
        from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
        import xml.dom.minidom

        root = Element('elements')

        for element in self.elements:
            class_name = element.__class__.__name__
            element_elem = Element(class_name)
            for attr, value in element.__dict__.items():
                child = SubElement(element_elem, attr)
                child.text = str(value)
            root.append(element_elem)

        tree = ElementTree(root)
        xml_str = tostring(root, encoding='utf-8')
        xml_parsed = xml.dom.minidom.parseString(xml_str)
        xml_content = xml_parsed.toprettyxml(indent="    ")

        with open(file_path, "w") as f:
            f.write(xml_content)





    def save_elements_to_json(self, file_path):
        with open(file_path, 'w') as f:
            json.dump([element.__dict__ for element in self.elements], f, ensure_ascii=False, indent=4)

    def write_elements(self):
        if self.elements:
            stringAfis=""
            #print("Elementele sunt:")
            for element in self.elements:
                if element:
                    stringAfis=stringAfis+"\n"+self.afisare_element(element)+"\n"
            #print(stringAfis)
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setText("Elementele sunt:")
            msg.setWindowTitle("Afisarea Elementelor")
            msg.setInformativeText(stringAfis)
            msg.setStandardButtons(QMessageBox.Ok)
            retval = msg.exec_()

    @abstractmethod
    def create_element(self, id: int, nume: str, cod_intern: str, pret: int, categorie: str) -> T:
        pass

    @abstractmethod
    def afisare_element(self, element: T):
        pass

    @abstractmethod
    def search_element(self, element_to_search: T) -> bool:
        pass
