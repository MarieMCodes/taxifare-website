import streamlit as st
import datetime
import requests
'''
## Welcome to your cab fare predictor
'''

st.markdown('''
You'll tell us your journey and we'll give you a price estimate!
''')

# Building sidebar as a group
st.sidebar.markdown('''Please provide details for your ride:''')
#grouping user input variables together
with st.form(key='my_form'):
    date=st.sidebar.date_input('Date input')
    time=st.sidebar.time_input('Time entry')
    p_long=st.sidebar.selectbox('Enter pickup longitude',[73.4,76.7])
    p_lat=st.sidebar.selectbox('Enter pickup latitude',[40.75,46.5])
    d_long=st.sidebar.selectbox('Enter dropoff longitude',[73.1,76.3])
    d_lat=st.sidebar.selectbox('Enter dropoff latitude',[40.2,46.4])
    passengers=st.sidebar.selectbox('Select amount of passengers', [1,2,3,4,5,6,7,8])
    submit_form=st.form_submit_button('Get Fare')

#https://taxifare.lewagon.ai/predict?pickup_latitude=40.7586625&pickup_longitude=-73.978761&dropoff_latitude=40.715184&dropoff_longitude=-73.991715&passenger_count=1&pickup_datetime=2024-06-11%2021:13:10
if submit_form:
    url = 'https://taxifare.lewagon.ai/predict'

#2. Let's build a dictionary containing the parameters for our API...
    params = {
        'pickup_datetime': f'{date} {time}',
        'pickup_longitude':p_long,
        'pickup_latitude':p_lat,
        'dropoff_longitude':d_long,
        'dropoff_latitude':d_lat,
        'passenger_count': passengers
    }


#3. Let's call our API using the `requests` package...
#@st.cache
    response = requests.get(url, params=params).json()

# Show and update progress bar
    bar = st.progress(50)
    bar.progress(100)

#4. Let's retrieve the prediction from the **JSON** returned by the API...
    fare=response['fare']


## Finally, we can display the prediction to the user
    st.write('your fare is:', fare)
