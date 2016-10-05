from flask import Flask, render_template, request, url_for, redirect, flash, session
import selenium
from selenium import webdriver
from content_management import content


TOPIC_DICT = content()
nombres = []

app = Flask(__name__)
app.secret_key = #insert key here

@app.route('/', methods = ['GET', 'POST'])
def homepage():
	error=None
	try:
		if request.method == 'POST':
			username = request.form['username']
			password = request.form['password']

			#browser = webdriver.Firefox()
			browser = webdriver.PhantomJS(executable_path=r'path\to\phantomjs.exe')
			browser.set_window_size(1120, 550)
			browser.implicitly_wait(10)
			browser.get(#webpage you'd like to scrap)
			emailElem = browser.find_element_by_id('username')
			emailElem.send_keys(username)
			passwordElem = browser.find_element_by_id('password')
			passwordElem.send_keys(password)
			entrar = browser.find_element_by_class_name('entrar')
			entrar.click()
			degree = browser.find_element_by_class_name('Arial11BlackBold')
			degree.click()
			browser.implicitly_wait(5)
			findmetoo = browser.find_elements_by_xpath('//td[@class="Arial11BlackBoldLink"]')[1]
			findmetoo.click()
			appweb = browser.find_elements_by_xpath('//span[@class="Arial11BlueBold ManoSola"]')[0]
			appweb.click()
			appweb2 = browser.find_elements_by_xpath('//span[@class="Arial11BlueBold ManoSola"]')[2].text

			nombres.append(appweb2)
			appweb4 = browser.find_elements_by_xpath('//span[@class="Arial11BlueBold ManoSola"]')[4].text

			nombres.append(appweb4)
			appweb6 = browser.find_elements_by_xpath('//span[@class="Arial11BlueBold ManoSola"]')[6].text

			nombres.append(appweb6)
			appweb8 = browser.find_elements_by_xpath('//span[@class="Arial11BlueBold ManoSola"]')[8].text

			nombres.append(appweb8)
			appweb10 = browser.find_elements_by_xpath('//span[@class="Arial11BlueBold ManoSola"]')[10].text

			nombres.append(appweb10)
			appweb12 = browser.find_elements_by_xpath('//span[@class="Arial11BlueBold ManoSola"]')[12].text

			nombres.append(appweb12)
			appweb14 = browser.find_elements_by_xpath('//span[@class="Arial11BlueBold ManoSola"]')[14].text

			nombres.append(appweb14)
			appweb16 = browser.find_elements_by_xpath('//span[@class="Arial11BlueBold ManoSola"]')[16].text

			nombres.append(appweb16)

			browser.quit()

			return redirect(url_for('dashboard'))
		elif request.method == 'GET':
			return render_template("main.html")

	except Exception as e:
		flash(e)
		return render_template("main.html", error=error)

@app.route('/dashboard/')
def dashboard():
	return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT, nombres=nombres)


@app.errorhandler(404)
def page_not_found(e):
	return render_template("404.html")

@app.errorhandler(405)
def method_not_found(e):
	return render_template("405.html")


if __name__ == "__main__":
    app.run()
