from api import API, TreeNode
from geocoders.geocoder import Geocoder


# Алгоритм "в лоб"
class SimpleQueryGeocoder(Geocoder):
    def _apply_geocoding(self, area_id: str) -> str:
        
        start_id = area_id
        arr = []
        while True:
            tree = API.get_area(area_id)
            area_id = tree.parent_id
            arr.append(tree.name)
            if tree.parent_id is None:
                break

        return f'{start_id},"{", ".join(reversed(arr))}"'
