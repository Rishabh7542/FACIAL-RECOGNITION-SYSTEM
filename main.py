from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from student import Student
import os

class Frs:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # 1st image
        img1=Image.open("sample_images/image_29.webp")
        img1=img1.resize((500,150),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=0,y=0,width=500,height=150)


        # 2nd image
        img2=Image.open("sample_images/image_31.webp")
        img2=img2.resize((500,150),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=500,y=0,width=500,height=150)



        # 3rd image
        img3=Image.open("sample_images/image_35.webp")
        img3=img3.resize((550,150),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl3=Label(self.root,image=self.photoimg3)
        f_lbl3.place(x=1000,y=0,width=550,height=150)


        # 4th image-backgroud image
        img4=Image.open("sample_images/image_34.jpg")
        img4=img4.resize((1550,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=150,width=1550,height=710)

        title_lbl=Label(bg_img,text="Facial Recognition System",font=("Verdana", 30,"bold"),bg="black",fg="orange")
        title_lbl.place(x=0,y=0,width=1550,height=50)


        # student deatils - button 1
        img5=Image.open("sample_images/image_27.webp")
        img5=img5.resize((200,200),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b1=Button(bg_img,image=self.photoimg5,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=200,height=200)

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("Verdana", 15,"italic"),bg="white",fg="red")
        b1_1.place(x=200,y=300,width=200,height=25)


        # Detect Face - button 2
        img6=Image.open("sample_images/image_3.jpg")
        img6=img6.resize((200,200),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b2=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b2.place(x=500,y=100,width=200,height=200)

        b2_1=Button(bg_img,text="Detect Face",cursor="hand2",font=("Verdana", 15,"italic"),bg="white",fg="red")
        b2_1.place(x=500,y=300,width=200,height=25)


        # Attendance button 3
        img7=Image.open("sample_images/image_13.jpg")
        img7=img7.resize((200,200),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b3=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b3.place(x=800,y=100,width=200,height=200)

        b3_1=Button(bg_img,text="Attendance",cursor="hand2",font=("Verdana", 15,"italic"),bg="white",fg="red")
        b3_1.place(x=800,y=300,width=200,height=25)


        #Help button 4
        img8=Image.open("sample_images/image_1.jpg")
        img8=img8.resize((200,200),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b4=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b4.place(x=1100,y=100,width=200,height=200)

        b4_1=Button(bg_img,text="Help",cursor="hand2",font=("Verdana", 15,"italic"),bg="white",fg="red")
        b4_1.place(x=1100,y=300,width=200,height=25)


        #Train Data button 5
        img9=Image.open("sample_images/image_7.jpg")
        img9=img9.resize((200,200),Image.ANTIALIAS)
        self.photoimg9=ImageTk.PhotoImage(img9)

        b5=Button(bg_img,image=self.photoimg9,cursor="hand2")
        b5.place(x=350,y=350,width=200,height=200)

        b5_1=Button(bg_img,text="Train Data",cursor="hand2",font=("Verdana", 15,"italic"),bg="white",fg="red")
        b5_1.place(x=350,y=550,width=200,height=25)

        #Photos button 6
        img10=Image.open("sample_images/image_8.jpg")
        img10=img10.resize((200,200),Image.ANTIALIAS)
        self.photoimg10=ImageTk.PhotoImage(img10)

        b6=Button(bg_img,image=self.photoimg10,cursor="hand2",command=self.open_img)
        b6.place(x=650,y=350,width=200,height=200)

        b6_1=Button(bg_img,text="Photos",cursor="hand2",command=self.open_img,font=("Verdana", 15,"italic"),bg="white",fg="red")
        b6_1.place(x=650,y=550,width=200,height=25)

        #Exit button 7
        img11=Image.open("sample_images/image_11.webp")
        img11=img11.resize((200,200),Image.ANTIALIAS)
        self.photoimg11=ImageTk.PhotoImage(img11)

        b7=Button(bg_img,image=self.photoimg11,cursor="hand2")
        b7.place(x=950,y=350,width=200,height=200)

        b7_1=Button(bg_img,text="Exit",cursor="hand2",font=("Verdana", 15,"italic"),bg="white",fg="red")
        b7_1.place(x=950,y=550,width=200,height=25)


    

# --------------------------------- Function Buttons------------------------

    # student details button
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    # photos button
    def open_img(self):
        os.startfile("photo_set")




if __name__ == "__main__":
    root=Tk()
    obj=Frs(root)
    root.mainloop()