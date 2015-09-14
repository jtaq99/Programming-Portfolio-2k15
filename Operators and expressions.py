while True:
	days = int(raw_input("Enter days: "))
	months = days / 30
	days = days % 30
	print "Months = %d Days = %d" % (months, days)
	
	if (raw_input("Enter another? ") == "n"):
		break