# Ex.05 Design a Website for Server Side Processing
## Date:

## AIM:
 To design a website to calculate the power of a lamp filament in an incandescent bulb in the server side. 


## FORMULA:
P = I<sup>2</sup>R
<br> P --> Power (in watts)
<br> I --> Intensity
<br> R --> Resistance

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM :
math.html
```
<html>
    <head>
        <style>
            body{
		background-color:red;
                margin-top: 20%;
                font-weight: bold;
            }
        </style>
        <script>
            function power()
            {
                const i=document.getElementById("in").value;
                const r=document.getElementById("resistance").value;
                const p= i*i*r; 
                document.getElementById("answer").innerText="Power :"+ p;
            }
        </script>
    </head>
        <body>
            <center>
                <input type="number" placeholder="Enter Intensity" id="in"><br><br>
                <input type="number" placeholder="Enter Resistance" id="resistance"><br><br>
                <input type="button" onclick="power()" value="Calculate power"><br><br>
                <label id="answer"></label>
            </center>
        </body>
</html>
```
views.py
```
from django.shortcuts import render 
def power(request): 
    context={} 
    context['power'] = "0" 
    context['I'] = "0" 
    context['R'] = "0" 
    if request.method == 'POST': 
        print("POST method is used")
        I =float( request.POST.get('intensity','0'))
        R = float(request.POST.get('resistance','0'))
        print('request=',request) 
        print('intensity=',I) 
        print('resistance=',R) 
        power = (((I)**2) * (R))
        context['power'] = power 
        context['I'] = I
        context['R'] = R 
        print('Power=',power) 
    return render(request,'mathapp/power.html',context)
```
urls.py
```
from django.contrib import admin 
from django.urls import path 
from mathapp import views 
urlpatterns = [ 
    path('admin/', admin.site.urls), 
    path('powerir/',views.power,name="powerir"),
    path('',views.power,name="powerir")
]
```
## OUTPUT
![alt text](<venkat/Screenshot 2025-05-08 171411.png>)
![alt text](<venkat/Screenshot 2025-05-08 171726.png>)
## RESULT:
The program for performing server side processing is completed successfully.
