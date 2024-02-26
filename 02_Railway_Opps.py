
class RailwayForm:
    formType="RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

harrysApplication=RailwayForm() # create a  object
harrysApplication.name="siddhartha"
harrysApplication.train="lkgdkjksbdb"
harrysApplication.printData()