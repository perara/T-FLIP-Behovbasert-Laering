import os

def generate():

    student_names = []

    # Read all student names
    with open('./Students.txt') as file:
        for line in file.readlines():
            student_names.append(line.replace("\n",""))

    # Create students directory
    try:
        os.mkdir('./Students')
        print("Directory 'Students' created.")
    except:
        print("Directory already exists.")

    # Create all student directories
    for student_name in student_names:
        student_dir = './Students/' + student_name
        student_task_dir = './Students/' + student_name + "/Tasks"

        if try_mkdir(student_dir):
            try_mkdir(student_task_dir)
        else:
            print("Student \"{0}\" already exists.".format(student_name))



def try_mkdir(path):
    try:
        os.mkdir(path)
        return True
    except:
        return False

