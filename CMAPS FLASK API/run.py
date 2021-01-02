from flask import Flask, render_template, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        AllamaIqbalTown_model = pickle.load(open('finalized_model_A1.sav', 'rb'))
        Cantt_model = pickle.load(open('finalized_model_A2.sav', 'rb'))
        Chung_model = pickle.load(open('finalized_model_A3.sav', 'rb'))
        GreenTown_model = pickle.load(open('finalized_model_A4.sav', 'rb'))
        Raiwind_model = pickle.load(open('finalized_model_A5.sav', 'rb'))
        Sabzazar_model = pickle.load(open('finalized_model_A6.sav', 'rb'))
        MughalPura_model = pickle.load(open('finalized_model_A7.sav', 'rb'))
        Shadbagh_model = pickle.load(open('finalized_model_A8.sav', 'rb'))
        ShadraTown_model = pickle.load(open('finalized_model_A9.sav', 'rb'))
        Ichra_model = pickle.load(open('finalized_model_A10.sav', 'rb'))
        JoharTown_model = pickle.load(open('finalized_model_A11.sav', 'rb'))
        FaisalTown_model = pickle.load(open('finalized_model_A12.sav', 'rb'))
        DefenceA_model = pickle.load(open('finalized_model_A13.sav', 'rb'))
        Anarkali_model = pickle.load(open('finalized_model_A14.sav', 'rb'))
        GulshanRavi_model = pickle.load(open('finalized_model_A15.sav', 'rb'))
        Gulberg_model = pickle.load(open('finalized_model_A16.sav', 'rb'))
        RaviRoad_model = pickle.load(open('finalized_model_A17.sav', 'rb'))
        GardenTown_model = pickle.load(open('finalized_model_A18.sav', 'rb'))
        MuslimTown_model = pickle.load(open('finalized_model_A19.sav', 'rb'))
        LytonRoad_model = pickle.load(open('finalized_model_A20.sav', 'rb'))
        Mozang_model = pickle.load(open('finalized_model_A21.sav', 'rb'))
        SamanAbad_model = pickle.load(open('finalized_model_A22.sav', 'rb'))
        RaceCourse_model = pickle.load(open('finalized_model_A23.sav', 'rb'))
        BarkiRoad_model = pickle.load(open('finalized_model_A24.sav', 'rb'))
        Shadman_model = pickle.load(open('finalized_model_A25.sav', 'rb'))
        Hadyara_model = pickle.load(open('finalized_model_A26.sav', 'rb'))
        ModelTown_model = pickle.load(open('finalized_model_A27.sav', 'rb'))
        SarwarRoad_model = pickle.load(open('finalized_model_A28.sav', 'rb'))
        

        if request.json['posting'] == 'AllamaIqbalTown':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.2845
            latitude = 31.5124
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],
                            'Latitude': [latitude],'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = AllamaIqbalTown_model.predict(input_data)
             
            if (prediction == 0):
                output = "ALLAMA IQBAL TOWN: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "ALLAMA IQBAL TOWN: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "ALLAMA IQBAL TOWN: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "ALLAMA IQBAL TOWN: Expected crime category is  Police Acts"
            else:
                output = "ALLAMA IQBAL TOWN: Could not predict category"
        elif request.json['posting'] == 'Anarkali':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.312
            latitude = 31.5698
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = Anarkali_model.predict(input_data)
             
            if (prediction == 0):
                output = "Anarkali: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "Anarkali: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "Anarkali: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "Anarkali: Expected crime category is  Police Acts"
            else:
                output = "Anarkali: Could not predict category"
        elif request.json['posting'] == 'BarkiRoad':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.5087
            latitude = 31.4789
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = BarkiRoad_model.predict(input_data)
             
            if (prediction == 0):
                output = "BarkiRoad: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "BarkiRoad: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "BarkiRoad: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "BarkiRoad: Expected crime category is  Police Acts"
            else:
                output = "BarkiRoad: Could not predict category"
        elif request.json['posting'] == 'Cantt':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3889
            latitude = 31.5196
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = Cantt_model.predict(input_data)
             
            if (prediction == 0):
                output = "Cantt: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "Cantt: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "Cantt: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "Cantt: Expected crime category is  Police Acts"
            else:
                output = "Cantt: Could not predict category"
        elif request.json['posting'] == 'Chung':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.1739
            latitude = 31.422
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = Chung_model.predict(input_data)
             
            if (prediction == 0):
                output = "Chung: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "Chung: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "Chung: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "Chung: Expected crime category is  Police Acts"
            else:
                output = "Chung: Could not predict category"
        elif request.json['posting'] == 'DefenceA':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.4388
            latitude = 31.4699
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = DefenceA_model.predict(input_data)
             
            if (prediction == 0):
                output = "DefenceA: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "DefenceA: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "DefenceA: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "DefenceA: Expected crime category is  Police Acts"
            else:
                output = "DefenceA: Could not predict category"
        elif request.json['posting'] == 'FaisalTown':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3045
            latitude = 31.476
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = FaisalTown_model.predict(input_data)
             
            if (prediction == 0):
                output = "FaisalTown: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "FaisalTown: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "FaisalTown: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "FaisalTown: Expected crime category is  Police Acts"
            else:
                output = "FaisalTown: Could not predict category"
        elif request.json['posting'] == 'GardenTown':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3191
            latitude = 31.5155
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = GardenTown_model.predict(input_data)
             
            if (prediction == 0):
                output = "GardenTown: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "GardenTown: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "GardenTown: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "GardenTown: Expected crime category is  Police Acts"
            else:
                output = "GardenTown: Could not predict category"
        elif request.json['posting'] == 'GreenTown':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3074
            latitude = 31.4346
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = GreenTown_model.predict(input_data)
             
            if (prediction == 0):
                output = "GreenTown: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "GreenTown: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "GreenTown: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "GreenTown: Expected crime category is  Police Acts"
            else:
                output = "GreenTown: Could not predict category"
        elif request.json['posting'] == 'Gulberg':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3441
            latitude = 31.5102
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = Gulberg_model.predict(input_data)
             
            if (prediction == 0):
                output = "Gulberg: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "Gulberg: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "Gulberg: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "Gulberg: Expected crime category is  Police Acts"
            else:
                output = "Gulberg: Could not predict category"
        elif request.json['posting'] == 'GulshanRavi':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.2795
            latitude = 31.5521
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = GulshanRavi_model.predict(input_data)
             
            if (prediction == 0):
                output = "GulshanRavi: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "GulshanRavi: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "GulshanRavi: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "GulshanRavi: Expected crime category is  Police Acts"
            else:
                output = "GulshanRavi: Could not predict category"
        elif request.json['posting'] == 'Hadyara':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3406
            latitude = 31.545
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = Hadyara_model.predict(input_data)
             
            if (prediction == 0):
                output = "Hadyara: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "Hadyara: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "Hadyara: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "Hadyara: Expected crime category is  Police Acts"
            else:
                output = "Hadyara: Could not predict category"
        elif request.json['posting'] == 'Ichra':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3183
            latitude = 31.5313
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = Ichra_model.predict(input_data)
             
            if (prediction == 0):
                output = "Ichra: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "Ichra: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "Ichra: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "Ichra: Expected crime category is  Police Acts"
            else:
                output = "Ichra: Could not predict category"
        elif request.json['posting'] == 'JoharTown':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.2942
            latitude = 31.4621
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = JoharTown_model.predict(input_data)
             
            if (prediction == 0):
                output = "JoharTown: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "JoharTown: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "JoharTown: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "JoharTown: Expected crime category is  Police Acts"
            else:
                output = "JoharTown: Could not predict category"
        elif request.json['posting'] == 'LytonRoad':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3115
            latitude = 31.5538
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = LytonRoad_model.predict(input_data)
             
            if (prediction == 0):
                output = "LytonRoad: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "LytonRoad: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "LytonRoad: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "LytonRoad: Expected crime category is  Police Acts"
            else:
                output = "LytonRoad: Could not predict category"
        elif request.json['posting'] == 'ModelTown':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3239
            latitude = 31.4805
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = ModelTown_model.predict(input_data)
             
            if (prediction == 0):
                output = "ModelTown: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "ModelTown: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "ModelTown: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "ModelTown: Expected crime category is  Police Acts"
            else:
                output = "ModelTown: Could not predict category"
        elif request.json['posting'] == 'Mozang':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3138
            latitude = 31.5597
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = Mozang_model.predict(input_data)
             
            if (prediction == 0):
                output = "Mozang: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "Mozang: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "Mozang: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "Mozang: Expected crime category is  Police Acts"
            else:
                output = "Mozang: Could not predict category"
        elif request.json['posting'] == 'MughalPura':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3586
            latitude = 31.569
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = MughalPura_model.predict(input_data)
             
            if (prediction == 0):
                output = "MughalPura: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "MughalPura: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "MughalPura: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "MughalPura: Expected crime category is  Police Acts"
            else:
                output = "MughalPura: Could not predict category"
        elif request.json['posting'] == 'MuslimTown':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3228
            latitude = 31.5194
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = MuslimTown_model.predict(input_data)
             
            if (prediction == 0):
                output = "MuslimTown: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "MuslimTown: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "MuslimTown: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "MuslimTown: Expected crime category is  Police Acts"
            else:
                output = "MuslimTown: Could not predict category"
        elif request.json['posting'] == 'RaceCourse':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3357
            latitude = 31.539
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = RaceCourse_model.predict(input_data)
             
            if (prediction == 0):
                output = "RaceCourse: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "RaceCourse: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "RaceCourse: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "RaceCourse: Expected crime category is  Police Acts"
            else:
                output = "RaceCourse: Could not predict category"
        elif request.json['posting'] == 'Raiwind':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.2137
            latitude = 31.2449
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = Raiwind_model.predict(input_data)
             
            if (prediction == 0):
                output = "Raiwind: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "Raiwind: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "Raiwind: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "Raiwind: Expected crime category is  Police Acts"
            else:
                output = "Raiwind: Could not predict category"
        elif request.json['posting'] == 'RaviRoad':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.302
            latitude = 31.5946
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = RaviRoad_model.predict(input_data)
             
            if (prediction == 0):
                output = "RaviRoad: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "RaviRoad: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "RaviRoad: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "RaviRoad: Expected crime category is  Police Acts"
            else:
                output = "RaviRoad: Could not predict category"
        elif request.json['posting'] == 'Sabzazar':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.2701
            latitude = 31.5209
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = Sabzazar_model.predict(input_data)
             
            if (prediction == 0):
                output = "Sabzazar: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "Sabzazar: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "Sabzazar: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "Sabzazar: Expected crime category is  Police Acts"
            else:
                output = "Sabzazar: Could not predict category"
        elif request.json['posting'] == 'SamanAbad':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.2985
            latitude = 31.5356
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = SamanAbad_model.predict(input_data)
             
            if (prediction == 0):
                output = "SamanAbad: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "SamanAbad: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "SamanAbad: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "SamanAbad: Expected crime category is  Police Acts"
            else:
                output = "SamanAbad: Could not predict category"
        elif request.json['posting'] == 'SarwarRoad':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3773
            latitude = 31.5467
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = SarwarRoad_model.predict(input_data)
             
            if (prediction == 0):
                output = "SarwarRoad: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "SarwarRoad: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "SarwarRoad: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "SarwarRoad: Expected crime category is  Police Acts"
            else:
                output = "SarwarRoad: Could not predict category"
        elif request.json['posting'] == 'Shadbagh':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3397
            latitude = 31.6001
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = Shadbagh_model.predict(input_data)
             
            if (prediction == 0):
                output = "Shadbagh: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "Shadbagh: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "Shadbagh: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "Shadbagh: Expected crime category is  Police Acts"
            else:
                output = "Shadbagh: Could not predict category"
        elif request.json['posting'] == 'Shadman':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.3309
            latitude = 31.5378
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = Shadbagh_model.predict(input_data)
             
            if (prediction == 0):
                output = "Shadman: Expected crime category is   Crime Against Person"
            elif(prediction == 1):
                output = "Shadman: Expected crime category is  Crime Against Property"
            elif(prediction == 2):
                output = "Shadman: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "Shadman: Expected crime category is  Police Acts"
            else:
                output = "Shadman: Could not predict category"
        elif request.json['posting'] == 'ShadraTown':
            area = 0
            day = request.json['day']
            date = request.json['date']
            month = request.json['month']
            year = request.json['year']
            hours = request.json['hours']
            minutes = request.json['minutes']
            longitude = 74.2824
            latitude = 31.6211
            location = 0
            PartOfTheDay = request.json['PartOfTheDay']
            
            user_data = pd.DataFrame({'Posting':[area],'Day': [day],
                            'Date': [date],'Month': [month],'Year': [year],
                            'Hours': [hours],'Minutes': [minutes],'Partoftheday': [PartOfTheDay],'Latitude': [latitude],
                            'Longitude': [longitude],'Locations': [location]})

            input_data = user_data.values
            prediction = ShadraTown_model.predict(input_data)
             
            if (prediction == 0):
                output = "ShadraTown: Expected crime category is Crime Against Person"
            elif(prediction == 1):
                output = "ShadraTown: Expected crime category is Crime Against Property"
            elif(prediction == 2):
                output = "ShadraTown: Expected crime category is  Ordinance"
            elif(prediction == 3):
                output = "ShadraTown: Expected crime category is  Police Acts"
            else:
                output = "ShadraTown: Could not predict category"
        else:
            output = 'could not predict anything'

    return jsonify(output)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        Day_model = pickle.load(open('finalized_model_day.sav', 'rb'))
        Area_model = pickle.load(open('finalized_model_area.sav', 'rb'))
        Month_model = pickle.load(open('finalized_model_month.sav', 'rb'))
        
        if request.json['Crime'] == 'Outraging the Modesty of Women':
            crime = 32
        elif request.json['Crime'] == 'Other Crime':
            crime = 29
        elif request.json['Crime'] == 'Punjab Arms Ordinance Bill of 2015':
            crime = 68
        elif request.json['Crime'] == 'Punjab Information Temporary Residence Ordinance':
            crime = 70
        elif request.json['Crime'] == 'Rape':
            crime = 40
        elif request.json['Crime'] == 'M/Cycle Theft':
            crime = 24
        elif request.json['Crime'] == 'Burglary':
            crime = 5
        elif request.json['Crime'] == 'Robbery':
            crime = 42
        elif request.json['Crime'] == 'Kidnapping':
            crime = 20
        elif request.json['Crime'] == 'Non-Fatal Accident':
            crime = 28
        elif request.json['Crime'] == 'Cheque Dishonour':
            crime = 9
        elif request.json['Crime'] == 'Miscellaneous':
            crime = 25
        elif request.json['Crime'] == 'Kite Flying act':
            crime = 57
        elif request.json['Crime'] == 'Begging Act':
            crime = 51
        elif request.json['Crime'] == 'Anti-Norcotics Act':
            crime = 47
        elif request.json['Crime'] == 'Punjab Security Ordinance 2015':
            crime = 71
        elif request.json['Crime'] == 'Overspeeding':
            crime = 33
        elif request.json['Crime'] == 'Other Vehicle Theft':
            crime = 31
        elif request.json['Crime'] == 'Hurt (personal feud)':
            crime = 17
        elif request.json['Crime'] == 'Punjab Sound System Regulation Ordinance':
            crime = 72
        elif request.json['Crime'] == 'Attack on Govt. Servant':
            crime = 2
        elif request.json['Crime'] == 'Narcotics':
            crime = 27
        elif request.json['Crime'] == 'Illegal Extortion':
            crime = 18
        elif request.json['Crime'] == 'Electricity Act':
            crime = 55
        elif request.json['Crime'] == 'Car Theft':
            crime = 8
        elif request.json['Crime'] == 'Gambling':
            crime = 14
        elif request.json['Crime'] == 'Arms Ordinance Act':
            crime = 50
        elif request.json['Crime'] == 'Anti-Terrorism Act':
            crime = 48
        elif request.json['Crime'] == 'Price Control Act':
            crime = 65
        elif request.json['Crime'] == 'Fatal Accident':
            crime = 13
        elif request.json['Crime'] == 'M/Cycle Snatching':
            crime = 23
        elif request.json['Crime'] == 'Attempted Murder':
            crime = 3
        elif request.json['Crime'] == 'Murder':
            crime = 26
        elif request.json['Crime'] == 'Punjab Local Government Ordinance 2016':
            crime = 37
        elif request.json['Crime'] == 'One Wheeling Act':
            crime = 62
        elif request.json['Crime'] == 'Loud Speaker Act':
            crime = 59
        elif request.json['Crime'] == 'Secretarianism':
            crime = 43
        elif request.json['Crime'] == 'Anti-terrorism Act 1997 Ata':
            crime = 49
        elif request.json['Crime'] == 'Punjab Marriage Function ordinance 2016':
            crime = 38
        elif request.json['Crime'] == 'Tresspassing':
            crime = 46
        elif request.json['Crime'] == 'Ehtram-e-Ramzan':
            crime = 12
        elif request.json['Crime'] == 'Smoking Health Ordinance':
            crime = 44
        elif request.json['Crime'] == 'Blind Murder':
            crime = 4
        elif request.json['Crime'] == '382 PPC':
            crime = 1
        elif request.json['Crime'] == 'Telephone Act':
            crime = 74
        elif request.json['Crime'] == 'Car Snatching':
            crime = 7
        elif request.json['Crime'] == 'Illegal Gas Cylinder Act':
            crime = 56
        elif request.json['Crime'] == 'Kidnapping Minors':
            crime = 21
        elif request.json['Crime'] == 'Dacoity/Robbery with Murder':
            crime = 11
        elif request.json['Crime'] == 'Habs e Beja':
            crime = 16
        elif request.json['Crime'] == 'Dacoity':
            crime = 10
        elif request.json['Crime'] == 'Punjab Food Authority Act 2011':
            crime = 36
        elif request.json['Crime'] == 'Cigrette Act':
            crime = 52
        elif request.json['Crime'] == 'Gang Rape':
            crime = 15
        elif request.json['Crime'] == 'Police Order Act':
            crime = 64
        elif request.json['Crime'] == 'Kidnap for Ransom':
            crime = 19
        elif request.json['Crime'] == 'Dengue Act':
            crime = 54
        elif request.json['Crime'] == 'New Punjab Local Govt Ord 2011':
            crime = 60
        elif request.json['Crime'] == 'Police Encounter':
            crime = 34
        elif request.json['Crime'] == 'LDA Act 1975':
            crime = 22
        elif request.json['Crime'] == 'Punjab Fertilizers Control Act':
            crime = 69
        elif request.json['Crime'] == 'Prohibition of Expressing Matters on Walls Act 1995':
            crime = 66
        elif request.json['Crime'] == 'Copyright Act':
            crime = 53
        elif request.json['Crime'] == 'Touheen Quran Act':
            crime = 75
        elif request.json['Crime'] == 'Local Government Act':
            crime = 58
        elif request.json['Crime'] == 'New Punjab Pure Food Ord 1960':
            crime = 61
        elif request.json['Crime'] == 'Petrolium Act 1934':
            crime = 63
        elif request.json['Crime'] == 'The Punjab Prohibition of Child Labour at Brick KIlns Ordinance 2016':
            crime = 0
        elif request.json['Crime'] == 'Punjab Animal Slaughter Control Act':
            crime = 35
        elif request.json['Crime'] == 'Protection of Pakistan Ordinance 2013':
            crime = 67
        elif request.json['Crime'] == 'Regulation and Control of Loudspeakers and Amplifiers':
            crime = 41
        elif request.json['Crime'] == 'Canal Cut':
            crime = 6
        elif request.json['Crime'] == ' The Anti Terrorism Act (ATA),1997':
            crime = 45
        elif request.json['Crime'] == 'Other Vehicle Snatching':
            crime = 30
        elif request.json['Crime'] == 'Tree Theft Act':
            crime = 76
        elif request.json['Crime'] == 'Railway Act':
            crime = 73
        elif request.json['Crime'] == 'Punjab University Broads Act':
            crime = 39
        else:
            output1 = "wrong input"

        if request.json['Model'] == 'area':
            user_data = pd.DataFrame({'Crime':[crime]})
            input_data = user_data.values
            predict = Area_model.predict(input_data)

            if (predict == 0):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in  Allama Iqbal Town"
            elif(predict == 1):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Anarkali"
            elif(predict == 2):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Cantt"
            elif(predict == 3):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Chung"
            elif(predict == 4):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Defence A"
            elif(predict == 5):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Faisal Town"
            elif(predict == 6):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Gardan Town"
            elif(predict == 7):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Green Town"
            elif(predict == 8):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Gulberg"
            elif(predict == 9):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Gulshan Ravi"
            elif(predict == 10):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Hadyara"
            elif(predict == 11):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Ichra"
            elif(predict == 12):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Johar Town"
            elif(predict == 13):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Lyton Road"
            elif(predict == 14):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Model Town"
            elif(predict == 15):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Mozang"
            elif(predict == 16):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Mughal Pura"
            elif(predict == 17):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Muslim Town"
            elif(predict == 18):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Race Course"
            elif(predict == 19):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Raiwind"
            elif(predict == 20):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Ravi Road"
            elif(predict == 21):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Sabzazar"
            elif(predict == 22):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Saman Abad"
            elif(predict == 23):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Sarwar Road"
            elif(predict == 24):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Shad Bagh"
            elif(predict == 25):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Shadman"
            elif(predict == 26):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in Shahdra Town"
            elif(predict == 27):
                output = "There is a 12.633769322235434 Percent chance of this crime occuring in barki road"
            else:
                output = "There is a12.633769322235434 Percent chance of this crime occuring in barki road"
        elif request.json['Model'] == 'day':
            user_data = pd.DataFrame({'Crime':[crime]})
            input_data = user_data.values
            predict = Day_model.predict(input_data)
            
            if (predict == 0):
                output = "There is a chance of this crime occuring on Friday"
            elif(predict == 1):
                output = "There is a chance of this crime occuring on Monday"
            elif(predict == 2):
                output = "There is a chance of this crime occuring on Saturday"     
            elif(predict == 3):
                output = "There is a chance of this crime occuring on Sunday"
            elif(predict == 4):
                output = "There is a chance of this crime occuring on Tuesday"
            elif(predict == 5):
                output = "There is a chance of this crime occuring on Thursday"
            elif(predict == 6):
                output = "There is a chance of this crime occuring on Wednesday"
            else:
                output = "could not predict anything"
        return jsonify(output)

@app.route('/predictThree', methods=['GET', 'POST'])
def predictThree():
    if request.method == 'POST':
        Month_model = pickle.load(open('finalized_model_month.sav', 'rb'))
        
        if request.json['Crime'] == 'Outraging the Modesty of Women':
            crime = 32
        elif request.json['Crime'] == 'Other Crime':
            crime = 29
        elif request.json['Crime'] == 'Punjab Arms Ordinance Bill of 2015':
            crime = 68
        elif request.json['Crime'] == 'Punjab Information Temporary Residence Ordinance':
            crime = 70
        elif request.json['Crime'] == 'Rape':
            crime = 40
        elif request.json['Crime'] == 'M/Cycle Theft':
            crime = 24
        elif request.json['Crime'] == 'Burglary':
            crime = 5
        elif request.json['Crime'] == 'Robbery':
            crime = 42
        elif request.json['Crime'] == 'Kidnapping':
            crime = 20
        elif request.json['Crime'] == 'Non-Fatal Accident':
            crime = 28
        elif request.json['Crime'] == 'Cheque Dishonour':
            crime = 9
        elif request.json['Crime'] == 'Miscellaneous':
            crime = 25
        elif request.json['Crime'] == 'Kite Flying act':
            crime = 57
        elif request.json['Crime'] == 'Begging Act':
            crime = 51
        elif request.json['Crime'] == 'Anti-Norcotics Act':
            crime = 47
        elif request.json['Crime'] == 'Punjab Security Ordinance 2015':
            crime = 71
        elif request.json['Crime'] == 'Overspeeding':
            crime = 33
        elif request.json['Crime'] == 'Other Vehicle Theft':
            crime = 31
        elif request.json['Crime'] == 'Hurt (personal feud)':
            crime = 17
        elif request.json['Crime'] == 'Punjab Sound System Regulation Ordinance':
            crime = 72
        elif request.json['Crime'] == 'Attack on Govt. Servant':
            crime = 2
        elif request.json['Crime'] == 'Narcotics':
            crime = 27
        elif request.json['Crime'] == 'Illegal Extortion':
            crime = 18
        elif request.json['Crime'] == 'Electricity Act':
            crime = 55
        elif request.json['Crime'] == 'Car Theft':
            crime = 8
        elif request.json['Crime'] == 'Gambling':
            crime = 14
        elif request.json['Crime'] == 'Arms Ordinance Act':
            crime = 50
        elif request.json['Crime'] == 'Anti-Terrorism Act':
            crime = 48
        elif request.json['Crime'] == 'Price Control Act':
            crime = 65
        elif request.json['Crime'] == 'Fatal Accident':
            crime = 13
        elif request.json['Crime'] == 'M/Cycle Snatching':
            crime = 23
        elif request.json['Crime'] == 'Attempted Murder':
            crime = 3
        elif request.json['Crime'] == 'Murder':
            crime = 26
        elif request.json['Crime'] == 'Punjab Local Government Ordinance 2016':
            crime = 37
        elif request.json['Crime'] == 'One Wheeling Act':
            crime = 62
        elif request.json['Crime'] == 'Loud Speaker Act':
            crime = 59
        elif request.json['Crime'] == 'Secretarianism':
            crime = 43
        elif request.json['Crime'] == 'Anti-terrorism Act 1997 Ata':
            crime = 49
        elif request.json['Crime'] == 'Punjab Marriage Function ordinance 2016':
            crime = 38
        elif request.json['Crime'] == 'Tresspassing':
            crime = 46
        elif request.json['Crime'] == 'Ehtram-e-Ramzan':
            crime = 12
        elif request.json['Crime'] == 'Smoking Health Ordinance':
            crime = 44
        elif request.json['Crime'] == 'Blind Murder':
            crime = 4
        elif request.json['Crime'] == '382 PPC':
            crime = 1
        elif request.json['Crime'] == 'Telephone Act':
            crime = 74
        elif request.json['Crime'] == 'Car Snatching':
            crime = 7
        elif request.json['Crime'] == 'Illegal Gas Cylinder Act':
            crime = 56
        elif request.json['Crime'] == 'Kidnapping Minors':
            crime = 21
        elif request.json['Crime'] == 'Dacoity/Robbery with Murder':
            crime = 11
        elif request.json['Crime'] == 'Habs e Beja':
            crime = 16
        elif request.json['Crime'] == 'Dacoity':
            crime = 10
        elif request.json['Crime'] == 'Punjab Food Authority Act 2011':
            crime = 36
        elif request.json['Crime'] == 'Cigrette Act':
            crime = 52
        elif request.json['Crime'] == 'Gang Rape':
            crime = 15
        elif request.json['Crime'] == 'Police Order Act':
            crime = 64
        elif request.json['Crime'] == 'Kidnap for Ransom':
            crime = 19
        elif request.json['Crime'] == 'Dengue Act':
            crime = 54
        elif request.json['Crime'] == 'New Punjab Local Govt Ord 2011':
            crime = 60
        elif request.json['Crime'] == 'Police Encounter':
            crime = 34
        elif request.json['Crime'] == 'LDA Act 1975':
            crime = 22
        elif request.json['Crime'] == 'Punjab Fertilizers Control Act':
            crime = 69
        elif request.json['Crime'] == 'Prohibition of Expressing Matters on Walls Act 1995':
            crime = 66
        elif request.json['Crime'] == 'Copyright Act':
            crime = 53
        elif request.json['Crime'] == 'Touheen Quran Act':
            crime = 75
        elif request.json['Crime'] == 'Local Government Act':
            crime = 58
        elif request.json['Crime'] == 'New Punjab Pure Food Ord 1960':
            crime = 61
        elif request.json['Crime'] == 'Petrolium Act 1934':
            crime = 63
        elif request.json['Crime'] == 'The Punjab Prohibition of Child Labour at Brick KIlns Ordinance 2016':
            crime = 0
        elif request.json['Crime'] == 'Punjab Animal Slaughter Control Act':
            crime = 35
        elif request.json['Crime'] == 'Protection of Pakistan Ordinance 2013':
            crime = 67
        elif request.json['Crime'] == 'Regulation and Control of Loudspeakers and Amplifiers':
            crime = 41
        elif request.json['Crime'] == 'Canal Cut':
            crime = 6
        elif request.json['Crime'] == ' The Anti Terrorism Act (ATA),1997':
            crime = 45
        elif request.json['Crime'] == 'Other Vehicle Snatching':
            crime = 30
        elif request.json['Crime'] == 'Tree Theft Act':
            crime = 76
        elif request.json['Crime'] == 'Railway Act':
            crime = 73
        elif request.json['Crime'] == 'Punjab University Broads Act':
            crime = 39
        else:
            output1 = "wrong input"

        user_data = pd.DataFrame({'Crime':[crime]})
        input_data = user_data.values
        predict = Month_model.predict(input_data)
        
        if (predict == 0):
            output = "There is a chance of this crime occuring in January"
        elif(predict == 1):
            output = "There is a chance of this crime occuring in Februaury"
        elif(predict == 2):
            output = "There is a chance of this crime occuring in March"     
        elif(predict == 3):
            output = "There is a chance of this crime occuring in April"
        elif(predict == 4):
            output = "There is a chance of this crime occuring in May"
        elif(predict == 5):
            output = "There is a chance of this crime occuring in June"
        elif(predict == 6):
            output = "There is a chance of this crime occuring in July"
        elif(predict == 7):
            output = "There is a chance of this crime occuring in August"
        elif(predict == 8):
            output = "There is a chance of this crime occuring in September"
        elif(predict == 9):
            output = "There is a chance of this crime occuring in October"
        elif(predict == 10):
            output = "There is a chance of this crime occuring in November"
        elif(predict == 11):
            output = "There is a chance of this crime occuring in December"

        return jsonify(output)


if __name__ == "__main__":
    app.run(debug=True)