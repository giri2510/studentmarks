from django.shortcuts import render, HttpResponse, HttpResponseRedirect
import numpy as np
import joblib


def index(request):

    if request.method == 'POST':
        hour = request.POST.get("hour", '')
        aa = float(hour)
        #feature_value=np.array(hour)
        #print("feature_value",feature_value)
        model = joblib.load("student123.pkl")
        percent = model.predict([[aa]])[0][0].round(2)
        return render(request, "index.html", {'percent': percent, 'hour': hour})
    return render(request, "index.html")
