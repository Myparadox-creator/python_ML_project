# load   the dataset 
import pandas as pd
df=pd.read_csv(r"C:\Users\ASUS\OneDrive\Desktop\Dataset\titanic.csv")
df1=df.drop(columns=['PassengerId','Name','Ticket','Fare'])
#  drop the Cabin column  as most of values are missing 
df2=df1.drop(columns=['Cabin'])
df2.fillna({'Age':df2['Age'].mean()},inplace=True)
#  drop thr rows  with  missing missing value
df3=df2.dropna()
df3.isnull().sum()
#apply  Labelencoding  to convert categorical value to numeric
import warnings
warnings.filterwarnings('ignore')
from sklearn.preprocessing import LabelEncoder
LE=LabelEncoder()
df3['Sex']=LE.fit_transform(df3['Sex'])
df3['Embarked']=LE.fit_transform(df3['Embarked'])
#separate input  and output
X=df3.drop(columns=['Survived'])
Y=df3['Survived']
#split  data into 2 parts ... one part for training (80% lets say)
#and other part  for testing  (20% let say)
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2, random_state=5)
## apply knn
from sklearn.neighbors import KNeighborsClassifier
K=KNeighborsClassifier(n_neighbors=5)
# train the KNN  model  by using 80% training data
K.fit(X_train,Y_train)
# test the KNN model  by using   20%   data
Y_pred_knn=K.predict(X_test)
# accuracy
from sklearn.metrics import accuracy_score
acc_knn=accuracy_score(Y_test,Y_pred_knn)
acc_knn=round(acc_knn*100,2)
#######################################################################################################################
#######################################################################################################################
def submit():
    pc=int(Epc.get())
    sex=int(Esex.get())
    age=float(Eage.get())
    sibsp=int(Esibsp.get())
    parch=int(Eparch.get())
    em=int(Eem.get())
    result=K.predict([[pc,sex,age,sibsp,parch,em]])
    #print(result)
    if result[0]==1:
        msg = "U WILL SURVIVED"
    else:
        msg = "U WILL NOT SURVIVED"
    m.showinfo(title="Titanic survival", message = msg)
def reset():
    Epc.delete(0, END)
    Esex.delete(0, END)
    Eage.delete(0, END)
    Esibsp.delete(0, END)
    Eparch.delete(0, END)
    Eem.delete(0, END)
    
from tkinter import *
import tkinter.messagebox as m
w = Tk()
L = Label(w, text="Titanic survival prediction", font=('arial',20,'bold'), relief='solid')
L.grid(row = 1, column = 1, columnspan=2)
#######2nd row
Lpc = Label(w, text ="Passenger class", font = ('arial',15,'bold'))
Lpc.grid(row=2, column=1)
Epc= Entry(w, font=('arial',20,'bold'), width=10)
Epc.grid(row=2, column=2)
######3rd row
Lsex=Label(w, text="sex", font=('arial', 15, 'bold'))
Lsex.grid(row=3,column=1)
Esex = Entry(w, font = ('arial', 20, 'bold'), width = 10)
Esex.grid(row=3,column=2)
######4th row
Lage = Label(w, text ="age", font = ('arial',15,'bold'))
Lage.grid(row=4,column=1)
Eage= Entry(w, font=('arial',20,'bold'))
Eage.grid(row = 4,column=2)
# row 5
Lsibsp=Label(w,text="sibsp",font=('arial',15,'bold'))
Lsibsp.grid(row=5,column=1)
Esibsp=Entry(w,font=('arial',20,'bold'),width=10)
Esibsp.grid(row=5,column=2)
# row 6
Lparch=Label(w,text="Parch",font=('arial',15,'bold'))
Lparch.grid(row=6,column=1)
Eparch=Entry(w,font=('arial',20,'bold'),width=10)
Eparch.grid(row=6,column=2)
# row -7
Lem=Label(w,text="Embarked",font=('arial',15,'bold'))
Lem.grid(row=7,column=1)
Eem=Entry(w,font=('arial',20,'bold'),width=10)
Eem.grid(row=7,column=2)
# row-8
B1=Button(w,text="SUBMIT",font=('arial',15,'bold'), command=submit)
B1.grid(row=8,column=1)
B2=Button(w,text="RESET",font=('arial',15,'bold'), command=reset)
B2.grid(row=8,column=2)
w.mainloop()