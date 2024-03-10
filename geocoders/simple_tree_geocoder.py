from api import API, TreeNode
from geocoders.custom_stack import CustomStack
from geocoders.geocoder import Geocoder


# Перебор дерева
class SimpleTreeGeocoder(Geocoder):
    def __init__(self, samples: int | None = None, data: list[TreeNode] | None = None):
        super().__init__(samples=samples)
        if data is None:
            self.__data = API.get_areas()
        else:
            self.__data = data

    def _apply_geocoding(self, area_id: str) -> str:
        
        area_id = str(area_id)
        start_id = area_id
        
        for i in range(len(self.__data)):
            stack = CustomStack()
            stack.append(self.__data[i])
            arr = []
            cur_node_name = None
            
            if self.__data[i].id == area_id:
                return f'{start_id},"{self.__data[i].name}"'
            
            while stack:
                
                current_node = stack.pop()
                
                if current_node.id == area_id:
                    arr.append(current_node.name)
                    break
                else:
                    if cur_node_name != None:
                        arr.remove(arr[-1])
                
                if current_node.areas is not None:
                    for area in current_node.areas:
                        stack.append(area)
                        cur_node_name = current_node.name
                        arr.append(current_node.name)
            

            arr = list(set(arr))
            return f'{start_id},"{", ".join(reversed(arr))}"'
