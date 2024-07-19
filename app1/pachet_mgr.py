import xml.etree.ElementTree as ET
from typing import Optional, List
from .abstract_mgr import AbstractMGR
from .produs_mgr import ProdusMGR
from .servici_mgr import ServiciuMGR
from entitati.pachet import Pachet
from entitati.ProdusAbstract import ProdusAbstract
from entitati.produs import Produs
from entitati.serviciu import Serviciu
import xml.etree.ElementTree as ET
import json
import xml.dom.minidom




class PachetMGR(AbstractMGR[Pachet]):

    def __init__(self, produs_mgr: ProdusMGR, servici_mgr: ServiciuMGR):
        super().__init__()
        self.produs_mgr = produs_mgr
        self.servici_mgr = servici_mgr

    def create_element(self, id: int, nume: str, cod_intern: str, pret: int, categorie: str) -> Optional[Pachet]:
        pachet = Pachet(id, nume, cod_intern, pret, categorie)
        if not self.search_element(pachet):
            return pachet
        return None

    def read_pachet(self, nr_elements: int):
        for cnt in range(nr_elements):
            print("Introdu un element")
            nume = input("Numele: ")
            cod_intern = input("Codul intern: ")
            categorie = input("Categoria: ")

            nr_elem = int(input("Cate elemente doriti sa adaugati in acest pachet?: "))
            price = 0
            anr_elem = 0

            new_pachet = self.create_element(cnt, nume, cod_intern, 0, categorie)

            for i in range(nr_elem):
                element_name = input(f"Introduceti numele elementului #{i + 1} care doriti sa fie inclus in acest pachet: ")

                prod_to_add = self.produs_mgr.return_element_dupa_nume(element_name)
                if prod_to_add and prod_to_add.can_add_to_package(new_pachet):
                    new_pachet.adaugare(prod_to_add)
                    price += prod_to_add.pret
                    anr_elem += 1

                serv_to_add = self.servici_mgr.return_element_dupa_nume(element_name)
                if serv_to_add and serv_to_add.can_add_to_package(new_pachet):
                    new_pachet.adaugare(serv_to_add)
                    price += serv_to_add.pret
                    anr_elem += 1

                if not prod_to_add and not serv_to_add:
                    print(f"Elementul '{element_name}' nu a fost gasit.")

            new_pachet.nr_elem = anr_elem
            new_pachet.pret = price
            self.elements.append(new_pachet)

    def init_lista_from_xml(self, file_path: str):
        tree = ET.parse(file_path)
        root = tree.getroot()

        for pachet_node in root.findall('Pachet'):
            nume = pachet_node.find('Nume').text
            cod_intern = pachet_node.find('CodIntern').text
            categorie = pachet_node.find('Categorie').text
            price = 0
            anr_elem = 0

            pachet = Pachet(len(self.elements) + 1, nume, cod_intern, price, categorie)

            element_nodes = pachet_node.findall("Elem_pachet/ProdusAbstract/Nume")
            for element_node in element_nodes:
                prod_to_add = self.produs_mgr.return_element_dupa_nume(element_node.text)
                if prod_to_add:
                    pachet.adaugare(prod_to_add)
                    price += prod_to_add.pret
                    anr_elem += 1

                serv_to_add = self.servici_mgr.return_element_dupa_nume(element_node.text)
                if serv_to_add:
                    pachet.adaugare(serv_to_add)
                    price += serv_to_add.pret
                    anr_elem += 1

            pachet.nr_elem = anr_elem
            pachet.pret = price
            self.elements.append(pachet)

    def adaugare_element_dupa_nume(self, idul: int, elementul: ProdusAbstract):
        for element in self.elements:
            if element and element.id == idul:
                element.adaugare(elementul)

            

    import xml.dom.minidom

    def save_elemente_to_xml(self, file_path: str):
        from xml.etree.ElementTree import Element, SubElement, tostring, ElementTree
    
        root = Element('elements')

        for element in self.elements:
            item = SubElement(root, 'element')
            for attr, value in element.__dict__.items():
                if attr == 'elem_pachet':
                # Serialize the list of elements inside the Pachet object
                    elem_pachet = SubElement(item, 'Elem_pachet')
                    for sub_element in value:
                        sub_item = SubElement(elem_pachet, 'ProdusAbstract')
                        for sub_attr, sub_value in sub_element.__dict__.items():
                            sub_child = SubElement(sub_item, sub_attr)
                            sub_child.text = str(sub_value)
                else:
                # Serialize other attributes normally
                    child = SubElement(item, attr)
                    child.text = str(value)

        tree = ElementTree(root)
        xml_str = tostring(root, encoding='utf-8')
    
    # Parse XML string
        xml_parsed = xml.dom.minidom.parseString(xml_str)
    
    # Write formatted XML to file
        with open(file_path, 'wb') as f:
            f.write(xml_parsed.toprettyxml(indent='\t', encoding='utf-8'))





    def afisare_element(self, pachet: Pachet):
        #print(pachet.afisare())
        return pachet.afisare()


    def write_pachet(self):
        self.write_elements()

    def save_elements_to_json(self, file_path):
        with open(file_path, 'w') as f:
            json_data = []
            for pachet in self.elements:
                pachet_data = {
                    'id': pachet.id,
                    'nume': pachet.nume,
                    'cod_intern': pachet.cod_intern,
                    'pret': pachet.pret,
                    'categorie': pachet.categorie,
                    'elem_pachet': []
                }
                for elem in pachet.elem_pachet:
                    if isinstance(elem, Produs) or isinstance(elem, Serviciu):
                        elem_data = {
                            'id': elem.id,
                            'nume': elem.nume,
                            'cod_intern': elem.cod_intern,
                            'pret': elem.pret,
                            'categorie': elem.categorie,
                            # Add any other attributes of Produs and Serviciu here
                        }
                        pachet_data['elem_pachet'].append(elem_data)
                json_data.append(pachet_data)
            json.dump(json_data, f, ensure_ascii=False, indent=4)

    def search_element(self, element_to_search: Pachet) -> bool:
        return any(element and element == element_to_search for element in self.elements)

    def search_element_name(self, name: str) -> Optional[Pachet]:
        for element in self.elements:
            if element and element.nume == name:
                return element
        return None
