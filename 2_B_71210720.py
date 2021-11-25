string = "p"
integer = 123

def check_data_type(x,y):
    y = y.lower()
    if(type(x)==type(string)) and (y == "str"):
        print("Jawaban Anda benar")
        return True
    elif(type(x)==type(integer)) and (y == "int"):
        print("Jawaban Anda benar")
        return True
    elif(type(x)==type(string)) and (y == "int"):
        print("Jawaban Anda salah, seharusnya adalah: str")
        return False
    elif(type(x)==type(integer)) and (y == "str"):
        print("Jawaban Anda salah, seharusnya adalah: int")
        return False
    else:
        print("Inputan Tidak Valid")
        return False
    
print(check_data_type("Kevin","STr")) 
print(check_data_type("Kevin","str")) 
print(check_data_type(12345,"str")) 
print(check_data_type("9347","int"))
print(check_data_type(9876,"int"))