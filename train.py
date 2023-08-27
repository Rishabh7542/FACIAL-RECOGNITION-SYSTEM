from ast import Try
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os 
import numpy as np


class train:                # making class
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")


        title_lbl=Label(self.root,text="TRAIN DATA SET",font=("Verdana", 30,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=0,y=0,width=1550,height=50)




        img_top=Image.open("sample_images/image_39.webp")
        img_top=img_top.resize((1550,740),Image.ANTIALIAS)
        self.photoimg_top_image=ImageTk.PhotoImage(img_top)

        f_lbl_top=Label(self.root,image=self.photoimg_top_image)
        f_lbl_top.place(x=0,y=50,width=1550,height=740)

        # train  button
        b6_1=Button(self.root,text="Train",cursor="hand2",command=self.train_classifier,font=("Verdana", 30,"italic"),bg="blue",fg="white")
        b6_1.place(x=65,y=395,width=340,height=50)


    def train_classifier(self):
        data_dir=("photo_set")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]

        for image in path:
            img=Image.open(image).convert('L')    # grayscale image
            imageNp=np.array(img,'uint8')          # uint8 is data type
            id=int(os.path.split(image)[1].split('.')[1])
            
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13                       # window closes on pressing enter
        ids=np.array(ids)


        # ----------------------Train the classifier and save-----------------

        clf=cv2.face.LBPHFaceRecgnizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training data set completed!!")













if __name__ == "__main__":      # making object
    root=Tk()
    obj=train(root)
    root.mainloop()