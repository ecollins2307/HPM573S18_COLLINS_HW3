# HW 3, Problem 1
# Note: Credit given to participants on Piazza, as parts of code this code is based on Piazza postings
#       Credit given to participants on StackOverflow as commented in code

# Setting up the model

# creating superclass Patient
class Patient:
    """superclass"""
    def __init__(self, name):
        """
        :param name: name of patient
        """
        self.name = name

    def discharge(self):
        """abstract method to be overwritten: prints the name and type of patient when called"""
        raise NotImplementedError("This is an abstract method and needs to be implemented in derived classes.")

# creating subclass EmergencyPatient
class EmergencyPatient(Patient):

    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        """
        :return:  prints the name and type of the patient
        """
        patientname = self.name
        patienttype = "Emergency Patient"
        print("Patient Name: ",patientname,"\n""Patient Type: ",patienttype,"\n\n")


# creating subclass HospitalizedPatient
class HospitalizedPatient(Patient):
    def __init__(self, name):
        Patient.__init__(self, name)

    def discharge(self):
        """
        :return:  prints the name and type of the patient
        """
        patientname = self.name
        patienttype = "Hospitalized Patient"
        print("Patient Name: ",patientname,"\n""Patient Type: ",patienttype,"\n\n")


# creating class Hospital
class Hospital:
    # setting variable attributes
    def __init__(self):
        self.patients = []
        self.cost = 0

    # creating admit function
    def admit(self, patients):
        """
        :return: admits a patient
        """
        self.patients.append(patients)

    # creating discharge_all function
    def discharge_all(self):
        """
        :return: iterate through hospital patients, call the appropriate previously created discharge function
        """
        i = 0
        for counter in self.patients:
            if type(self.patients[i]) == EmergencyPatient:
                EmergencyPatient.discharge(self.patients[i])
            elif type(self.patients[i]) == HospitalizedPatient:
                HospitalizedPatient.discharge(self.patients[i])
            else:
                raise ValueError("Error! Unknown patient class detected")
            i += 1

    # creating get_total_cost function
    def get_total_cost(self):
        """
        :return: iterate through hospital patients, assign cost by patient,
        """
        j = 0
        for othercounter in self.patients:
            if type(self.patients[j]) == EmergencyPatient:
                self.cost += 1000
            elif type(self.patients[j]) == HospitalizedPatient:
                self.cost += 2000
            else:
                raise ValueError("Error! Unknown patient class detected")
            j += 1
            totalcost = '${:,.2f}'.format(self.cost) # per https://stackoverflow.com/questions/21208376/converting-float-to-dollars-and-cents
        print("Today's Total Operating Cost: ",totalcost)


# Testing the model

# Creating hospital
myHospital = Hospital()
# Admitting 2 patients that need hospitalized
Patient1 = HospitalizedPatient("John Smith")
Patient2 = HospitalizedPatient("John Doe")
myHospital.admit(Patient1)
myHospital.admit(Patient2)
# Admitting 3 patients that need emergency treatment
Patient3 = EmergencyPatient("Jane Smith")
Patient4 = EmergencyPatient("Jane Doe")
Patient5 = EmergencyPatient("Smitty Werbenjagermanjensen")
myHospital.admit(Patient3)
myHospital.admit(Patient4)
myHospital.admit(Patient5)
# End of day, discharge patients
myHospital.discharge_all()
# End of day, print total cost
myHospital.get_total_cost()
