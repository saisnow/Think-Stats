import Pmf
hist  = Pmf.MakeHistFromList([1,2,2,3,3,4,4,4,5])

def AllModes(hist):
	frq = []
	Max = 0
	for val, freq in hist.Items():

		if(max < freq):
			print(val)

		
