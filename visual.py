from flask import Flask, render_template, url_for, flash, redirect, request
import scrape_twitter
import temp, failsafe
import random

texts = ['dog pics','cat pics','sunsets','photography','nba pics','canadian landscape','shopify']
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	return render_template('landing.html',title='Visualize Twitter',text=random.choice(texts))


@app.route('/about')
def about():
	return render_template('about.html',title = 'About me')

@app.route('/search', methods=['GET', 'POST'])
def search():
	texts = request.args.get('text', '')
	if texts:
		posts = scrape_twitter.get_pictures(texts, 40, 40)
		if posts: return render_template('home.html',posts=posts,title='Visualize Twitter')
		else: return redirect(url_for('home'))
	else: return redirect(url_for('home'))

	


if __name__ == '__main__':
	app.run(debug=True)