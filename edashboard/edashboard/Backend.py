from edashboard.models import Building, Sensor

class Backend:

    def getBuildingStrings(self):
        buildings = Building.objects.all()
        b_strings = []
        for building in buildings:
            b_strings.append(str(building))
        return b_strings

    """
    A function that takes a building id, sensor type, inital date,
    and final date as inputs.
    The function returns sample values as an array to be passed to a chart builder.
    """
    def getData(self, b_id, s_type, init_date, fin_date):
        return
