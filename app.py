import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

taxis = sns.load_dataset('taxis')

weekend_rides = taxis[taxis['pickup'].dt.dayofweek.isin([5, 6])]
weekday_rides = taxis[taxis['pickup'].dt.dayofweek.isin([0,1,2,3,4])]
weekday_rides['pickup_period'] = pd.cut(taxis['pickup'].dt.hour, bins=[-1, 6, 12, 18, 24], labels=['Night', 'Morning', 'Daylight', 'Dawn'])
weekend_rides['pickup_period'] = pd.cut(taxis['pickup'].dt.hour, bins=[-1, 6, 12, 18, 24], labels=['Night', 'Morning', 'Daylight', 'Dawn'])
weekday_rides_by_period = weekday_rides.groupby('pickup_period',observed=True).size()
weekend_rides_by_period = weekend_rides.groupby('pickup_period',observed=True).size()
borough_rides = taxis.groupby(['pickup_borough', 'color']).size().reset_index(name='total_rides')

st.set_page_config(layout="wide")
st.title('Usecase of streamlit')

st.subheader('Dateset')
with st.expander(label='Following dataset is of taxi rides in New York State in year of 2019',expanded=True):
    st.dataframe(data=taxis)

st.header('Discriptive Analysis')
st.subheader('Summary of dataset')

c = st.container()
c.dataframe(taxis.describe())

col1, col2 = st.columns([0.5, 0.5],gap='medium')
with col1:
    st.subheader("Fair - Distance Plot")
    fig, ax = plt.subplots(figsize=(7.5, 5))
    sns.scatterplot(data=taxis, x='distance', y='fare', size='passengers', alpha=0.8, hue='payment', palette='viridis', ax=ax)
    st.pyplot(fig)

with col2:
    st.subheader("Rides - Taxi Type Plot")
    fig, ax = plt.subplots(figsize=(7.5,5))
    sns.barplot(data=borough_rides, x='color', y='total_rides', hue='pickup_borough',ax=ax,palette='pastel')
    st.pyplot(fig)

st.subheader('Plot of Rides Fare and Tip Distribution on Weekdays and Weekend')

with st.expander(label='Plot',expanded=True):
    fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(25,15))
    ax[0,0].set_title('Weekday Rides - Fare Distribution', fontsize=12)
    ax[1,0].set_title('Weekend Rides - Fare Distribution', fontsize=12)
    ax[0,1].set_title('Weekday Rides - Tip Distribution', fontsize=12)
    ax[1,1].set_title('Weekend Rides - Tip Distribution', fontsize=12)
    ax[0,0].set_xlabel('Fare', fontsize=12)
    ax[0,0].set_ylabel('Count', fontsize=12)
    ax[1,0].set_xlabel('Fare', fontsize=12)
    ax[1,0].set_ylabel('Count', fontsize=12)
    ax[0,1].set_xlabel('Tip', fontsize=12)
    ax[0,1].set_ylabel('Count', fontsize=12)
    ax[1,1].set_xlabel('Tip', fontsize=12)
    ax[1,1].set_ylabel('Count', fontsize=12)
    ax[0,0].grid(axis='y', linestyle='--', alpha=0.7)
    ax[0,1].grid(axis='y', linestyle='--', alpha=0.7)
    ax[1,0].grid(axis='y', linestyle='--', alpha=0.7)
    ax[1,1].grid(axis='y', linestyle='--', alpha=0.7)
    fig.suptitle('Ride Fare and Tip Distributions', fontsize=16)
    sns.histplot(weekday_rides,x='fare',bins=15,kde=True,hue='payment',ax=ax[0,0]) 
    sns.histplot(weekend_rides,x='fare',bins=15,kde=True,hue='payment',ax=ax[1,0]) 
    sns.histplot(weekday_rides,x='tip',bins=15,kde=True,hue='payment',ax=ax[0,1]) 
    sns.histplot(weekend_rides,x='tip',bins=15,kde=True,hue='payment',ax=ax[1,1]) 
    st.pyplot(fig=fig)

st.subheader('Plot Determines the Lifestyle of Citizen in NY State')

with st.expander(label='Plot',expanded=True):
    fig, ax = plt.subplots(nrows=2,ncols=2,figsize=(25,15))
    ax[0,0].set_title('Taxi type - Fare Distribution', fontsize=12)
    ax[0,1].set_title('Total Rides by Borough - Taxi Color', fontsize=12)
    ax[1,0].set_title('Weekday Rides - Time Period', fontsize=12)
    ax[1,1].set_title('Weekend Rides - Time Period', fontsize=12)
    ax[0,0].set_xlabel('Taxi Type', fontsize=12)
    ax[0,0].set_ylabel('Total Fare', fontsize=12)
    ax[0,1].set_xlabel('Borough', fontsize=12)
    ax[0,1].set_ylabel('Total Rides', fontsize=12)
    ax[1,0].set_xlabel('Time Period', fontsize=12)
    ax[1,0].set_ylabel('Total Rides', fontsize=12)
    ax[1,1].set_xlabel('Time Period', fontsize=12)
    ax[1,1].set_ylabel('Total Rides', fontsize=12)
    ax[0,0].grid(axis='y', linestyle='--', alpha=0.7)
    ax[0,1].grid(axis='y', linestyle='--', alpha=0.7)
    ax[1,0].grid(axis='y', linestyle='--', alpha=0.7)
    ax[1,1].grid(axis='y', linestyle='--', alpha=0.7)
    fig.suptitle('Lifestyle of NY State Citizen', fontsize=16)
    sns.boxplot(data=taxis, x='color', y='total', palette='Set2', ax=ax[0,0])
    sns.barplot(data=borough_rides, x='pickup_borough', y='total_rides', hue='color', ax=ax[0,1])
    sns.barplot(x=weekday_rides_by_period.index, y=weekday_rides_by_period.values, ax=ax[1,0], width=0.5, palette='viridis')
    sns.barplot(x=weekend_rides_by_period.index, y=weekend_rides_by_period.values, ax=ax[1,1], width=0.5, palette='viridis')
    st.pyplot(fig)