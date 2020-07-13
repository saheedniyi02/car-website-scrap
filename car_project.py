from bs4 import BeautifulSoup
import requests
import csv
csv_file=open("/storage/emulated/0/car_price_scrap.csv","a")
csv_writer=csv.writer(csv_file)
csv_writer.writerow(["title","price","Make","Model","Year_of_manufacture","Condition","Transmission","Exchange","fuel_type","body_type","address_of_sale","Mileage"])
for i in range(50,65):
	link=f"https://deals.jumia.com.ng/cars/?page={i}&append=true&sort=newest"
	req=requests.get(link).text
	soup_page=BeautifulSoup(req,'lxml')
	one_car=soup_page.find_all("div",class_="post")
	for car in one_car:
		car_link=car.find("a")
		title=car_link.get('title')
		price=car.find("div",class_="price-date").span.text.split(" ")[48]
		address_of_sale=car.find("span",class_="address").text.split(" ")[-45]
		#print(address_of_sale,price,title)
		link_request=requests.get("https://deals.jumia.com.ng"+car_link.get('href')).text
		soup_link=BeautifulSoup(link_request,"lxml")
		#print(soup_link)
		description=soup_link.find('div',class_="post-text-content").p.text
		div_info=soup_link.find("div",class_="post-attributes")
		try:
			for i in div_info.find_all("h3"):
				
				value=i.find("span").text
				property=i.text.replace(value,"")
				if property=="Make":
					Make=value
				elif property=="Model":
					Model=value
				elif property=="Year":
					Year_of_manufacture=value
				elif property=="Condition":
					Condition=value
				elif property=="Transmission":
					Transmission=value
				
				elif property=="Mileage":
					Mileage=value
				elif property=="Exchange":
					Exchange=value
				elif property=="Fuel":
					fuel_type=value
				elif property=="Body":
					body_type=value
				elif property=="Trim":
					Trim=value
				elif property=="Registered":
					Registered=value
				else:
					miscallenous=value
			try:
				Model
			except NameError:
				Model=None
			try:
				Make
			except NameError:
				Make=None
			try:
				Year_of_manufacture
			except NameError:
				Year_of_manufacture=None
			try:
				Transmission
			except NameError:
				Transmission=None
			try:
				Mileage
			except NameError:
				Mileage=None
			try:
				fuel_type
			except NameError:
				fuel_type=None
			try:
				body_type
			except NameError:
				body_type=None
			try:
				Trim
			except NameError:
				Trim=None
			try:
				Registered
			except NameError:
				Registered=None
			try:
				Condition6
			except NameError:
				Condition=None
			try:
				Exchange
			except NameError:
				Exchange=None
			try:
				miscallenous
			except NameError:
				miscallenous=None
			csv_writer.writerow([title,price,Make,Model,Year_of_manufacture,Condition,Transmission,Exchange,fuel_type,body_type,address_of_sale,Mileage])
			print(title,price,Make,Model,Year_of_manufacture,Condition,Transmission,Exchange,fuel_type,body_type,address_of_sale,Mileage)
		except AttributeError:
			pass
csv_file.close()
		

				
				

		
#		for i in div_info.find_all("h3"):
#			value=i.find("span").text
#			property=i.text.replace(value,"")
#			if property=="Make":
#				Make=value
#			elif property=="Model":
#				Model=value
#			elif property=="Year":
#				Year_of_manufacture=value
#			elif property=="Condition":
#				Condition=value
#			elif property=="Transmission":
#				Transmission=value
#			elif property=="Mileage":
#				Mileage=value
#			elif property=="Exchange":
#				Exchange=value
#			elif property=="Fuel":
#					fuel_type=value
#			elif property=="Body":
#				body_type=value
#			elif property=="Trim":
#				Trim=value
#			elif property=="Registered":
#				Registered=value
#			else:
#				miscallenous=value
#		try:
#			Model
#		except NameError:
#			Model=None
#		try:
#			Make
#		except NameError:
#			Make=None
#		try:
#			Year_of_manufacture
#		except NameError:
#			Year_of_manufacture=None
#		try:
#			Transmission
#		except NameError:
#			Transmission=None
#		try:
#			Mileage
#		except NameError:
#			Mileage=None
#		try:
#			fuel_type
#		except NameError:
#			fuel_type=None
#		try:
#			body_type
#		except NameError:
#			body_type=None
#		try:
#			Trim
#		except NameError:
#			Trim=None
#		try:
#			Registered
#		except NameError:
#			Registered=None
#		try:
#			Condition6
#		except NameError:
#			Condition=None
#		try:
#			Exchange
#		except NameError:
#			Exchange=None
#		try:
#			miscallenous
#		except NameError:
#			miscallenous=None
#		csv_writer.writerow([title,price,Make,Model,Year_of_manufacture,Condition,Transmission,Exchange,fuel_type,body_type,address_of_sale,Mileage])
#		print(title,price,Make,Model,Year_of_manufacture,Condition,Transmission,Exchange,fuel_type,body_type,address_of_sale,Mileage)
#csv_file.close()
#		

#				
				
