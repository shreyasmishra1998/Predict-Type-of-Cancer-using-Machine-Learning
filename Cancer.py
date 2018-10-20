import codecs
import csv
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn import tree
from sklearn.externals.six import StringIO
import pydotplus
filepath = "Potential datasets for recruitment (Cancer).csv"
with codecs.open(filepath,"r") as csvfile:
    reader = csv.reader(csvfile)
    data1 = [row for row in reader]
y = (np.shape(data1))
x = list(y)
data = data1
i = 1
s = 0
count = 0
while(i<700):
    if(data1[i][6] == "?"):
        i = i + 1
        count = count + 1
    else:
        s = s + float(data1[i][6])
        i = i + 1
avg = s/(x[0]-count)

i=0
j=0   
while(i<700):
    while(j<11):
        if(data1[i][j])=="?":
            data[i][j] = avg
            j = j + 1
        else:
            j = j + 1
    j = 0
    i = i + 1
i = []
j = 0
k = 101
while(k>100 and k<200):
    i.append(k)
    k = k + 1
k = 301
while(k>300 and k<400):
    i.append(k)
    k = k + 1    
target_names = ['Benign','Malignant']
j = 1
feature_names = []
while(j<=9):
    feature_names.append(data[0][j])
    j = j + 1
j=1
target = []
while(j<700):
    target.append(data[j][10])
    j = j + 1
k = 0
testing_target = []
testing_data = []
k = 0
while(k < len(i)):
    testing_target.append(target[i[k]])
    testing_data.append(data[i[k]+1][0:9])
    k = k + 1
training_target = []
training_data = []
j=2
while(j<700):
    if(j in i):
        j = j + 1
    else:
        training_target.append(data[j-1][10])
        training_data.append(data[j-1][0:9])
        j = j + 1
        
clf = tree.DecisionTreeClassifier()
clf.fit(training_data,training_target)

print(testing_target)
predictions = clf.predict(testing_data)
print(predictions)
print(accuracy_score(testing_target,predictions))

#Decision Tree in the PDF file
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,feature_names = feature_names,class_names = target_names,filled = True, rounded = True, impurity = False)
graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("Cancer.pdf")  

predictions = list(predictions)
a = 0
fpcount = 0
fncount = 0
while(a<len(testing_target)):
    if(testing_target[a] != predictions[a]):
        if(testing_target[a]=="2" and predictions[a]=="4"):
            fpcount = fpcount + 1
            a = a + 1
        elif(testing_target[a]=="4" and predictions[a]=="2"):
            fncount = fncount + 1
            a = a + 1
    else:
        a = a + 1
print("False Positives: ",fpcount)
print("False Negatives: ",fncount)
        











