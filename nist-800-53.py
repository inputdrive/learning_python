def create_intake_form():
    form = {}
    
    print("NIST 800-53r5 AC-Family Controls Intake Form")
    print("---------------------------------------------")
    
    form['control_id'] = input("Control ID: ")
    form['control_name'] = input("Control Name: ")
    form['control_description'] = input("Control Description: ")
    form['control_impact'] = input("Control Impact: ")
    form['control_status'] = input("Control Status: ")
    
    return form

intake_form = create_intake_form()
print(intake_form)