from abc import ABC, abstractmethod

class IPackageable(ABC):
    
    @abstractmethod
    def can_add_to_package(self, pachet):
        pass
    
    @abstractmethod
    def afisare(self):
        pass
