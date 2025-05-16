
from farmers.models import CropData, LivestockData, MachineryUse


def calculate_carbon_footprint(farm):
    carbon = 0
    crops = CropData.objects.filter(farm=farm)
    livestock = LivestockData.objects.filter(farm=farm)
    machinery = MachineryUse.objects.filter(farm=farm)

    for crop in crops:
        carbon += crop.quantity_fertilizer * 1.5
    for animal in livestock:
        carbon += animal.count * 2.0
    for machine in machinery:
        carbon += machine.estimated_consumption * 2.5

    return round(carbon, 2)