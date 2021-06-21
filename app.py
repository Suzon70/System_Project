#import libraries
from flask import Flask, render_template,request
import pickle#Initialize the flask App
app = Flask(__name__)



def makeTokens(f):
    
    tkns_BySlash = str(f.encode('utf-8')).split('/')	# make tokens after splitting by slash
    total_Tokens = []
    
    for i in tkns_BySlash:
        
        tokens = str(i).split('-')	# make tokens after splitting by dash
        tkns_ByDot = []
        
        for j in range(0,len(tokens)):
            
            temp_Tokens = str(tokens[j]).split('.')	# make tokens after splitting by dot
            tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
        
    total_Tokens = list(set(total_Tokens))	#remove redundant tokens
    
    if 'com' in total_Tokens:
        total_Tokens.remove('com')	#removing .com 
        
    return total_Tokens









model = pickle.load(open('model.pkl', 'rb'))

vectorizer = pickle.load(open('vectorizer.pkl','rb'))



X_predict=["facebook.com/","ghdkfjdkfl23455.com/fhdkdd/fjd/djf","ahrenhei.without-transfer.ru/nethost.exe"]
X_predict = vectorizer.transform(X_predict)
print(model.predict(X_predict))

#default page of our web-app
@app.route('/')
def home():
    return render_template('index.html')


#To use the predict button in our web-app
@app.route('/predict',methods=['POST'])
def predict():
    int_features = [request.form.get("Url")]
    int_features = vectorizer.transform(int_features)
    prediction = model.predict(int_features)
    #output = model.predict(X_predict)
    output = prediction[0]
    return render_template('index.html',prediction_text='The prediction over given URL is {}'.format(output))





if __name__ == "__main__":
    app.run(debug = True)

