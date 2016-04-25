#! /usr/local/bin/python

import time, os, pickle
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
from socket import gaierror
from peewee import *

db = SqliteDatabase('scraper.db')
# db = MySQLDatabase('scraper', host="localhost", user="root", passwd="root") # mysql settings

class BaseModel(Model):
    class Meta:
        database = db

class Mensch(BaseModel):
    name = CharField()
    email = CharField()
    nummer = CharField()
    workarea = CharField()
    profession = CharField()
    detailedprof = CharField()
    address = CharField()
    zipcode = CharField()
    state = CharField()
    tel1 = CharField()
    tel2 = CharField()
    tel3 = CharField()
    county = CharField()

class Meta:
    indexes = ((('name', 'email', 'nummer', 'workarea', 'profession', 'detailedprof', 'county'), True))

def createperson():
    personname = browser.find_by_css('td:nth-child(1) tr:nth-child(1) td+ td').first.text + ' ' + browser.find_by_css('td:nth-child(1) tr:nth-child(2) td+ td').first.text
    personemail = browser.find_by_css('.mail').first.text
    personnummer = browser.find_by_css('td+ td tr:nth-child(1) td+ td').first.text
    address1 = browser.find_by_css('td:nth-child(1) tr:nth-child(4) td+ td').first.text
    zipcode1 = browser.find_by_css('td:nth-child(1) tr:nth-child(5) td+ td').first.text
    state1 = browser.find_by_css('td:nth-child(1) tr:nth-child(6) td+ td').first.text
    tel11 = browser.find_by_css('td+ td tr:nth-child(3) td+ td').first.text
    tel21 = browser.find_by_css('td+ td tr:nth-child(4) td+ td').first.text
    tel31 = browser.find_by_css('td+ td tr:nth-child(5) td+ td').first.text
    #mensch = Mensch(name = personname, email = personemail, nummer = personnummer, workarea = curworkarea, profession = curprofession, detailedprof = curdetailedprof, address = address1, zipcode = zipcode1, state = state1, tel1 = tel11, tel2 = tel21, tel3 = tel31 county = curcounty)
    if mensch.save():
        print personname + " has been saved"

db.create_tables([Mensch], safe=True) # create the table if it doesn't exist

done = False

while not done: # restart in case of ElementDoesNotExist exception
	try:
	
		# load last used options
		
		if os.path.isfile('options.dump'):
			with open('options.dump', 'rb') as dmp:
				lastoptvalues = pickle.load(dmp) 
				lastoptkeys = ["county", "municipality", "workarea", "profession", "detailedprof"]
				lastoptions = dict(zip(lastoptkeys, lastoptvalues))
				print "Restoring last used options..."
			
		browser = Browser('phantomjs', user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) AppleWebKit/600.5.15 (KHTML, like Gecko) Version/8.0.5 Safari/600.5.15)"
		browser.driver.set_window_size(1366, 768)
		
		url = "http://www.arbetsformedlingen.se"
		browser.visit(url)
		browser.find_by_css('.sidhuvud .btn-login, .sidhuvud-globalmeny-sok .btn-group > .btn, .sidhuvud-globalmeny-sok .btn-group > .btn:first-child, .sidhuvud-globalmeny-sok .btn-group > .btn:last-child').click()
		browser.find_by_css('.inloggnings-tabbar .nav-tabs li:nth-child(2) a ').click()
		browser.fill("user", "christoffer@blueillume.com")
		browser.fill("password",'Ejc2Tc6')
		browser.execute_script('document.forms["konto"].submit()')
		
		# locating the searchform
		
		time.sleep(5) # waiing for the page to load
	
		try:
			browser.find_by_css('#mainTabMenu ul li:nth-child(1) a').click()
			browser.find_by_css('.sv-text-portlet-content p.flikmeny a').click()
			browser.find_by_css('.linkBold:nth-child(1)').click()
			searchurl = browser.driver.current_url.replace("https", "http") # saving the url to the searchform for later
		except AttributeError:
			time.sleep(5) # wait a little longer
		
		countyoptions = [c.value for c in browser.find_by_name('selectlistLan').find_by_tag('option')[1:]]
		
		try:
			countyoptions = countyoptions[countyoptions.index(lastoptions['county']):] # slice up to the last-searched county
		except NameError:
			pass
		
		
		counties = {c.value: c.text for c in browser.find_by_name('selectlistLan').find_by_tag('option')[1:]}
		
		for county in countyoptions:
			browser.select('selectlistLan', county)
			curcounty = counties[county]
			print "Current county: " + curcounty
		
			municipalityoptions = [c.value for c in browser.find_by_name('selectlistKommun').find_by_tag('option')[1:]]
		
			try:
				municipalityoptions = municipalityoptions[municipalityoptions.index(lastoptions['municipality']):] # slice up to the last-searched municipality
			except NameError:
				pass
		
			municipalities = {c.value: c.text for c in browser.find_by_name('selectlistKommun').find_by_tag('option')[1:]}
			
			uno = True
		
			for municipality in municipalityoptions:
				if uno:
					uno = False
				else: 
					browser.select('selectlistLan', county)
					print "Current county: " + curcounty
		
				browser.select('selectlistKommun', municipality)
				curmunicipality = municipalities[municipality]
				print "Current municipality: " + curmunicipality
			
				workareadropdownoptions = [c.value for c in browser.find_by_name('selectlistYrkesomrade').find_by_tag('option')[1:]]
				
				try:
					workareadropdownoptions = workareadropdownoptions[workareadropdownoptions.index(lastoptions['workarea']):] # slice up to the last-searched workarea
				except NameError:
					pass
		
				workareas = {c.value: c.text for c in browser.find_by_name('selectlistYrkesomrade').find_by_tag('option')[1:]}
				
				ein = True
		
				for workarea in workareadropdownoptions:
					if ein:
						ein = False
					else: 
						browser.select('selectlistLan', county)
						print "Current county: " + curcounty
						browser.select('selectlistKommun', municipality)
						print "Current municipality: " + curmunicipality
				
					browser.select('selectlistYrkesomrade', workarea)
					curworkarea = workareas[workarea]
					print "Current workarea: " + curworkarea
				
					profdropdownoptions = [c.value for c in browser.find_by_name('selectlistDelomrade').find_by_tag('option')[1:]]
		
					try:
						profdropdownoptions = profdropdownoptions[profdropdownoptions.index(lastoptions['profession']):] # slice up to the last-searched profession
					except NameError:
						pass
		
					professions = {c.value: c.text for c in browser.find_by_name('selectlistDelomrade').find_by_tag('option')[1:]}
				
					first = True
				
					for profession in profdropdownoptions:
						if first:
							first = False
						else:
							browser.select('selectlistLan', county)
							print "Current county: " + curcounty
							browser.select('selectlistKommun', municipality)
							print "Current municipality: " + curmunicipality
							browser.select('selectlistYrkesomrade', workarea)
							print "Current workarea: " + curworkarea
				
						browser.select('selectlistDelomrade', profession)
						curprofession = professions[profession]
						print "Current profession: " + curprofession
					
						browser.find_by_name('cmdSearch').click()
						
						# Selecting detailed profession
					
						profradiooptions = [c.value for c in browser.find_by_name('iYrkeBenamningID')]
		
						try:
							profradiooptions = profradiooptions[profradiooptions.index(lastoptions['detailedprof']):] # slice up to the last-searched detailed profession
							del lastoptions # we don't need it anymore since we've restored last options 
						except NameError:
							pass
						
						secfirst = True
						for radiooption in profradiooptions:
							if secfirst:
								secfirst = False
							else:
								browser.select('selectlistLan', county)
								print "Current county: " + curcounty
								browser.select('selectlistKommun', municipality)
								print "Current municipality: " + curmunicipality 
								browser.select('selectlistYrkesomrade', workarea)
								print "Current workarea: " + curworkarea
								browser.select('selectlistDelomrade', profession)
								print "Current profession: " + curprofession
								browser.find_by_name('cmdSearch').click()
				
							browser.choose('iYrkeBenamningID', radiooption) 
							curdetailedprof = browser.find_by_value(radiooption).find_by_xpath('..').text
							
							print "Current detailed profession: " + curdetailedprof
						
							browser.find_by_name('cmdSearch').click()
		
							# Saving current options to an external file
		
							currentoptions = (county, municipality, workarea, profession, radiooption)
		
							with open('options.dump', 'wb+') as dmp:
								pickle.dump(currentoptions, dmp)
							
							# Saving entries
							
							firstperson = browser.find_by_css('table+ table td+ td a')
		
							if firstperson !=[]:
								firstperson.first.click() # open the first person
							else:
								print("Nothing found")
								browser.visit(searchurl) # going back to the searchform
								continue # next iteration of profradiooptions-loop
							numofentries = int(browser.find_by_css('div[align="middle"] b').first.text.split()[3])
							print str(numofentries) + " entries found"
						
							thirdfirst = True 
						
							for r in range(numofentries):
								if thirdfirst:
									thirdfirst = False
								else:
									if numofentries == 1:
										break
									browser.find_by_css('div[align="right"] a').first.click() # click next
								try:
									createperson()
								except IntegrityError:
									print "A person already exists and was ignored"
								except Exception as e:
									continue
							
							browser.visit(searchurl) # going back to the searchform
		os.remove('options.dump') # remove options backup if scraper ended successfully
	except (ElementDoesNotExist, AttributeError, ValueError) as e:
		print "The webpage wasn't fully loaded, restarting..."
		with open("log.txt", "a") as log:
			log.write(time.strftime('%Y-%m-%d %H:%M:%S') + "\t"+ str(e) + "\tThe webpage wasn't fully loaded, restarting...\n")
		pass
	except gaierror as e:
		print "No connection to the network, restarting..."
		with open("log.txt", "a") as log:
			log.write(time.strftime('%Y-%m-%d %H:%M:%S') + "\t"+ str(e) + "\t No connection to the network, restarting...\n")
		pass
	
	except KeyboardInterrupt:
		print "\nInterrupted :("
		done = True
else:
	done = True
