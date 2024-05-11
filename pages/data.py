SurveyName="New Untitled Survey"
Longitude=""
Lattitude=""
Intervals=0
Elevation=""
global p1
p1=0
global p2
p2= Intervals
value=""


dataset={"P1":[],"P2":[],"Reading 1":[],"Reading 2":[],"":[],"SP Reading":[]}

def add_data(rd1,rd2):
	global p1
	dataset["P1"]+=[p1]
	p1 = p1 + Intervals
	global p2
	dataset["P2"]+=[p2]
	p2 = p2 + Intervals
	rd = (rd1+rd2)/2
	dataset["Reading 1"]+=[rd1]
	dataset["Reading 2"]+=[rd2]
	dataset["SP Reading"]+=[rd]

def config():
	dataset={"P1":[],"P2":[],"Reading 1":[],"Reading 2":[],"":[],"SP Reading":[]}


