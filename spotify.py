from flask import*
import requests
API_KEY='d033e5d480d3c063dd2f3e82259a9098'
URL='https://api.themoviedb.org/3/search/movie'
app=Flask(__name__)
@app.route('/')
@app.route('/home',methods=['GET','POST'])
def home():
    if request.method=='POST':
        name=request.form['movie_title']
        year=request.form['year']
        lang=request.form['lang']
        params={
            'api_key':API_KEY,
            'query':name,
            'year':year,
            'lang':lang
        }
        response=requests.get(URL,params=params)
        if response.status_code==200:
            movie=response.json()
            return render_template('movieview.html',movie=movie)
        else:
            return "<html><body><h1>Movie not found!</h1></body></html>"
    else:
        return render_template('movieindex.html')
if __name__=='__main__':
    app.run(debug=True)