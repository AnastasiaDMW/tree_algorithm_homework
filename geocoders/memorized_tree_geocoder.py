from api import TreeNode, API
from geocoders.custom_stack import CustomStack
from geocoders.geocoder import Geocoder


# Инверсия дерева
class MemorizedTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data
        self.countries_dict = {}
        self.path = []
        self.write_data()
    
    def write_data(self):
        
        for i in range(len(self.__data)):
            self.write_nodes_path(self.__data[i])
    
    def write_nodes_path(self, treeNode: TreeNode):
        self.path.append(treeNode.name)
        for i in range(len(treeNode.areas)):
            if treeNode.areas[i].areas is not None:
                self.write_nodes_path(treeNode.areas[i])
            else:
                self.path.append(treeNode.areas[i].name)
                self.countries_dict[treeNode.areas[i].id] = f'"{", ".join(self.path)}"'
                self.path.remove(treeNode.areas[i].name)
        self.countries_dict[treeNode.id] = f'"{", ".join(self.path)}"'
        self.path.remove(treeNode.name)
        

    def _apply_geocoding(self, area_id: str) -> str:
        
        return f"{area_id},"+self.countries_dict[str(area_id)]
