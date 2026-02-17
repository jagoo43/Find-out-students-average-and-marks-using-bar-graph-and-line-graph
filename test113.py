import matplotlib.pyplot as plt
names=["ravi","imran","karan","sara"]
marks=[70,85,92,77]
percentages=[]
for i in marks:
        percentages.append((i/100)*100)
print(percentages)
def linechart():
        plt.plot(names,percentages)
        plt.show()
def barchart():
        plt.bar(names,percentages)
        plt.show()
linechart()
barchart()