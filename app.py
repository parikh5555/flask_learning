from flask import Flask, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy 
from datetime import datetime

app =Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Todo(db.Model):
	id = db.Column(db.Integer, primary_key = True)
	name = db.Column(db.String(200), nullable = False)
	phone = db.Column(db.Integer, default =0)
	email = db.Column(db.String(200), nullable = False)
	date_created = db.Column(db.DateTime, default = datetime.utcnow)

	def __repr__(self):
		return '<Task %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])
def index():
	if request.method =='POST':
		resume_phone = request.form.get('phone')
		resume_email = request.form.get('email')
		resume_name = request.form.get('name')
		new_resume = Todo(name = resume_name, email=resume_email, phone = resume_phone)
		try:
			db.session.add(new_resume)
			db.session.commit()
			resumeb = Todo.query.all()
			return render_template('final_out.html')
		except Exception as E:
			return str(E)
	else :
		resume = Todo.query.order_by(Todo.date_created).all()
		print (resume[0].phone)
		return render_template('index.html')

if __name__ == "__main__":
	app.run(debug=True)
