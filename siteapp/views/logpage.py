from flask import Blueprint, render_template, request, redirect
from siteapp.config.db_connect import mydb


bp = Blueprint(__name__, __name__, template_folder='templates')


@bp.route('/logpage', methods=['POST', 'GET'])


def show():
	errors = {"fail": ''}
	if request.method == 'POST':
		if request.form.get('login'):
			username = request.form.get('username')
			password = request.form.get('password')
			
			#put data in the table
			mycursor = mydb.cursor()
			sql = "SELECT * FROM credentials WHERE username=%s AND password=%s"
			val = (username, password)
			mycursor.execute(sql, val)
			myresult = mycursor.fetchall()
			if len(myresult) > 0:
				return redirect('/')
			else:
				errors['fail'] = 'Name or password incorect !'
				return redirect('/books')



	return render_template('logpage.html')