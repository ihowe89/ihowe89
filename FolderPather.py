# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 15:30:41 2022
OOP styled python code with a separate GUI and Folder_Pather class
tkinter opens a form for input of an 8 digit project number, prompts if you want to open ( if it exists)or to create / open (if it doesn't exist')
it copies or unzips a variety of template folders to new project folders.
@author: ihowe
"""
   
import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import shutil
import zipfile
import sys

class FolderPather:
    def __init__(self, project_num):
        self.project_num = project_num
        self.project_root = r'Q:\GIS\Admin\Scripts\FolderPather\Working\Projects_test' #root path for projects
        self.project_folder = self.folder_setup()
       
    def folder_setup(self):  #creates folder / sub folders ie if input is 11111111 it creates / navigates to 11111000s\11111111 
        project_folder = ''
        project_sub = os.path.join(self.project_root, self.project_num[:5])

        if len(self.project_num) == 8:
            project_folder = os.path.join(project_sub + '000s', self.project_num)
            
        return project_folder

    def folder_exists(self):
        return os.path.isdir(self.project_folder)

    def create_folder(self):
        if not self.folder_exists():
            os.makedirs(self.project_folder)
    
    def open_folder(self):
        os.startfile(self.project_folder)

    def copy_and_unzip_files(self):
        gis_src = r'Q:\GIS\Admin\Scripts\FolderPather\Working\TEMPLATE_GIS.zip'
        gis_dest = self.project_folder
        audit = r'Q:\GIS\Admin\Scripts\FolderPather\Working\QA AuditTemplate_LI.xlsx'
        aud_dest =os.path.join(self.project_folder,r'GIS\Maps\Deliverables\_PDF')
        with zipfile.ZipFile(gis_src, 'r') as zip_ref:
            zip_ref.extractall(gis_dest)
        shutil.copy(audit, aud_dest)
           
class GUI(FolderPather): #inherits FolderPather class methods
    def __init__(self):
        self.root = Tk()
        self.root.title("Folder Pather")
        self.root.configure(bg="#000000")
        self.canvas = Canvas(self.root, width=400, height=200, bg="#297D70")
        self.canvas.pack()
        self.prompt = Label(self.canvas, text="Type in an 8-digit project number", font=("Arial", 14))
        self.canvas.create_window(200,50,window = self.prompt)
        self.entry = Entry(self.canvas, width=20)
        self.canvas.create_window(200, 100, window=self.entry)
        self.create_button = Button(self.canvas, text="Create or Open", font=("Arial", 14), command=self.on_submit)
        self.canvas.create_window(200, 150, window=self.create_button)
        self.root.mainloop()
        
    def on_submit(self):
        project_num = self.entry.get()
        if len(project_num) != 8:
            result = tkinter.messagebox.askquestion('Warning','Project numbers must be 8 digits, try again?', icon = 'warning')
            if result == 'yes':
                self.restart()
        
        super().__init__(project_num) #inserts the project_num variable value into the FolderPather parent class enabling use of FolderPather methods
        if self.folder_exists():
            result = tkinter.messagebox.askquestion('Open Folder', 'This folder already exists, open it?', icon = 'warning')
            if result == 'yes':
                self.open_folder()
                sys.exit()
        else:
            self.create_folder()
            self.copy_and_unzip_files()
            self.open_folder()
  
    def restart(self):
            self.root.destroy()
            GUI()        
    
if __name__ == "__main__":
    gui = GUI()
    
# class FolderPather:
#     def __init__(self, project_num):
#         self.project_num = project_num
#         self.project_root = r'Q:\GIS\Admin\Scripts\FolderPather\Working\Projects_test' #root path for projects
#         self.project_folder = self.folder_setup()
        
       
#     def folder_setup(self):
#         project_root = self.project_root
#         project_folder = ''
#         project_sub = os.path.join(self.project_root, self.project_num[:5])

#         if len(self.project_num) == 8:
#             project_folder = os.path.join(project_sub + '000s', self.project_num)
            
#         return project_folder

#     def folder_exists(self):
#         return os.path.isdir(self.project_folder)

#     def create_folder(self):
#         if not self.folder_exists():
#             os.makedirs(self.project_folder)
    
#     def open_folder(self):
#         os.startfile(self.project_folder)

#     def copy_and_unzip_files(self):
#         gis_src = r'Q:\GIS\Admin\Scripts\FolderPather\Working\TEMPLATE_GIS.zip'
#         gis_dest = self.project_folder
#         audit = r'Q:\GIS\Admin\Scripts\FolderPather\Working\QA AuditTemplate_LI.xlsx'
#         aud_dest =os.path.join(self.project_folder,r'GIS\Maps\Deliverables\_PDF')
#         with zipfile.ZipFile(gis_src, 'r') as zip_ref:
#             zip_ref.extractall(gis_dest)
#         shutil.copy(audit, aud_dest)
           
# class GUI(FolderPather):
#     def __init__(self):
#         self.root = Tk()
#         self.root.title("Folder Pather")
#         self.root.configure(bg="#000000")
#         self.canvas = Canvas(self.root, width=400, height=200, bg="#297D70")
#         self.canvas.pack()
#         self.prompt = Label(self.canvas, text="Type in an 8-digit project number", font=("Arial", 14))
#         self.canvas.create_window(200,50,window = self.prompt)
#         self.entry = Entry(self.canvas, width=20)
#         self.canvas.create_window(200, 100, window=self.entry)
#         self.create_button = Button(self.canvas, text="Create or Open", font=("Arial", 14), command=self.on_submit)
#         self.canvas.create_window(200, 150, window=self.create_button)
#         self.root.mainloop()
        
#     def on_submit(self):
#         project_num = self.entry.get()
#         if len(project_num) != 8:
#             result = tkinter.messagebox.askquestion('Warning','Project numbers must be 8 digits, try again?', icon = 'warning')
#             if result == 'yes':
#                 self.restart()
                
#         super().__init__(project_num)
#         if self.folder_exists():
#             result = tkinter.messagebox.askquestion("Open Folder?", "Do you want to open the folder?", icon='warning')
#             if result == 'yes':
#                 self.open_folder()
#         else:
#             result = tkinter.messagebox.askquestion("Create Folder?", "Do you wish to create the folder?", icon = 'warning')
#             if result =='yes':
#                 self.create_folder()
#                 self.copy_and_unzip_files()
#                 self.open_folder()
   
#     def restart(self):
#             self.root.destroy()
#             GUI()        
    
# if __name__ == "__main__":
#     gui = GUI()
     