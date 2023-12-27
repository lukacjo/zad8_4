from flask import Flask, render_template, request, redirect

app = Flask(__name__)

    
@app.route('/mypage/me')
def me():  
    return render_template("me.html")

@app.route('/mypage/contact', methods=['POST', 'GET'])
def contact():  
    if request.method == 'POST': 
        my_text = request.form.get('my_text') 
        print(my_text)
        return redirect("/mypage/contact")
    else:
        return render_template("contact.html")

if __name__ == '__main__':
    app.run(debug=True)