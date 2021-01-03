import os
try:
    os.system("pyuic5 -x main1.ui -o converted_form.py")
except:
    print("can't find pyuic5")

from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QMainWindow,QApplication,QHeaderView,QTableWidgetItem,QWidget
import sqlite3,sys
import datetime

from converted_form import *
from delet_form import *
from edit_form import *
from edit_familly import *
from edit_visit import *
from edit_spons import *
from edit_meteriele import *
import sqlite3
db=sqlite3.connect("amal.db")
cr=db.cursor()

class guiForm(QMainWindow):
    def __init__(self):
        super().__init__()
        #table
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("جمعية الامل")

        self.ui.table1.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch)
        self.ui.table2.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch)
        self.ui.table3.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch)
        self.ui.table4.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch)
        self.ui.table5.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch)
        #self.ui.table6.horizontalHeader().setSectionResizeMode( 
            #QHeaderView.Stretch)
        self.ui.table7.horizontalHeader().setSectionResizeMode( 
            QHeaderView.Stretch)
        self.ui.choose1.currentIndexChanged.connect(self.comoboxCurrentValue)
       # الاشخاص
        self.ui.pushButton_7.clicked.connect(self.person_add)
        self.ui.pushButton_6.clicked.connect(self.person_edit)
        self.ui.pushButton_5.clicked.connect(self.person_remove)
        self.show_prson_table()
        self.ui.dateEdit.setDisplayFormat("dd/MM/yyyy")
       # عائلات
        self.ui.pushButton_14.clicked.connect(self.familly_add)
        self.ui.pushButton_13.clicked.connect(self.familly_edit)
        self.ui.pushButton_12.clicked.connect(self.familly_remove)
        self.show_familly_table()
       #زيارات اطباء
        self.ui.pushButton_18.clicked.connect(self.visitdoctor_add)
        self.ui.pushButton_17.clicked.connect(self.visitdoctor_edit)
        self.ui.pushButton_16.clicked.connect(self.visitdoctor_remove)
        self.show_visitdoctor_table()
        self.inestItem_in_cb_DoctorName()
        self.ui.dateEdit_2.setDisplayFormat("dd/MM/yyyy")
       #كفالات
        self.ui.dateEdit_3.setDisplayFormat("dd/MM/yyyy")
        self.ui.pushButton_20.clicked.connect(self.add_spons)
        self.ui.pushButton_21.clicked.connect(self.remove_spons)
        
        self.ui.pushButton_24.clicked.connect(self.add_person_spons)
        self.ui.pushButton_23.clicked.connect(self.edit_person_spons)
        self.ui.pushButton_22.clicked.connect(self.remove_person_spons)
        self.ui.dateEdit_3.setDisplayFormat("dd/MM/yyyy")
        self.ui.dateEdit_4.setDisplayFormat("dd/MM/yyyy")
        self.inestItem_in_cb_spons()
        self.inestItem_in_cb_sponsType()
        self.show_spons_table()
       #مواد
        self.ui.pushButton_27.clicked.connect(self.add_materiel)
        self.ui.pushButton_25.clicked.connect(self.remove_materiel)
        self.ui.pushButton_26.clicked.connect(self.edit_materiel)
        self.show_materiel_table()
       #فواتير
       #تقارير
       #مسلمات

#***********************الاشخاص

    def comoboxCurrentValue(self):
        #self.ui.choose1.setCurrentIndex(3)
        list_=[self.ui.textEdit,self.ui.label_22,self.ui.label_7,self.ui.lineEdit_7,self.ui.label_20,
        self.ui.comboBox_2,self.ui.dateEdit,self.ui.label_21,self.ui.label_12
        ,self.ui.lineEdit_2
        ]
        if self.ui.choose1.currentIndex()==0:
            for i in list_:
                i.show()



        elif self.ui.choose1.currentIndex() in (1,2) :
            for i in list_:
                i.show()
            for i in range(4):
                list_[i].hide()


        elif self.ui.choose1.currentIndex()==3:
            for i in list_:
                i.show()
            self.ui.lineEdit_7.hide()
            self.ui.label_22.hide()
        
        elif self.ui.choose1.currentIndex()==4:
            for i in list_:
                if i in [self.ui.label_22,self.ui.lineEdit_7]:
                    i.show()
                else:
                    i.hide()
# الاشخاص
    def person_add(self):
        list_=[self.ui.lineEdit_5,self.ui.lineEdit_2
        ,self.ui.lineEdit_7]

        cb_city=self.ui.comboBox_2
        cb_person=self.ui.choose1
        adreas=self.ui.textEdit
        date=self.ui.dateEdit
        def reset():
            list_=[self.ui.lineEdit_5,self.ui.lineEdit_2,self.ui.lineEdit_7]
            for i in list_: 
                i.setText("")
            self.ui.comboBox_2.setCurrentIndex(0)
            #self.ui.choose1.setCurrentIndex(0)
            self.ui.textEdit.setText("")

        if cb_person.currentIndex()==0:
            self.ui.label.setText("حدد نوع الشخص")

        elif cb_person.currentIndex() in (1,2):
            if list_[0].text().replace(" ","").isalpha() and list_[1].text().isdigit() and cb_city.currentIndex()!=0:
                self.ui.label.setText("تم اضافة بنجاح")
                cr.execute(f"INSERT INTO person(type_of_peson,name,place_of_birth,date_of_birth,national_number)VALUES('{cb_person.currentText()}','{list_[0].text()}','{cb_city.currentText()}','{date.text()}',{list_[1].text()});")
                #print(list_[0].text(),list_[1].text(),cb_city.currentText(),cb_person.currentText())
                db.commit()
                reset()
            else:
                self.ui.label.setText("قيمة خاطئة او حقل فارغ")
        elif cb_person.currentIndex()== 3:
            if list_[0].text().replace(" ","").isalpha() and list_[1].text().isdigit() and cb_city.currentIndex()!=0 and adreas.toPlainText().replace(" ","").isalnum():
                self.ui.label.setText("تم اضافة بنجاح")
                cr.execute(f"INSERT INTO person(type_of_peson,name,place_of_birth,date_of_birth,national_number,address)VALUES('{cb_person.currentText()}','{list_[0].text()}','{cb_city.currentText()}','{date.text()}',{list_[1].text()},'{adreas.toPlainText()}');")
                #print(list_[0].text(),list_[1].text(),cb_city.currentText(),cb_person.currentText())
                db.commit()
                reset()
            else:
                self.ui.label.setText("قيمة خاطئة او حقل فارغ")
        
        elif cb_person.currentIndex()== 4:
            if self.ui.lineEdit_7.text().replace(" ","").isalpha() and list_[0].text().replace(" ","").isalpha():
                self.ui.label.setText("تم اضافة بنجاح")
                #print(list_[0].text(),list_[1].text(),cb_city.currentText(),cb_person.currentText())
                cr.execute(f"INSERT INTO person(type_of_peson,name,speciality)VALUES('{cb_person.currentText()}','{list_[0].text()}','{self.ui.lineEdit_7.text()}');")
                db.commit()
                reset()
            else:
                self.ui.label.setText("قيمة خاطئة او حقل فارغ")        
        self.inestItem_in_cb_DoctorName()
        self.inestItem_in_cb_spons()
        self.show_prson_table()
    def person_remove(self):
        print("remove person")
        obj1=Ui_Form_delet()
        obj1.setWindowTitle("حذف شخص")
        obj1.show()
        number_of_record=len(cr.execute("select id from person;").fetchall())
        def get_number():
            if obj1.lineEdit.text().isdecimal():
                if int(obj1.lineEdit.text())<=0 or int(obj1.lineEdit.text())>number_of_record:
                    obj1.lable_error.setText("مستخدم غير موجود")
                else:
                    record=cr.execute(f"SELECT id FROM person LIMIT {int(obj1.lineEdit.text())}").fetchall()
                    cr.execute(f"delete from person where id={record[len(record)-1][0]}")
                    db.commit()
                    #print(record)
                    #print()
                    obj1.hide()
                    self.show_prson_table()
                    self.inestItem_in_cb_DoctorName()
                    self.inestItem_in_cb_spons()
            else:
                obj1.lable_error.setText("ادخل رقم صحيح")
        obj1.pushButton.clicked.connect(get_number)
        
    def person_edit(self):
        obj1=Ui_Form_delet()
        obj2=Ui_Form_edit()
        obj2.dateEdit.setDisplayFormat("yyyy/MM/dd")
        obj1.show()
        obj1.setWindowTitle("تعديل شخص")
        obj1.pushButton.setText("تعديل")
        obj1.lineEdit.clear()
        obj1.lable_error.setText("")
        cb=""
        id_=0
        
        def insert_edit():
            global cb
            global id_
                    #database check
            if cb in ("موظفين","كفلاء"):
                if obj2.lineEdit_5.text().replace(" ","").isalpha() and obj2.lineEdit_2.text().isdecimal() and obj2.comboBox_2.currentIndex()!=0:
                    obj2.erro_messsage.setText("تم تعديل")
                    cr.execute(f"UPDATE person SET name='{obj2.lineEdit_5.text()}',place_of_birth='{obj2.comboBox_2.currentText()}',date_of_birth='{obj2.dateEdit.text()}',national_number='{obj2.lineEdit_2.text()}' where id={id_};")
                    db.commit()
                    self.inestItem_in_cb_DoctorName()
                    self.inestItem_in_cb_spons()
                else:
                    obj2.erro_messsage.setText("قيمة خاطئة او حقل فارغ")
            elif cb=="مستفيدين":
                if obj2.lineEdit_5.text().replace(" ","").isalpha() and obj2.lineEdit_2.text().isdecimal() and obj2.comboBox_2.currentIndex()!=0 and obj2.textEdit.toPlainText().replace(" ","").isalnum():
                    obj2.erro_messsage.setText("تم تعديل")
                    cr.execute(f"UPDATE person SET name='{obj2.lineEdit_5.text()}',place_of_birth='{obj2.comboBox_2.currentText()}',date_of_birth='{obj2.dateEdit.text()}',national_number='{obj2.lineEdit_2.text()}',address='{obj2.textEdit.toPlainText()}' where id={id_};")
                    db.commit()
                    self.inestItem_in_cb_DoctorName()
                    self.inestItem_in_cb_spons()    
                else:
                    obj2.erro_messsage.setText("قيمة خاطئة او حقل فارغ")
            elif cb=="اطباء":
                if obj2.lineEdit_5.text().replace(" ","").isalpha() and obj2.lineEdit_7.text().replace(" ","").isalpha():
                    obj2.erro_messsage.setText("تم تعديل")
                    cr.execute(f"UPDATE person SET name='{obj2.lineEdit_5.text()}',speciality='{obj2.lineEdit_7.text()}' where id={id_};")
                    db.commit()
                    self.inestItem_in_cb_DoctorName()
                    self.inestItem_in_cb_spons()
                else:
                    obj2.erro_messsage.setText("قيمة خاطئة او حقل فارغ")
            self.show_prson_table()
            
        def show_edit_form():
            global cb
            global id_
            if cb in ("موظفين","كفلاء"):
                obj2.label_7.hide()
                obj2.textEdit.hide()
                obj2.label_22.hide()
                obj2.lineEdit_7.hide()
                rec=cr.execute(f"select * from person where id={id_}").fetchall()
                obj2.dateEdit.setDate(datetime.datetime.strptime(str(rec[0][4]).replace("/","-"), '%Y-%m-%d').date())
                obj2.lineEdit_5.setText(rec[0][2])
                obj2.lineEdit_2.setText(str(rec[0][5]))
                obj2.comboBox_2.setCurrentText(rec[0][3])
                obj2.show()

            elif cb=="مستفيدين":
                obj2.label_22.hide()
                obj2.lineEdit_7.hide()
                rec=cr.execute(f"select * from person where id={id_}").fetchall()
                obj2.dateEdit.setDate(datetime.datetime.strptime(str(rec[0][4]).replace("/","-"), '%Y-%m-%d').date())
                obj2.lineEdit_5.setText(rec[0][2])
                obj2.lineEdit_2.setText(str(rec[0][5]))
                obj2.comboBox_2.setCurrentText(rec[0][3])
                obj2.textEdit.setText(rec[0][6])
                print(rec)
                obj2.show()

                obj2.show()
            elif cb=="اطباء":
                list_=[obj2.label_7,obj2.textEdit,obj2.label_12,obj2.lineEdit_2,obj2.label_21,obj2.label_20,obj2.dateEdit,obj2,obj2.comboBox_2]
                for i in list_:
                    i.hide()
                rec=cr.execute(f"select * from person where id={id_}").fetchall()
                obj2.lineEdit_5.setText(rec[0][2])
                obj2.lineEdit_7.setText(str(rec[0][7]))

                obj2.show()
            
        def get_number():
            global cb
            global id_
            number_of_record=len(cr.execute("select id from person;").fetchall())
            if obj1.lineEdit.text().isdecimal():
                if int(obj1.lineEdit.text())<=0 or int(obj1.lineEdit.text())>number_of_record:
                    obj1.lable_error.setText("مستخدم غير موجود")
                else:
                    record=cr.execute(f"SELECT type_of_peson,id FROM person LIMIT {int(obj1.lineEdit.text())}").fetchall()

                    cb=record[len(record)-1][0]
                    id_=record[len(record)-1][1]
                    obj1.hide()
                    show_edit_form()

            else:
                obj1.lable_error.setText("ادخل رقم صحيح")
                    

        obj2.pushButton_6.clicked.connect(insert_edit)
        obj1.pushButton.clicked.connect(get_number)

    def show_prson_table(self):
        records=cr.execute("select type_of_peson,name,place_of_birth,date_of_birth,national_number,address,speciality from person;").fetchall()
        self.ui.table1.setRowCount(len(records))

        for row,items in enumerate(records):
            for column,item in enumerate(items):
                self.ui.table1.setItem(row,column,QTableWidgetItem(str(item)))
                #print(row,column,item)
#***********************عائلات

    def familly_add(self):
        list_alpha=[self.ui.lineEdit_3,self.ui.lineEdit_6,self.ui.lineEdit_12]
        list_num=[self.ui.lineEdit_8,self.ui.lineEdit_9, self.ui.lineEdit_10]
        list_textalph_num=[self.ui.textEdit_2,self.ui.textEdit_3]
        number_of_familly=self.ui.spinBox.text()
        def reset():
            for i in list_alpha+list_num+list_textalph_num:
                i.setText("")
            self.ui.spinBox.clear()

        check_alpha=True
        check_alph_num=True
        check_num=True
        for i in list_alpha:
            check_alpha=check_alpha*i.text().replace(" ","").isalpha()
        #print(check)
        for i in list_num:
            check_num=check_num*i.text().isdecimal()
        #print(check_num)
        for i in list_textalph_num:
            check_alph_num=check_alph_num*i.toPlainText().replace(" ","").isalnum()
        
        if check_alph_num and check_alpha and check_num :
            self.ui.label_137.setText("تم اضافة بنجاح")
            cr.execute(f"insert into famillys (husband_name,wife_name,husband_job,national_number,phone_number,family_book_number,current_addreas,last_addreas,familly_member)values('{list_alpha[0].text()}','{list_alpha[1].text()}','{list_alpha[2].text()}','{list_num[0].text()}','{list_num[1].text()}','{list_num[2].text()}','{list_textalph_num[0].toPlainText()}','{list_textalph_num[1].toPlainText()}','{number_of_familly}')")
            db.commit()
            self.show_familly_table()
            reset()
        else:
            self.ui.label_137.setText("قيمة خاطئة او حقل فارغ")


    def familly_remove(self):
        print("remove familly")
        obj1=Ui_Form_delet()
        obj1.setWindowTitle("حذف عائلة")
        obj1.show()
        number_of_record=len(cr.execute("select id from famillys;").fetchall())

        def get_number():
            if obj1.lineEdit.text().isdecimal():
                if int(obj1.lineEdit.text())<=0 or int(obj1.lineEdit.text())>number_of_record:
                    obj1.lable_error.setText("مستخدم غير موجود")
                else:
                    record=cr.execute(f"SELECT id FROM famillys LIMIT {int(obj1.lineEdit.text())}").fetchall()
                    cr.execute(f"delete from famillys where id={record[len(record)-1][0]}")
                    db.commit()
                    obj1.hide()
                    self.show_familly_table()
            else:
                obj1.lable_error.setText("ادخل رقم صحيح") 
        obj1.pushButton.clicked.connect(get_number)

    def familly_edit(self):
        obj1=Ui_Form_delet()
        obj2=Ui_Form_edit_familly()
        obj1.setWindowTitle("تعديل عائلة")
        obj1.pushButton.setText("تعديل")
        obj1.show()
        number_of_record=len(cr.execute("select id from famillys;").fetchall())
        id_=None

        def insert_edit():
            global id_
            list_num=[obj2.lineEdit_26,obj2.lineEdit_27,obj2.lineEdit_29]
            list_alpha=[obj2.lineEdit_28,obj2.lineEdit_30,obj2.lineEdit_4]
            list_alpha_number=[obj2.textEdit_7,obj2.textEdit_6]
            cheke_num=True
            cheke_alpha=True
            cheke_alpha_num=True
            for i in list_alpha:
                cheke_alpha*=i.text().replace(" ","").isalpha()
            for i in list_num:
                cheke_num*=i.text().isdecimal()
            for i in list_alpha_number:
                cheke_alpha_num*=i.toPlainText().replace(" ","").isalnum()
            obj2.spinBox_3.text()
            if cheke_alpha and cheke_alpha_num and cheke_num:
                obj2.label_143.setText("تم اضافة بنجاح")
                cr.execute(f"update famillys set husband_name='{list_alpha[2].text()}',wife_name='{list_alpha[1].text()}',husband_job='{list_alpha[0].text()}',national_number='{list_num[0].text()}',phone_number='{list_num[1].text()}',family_book_number='{list_num[2].text()}',current_addreas='{list_alpha_number[0].toPlainText()}',last_addreas='{list_alpha_number[1].toPlainText()}',familly_member='{obj2.spinBox_3.text()}' where id={id_}")
                db.commit()
                self.show_familly_table()
            else:
                obj2.label_143.setText("قيمة خاطئة او حقل فارغ")
        def show_familly_info():
            global id_
            record=cr.execute(f"select husband_name,wife_name,national_number,phone_number,family_book_number,familly_member,husband_job,current_addreas,last_addreas from famillys where id={id_};").fetchall()
            obj2.lineEdit_4.setText(record[0][0])
            obj2.lineEdit_30.setText(record[0][1])
            obj2.lineEdit_26.setText(record[0][2])
            obj2.lineEdit_27.setText(record[0][3])
            obj2.lineEdit_29.setText(record[0][4])
            obj2.spinBox_3.setValue(int(record[0][5]))   #spinBox
            obj2.lineEdit_28.setText(record[0][6])
            obj2.textEdit_7.setText(record[0][7])
            obj2.textEdit_6.setText(record[0][8])
            
        def get_number():
            global id_
            if obj1.lineEdit.text().isdecimal():
                if int(obj1.lineEdit.text())<=0 or int(obj1.lineEdit.text())>number_of_record:
                    obj1.lable_error.setText("مستخدم غير موجود")
                else:
                    record=cr.execute(f"SELECT id FROM famillys LIMIT {int(obj1.lineEdit.text())}").fetchall()
                    id_=record[len(record)-1][0]
                    obj1.hide()
                    obj2.show()
                    show_familly_info()
                    print(id_)    
            else:
                obj1.lable_error.setText("ادخل رقم صحيح") 

        obj1.pushButton.clicked.connect(get_number)
        obj2.pushButton_29.clicked.connect(insert_edit)
        

    def show_familly_table(self):
        records=cr.execute("select husband_name,wife_name,national_number,family_book_number,familly_member,husband_job,current_addreas,last_addreas from famillys;").fetchall()
        self.ui.table2.setRowCount(len(records))
        for row,items in enumerate(records):
            for column,item in enumerate(items):
                self.ui.table2.setItem(row,column,QTableWidgetItem(str(item)))
#***********************زيارات الاطباء
    def visitdoctor_add(self):
        def reset():
            self.ui.comboBox.setCurrentIndex(0)
            self.ui.comboBox_4.setCurrentIndex(0)
            self.ui.textEdit_4.setText("")
            self.ui.label_33.setText("")
        tp="اطباء"
        if self.ui.comboBox.currentIndex()!=0 and self.ui.comboBox_4.currentIndex()!=0 and self.ui.textEdit_4.toPlainText().replace(" ","").isalnum():
            self.ui.label_138.setText("تم اضافة بنجاح")
            sp=cr.execute(f"select speciality from person where name='{self.ui.comboBox.currentText()}' and type_of_peson='{tp}'").fetchone()
            print(sp)
            cr.execute(f"insert into doctors_visits(doctor_name,speciality,beneficiary_name,diagnose_date,diagnose)values('{self.ui.comboBox.currentText()}','{sp[0]}','{self.ui.comboBox_4.currentText()}','{self.ui.dateEdit_2.text()}','{self.ui.textEdit_4.toPlainText()}')")
            db.commit()
            reset()
            self.show_visitdoctor_table()
        else:
            self.ui.label_138.setText("قيمة خاطئة او حقل فارغ")

    def visitdoctor_remove(self):
        obj1=Ui_Form_delet()
        obj1.setWindowTitle("حذف زيارة")
        obj1.show()
        number_of_record=len(cr.execute("select id from doctors_visits;").fetchall())
        def get_number():
            if obj1.lineEdit.text().isdecimal():
                if int(obj1.lineEdit.text())<=0 or int(obj1.lineEdit.text())>number_of_record:
                    obj1.lable_error.setText("مستخدم غير موجود")
                else:
                    record=cr.execute(f"SELECT id FROM doctors_visits LIMIT {int(obj1.lineEdit.text())}").fetchall()
                    cr.execute(f"delete from doctors_visits where id={record[len(record)-1][0]}")
                    db.commit()
                    #print(record)
                    #print()
                    obj1.hide()
                    self.show_visitdoctor_table()
            else:
                obj1.lable_error.setText("ادخل رقم صحيح")
        obj1.pushButton.clicked.connect(get_number)

    def visitdoctor_edit(self):
        print("*****editing***********")
        obj1=Ui_Form_delet()
        obj1.setWindowTitle("تعديل زيارة")
        obj1.pushButton.setText("تعديل")
        obj1.show()
        obj2=Ui_Form_edit_visit()
        obj2.dateEdit_2.setDisplayFormat("yyyy/MM/dd")

        id_=None
        number_of_record=len(cr.execute("select id from doctors_visits;").fetchall())
        def insert_into_db():
            global id_
            tp="اطباء"

            if obj2.comboBox_4.currentIndex()!=0 and obj2.comboBox.currentIndex()!=0 and obj2.textEdit_4.toPlainText().replace(" ","").isalnum():
                sp=cr.execute(f"select speciality from person where name='{obj2.comboBox.currentText()}' and type_of_peson='{tp}';").fetchone()
                
                cr.execute(f"update doctors_visits set doctor_name='{obj2.comboBox.currentText()}',speciality='{sp[0]}',beneficiary_name='{obj2.comboBox_4.currentText()}',diagnose_date='{obj2.dateEdit_2.text()}',diagnose='{obj2.textEdit_4.toPlainText()}' where id={id_}")
                db.commit()
                obj2.label_138.setText("تم التعديل بنجاح")
                self.show_visitdoctor_table()
            else:
                obj2.label_138.setText("قيمة خاطئة او حقل فارغ")

        def insert_info():
            global id_
            record=cr.execute(f"select * from doctors_visits where id={id_};").fetchall()
            print(record[0])
            obj2.textEdit_4.setText(record[0][5])
            
            str_="اطباء"
            obj2.comboBox.clear()
            obj2.comboBox_4.clear()
            obj2.comboBox.addItem("-----------")
            obj2.comboBox_4.addItem("-----------")
            record_doctor=cr.execute(f"select name from person where type_of_peson='{str_}';").fetchall()
            str_="مستفيدين"
            record_benefite=cr.execute(f"select name from person where type_of_peson='{str_}';").fetchall()
            for item in record_doctor:
                obj2.comboBox.addItem(item[0])
            for item in record_benefite:
                obj2.comboBox_4.addItem(item[0])
            obj2.dateEdit_2.setDate(datetime.datetime.strptime(str(record[0][4]).replace("/","-"), '%Y-%m-%d').date())
            obj2.comboBox.setCurrentText(record[0][1])
            obj2.comboBox_4.setCurrentText(record[0][3])
        def get_number():
            global id_
            if obj1.lineEdit.text().isdecimal():
                if int(obj1.lineEdit.text())<=0 or int(obj1.lineEdit.text())>number_of_record:
                    obj1.lable_error.setText("مستخدم غير موجود")
                else:
                    record=cr.execute(f"SELECT id FROM doctors_visits LIMIT {int(obj1.lineEdit.text())}").fetchall()
                    id_=record[len(record)-1][0]
                    insert_info()
                    obj1.hide()
                    obj2.show()
            else:
                obj1.lable_error.setText("ادخل رقم صحيح")
        obj1.pushButton.clicked.connect(get_number)
        obj2.pushButton_17.clicked.connect(insert_into_db)
    def show_visitdoctor_table(self):
        records=cr.execute("select doctor_name,speciality,beneficiary_name,diagnose_date,diagnose from doctors_visits;").fetchall()
        self.ui.table3.setRowCount(len(records))

        for row,items in enumerate(records):
            for column,item in enumerate(items):
                self.ui.table3.setItem(row,column,QTableWidgetItem(str(item)))

    def inestItem_in_cb_DoctorName(self):
        str_="اطباء"
        self.ui.comboBox.clear()
        self.ui.comboBox_4.clear()
        self.ui.comboBox.addItem("-----------")
        self.ui.comboBox_4.addItem("-----------")
        record_doctor=cr.execute(f"select name from person where type_of_peson='{str_}';").fetchall()
        str_="مستفيدين"
        record_benefite=cr.execute(f"select name from person where type_of_peson='{str_}';").fetchall()
        for item in record_doctor:
            self.ui.comboBox.addItem(item[0])
        for item in record_benefite:
            self.ui.comboBox_4.addItem(item[0])
#***********************كفلات
 #******* انواع كفالات
    def add_spons(self):
        print("add_spons")
        if self.ui.lineEdit_21.text().replace(" ","").isalpha():
            self.ui.label_139.setText("تم اضافة كفالة")
            cr.execute(f"insert into sponsor_types(sponsor_type)values('{self.ui.lineEdit_21.text()}')")
            db.commit()
            self.ui.lineEdit_21.clear()
            self.inestItem_in_cb_sponsType()
            
        else:
            self.ui.label_139.setText("ادخل كفالة صحيحة") 
    def remove_spons(self):
        obj1=Ui_Form_delet()
        obj1.setWindowTitle("حذف نوع كفالة")
        obj1.pushButton.setText("حذف")
        obj1.label.setText("ادخل نوع الكفالة")
        obj1.label.resize(106,25)
        obj1.lineEdit.setPlaceholderText("")

        obj1.show()
        def del_spons():
            if obj1.lineEdit.text().replace(" ","").isalpha():
                record=cr.execute("select sponsor_type from sponsor_types").fetchall()
                if (obj1.lineEdit.text(),) in record:
                    cr.execute(f"delete from sponsor_types where sponsor_type='{obj1.lineEdit.text()}'").fetchall()
                    db.commit()
                    self.inestItem_in_cb_sponsType()
                    obj1.hide()
                else:
                    obj1.lable_error.setText("كفالة غير موجودة")

            else:
                obj1.lable_error.setText("قيمة خاطئة او حقل فارغ")
        obj1.pushButton.clicked.connect(del_spons)


    def inestItem_in_cb_sponsType(self):
        self.ui.comboBox_3.clear()
        self.ui.comboBox_3.addItem("-----------")
        record_spons_type=cr.execute(f"select sponsor_type from sponsor_types;").fetchall()
        for item in record_spons_type:
            self.ui.comboBox_3.addItem(item[0])
    
 #******* الكفلات
    def inestItem_in_cb_spons(self):
        str_="كفلاء"
        self.ui.comboBox_6.clear()
        self.ui.comboBox_8.clear()
        self.ui.comboBox_6.addItem("-----------")
        self.ui.comboBox_8.addItem("-----------")
        record_spons=cr.execute(f"select name from person where type_of_peson='{str_}';").fetchall()
        str_="مستفيدين"
        record_benefite=cr.execute(f"select name from person where type_of_peson='{str_}';").fetchall()
        for item in record_spons:
            self.ui.comboBox_6.addItem(item[0])
        for item in record_benefite:
            self.ui.comboBox_8.addItem(item[0])
        
    def add_person_spons(self):
        def reset():
            self.ui.comboBox_6.setCurrentIndex(0)
            self.ui.comboBox_8.setCurrentIndex(0)
            self.ui.comboBox_3.setCurrentIndex(0)
        if self.ui.comboBox_6.currentIndex()!=0 and self.ui.comboBox_8.currentIndex()!=0 and self.ui.comboBox_3.currentIndex()!=0:
            cr.execute(f"insert into sponsor (sponsor_name,beneficiary_name,starting_sponsor_date,expiry__sponsor_date,sponsor_type)values('{self.ui.comboBox_6.currentText()}','{self.ui.comboBox_8.currentText()}','{self.ui.dateEdit_3.text()}','{self.ui.dateEdit_4.text()}','{self.ui.comboBox_3.currentText()}');")
            db.commit()
            self.ui.label_139.setText("تمت الاضافة بنجاح")
            reset()
        
        else:
            self.ui.label_139.setText("قيمة خاطئة او حقل فارغ")
        self.show_spons_table()
    def edit_person_spons(self):
        obj1=Ui_Form_delet()
        obj1.show()
        obj2=Ui_Form_edit_spons()
        obj2.dateEdit_3.setDisplayFormat("yyyy/MM/dd")
        obj2.dateEdit_4.setDisplayFormat("yyyy/MM/dd")
        obj1.setWindowTitle("تعديل كفالة") 
        obj1.pushButton.setText("تعديل")
        number_of_record=len(cr.execute("select id from sponsor;").fetchall())
        id_=None
        def update_info():
            global id_
            obj2.comboBox_6.currentText()
            cr.execute(f"update sponsor set sponsor_name='{obj2.comboBox_6.currentText()}',beneficiary_name='{obj2.comboBox_8.currentText()}',starting_sponsor_date='{obj2.dateEdit_3.text()}',expiry__sponsor_date='{obj2.dateEdit_4.text()}',sponsor_type='{obj2.comboBox_3.currentText()}' where id={id_} ")
            db.commit()
            obj2.label_139.setText("تم التعديل")
            self.show_spons_table()
        def insert_info():
            global id_
            obj2.comboBox_6.clear()
            obj2.comboBox_8.clear()
            obj2.comboBox_3.clear()
            
            str_="كفلاء"
            cb_1=cr.execute(f"select name from person where type_of_peson='{str_}';").fetchall()
            str_="مستفيدين"
            cb_2=cr.execute(f"select name from person where type_of_peson='{str_}';").fetchall()
            cb_3=cr.execute(f"select sponsor_type from sponsor_types;").fetchall()
            for item in cb_1:
                obj2.comboBox_6.addItem(item[0])
            for item in cb_2:
                obj2.comboBox_8.addItem(item[0])
            for item in cb_3:
                obj2.comboBox_3.addItem(item[0])
            cb_1=cr.execute(f"select sponsor_name,beneficiary_name,starting_sponsor_date,expiry__sponsor_date,sponsor_type from sponsor where id='{id_}';").fetchall()
            obj2.comboBox_6.setCurrentText(cb_1[0][0])
            obj2.comboBox_8.setCurrentText(cb_1[0][1])
            obj2.comboBox_3.setCurrentText(cb_1[0][4])
            obj2.dateEdit_3.setDate(datetime.datetime.strptime(str(cb_1[0][2]).replace("/","-"), '%Y-%m-%d').date())
            obj2.dateEdit_4.setDate(datetime.datetime.strptime(str(cb_1[0][3]).replace("/","-"), '%Y-%m-%d').date())
        def get_number():
            global id_
            if obj1.lineEdit.text().isdecimal():
                if int(obj1.lineEdit.text())<=0 or int(obj1.lineEdit.text())>number_of_record:
                    obj1.lable_error.setText("مستخدم غير موجود")
                else:
                    record=cr.execute(f"SELECT id FROM sponsor LIMIT {int(obj1.lineEdit.text())}").fetchall()
                    id_=record[len(record)-1][0]
                    insert_info()
                    obj1.hide()
                    insert_info()
                    obj2.show()
            else:
                obj1.lable_error.setText("ادخل رقم صحيح")
        obj1.pushButton.clicked.connect(get_number)
        obj2.pushButton_23.clicked.connect(update_info)
    def remove_person_spons(self):
        obj1=Ui_Form_delet()
        obj1.setWindowTitle("حذف كفالة")
        obj1.pushButton.setText("حذف")
        obj1.show()
        number_of_record=len(cr.execute("select id from sponsor;").fetchall())
        def get_number():
            if obj1.lineEdit.text().isdecimal():
                if int(obj1.lineEdit.text())<=0 or int(obj1.lineEdit.text())>number_of_record:
                    obj1.lable_error.setText("مستخدم غير موجود")
                else:
                    record=cr.execute(f"SELECT id FROM sponsor LIMIT {int(obj1.lineEdit.text())}").fetchall()
                    cr.execute(f"delete from sponsor where id={record[len(record)-1][0]}")
                    db.commit()
                    obj1.hide()
                    self.show_spons_table()

            else:
                obj1.lable_error.setText("قيمة خاطئة او حقل فارغ")
        obj1.pushButton.clicked.connect(get_number)
    def show_spons_table(self):
        records=cr.execute("select sponsor_name,beneficiary_name,starting_sponsor_date,expiry__sponsor_date,sponsor_type from sponsor;").fetchall()
        self.ui.table4.setRowCount(len(records))
        for row,items in enumerate(records):
            for column,item in enumerate(items):
                self.ui.table4.setItem(row,column,QTableWidgetItem(str(item)))
#***********************المواد
    def add_materiel(self):
        def reset():
            self.ui.lineEdit_22.clear()
            self.ui.lineEdit_52.clear()
            self.ui.textEdit_5.clear()
        if self.ui.lineEdit_22.text().isdecimal() and self.ui.lineEdit_52.text().replace(" ","").isalnum() and self.ui.textEdit_5.toPlainText().replace(" ","").isalnum():
            self.ui.label_140.setText("تم الاضافة بنجاح")
            cr.execute(f"insert into materials(material_symbol,item_describe,notes)values('{self.ui.lineEdit_22.text()}','{self.ui.lineEdit_52.text()}','{self.ui.textEdit_5.toPlainText()}')")
            db.commit()
            self.show_materiel_table()
            reset()
        else:
            self.ui.label_140.setText("حقل فارغ او قيمة خاطئة")

    def remove_materiel(self):
        obj1=Ui_Form_delet()
        obj1.show()
        obj1.setWindowTitle("حذف مادة")
        number_of_record=len(cr.execute("select id from materials;").fetchall())

        def get_number():
            if obj1.lineEdit.text().isdecimal():
                if int(obj1.lineEdit.text())<=0 or int(obj1.lineEdit.text())>number_of_record:
                    obj1.lable_error.setText("مستخدم غير موجود")
                else:
                    record=cr.execute(f"SELECT id FROM materials LIMIT {int(obj1.lineEdit.text())}").fetchall()
                    cr.execute(f"delete from materials where id={record[len(record)-1][0]}")
                    db.commit()
                    obj1.hide()
                    self.show_materiel_table()
            else:
                obj1.lable_error.setText("ادخل رقم صحيح")

        obj1.pushButton.clicked.connect(get_number)

    def edit_materiel(self):
        obj1=Ui_Form_delet()
        obj1.show()
        obj1.setWindowTitle("تعديل مادة")
        obj1.pushButton.setText("تعديل")
        obj2=Ui_Form_edit_meteriel()
        number_of_record=len(cr.execute("select id from materials;").fetchall())
        id_=None
        def update_info():
            global id_
            if obj2.lineEdit_22.text().isdecimal() and obj2.lineEdit_52.text().replace(" ","").isalpha() and  obj2.textEdit_5.toPlainText().replace(" ","").isalpha():
                cr.execute(f"update materials set  material_symbol='{obj2.lineEdit_22.text()}',item_describe='{obj2.lineEdit_52.text()}',notes='{obj2.textEdit_5.toPlainText()}' where id={id_}")
                db.commit()
                obj2.label_140.setText("تمت  التعديل  بنجاح") 
                self.show_materiel_table()
            else:
                obj2.label_140.setText("قيمة خاطئة او حقل فارغ")
        def insert_info():
            global id_
            record=cr.execute(f"select material_symbol,item_describe,notes from materials where id={id_};").fetchone()
            obj2.lineEdit_22.setText(record[0])
            obj2.lineEdit_52.setText(record[1])
            obj2.textEdit_5.setText(record[2])
            
        def get_number():
            global id_
            if obj1.lineEdit.text().isdecimal():
                if int(obj1.lineEdit.text())<=0 or int(obj1.lineEdit.text())>number_of_record:
                    obj1.lable_error.setText("مستخدم غير موجود")
                else:
                    record=cr.execute(f"SELECT id FROM materials LIMIT {int(obj1.lineEdit.text())}").fetchall()
                    id_=record[len(record)-1][0]
                    obj1.hide()
                    insert_info()
                    obj2.show()
            else:
                obj1.lable_error.setText("ادخل رقم صحيح")
        obj1.pushButton.clicked.connect(get_number)
        obj2.pushButton_26.clicked.connect(update_info)

    def show_materiel_table(self):
        records=cr.execute("select material_symbol,item_describe,notes from materials;").fetchall()
        self.ui.table5.setRowCount(len(records))
        for row,items in enumerate(records):
            for column,item in enumerate(items):
                self.ui.table5.setItem(row,column,QTableWidgetItem(str(item)))

if __name__ == '__main__':
    app = QApplication(sys.argv)

    obj0=guiForm()
    obj0.show()

    app.exec_()
db.close()

