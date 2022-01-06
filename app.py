from flask import Flask,render_template,request
from flask.json import jsonify
import pandas as pd
import pickle

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('CustomerForm.html')

@app.route('/handle', methods=['GET','POST'])
def handle_form():
    age = request.form["age"]  
    bpr = request.form["bpr"]
    sg = request.form["sg"]
    al = request.form["al"]
    su = request.form["su"]
    rbc = request.form["rbc"]
    pc = request.form["pc"]
    pcc = request.form["pcc"]
    ba = request.form["ba"]
    bgr = request.form["bgr"]
    bu = request.form["bu"]
    sc = request.form["sc"]
    sod = request.form["sod"]
    pot = request.form["pot"]
    hem = request.form["hem"]
    pcv = request.form["pcv"]
    wc = request.form["wc"]
    rc = request.form["rc"]
    htn = request.form["htn"]
    dm = request.form["dm"]
    cad = request.form["cad"]
    appet = request.form["appet"]
    pe = request.form["pe"]
    ane = request.form["ane"]

    results = {
        'age':age,
        'bpr':bpr,
        'pc':pc,
        'bgr':bgr,
        'hem':hem,
        'wc':wc,
        'rc':rc,
        'htn':htn,
        'dm':dm,
        'appet':appet,
        'ane':ane
    }

    df = pd.DataFrame(results,index=[0])
    df.replace({"normal":1,"abnormal":0},inplace=True)
    df.replace({"present":1,"notpresent":0},inplace=True)
    df.replace({"good":1,"poor":0},inplace=True)
    #replacing the values of no, yes to 0,1 respectively
    df.replace({"no":0,"yes":1,"\tno":0,"\tyes":1," yes":1},inplace=True)
    
    df = df[['age','bpr','rc','wc','appet','pc','htn','hem','bgr','dm','ane']]
    model = pickle.load(open('model.pkl','rb'))
    predicts = int(model.predict(df))

    message = ['You have tested Negative ','You have tested Positive']
    print(predicts)

    return jsonify({
        'result':predicts
    })

if __name__=="__main__":
    app.run(debug=True)