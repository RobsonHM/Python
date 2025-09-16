class computer:
    def __init__(self, CPU, ram, SSD, PS, MB, GC): # variable = "" if you wanna set a default value in case this value is not provide 
        self.CPU = CPU
        self.ram = ram
        self.SSD = SSD
        self.PS = PS
        self.MB = MB
        self.GC = GC

    def set_KB(self,KB):
        self.KB = KB

MyPC = computer("AMD Ryzen 7" , "64G Ram", "2T SSD NVMe", "850W Gold", "Gigabyte", "RTX 5070")
MyPC.set_KB("Mechanical Keyboard")
print(f"My PC: {MyPC.PS}")

print(MyPC.__dict__)
