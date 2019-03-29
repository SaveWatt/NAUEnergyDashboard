from edashboard.models import Building, Sensor

class Backend:

    def getBuildingStrings(self):
        buildings = Building.objects.all()
        b_strings = []
        for building in buildings:
            b_strings.append(str(building))
        return b_strings
