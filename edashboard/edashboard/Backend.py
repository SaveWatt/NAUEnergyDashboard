from edashboard.models import Building, Sensor

class Backend:

    def getBuildingStrings(self):
        buildings = Building.objects.all()
        b_strings = []
        for building in buildings:
            b_strings.append(str(building))
        return b_strings

    def getNumStrings(self):
        b_strings = self.getBuildingStrings()
        for i in range(len(b_strings)):
            for j in range(0,len(b_strings)-1):
                if(int(self.getNum(b_strings[j])) > int(self.getNum(b_strings[j+1]))):
                    temp = b_strings[j+1]
                    b_strings[j+1] = b_strings[j]
                    b_strings[j] = temp

        for i in range(len(b_strings)):
            b_strings[i] = self.getNumId(b_strings[i]) + " "+ self.getName(b_strings[i])
        return b_strings

    def getNum(self,str):
        num = ""
        str2 = str.split(" (B")
        for i in str2[1]:
            if(i.isdigit()):
                num = num + i
        return num

    def getNumId(self,str):
        num = ""
        str2 = str.split(" (B")
        return str2[1].split(")")[0]

    def getName(self,str):
        num = ""
        str2 = str.split(" (B")
        return str2[0]
