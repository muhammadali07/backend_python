#file grade_in.py
nilai = input("Inputkan nilaimu: ")

if int(nilai) >= 90:
   grade = "A"
elif int(nilai) >= 80:
   grade = "B+"
elif int(nilai) >= 70:
   grade = "B"
elif int(nilai) >= 60:
   grade = "C+"
elif int(nilai) >= 50:
   grade = "C"
elif int(nilai) >= 40:
   grade = "D"
else:
   grade = "E"

print("Grade: %s" % grade)