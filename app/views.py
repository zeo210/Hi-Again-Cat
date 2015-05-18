from flask import render_template, flash, request, redirect, make_response
from app import app
from app.forms import CatForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    form = CatForm()
    query = request.args.get('query')
    print(query)
    if form.validate_on_submit():
        return redirect('/search?query=' + form.search.data)
    elif query:
        input = query
        if query.endswith('.html'):
            print("return source text")
            resp = make_response(render_template('empty.html'))
            if query == "search.html":
                resp = make_response(render_template('search.html', source=True))
            elif query == "index.html":
                resp = make_response(render_template('index.html', source=True))
            elif query[:-5].isdigit():
                resp = make_response(render_template('result.html', cat_number=str(int(query[:-5])%10), source=True))
            resp.mimetype = 'text/plain'
            return resp
        if input.isdigit():
            print("return page mod number")
            return render_template('result.html', cat_number=str(int(input)%10) , source=False)
        flash("invalid query")
    return render_template('search.html',
                           form=form)