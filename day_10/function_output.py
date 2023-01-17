

def full_name(f_name, l_name):
    if f_name == "" or l_name == "":
        return "Ops You didn't valid outputs"
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"
print(full_name(input("What is you first name? "),
      input("And your last name? ")))