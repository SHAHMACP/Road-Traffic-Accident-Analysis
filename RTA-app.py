import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open('rfc.pkl','rb'))


@app.route('/')
def home():
    return render_template("RTA.html")


@app.route("/predict", methods=['POST'])
def predict():
    Age_band_of_driver = request.form['Age_band_of_driver']
    if Age_band_of_driver=="18-30":
        Age_band_of_driver=0
    elif Age_band_of_driver=="31-50":
        Age_band_of_driver=1
    elif Age_band_of_driver=="Over 51":
        Age_band_of_driver=2
    elif Age_band_of_driver=="Under 18":
        Age_band_of_driver=3    
    
    
    Sex_of_driver = request.form['Sex_of_driver']  
    if Sex_of_driver=="Male":
        Sex_of_driver = 1
    elif Sex_of_driver=="Female":
        Sex_of_driver=0 
            
    Driving_experience = request.form['Driving_experience']
    if Driving_experience=="5-10yr":
        Driving_experience=2
    elif Driving_experience=="2-5yr":
        Driving_experience=1
    elif Driving_experience=="Above 10yr":
        Driving_experience=3
    elif Driving_experience=="1-2yr":
        Driving_experience=0
    elif Driving_experience=="Below 1yr":
        Driving_experience=4
    elif Driving_experience=="No Licence":
        Driving_experience=5
            
            
    Type_of_vehicle = request.form['Type_of_vehicle']
    if Type_of_vehicle=="Automobile":
        Type_of_vehicle=0
    elif Type_of_vehicle=="Lorry":
        Type_of_vehicle=4
    elif Type_of_vehicle=="Public Vehicles":
        Type_of_vehicle=7
    elif Type_of_vehicle=="Other":
        Type_of_vehicle=6
    elif Type_of_vehicle=="Stationwagen":
        Type_of_vehicle=10
    elif Type_of_vehicle=="Long lorry":
        Type_of_vehicle=3
    elif Type_of_vehicle=="Taxi":
        Type_of_vehicle=11
    elif Type_of_vehicle=="Motorcycle":
        Type_of_vehicle=5
    elif Type_of_vehicle=="Special vehicle":
        Type_of_vehicle=9
    elif Type_of_vehicle=="Ridden horse":
        Type_of_vehicle=8
    elif Type_of_vehicle=="Turbo":
        Type_of_vehicle=12
    elif Type_of_vehicle=="Bajaj":
        Type_of_vehicle=1
    elif Type_of_vehicle=="Bicycle":
        Type_of_vehicle=2  
            
        
    Lanes_or_Medians = request.form['Lanes_or_Medians']   
    if Lanes_or_Medians=="Two-way (divided with broken lines road marking)":
        Lanes_or_Medians=2
    elif Lanes_or_Medians=="Undivided Two way":
        Lanes_or_Medians=4
    elif Lanes_or_Medians=="other":
        Lanes_or_Medians=5
    elif Lanes_or_Medians=="Double carriageway (median)":
        Lanes_or_Medians=0
    elif Lanes_or_Medians=="One way":
        Lanes_or_Medians=1
    elif Lanes_or_Medians=="Two-way (divided with solid lines road marking)":
        Lanes_or_Medians=3    
            
           
    Road_allignment = request.form['Road_allignment']    
    if Road_allignment=="Tangent road with flat terrain":
        Road_allignment=5
    elif Road_allignment=="Tangent road with mild grade and flat terrain":
        Road_allignment=6
    elif Road_allignment=="Steep grade downward with mountainous terrain":
        Road_allignment=3
    elif Road_allignment=="Tangent road with mountainous terrain and":
        Road_allignment=7
    elif Road_allignment=="Gentle horizontal curve":
        Road_allignment=1
    elif Road_allignment=="Escarpments":
        Road_allignment=0
    elif Road_allignment=="Sharp reverse curve":
        Road_allignment=2
    elif Road_allignment=="Tangent road with rolling terrain":
        Road_allignment=8
    elif Road_allignment=="Steep grade upward with mountainous terrain":
        Road_allignment=4
            
      
    Types_of_Junction = request.form['Types_of_Junction']    
    if Types_of_Junction=="Y Shape":
        Types_of_Junction=6
    elif Types_of_Junction=="No junction":
        Types_of_Junction=1
    elif Types_of_Junction=="Crossing":
        Types_of_Junction=0
    elif Types_of_Junction=="Other":
        Types_of_Junction=3
    elif Types_of_Junction=="O Shape":
        Types_of_Junction=2
    elif Types_of_Junction=="T Shape":
        Types_of_Junction=4
    elif Types_of_Junction=="X Shape":
        Types_of_Junction=5   
            
       
    Road_surface_type = request.form['Road_surface_type']   
    if Road_surface_type=="Asphalt roads":
        Road_surface_type=0
    elif Road_surface_type=="Earth roads":
        Road_surface_type=2
    elif Road_surface_type=="Gravel roads":
        Road_surface_type=3
    elif Road_surface_type=="Other":
        Road_surface_type=4
    elif Road_surface_type=="Asphalt roads with some distress":
        Road_surface_type=1   
            
        
    Road_surface_conditions = request.form['Road_surface_conditions']
    if Road_surface_conditions=="Dry":
        Road_surface_conditions=0
    elif Road_surface_conditions=="Wet or damp":
        Road_surface_conditions=3
    elif Road_surface_conditions=="Snow":
        Road_surface_conditions=2
    elif Road_surface_conditions=="Flood over 3cm. deep":
        Road_surface_conditions=1        
       
             
    Type_of_collision = request.form['Type_of_collision']
    if Type_of_collision=="Vehicle with vehicle collision":
        Type_of_collision=7
    elif Type_of_collision=="Collision with roadside objects":
        Type_of_collision=2
    elif Type_of_collision=="Collision with pedestrians":
        Type_of_collision=1
    elif Type_of_collision=="Rollover":
        Type_of_collision=6
    elif Type_of_collision=="Collision with animals":
        Type_of_collision=0
    elif Type_of_collision=="Collision with roadside-parked vehicles":
        Type_of_collision=3
    elif Type_of_collision=="Fall from vehicles":
        Type_of_collision=4
    elif Type_of_collision=="Other":
        Type_of_collision=5
    elif Type_of_collision=="With Train":
        Type_of_collision=8
        
    Number_of_vehicles_involved= int(request.form['Number_of_vehicles_involved'])
            
   
    Vehicle_movement = request.form['Vehicle_movement']
    if Vehicle_movement=="Going straight":
        Vehicle_movement=2
    elif Vehicle_movement=="Moving Backward":
        Vehicle_movement=3
    elif Vehicle_movement=="Other":
        Vehicle_movement=4
    elif Vehicle_movement=="Reversing":
        Vehicle_movement=7
    elif Vehicle_movement=="Turnover":
        Vehicle_movement=9
    elif Vehicle_movement=="Getting off":
        Vehicle_movement=1
    elif Vehicle_movement=="Entering a junction":
        Vehicle_movement=0
    elif Vehicle_movement=="Overtaking":
        Vehicle_movement=5
    elif Vehicle_movement=="Stopping":
        Vehicle_movement=8
    elif Vehicle_movement=="U-Turn":
        Vehicle_movement=10
    elif Vehicle_movement=="Waiting to go":
        Vehicle_movement=11
    elif Vehicle_movement=="Parked":
        Vehicle_movement=6
    
      
    Cause_of_accident = request.form['Cause_of_accident']
    if Cause_of_accident=="No distancing":
        Cause_of_accident=9
    elif Cause_of_accident=="Changing lane to the right":
        Cause_of_accident=1
    elif Cause_of_accident=="Changing lane to the left":
        Cause_of_accident=0
    elif Cause_of_accident=="Driving carelessly":
        Cause_of_accident=2
    elif Cause_of_accident=="No priority to vehicle":
        Cause_of_accident=11
    elif Cause_of_accident=="Moving Backward":
        Cause_of_accident=8
    elif Cause_of_accident=="No priority to pedestrian":
        Cause_of_accident=10
    elif Cause_of_accident=="Other":
        Cause_of_accident=12
    elif Cause_of_accident=="Overtaking":
        Cause_of_accident=15
    elif Cause_of_accident=="Driving under the influence of drugs":
        Cause_of_accident=4
    elif Cause_of_accident=="Driving to the left":
        Cause_of_accident=3
    elif Cause_of_accident=="Overspeed":
        Cause_of_accident=14
    elif Cause_of_accident=="Getting off the vehicle improperly":
        Cause_of_accident=6
    elif Cause_of_accident=="Overturning":
        Cause_of_accident=16
    elif Cause_of_accident=="Turnover":
        Cause_of_accident=17
    elif Cause_of_accident=="Overloading":
        Cause_of_accident=13
    elif Cause_of_accident=="Drunk driving":
        Cause_of_accident=5
    elif Cause_of_accident=="Improper parking":
        Cause_of_accident=7
        
        
    data = np.array([Age_band_of_driver, Sex_of_driver, Driving_experience,
       Type_of_vehicle, Lanes_or_Medians, Road_allignment,
       Types_of_Junction, Road_surface_type, Road_surface_conditions,
       Type_of_collision, Number_of_vehicles_involved, Vehicle_movement,
       Cause_of_accident]).reshape(1,-1)
        
    pred = model.predict(data)
    out=pred[0]
    #Accident_Severity = ('serious_injury','slight_injury','fatal_injury')
    #if Accident_Severity == 0:
     #   severity = 'seriour_injury' 
    #elif Accident_Severity == 1:
     #   severity = 'slight_injury'
    #else:
     #   severity = 'fatal_injury' 
    
    
    

    return render_template("RTA.html", prediction_text="Accident Severity is: {}".format(out))


if __name__ == "__main__":
    app.run()

