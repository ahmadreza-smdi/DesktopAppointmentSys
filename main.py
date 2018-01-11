from config import *

global id_number = 0


class patient:
    def __init__(self,fname,lname,id_number,national_id
                ,phone_number,address,plate_number
                ,post_code,special_disease,blood_type):
               
                self.fname = fname
                self.lname = lname
                self.id_number = id_number
                self.national_id = national_id
                self.phone_number = phone_number
                self.address = address
                self.plate_number =plate_number
                self.post_code = post_code
                self.special_disease = special_disease
                self.blood_type = blood_type

			cur.execute(("INSERT INTO patient ( fname, lname,id ,national_id,phone_number,address ,plate_number,post_code,special_disease,blood_type)
                                        VALUES ('%s','%s','%s' ,'%s','%s','%s','%s','%s','%s','%s')")
				                                %(self.fname, self.lname,self.id_number ,self.national_id,self.phone_number,
				                                self.address ,self.plate_number,self.post_code,self.special_disease,self.blood_type))




def add_patient():
    print("Please enter the requested elements")
    fname = input("First name:")
    lname = input("Last name:")
    id_number = id_number + 1
    national_id = input ("National id:")
    phone_number = input ("phone number:")
    address = input ("Address:")
    plate_number = input("Plate number:")
    post_code = input("Post code:")
    special_disease = input ("Special disease:")
    blood_type = input("Blood type:")
    new =patient('%s','%s','%s' ,'%s','%s','%s','%s','%s','%s','%s')")
            %(fname,lname,id_number,national_id,phone_number,address,plate_number,post_code,special_disease,blood_type))




def del_patient():
    del_id = input("Enter the id that you like to delete:")
    cur.execute(("DELETE FROM patient WHERE id = '%s'")%(del_id))





def update_patient():
    up_id = input("Enter the id that you like to update:")
    up_field =input ("What do you want to update ?").lower()
    a = []
    a = cur.execute(("SELECT '%s' FROM patient WHERE id = '%s'")%(del_id,up_field))
    print("The last value of that was {}".format(a))
    b = input("enter the new value:")
    cur.execute("UPDATE patient SET '%s' = '%s' WHERE id = '%s' ")%(up_field,b,up_id)



