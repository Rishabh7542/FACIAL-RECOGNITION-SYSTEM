from ast import Try
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2


class Student:                # making class
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")

        # ------------------variables--------------
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.var_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_room=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_instructor=StringVar()
        self.var_radio1=StringVar()
        self.var_radio2=StringVar()





        # 1st image
        img1=Image.open("sample_images/image_14.jpg")
        img1=img1.resize((500,200),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl1=Label(self.root,image=self.photoimg1)
        f_lbl1.place(x=0,y=0,width=500,height=200)


        # 2nd image
        img2=Image.open("sample_images/image_15.jpg")
        img2=img2.resize((500,200),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl2=Label(self.root,image=self.photoimg2)
        f_lbl2.place(x=500,y=0,width=500,height=200)



        # 3rd image
        img3=Image.open("sample_images/image_16.jpg")
        img3=img3.resize((550,200),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        f_lbl3=Label(self.root,image=self.photoimg3)
        f_lbl3.place(x=1000,y=0,width=550,height=200)


        # 4th image-backgroud image
        img4=Image.open("sample_images/image_17.jpeg")
        img4=img4.resize((1550,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        bg_img=Label(self.root,image=self.photoimg4)
        bg_img.place(x=0,y=200,width=1550,height=710)

        title_lbl=Label(bg_img,text="Student Details",font=("Verdana", 30,"bold"),bg="black",fg="yellow")
        title_lbl.place(x=0,y=0,width=1550,height=50)

        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=10,y=60,width=1500,height=550)

        # left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Verdana", 12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=510)

        img_left=Image.open("sample_images/image_56.jpg")
        img_left=img_left.resize((720,100),Image.ANTIALIAS)
        self.photoimg_left_image=ImageTk.PhotoImage(img_left)

        f_lbl_left=Label(left_frame,image=self.photoimg_left_image)
        f_lbl_left.place(x=0,y=0,width=725,height=100)

        # Current Course Information Box
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("Verdana", 12,"bold"))
        current_course_frame.place(x=5,y=100,width=715,height=110)
        
        # Deprtment Label
        dep_label=Label(current_course_frame,text="Department",font=("Verdana", 12,"bold"),bg="yellow")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)
        
        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("Verdana", 12,"bold"),width=17,state="read only")
        dep_combo["values"]=("Select Department","BSBE","CSE","Civil","Chemical","ECE","EEE","M&C","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        # Course Label
        course_label=Label(current_course_frame,text="Course",font=("Verdana", 12,"bold"),bg="yellow")
        course_label.grid(row=0,column=2,padx=10,sticky=W)
        
        course_combo=ttk.Combobox(current_course_frame,textvariable=self.var_course,font=("Verdana", 12,"bold"),width=17,state="read only")
        course_combo["values"]=("Select Course","BTech","BDes","MTech")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        # Year Label
        year_label=Label(current_course_frame,text="Year",font=("Verdana", 12,"bold"),bg="yellow")
        year_label.grid(row=1,column=0,padx=10,sticky=W)
        
        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("Verdana", 12,"bold"),width=17,state="read only")
        year_combo["values"]=("Select Year","2019-2023","2020-2024","2021-2025","2022-2026","2022-2024","2021-2023")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)
  
        # Semester Label
        sem_label=Label(current_course_frame,text="Semester",font=("Verdana", 12,"bold"),bg="yellow")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)
        
        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semester,font=("Verdana", 12,"bold"),width=17,state="read only")
        sem_combo["values"]=("Select Semester","1st","2nd","3rd","4th","5th","6th","7th","8th")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)







        # Class and Student Information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class and Student Information",font=("Verdana", 12,"bold"))
        class_student_frame.place(x=5,y=213,width=715,height=270)
        
        # StudentId
        studentId_label=Label(class_student_frame,text="Student Id",font=("Verdana", 11,"bold"),bg="yellow")
        studentId_label.grid(row=0,column=0,padx=10,pady=4,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_id,width=16,font=("Verdana", 11,"bold"))
        studentId_entry.grid(row=0,column=1,padx=10,pady=4,sticky=W)


        # Student Name
        studentName_label=Label(class_student_frame,text="Student Name",font=("Verdana", 11,"bold"),bg="yellow")
        studentName_label.grid(row=0,column=2,padx=10,pady=4,sticky=W)
        
        studentId_entry=ttk.Entry(class_student_frame,textvariable=self.var_std_name,width=16,font=("Verdana", 11,"bold"))
        studentId_entry.grid(row=0,column=3,padx=10,pady=4,sticky=W)


        # Class room no.
        class_room_label=Label(class_student_frame,text="Class Room no.",font=("Verdana", 11,"bold"),bg="yellow")
        class_room_label.grid(row=1,column=0,padx=10,pady=4,sticky=W)
        
        # class_room_entry=ttk.Entry(class_student_frame,textvariable=self.var_room,width=16,font=("Verdana", 11,"bold"))
        # class_room_entry.grid(row=1,column=1,padx=10,pady=4,sticky=W)

        class_room_combo=ttk.Combobox(class_student_frame,textvariable=self.var_room,font=("Verdana", 12,"bold"),width=14,state="read only")
        class_room_combo["values"]=("","5001","5002","5003","5004","5005","5006")
        class_room_combo.current(0)
        class_room_combo.grid(row=1,column=1,padx=12,pady=4,sticky=W)
  

        # Roll number
        roll_no_label=Label(class_student_frame,text="Roll No.",font=("Verdana", 11,"bold"),bg="yellow")
        roll_no_label.grid(row=1,column=2,padx=10,pady=4,sticky=W)
        
        roll_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=16,font=("Verdana", 11,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=4,sticky=W)

        # Gender
        gender_label=Label(class_student_frame,text="Gender",font=("Verdana", 11,"bold"),bg="yellow")
        gender_label.grid(row=2,column=0,padx=10,pady=4,sticky=W)
        
        # gender_entry=ttk.Entry(class_student_frame,textvariable=self.var_gender,width=16,font=("Verdana", 11,"bold"))
        # gender_entry.grid(row=2,column=1,padx=10,pady=4,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("Verdana", 12,"bold"),width=14,state="read only")
        gender_combo["values"]=("","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=12,pady=4,sticky=W)
  


        # Date of Birth
        dob_label=Label(class_student_frame,text="Date of Birth",font=("Verdana", 11,"bold"),bg="yellow")
        dob_label.grid(row=2,column=2,padx=10,pady=4,sticky=W)
        
        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=16,font=("Verdana", 11,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=4,sticky=W)

        # Email
        email_label=Label(class_student_frame,text="Email",font=("Verdana", 11,"bold"),bg="yellow")
        email_label.grid(row=3,column=0,padx=10,pady=4,sticky=W)
        
        email_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=16,font=("Verdana", 11,"bold"))
        email_entry.grid(row=3,column=1,padx=10,pady=4,sticky=W)

        # Phone number
        phone_no_label=Label(class_student_frame,text="Phone No.",font=("Verdana", 11,"bold"),bg="yellow")
        phone_no_label.grid(row=3,column=2,padx=10,pady=4,sticky=W)
        
        phone_no_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=16,font=("Verdana", 11,"bold"))
        phone_no_entry.grid(row=3,column=3,padx=10,pady=4,sticky=W)

        # Course Instructor
        course_inst_label=Label(class_student_frame,text="Course Instructor",font=("Verdana", 11,"bold"),bg="yellow")
        course_inst_label.grid(row=4,column=0,padx=10,pady=4,sticky=W)
        
        # course_inst_entry=ttk.Entry(class_student_frame,textvariable=self.var_instructor,width=16,font=("Verdana", 11,"bold"))
        # course_inst_entry.grid(row=4,column=1,padx=10,pady=4,sticky=W)

        course_inst_combo=ttk.Combobox(class_student_frame,textvariable=self.var_instructor,font=("Verdana", 12,"bold"),width=14,state="read only")
        course_inst_combo["values"]=("","Prof. Vipul Datta","Prof. Ashok Kumar","Prof. Mahuya De","Prof. Mihir Kumar","Prof. Resmi Suresh")
        course_inst_combo.current(0)
        course_inst_combo.grid(row=4,column=1,padx=12,pady=4,sticky=W)
  



        # Radio Buttons
        radiobtn1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="Take a photo sample",value="Yes")
        radiobtn1.grid(row=5,column=0,padx=10,pady=2)

        
        radiobtn2=ttk.Radiobutton(class_student_frame,variable=self.var_radio2,text="Do not take photo sample",value="No")
        radiobtn2.grid(row=5,column=1,padx=10,pady=2)


        # Button Frame
        button_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        button_frame.place(x=0,y=190,width=705,height=33)

        # Save button
        save_btn=Button(button_frame,text="Save",command=self.add_data,width=16,font=("Verdana", 11,"bold"),bg="light green")
        save_btn.grid(row=0,column=0)

        # Update button
        update_btn=Button(button_frame,text="Update",command=self.update_data,width=17,font=("Verdana", 11,"bold"),bg="light blue")
        update_btn.grid(row=0,column=1)

        # Delete button
        delete_btn=Button(button_frame,text="Delete",command=self.delete_data,width=16,font=("Verdana", 11,"bold"),bg="red")
        delete_btn.grid(row=0,column=2)

        # Reset button
        reset_btn=Button(button_frame,text="Reset",command=self.reset_data,width=17,font=("Verdana", 11,"bold"),bg="gold")
        reset_btn.grid(row=0,column=3)

        # 2nd button frame
        button2_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        button2_frame.place(x=0,y=222,width=705,height=27)

        # Take photo sample
        take_photo_btn=Button(button2_frame,command=self.generate_dataset,text="Take photo sample",width=34,font=("Verdana", 11,"bold"),bg="orange")
        take_photo_btn.grid(row=0,column=0)

        # Update photo sample
        update_photo_btn=Button(button2_frame,text="Update photo sample",width=35,font=("Verdana", 11,"bold"),bg="orange")
        update_photo_btn.grid(row=0,column=1)









        # right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("Verdana", 12,"bold"))
        right_frame.place(x=750,y=10,width=730,height=510)

        img_right=Image.open("sample_images/image_58.jpg")
        img_right=img_right.resize((720,100),Image.ANTIALIAS)
        self.photoimg_right_image=ImageTk.PhotoImage(img_right)

        f_lbl_right=Label(right_frame,image=self.photoimg_right_image)
        f_lbl_right.place(x=0,y=0,width=725,height=100)



        # ----------------- Searching System --------------------

        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("Verdana", 12,"bold"))
        search_frame.place(x=5,y=110,width=715,height=65)
        
        search_label=Label(search_frame,text="Search By:",font=("Verdana", 12,"bold"),bg="gold")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)
        
        search_combo=ttk.Combobox(search_frame,font=("Verdana", 12,"bold"),width=13,state="read only")
        search_combo["values"]=("Select","Student Name","Student Id","Roll No.","Phone No.")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=5,sticky=W)

        search_entry=ttk.Entry(search_frame,width=13,font=("Verdana", 12,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=4,sticky=W)

        search_btn=Button(search_frame,text="Search",width=10,font=("Verdana", 12,"bold"),bg="light green")
        search_btn.grid(row=0,column=3,padx=2)

        show_all_btn=Button(search_frame,text="Show All",width=10,font=("Verdana", 12,"bold"),bg="light blue")
        show_all_btn.grid(row=0,column=4,padx=2)



        # -------------Table Frame------------
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=180,width=715,height=300)

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=("Dep","Course","Year","Sem","Id","Name","Room","Roll","Gender","DOB","Email","Phone","Instructor","Photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)


        self.student_table.heading("Dep",text="Department")
        self.student_table.heading("Course",text="Course")
        self.student_table.heading("Year",text="Year")
        self.student_table.heading("Sem",text="Semester")
        self.student_table.heading("Id",text="StudentId")
        self.student_table.heading("Name",text="Student Name")
        self.student_table.heading("Room",text="Room No.")
        self.student_table.heading("Roll",text="Roll No.")
        self.student_table.heading("Gender",text="Gender")
        self.student_table.heading("DOB",text="Date of Birth")
        self.student_table.heading("Email",text="Email")
        self.student_table.heading("Phone",text="Phone No.")
        self.student_table.heading("Instructor",text="Course Instructor")
        self.student_table.heading("Photo",text="Photo")

        self.student_table["show"]="headings"

        self.student_table.column("Dep",width=100)
        self.student_table.column("Course",width=100)
        self.student_table.column("Year",width=100)
        self.student_table.column("Sem",width=100)
        self.student_table.column("Id",width=100)
        self.student_table.column("Name",width=100)
        self.student_table.column("Roll",width=100)
        self.student_table.column("Gender",width=100)
        self.student_table.column("Room",width=100)
        self.student_table.column("DOB",width=100)
        self.student_table.column("Email",width=100)
        self.student_table.column("Phone",width=100)
        self.student_table.column("Instructor",width=100)
        self.student_table.column("Photo",width=100)

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    
    # --------------------------Function Declarartion---------------------------
    
    def add_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Bc4xz*G9mty",database="face_recogniser")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                
                                                                                                    self.var_dep.get(),
                                                                                                    self.var_course.get(),
                                                                                                    self.var_year.get(),
                                                                                                    self.var_semester.get(),
                                                                                                    self.var_std_id.get(),
                                                                                                    self.var_std_name.get(),
                                                                                                    self.var_room.get(),
                                                                                                    self.var_roll.get(),
                                                                                                    self.var_gender.get(),
                                                                                                    self.var_dob.get(),
                                                                                                    self.var_email.get(),
                                                                                                    self.var_phone.get(),
                                                                                                    self.var_instructor.get(),
                                                                                                    self.var_radio1.get(),
                                                                                                    

                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","Student details has been added successfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
    

# ---------------------fetch data-------------
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Bc4xz*G9mty",database="face_recogniser")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()





# ---------------------- get cursor(update)---------------------
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_room.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_instructor.set(data[12]),
        self.var_radio1.set(data[13])

    # --------------update funtion----------
    def update_data(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Do you want to update this student's details",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Bc4xz*G9mty",database="face_recogniser")
                    my_cursor=conn.cursor()

                    my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Room=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Instructor=%s,Photo=%s where StudentId=%s",(

                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                        self.var_course.get(),
                                                                                                                                                        self.var_year.get(),
                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                        self.var_room.get(),
                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                        self.var_instructor.get(),
                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                        self.var_std_id.get(),

                                                                                                                                                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            
            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)



# ---------delete function-----------------
    def delete_data(self):
        if self.var_std_id.get()=="":
            messagebox.showerror("Error","Student Id must be required",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Do you want to delete this student's record",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Bc4xz*G9mty",database="face_recogniser")
                    my_cursor=conn.cursor()
                    sql="delete from student where StudentId=%s"
                    val=(self.var_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted student details",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)





# ----------Reset function------------------------
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_course.set("Select Course")
        self.var_year.set("Select Year")
        self.var_semester.set("Select Semester")
        self.var_std_id.set("")
        self.var_std_name.set("")
        self.var_room.set("")
        self.var_roll.set("")
        self.var_gender.set("")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_instructor.set("")
        self.var_radio1.set("")








# ---------------------- Generate data set (Take photo samples) -----------------
    def generate_dataset(self):
        if self.var_dep.get()=="Select Department" or self.var_std_name.get()=="" or self.var_std_id.get()=="":
            messagebox.showerror("Error","All Fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Bc4xz*G9mty",database="face_recogniser")
                my_cursor=conn.cursor()  
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Course=%s,Year=%s,Semester=%s,Name=%s,Room=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Instructor=%s,Photo=%s where StudentId=%s",(

                                                                                                                                                        self.var_dep.get(),
                                                                                                                                                        self.var_course.get(),
                                                                                                                                                        self.var_year.get(),
                                                                                                                                                        self.var_semester.get(),
                                                                                                                                                        self.var_std_name.get(),
                                                                                                                                                        self.var_room.get(),
                                                                                                                                                        self.var_roll.get(),
                                                                                                                                                        self.var_gender.get(),
                                                                                                                                                        self.var_dob.get(),
                                                                                                                                                        self.var_email.get(),
                                                                                                                                                        self.var_phone.get(),
                                                                                                                                                        self.var_instructor.get(),
                                                                                                                                                        self.var_radio1.get(),
                                                                                                                                                        self.var_std_id.get()==id+1,

                                                                                                                                                    ))
          
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

            # ----------------- Load predefined data on face frontals from opencv--------------------
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)

                    # scaling fctor = 1.3
                    # Minimum Neighbour = 5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped

                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1

                        face=cv2.resize(face_cropped(my_frame),(400,400))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="photo_set/image."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX_SMALL,2,(0,255,0),2)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break

                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating dataset completed completed!!")

            except Exception as es:
                messagebox.showerror("Error",f"Due to:{str(es)}",parent=self.root)











if __name__ == "__main__":      # making object
    root=Tk()
    obj=Student(root)
    root.mainloop()