from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout


class Mainapp(App):
	def __init__(self):
		super().__init__()
		self.label1 = Label(text='начисления')
		self.acc = TextInput()
		self.label2 = Label(text='пени')
		self.pen = TextInput()
		self.label3 = Label(text='перерасчет')
		self.recal = TextInput()
		self.label4 = Label(text='с пенями:')
		self.onpen = Label(text='0')
		self.label5 = Label(text='без пеней:')
		self.nopen = Label(text='0')
		self.label6 = Label(text='госпошлина приказ:')
		self.gpord = Label(text='0')
		self.label7 = Label(text='госпошлина иск:')
		self.gpisk = Label(text='0')
		self.c = Button(text='расчитать', )
		self.clear = Button(text='сброс')
		
		self.c.bind(on_press=self.calc)
		self.clear.bind(on_press=self.reset)
		
	

	def reset(self,*args):
		self.onpen.text = '0'
		self.nopen.text = '0'
		self.gpord.text = '0'
		self.gpisk.text = '0'
		self.acc.text = ''
		self.pen.text = ''
		self.recal.text = ''
		
	def calc(self,*args):
		acc = self.acc.text
		pen = self.pen.text
		recal = self.recal.text
		
		try:	
		
			w_pen = round(float(acc) + float(recal), 2)
			self.onpen.text = str(w_pen)
			no_pen = round((float(acc) + float(recal)) - float(pen), 2)
			self.nopen.text = str(no_pen)
	
			if w_pen <= 10000:
				self.gpord.text = '200'
				self.gpisk.text = '400'
			elif w_pen > 10000 and w_pen <= 20000:
				gp = round(((w_pen / 100) * 4) / 2, 2)
				self.gpord.text = str(gp)
				self.gpisk.text = str(gp * 2)
			elif w_pen > 20000 and w_pen <= 100000:
				gp = round(((((w_pen - 20000) / 100) * 3) + 800) / 2, 2)
				self.gpisk.text = str(gp * 2)
				self.gpord.text = str(gp)
			elif w_pen > 100000 and w_pen <= 200000:
				gp = round(((((w_pen - 100000) / 100) * 2) + 3200) / 2, 2)
				self.gpisk.text = str(gp * 2)
				self.gpord.text = str(gp)
			elif w_pen > 200000 and w_pen <= 1000000:
				gp = round(((((w_pen-200000) / 100) * 1) + 5200) / 2, 2)
				self.gpisk.text = str(gp * 2)
				self.gpord.text = str(gp)
			elif w_pen > 1000000:
				gp = round(((((w_pen - 1000000) / 100) * 0.5) + 13200) / 2, 2)
				if gp > 30000:
					self.gpord.text = '30000'
					self.gpisk.text = '60000'
				else:
					self.gpisk.text = str(gp * 2)
					self.gpord.text = str(gp)
		
		except ValueError:
			pass

	def build(self):
		layout = GridLayout(cols=2)
		layout.add_widget(self.label1)
		layout.add_widget(self.acc)
		layout.add_widget(self.label2)
		layout.add_widget(self.pen)
		layout.add_widget(self.label3)
		layout.add_widget(self.recal)
		layout.add_widget(self.label4)
		layout.add_widget(self.onpen)
		layout.add_widget(self.label5)
		layout.add_widget(self.nopen)
		layout.add_widget(self.label6)
		layout.add_widget(self.gpord)
		layout.add_widget(self.label7)
		layout.add_widget(self.gpisk)
		layout.add_widget(self.c)
		layout.add_widget(self.clear)
		return layout
		
if __name__ == '__main__':
	app=Mainapp()
	app.run()