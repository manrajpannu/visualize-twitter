from flask import Flask, render_template, url_for, flash, redirect, request
import scrape_twitter
import temp, failsafe


app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
	# scrape_twitter.get_pictures('pictures', 40, 3) 
	try:
		if temp.posts:
			return render_template('home.html',posts=temp.posts,title='Visualize Twitter')
		else: 
			return render_template('home.html',posts=failsafe.posts,title='Visualize Twitter')
	except: return render_template('home.html',posts=failsafe.posts,title='Visualize Twitter')



@app.route('/about')
def about():
	return render_template('about.html',title = 'About me')

@app.route('/search', methods=['GET', 'POST'])
def search():
	texts = request.args.get('text', '')
	if texts:
		scrape_twitter.get_pictures(texts, 40, 40)
		posts = temp.posts
		if posts:
			return render_template('home.html',posts=posts,title='Visualize Twitter')
		else: 
			posts = failsafe.posts
			return render_template('home.html',posts=posts,title='Visualize Twitter')
	else: 
		if temp.posts:
			return render_template('home.html',posts=temp.posts,title='Visualize Twitter')
		else: return render_template('home.html',posts=failsafe.posts,title='Visualize Twitter')



if __name__ == '__main__':
	app.run(debug=True)