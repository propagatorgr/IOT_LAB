from gpiozero import MotionSensor # Εισάγουμε την βιβλιοθήκη ελέγχου του ανιχνευτή.
pir = MotionSensor(4)  # Δηλώνουμε την έξοδο στο GP4
while True:   # Αρχή δομής επανάληψης
    pir.wait_for_motion() # Αναμονή κίνησης
    print("You moved")    # Τύπωσε το μήνυμα μόλις ανιχνευτεί κίνηση.
    pir.wait_for_no_motion() # Τερματισμός αναμονής κίνησης
# Τέλος δομής επανάληψης.
