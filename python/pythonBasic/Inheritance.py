'''Inheritance, Inheritance is the ability of any class to extract and use
features of other classes. It is the process by which new classes called the
derived classes are created from existing classes called Base classes.'''

class studentMH:

    # Constructor
    def __init__(self, name, city):
        self.name=name
        self.city=city

    # To get name
    def chaater(self):  ## This is called inheritance
        return(self.name, self.city)

    # this class people belongs to pune
    def resident(self):
        print('he is from pune')


# Inherited or Sub class (Note Person in bracket)
class studentHR(studentMH):

    # Here we return ambala
    def resident(self):
        print('he is from Ambala')

# Driver code  (# An Object of StudentMH )
std1 = studentMH("Praveen","Saini")
print(std1.chaater())
std1.resident()

# Driver code  (# An Object of StudentHR inheritance oh MH and overriding resident method )
std1 = studentHR("Praveen","Saini")
print(std1.chaater())
std1.resident()