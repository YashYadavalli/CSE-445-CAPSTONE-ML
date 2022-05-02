import tkinter as tk
from tkinter import Message ,Text
from PIL import Image, ImageTk
import pandas as pd

import tkinter.ttk as ttk
import tkinter.font as font
import tkinter.messagebox as tm
import matplotlib.pyplot as plt
import csv
import numpy as np
from PIL import Image, ImageTk
from tkinter import filedialog
import tkinter.messagebox as tm
import preprocess as pre
import SVMALG as svmproc
import LRALG as lrproc
import prediction as pred


bgcolor="#02FF01"
bgcolor1="#818ee3"
fgcolor="#120f0f"


def Home():
	global window
	def clear():
	    print("Clear1")
	    txt.delete(0, 'end') 
	    txt1.delete(0, 'end')  
	    txt2.delete(0, 'end')
	    txt3.delete(0, 'end')
	    txt4.delete(0, 'end')
	    txt5.delete(0, 'end')
	    txt6.delete(0, 'end')
	    txt7.delete(0.0, 'end')
	    txt8.delete(0, 'end')
	    txt9.delete(0.0, 'end')



	window = tk.Tk()
	window.title("CROP PREDICTION")

 
	window.geometry('1280x720')
	window.configure(background=bgcolor)
	#window.attributes('-fullscreen', True)

	window.grid_rowconfigure(0, weight=1)
	window.grid_columnconfigure(0, weight=1)
	

	message1 = tk.Label(window, text="CROP PREDICTION" ,bg=bgcolor  ,fg=fgcolor  ,width=50  ,height=3,font=('Algerian', 30, 'italic bold ')) 
	message1.place(x=10, y=15)

	lbl = tk.Label(window, text="Select Dataset",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl.place(x=30, y=120)
	
	txt = tk.Entry(window,width=60,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt.place(x=250, y=130)


	lbl1 = tk.Label(window, text="Temperature",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl1.place(x=10, y=250)
	
	txt1 = tk.Entry(window,width=15,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt1.place(x=220, y=260)

	lbl2 = tk.Label(window, text="Humidity",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl2.place(x=10, y=300)
	
	txt2 = tk.Entry(window,width=15,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt2.place(x=220, y=310)

	lbl3 = tk.Label(window, text="Soil Moisture",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl3.place(x=10, y=350)
	
	txt3 = tk.Entry(window,width=15,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt3.place(x=220, y=360)

	lbl4 = tk.Label(window, text="Rain Fall",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl4.place(x=10, y=400)
	
	txt4 = tk.Entry(window,width=15,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt4.place(x=220, y=410)

	lbl5 = tk.Label(window, text="PH",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl5.place(x=10, y=450)
	
	txt5 = tk.Entry(window,width=15,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt5.place(x=220, y=460)

	lbl6 = tk.Label(window, text="SVM - CROP",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl6.place(x=420, y=250)
	
	txt6 = tk.Entry(window,width=25,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt6.place(x=630, y=260)

	lbl7 = tk.Label(window, text="SVM Fertilizer",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl7.place(x=420, y=300)
	
	#txt7 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	#txt7.place(x=630, y=390)
	txt7 = Text(window, width = 30, height = 5, bg="white",fg="red",font=('times', 15, ' bold '))
	txt7.place(x=630, y=310)


	lbl8 = tk.Label(window, text="LR - CROP",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl8.place(x=420, y=450)
	
	txt8 = tk.Entry(window,width=25,bg="white" ,fg="black",font=('times', 15, ' bold '))
	txt8.place(x=630, y=460)

	lbl9 = tk.Label(window, text="LR Fertilizer",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl9.place(x=420, y=500)
	
	#txt9 = tk.Entry(window,width=20,bg="white" ,fg="black",font=('times', 15, ' bold '))
	#txt9.place(x=800, y=490)
	txt9 = Text(window, width = 30, height = 5, bg="white",fg="red",font=('times', 15, ' bold '))
	txt9.place(x=630, y=500)

	lbl10 = tk.Label(window, text="SVM Yield & Techonolgy",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl10.place(x=980, y=250)

	txt10 = Text(window, width = 30, height = 5, bg="white",fg="red",font=('times', 15, ' bold '))
	txt10.place(x=960, y=310)

	lbl11 = tk.Label(window, text="LR Yield & Techonolgy",width=20  ,height=2  ,fg=fgcolor  ,bg=bgcolor ,font=('times', 15, ' bold ') ) 
	lbl11.place(x=980, y=450)

	txt11 = Text(window, width = 30, height = 5, bg="white",fg="red",font=('times', 15, ' bold '))
	txt11.place(x=960, y=500)

	def browse():
		path=filedialog.askopenfilename()
		print(path)
		txt.delete(0, 'end') 
		txt.insert('end',path)
		if path !="":
			print(path)
		else:
			tm.showinfo("Input error", "Select Dataset")	

	def preproc():
		sym=txt.get()
		if sym != "" :
			pre.process(sym)
			print("preprocess")
			tm.showinfo("Input", "Preprocess Successfully Finished")
		else:
			tm.showinfo("Input error", "Select Dataset")

	def Svmprocess():
		svmproc.process("results/data2.csv")
		tm.showinfo("Input", "SVM Successfully Finished")

	def Regressionprocess():
		lrproc.process("results/data2.csv")
		tm.showinfo("Input", "Logistic Regression Successfully Finished")


	def Predictprocess():
		txt6.delete(0, 'end')
		txt7.delete(0.0, 'end')
		txt8.delete(0, 'end')
		txt9.delete(0.0, 'end')
		txt10.delete(0.0, 'end')
		txt11.delete(0.0, 'end')

		sym1=txt1.get()
		sym2=txt2.get()
		sym3=txt3.get()
		sym4=txt4.get()
		sym5=txt5.get()
		sym="results/data2.csv"
		
		if sym1 != "" and sym2 != "" and sym3 != "" and sym4 != "" and sym5 != "":
			s=[int(sym1),int(sym2),int(sym3),int(sym4),int(sym5)]
			sv,lr=pred.process(sym,s)
			g=sv[0]
			f="NO"
			Fertilizer="-----"
			Tech="----"

			if g==0:
				f="NO"
				f = "Wheat"
				Fertilizer="\nSuper phosphate-155 kg/acre \n Muriate of potash-20 kg/acre \n Nitro phophate-125 kg/acre"
				Tech="Yield: 3.5 thousand kilograms per hectare \n-1.use reaper machine to segregate seed from the crop \n 2.use nac wheat cutter to cut the crop more effiently \n 3.use water sprinkler to make the water reach at every end of the ground \n"
				
			if g==1:
				f = "Wheat"
				Fertilizer="\nSuper phosphate-155 kg/acre \n Muriate of potash-20 kg/acre \n Nitro phophate-125 kg/acre"
				Tech="Yield: 3.5 thousand kilograms per hectare\n-1.use reaper machine to segregate seed from the crop \n 2.use nac wheat cutter to cut the crop more effiently \n 3.use water sprinkler to make the water reach at every end of the ground \n"

			if g==2:
				f = "Oats"
				Fertilizer="\nNitorgen-110 kg/acre \n P2O5 20-30 kg/acre \n K2O-17 kg/acre \n Sulphur-10 kg/acre\n"
				Tech="Yield: 400-600 quintals per hectare\n-1.use reaper machine to segregate seed from the crop \n 2.use water sprinkler to make the water reach at every end of the ground \n 3. plough by disc harrow and use leveler after 2-3 plough by cultivator.\n"

			if g==3:
				f = "Gram"
				Fertilizer="\nNitorgen-12.5 kg/acre  \nP2O5-25 kg/acre \nK2O-12.5 kg/acre \nSulphur-10 kg/acre \n"
				Tech="Yield: 40-50 tonnes/ha-1.use disk harrow to plough (6cm) for land preparation \n 2.use leveler to level the ground \n 3.dry the seed in the afternoon for more quality output \n"

			if g==4:
				f = "Pea"
				Fertilizer="\nNitorgen-55 kg/acre \nPhosphorus-20 kg/acre \nPotash-40 kg/acre \n"
				Tech="Yeild: 45 to 60 quintals per hectare-1.Loam and light loam soil is suitable for peas\n 2.First plough should be done by disc harrow and subsequent 2-3 plough by local plough or cultivator \n 3.Sowing should be done at a distance of 20cm (dwarf) and 30 cm for long variety behind the plough \n"
			if g==5:
				f = "Tea"
				Fertilizer="\nAmmonium phosphate-35 kg/acre \nPotassium sulphate-15 kg/acre \nMOP-12 kg/acre \nMagnesium sulphate-15 kg/acre \nZinc sulphate-3 kg/acre \n"
				Tech="Yiled: 3000-4000kg per/hectares\n-1.GREEN LEAF SIFTER is designed to remove extraneous matter such as stones, metal pieces.\n 2.GREEN LEAF SHREDDER is a pre-conditioning machine. The machine shreds the leaves into small pieces .\n 3.use water sprinkler to make the water reach at every end of the ground \n"

			if g==6:
				f = "Rice"
				Fertilizer="\nP2O5-35 kg/acre \nK2O-50 kg/acre \n"
				Tech="Yiled:3 to 6 tons per Hec \n-1.use crop calender to get better idea to what on what day to get good product \n 2.select the best variety and quality of grain by using float test on the seed before planting and remove any seeds that float \n 3.use leveler to level the ground (the most important thing to do)and Harder plowlayer at 10 cm to stop water penetration \n 4.use IRRI bags to store the final product (most efficient storage)\n"

			if g==7:
				f = "Bajra"
				Fertilizer="Nitrogen-80 kg/acre \nPhosphorous-40 kg/acre \nPhotash-40 kg/acre \n"
				Tech="Yield: 12 to 16 quintals/ha2 \n-1.The crop needs very fine tilt because the seeds are too small\n 2. 2-3 harrowings and a ploughing is followed so that a fine tilth may be obtained to facilitate the sowing and proper distribution of seed at appropriate depth\n 3. Grains are separated either by beating the earheads with sticks or by trampling the earheads under bullock feet.\n 4.The separated grains must be cleaned and dried in sun to bring about 12-14% moisture after which the grains may be bagged and stored in a moisture proof store \n"
			if g==8:
				f = "Maize"
				Fertilizer="P2O5-24 kg/acre \nK2O-12 kg/acre \n"
				Tech="Yield:4 tonnes per hectare\n-1.use Raised bed (ridge) planting which considered as the best planting method for maize \n 2.use Furrow planting which controll water evoperation \n 3.use water sprinkler to make the water reach at every end of the ground \n"
			if g==9:
				f = "Cotton"
				Fertilizer="Nitrogen-150 kg/acre \nPhosphorous-60 kg/acre \nPotassium-90 kg/acre \n"
				Tech="Yield: 462 kilograms per hec\n-1.use double cropping technique (which encourage us to grow wheat and cotton on the same time) \n 2.use water sprinkler to make the water reach at every end of the ground \n 3.use spindle picker to harvest the cotton \n 4.The cotton stripper machine removes the top portion of the plant \n"

			if g==10:
				f = "Groundnut"
				Fertilizer="Nitrogen-25 kg/acre \nPhosphorous-50 kg/acre \nPotassium-75 kg/acre \nSulphur sludge-60 kg/acre \n"
				Tech="Yeild: 2051 kg/ha\n-1.use optimum machine diggers which is efficient in harvesting the groundnut crop \n 2.Hydraulic system is needed to enhance maneuverability .\n 3.gear box to control the digging speed of the machine.\n"

			if g==11:
				f = "Jute"
				Fertilizer="Urea-8 kg/acre \nNitrogen-10 kg/acre \nN,P2O5 and K2O-20 kg/acre \n"
				Tech="Yield around 2500Kg/ha-1.mechanical retting (extraction of fibers from the long lastic life stem ) \n 2.chemical retting(boiling and aplying chemical) \n 3.water retting \n"

			if g==12:
				f = "Sugarcane"
				Fertilizer="Zinc sulphate-37.5 kg/acre \nFerrous sulphate-100 kg/acre \n"
				Tech="Yield: 82 metric tons/ha\n-1.lime and gypsum application \n 2.organic compost (mandatory in soil) \n 3.requirement of tractor and trucks for fast transportation and helps us to maintain good quality \n"

			if g==13:
				f = "Turmeric"
				Fertilizer="Nitrogen-120 kg/acre \nP2O5-50 kg/acre \nK2O-80 kg/acre \n"
				Tech="Yield: 20-25 tonnes/Ha\n-1.curing of turmeric crop (remove copper and galvanized iron) \n 2.use ploshing method to give them good aprearance \n 3.mulching and weeding used to conserve soil moisture \n"

			if g==14:
				f = "No Crop"
				f = "Wheat"
				Fertilizer="Super phosphate-155 kg/acre \n Muriate of potash-20 kg/acre \n Nitro phophate-125 kg/acre"
				Tech="Yield: 3.5 thousand kilograms per hectare \n- 1.use reaper machine to segregate seed from the crop \n 2.use nac wheat cutter to cut the crop more effiently \n 3.use water sprinkler to make the water reach at every end of the ground \n"

			txt6.insert(0, f)
			txt7.insert(0.0, Fertilizer)
			txt10.insert(0.0, Tech)
			g=lr[0]


			f="NO"
			Fertilizer="-----"
			Tech="----"

			if g==0:
				f="NO"
				f = "Wheat"
				Fertilizer="Super phosphate-155 kg/acre \n Muriate of potash-20 kg/acre \n Nitro phophate-125 kg/acre"
				Tech="Yield: 3.5 thousand kilograms per hectare \n-1.use reaper machine to segregate seed from the crop \n 2.use nac wheat cutter to cut the crop more effiently \n 3.use water sprinkler to make the water reach at every end of the ground \n"
				
			if g==1:
				f = "Wheat"
				Fertilizer="Super phosphate-155 kg/acre \n Muriate of potash-20 kg/acre \n Nitro phophate-125 kg/acre"
				Tech="Yield: 3.5 thousand kilograms per hectare\n-1.use reaper machine to segregate seed from the crop \n 2.use nac wheat cutter to cut the crop more effiently \n 3.use water sprinkler to make the water reach at every end of the ground \n"

			if g==2:
				f = "Oats"
				Fertilizer="Nitorgen-110 kg/acre \n P2O5 20-30 kg/acre \n K2O-17 kg/acre \n Sulphur-10 kg/acre\n"
				Tech="Yield: 400-600 quintals per hectare\n-1.use reaper machine to segregate seed from the crop \n 2.use water sprinkler to make the water reach at every end of the ground \n 3. plough by disc harrow and use leveler after 2-3 plough by cultivator.\n"

			if g==3:
				f = "Gram"
				Fertilizer="Nitorgen-12.5 kg/acre  \nP2O5-25 kg/acre \nK2O-12.5 kg/acre \nSulphur-10 kg/acre \n"
				Tech="Yield: 40-50 tonnes/ha\n-1.use disk harrow to plough (6cm) for land preparation \n 2.use leveler to level the ground \n 3.dry the seed in the afternoon for more quality output \n"

			if g==4:
				f = "Pea"
				Fertilizer="Nitorgen-55 kg/acre \nPhosphorus-20 kg/acre \nPotash-40 kg/acre \n"
				Tech="Yeild: 45 to 60 quintals per hectare\n-1.Loam and light loam soil is suitable for peas\n 2.First plough should be done by disc harrow and subsequent 2-3 plough by local plough or cultivator \n 3.Sowing should be done at a distance of 20cm (dwarf) and 30 cm for long variety behind the plough \n"
			if g==5:
				f = "Tea"
				Fertilizer="Ammonium phosphate-35 kg/acre \nPotassium sulphate-15 kg/acre \nMOP-12 kg/acre \nMagnesium sulphate-15 kg/acre \nZinc sulphate-3 kg/acre \n"
				Tech="Yiled: 3000-4000kg per/hectares\n-1.GREEN LEAF SIFTER is designed to remove extraneous matter such as stones, metal pieces.\n 2.GREEN LEAF SHREDDER is a pre-conditioning machine. The machine shreds the leaves into small pieces .\n 3.use water sprinkler to make the water reach at every end of the ground \n"

			if g==6:
				f = "Rice"
				Fertilizer="P2O5-35 kg/acre \nK2O-50 kg/acre \n"
				Tech="Yiled:3 to 6 tons per Hec \n-1.use crop calender to get better idea to what on what day to get good product \n 2.select the best variety and quality of grain by using float test on the seed before planting and remove any seeds that float \n 3.use leveler to level the ground (the most important thing to do)and Harder plowlayer at 10 cm to stop water penetration \n 4.use IRRI bags to store the final product (most efficient storage)\n"

			if g==7:
				f = "Bajra"
				Fertilizer="Nitrogen-80 kg/acre \nPhosphorous-40 kg/acre \nPhotash-40 kg/acre \n"
				Tech="Yield: 12 to 16 quintals/ha2 \n-1.The crop needs very fine tilt because the seeds are too small\n 2. 2-3 harrowings and a ploughing is followed so that a fine tilth may be obtained to facilitate the sowing and proper distribution of seed at appropriate depth\n 3. Grains are separated either by beating the earheads with sticks or by trampling the earheads under bullock feet.\n 4.The separated grains must be cleaned and dried in sun to bring about 12-14% moisture after which the grains may be bagged and stored in a moisture proof store \n"
			if g==8:
				f = "Maize"
				Fertilizer="P2O5-24 kg/acre \nK2O-12 kg/acre \n"
				Tech="Yield:4 tonnes per hectare\n-1.use Raised bed (ridge) planting which considered as the best planting method for maize \n 2.use Furrow planting which controll water evoperation \n 3.use water sprinkler to make the water reach at every end of the ground \n"
			if g==9:
				f = "Cotton"
				Fertilizer="Nitrogen-150 kg/acre \nPhosphorous-60 kg/acre \nPotassium-90 kg/acre \n"
				Tech="Yield: 462 kilograms per hec\n-1.use double cropping technique (which encourage us to grow wheat and cotton on the same time) \n 2.use water sprinkler to make the water reach at every end of the ground \n 3.use spindle picker to harvest the cotton \n 4.The cotton stripper machine removes the top portion of the plant \n"

			if g==10:
				f = "Groundnut"
				Fertilizer="Nitrogen-25 kg/acre \nPhosphorous-50 kg/acre \nPotassium-75 kg/acre \nSulphur sludge-60 kg/acre \n"
				Tech="Yeild: 2051 kg/ha\n-1.use optimum machine diggers which is efficient in harvesting the groundnut crop \n 2.Hydraulic system is needed to enhance maneuverability .\n 3.gear box to control the digging speed of the machine.\n"

			if g==11:
				f = "Jute"
				Fertilizer="Urea-8 kg/acre \nNitrogen-10 kg/acre \nN,P2O5 and K2O-20 kg/acre \n"
				Tech="Yield around 2500Kg/ha\n-1.mechanical retting (extraction of fibers from the long lastic life stem ) \n 2.chemical retting(boiling and aplying chemical) \n 3.water retting \n"

			if g==12:
				f = "Sugarcane"
				Fertilizer="Zinc sulphate-37.5 kg/acre \nFerrous sulphate-100 kg/acre \n"
				Tech="Yield: 82 metric tons/ha\n-1.lime and gypsum application \n 2.organic compost (mandatory in soil) \n 3.requirement of tractor and trucks for fast transportation and helps us to maintain good quality \n"

			if g==13:
				f = "Turmeric"
				Fertilizer="Nitrogen-120 kg/acre \nP2O5-50 kg/acre \nK2O-80 kg/acre \n"
				Tech="Yield: 20-25 tonnes/Ha\n-1.curing of turmeric crop (remove copper and galvanized iron) \n 2.use ploshing method to give them good aprearance \n 3.mulching and weeding used to conserve soil moisture \n"

			if g==14:
				f = "No Crop"
				f = "Wheat"
				Fertilizer="Super phosphate-155 kg/acre \n Muriate of potash-20 kg/acre \n Nitro phophate-125 kg/acre"
				Tech="Yield: 3.5 thousand kilograms per hectare \n- 1.use reaper machine to segregate seed from the crop \n 2.use nac wheat cutter to cut the crop more effiently \n 3.use water sprinkler to make the water reach at every end of the ground \n"


			txt8.insert(0, f)
			txt9.insert(0.0, Fertilizer)
			txt11.insert(0.0, Tech)

			
			tm.showinfo("Input", "Prediction Successfully Finished")
		else:
			tm.showinfo("Input error", "Enter All Fields")

	browse = tk.Button(window, text="Browse", command=browse  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1, activebackground = "Red" ,font=('times', 15, ' bold '))
	browse.place(x=250, y=180)


	clearButton = tk.Button(window, text="Clear", command=clear  ,fg=fgcolor  ,bg=bgcolor1  ,width=20  ,height=1 ,activebackground = "Red" ,font=('times', 15, ' bold '))
	clearButton.place(x=600, y=180)
	 
	proc = tk.Button(window, text="Preprocess", command=preproc  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	proc.place(x=50, y=650)
	

	trainbutton = tk.Button(window, text="SVM", command=Svmprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	trainbutton.place(x=350, y=650)


	DCbutton = tk.Button(window, text="LOGISTIC REGRESSION", command=Regressionprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	DCbutton.place(x=650, y=650)

	DCbutton1 = tk.Button(window, text="Prediction", command=Predictprocess  ,fg=fgcolor   ,bg=bgcolor1   ,width=20  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	DCbutton1.place(x=1000, y=650)

	quitWindow = tk.Button(window, text="Quit", command=window.destroy  ,fg=fgcolor   ,bg=bgcolor1  ,width=15  ,height=2, activebackground = "Red" ,font=('times', 15, ' bold '))
	quitWindow.place(x=940, y=100)

	window.mainloop()
Home()

