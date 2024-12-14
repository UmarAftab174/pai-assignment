# Taxi Rides Analysis in New York State - Streamlit Application

This project is a Streamlit web application designed to perform an in-depth analysis of taxi rides in New York State for the year 2019. The app provides interactive visualizations and descriptive analysis to explore various aspects of taxi rides, such as fares, tips, ride times, and borough-wise distributions. It is developed as part of the university course **"Programming for AI".**

---

## Features

### 1. Dataset Overview
- Displays the dataset using an interactive data table.
- Provides a summary and descriptive statistics of the dataset.

### 2. Visualizations

#### A. **Scatter Plot**: 
- Plots the relationship between `distance` and `fare`.
- Includes passenger count and payment type as additional features.

#### B. **Bar Plot**: 
- Shows the total number of rides by taxi type (color) and pickup borough.

#### C. **Histogram**:
- Compares the distribution of fares and tips on weekdays and weekends.
- Includes separate plots for different payment types.

#### D. **Box Plot and Bar Plots**:
- Visualizes the total fare by taxi type and borough-wise ride counts.
- Illustrates ride distributions based on time periods for weekdays and weekends.

### 3. Interactive Layout
- Utilizes Streamlit's layout features (containers, columns, and expanders) for a responsive and user-friendly interface.

---

## How to Run the App

### Requirements
Ensure the following Python packages are installed:
- **streamlit**
- **pandas**
- **matplotlib**
- **seaborn**

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/<UmarAftab174>/<pai-assignment>.git
   ```

2. Navigate to the project directory:
   ```bash
   cd <pai-assignment>
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

5. Open the link provided by Streamlit in your browser (usually `https://pai-assignment-buck.streamlit.app/`).

---

## File Structure

```plaintext
<pai-assignment>/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
└── README.md              # Documentation (this file)
```

---

## Dataset Description
- The dataset used is the **"Taxis"** dataset from Seaborn's built-in dataset collection.
- Displays a detailed dataset of taxi rides.
   - Columns in the dataset include:
     - `pickup`: Timestamp of ride pickup.
     - `dropoff`: Timestamp of ride dropoff.
     - `passengers`: Number of passengers in the ride.
     - `distance`: Distance covered in the ride (in miles).
     - `fare`: Fare charged for the ride.
     - `tip`: Tip given for the ride.
     - `tolls`: Tolls charged during the ride.
     - `total`: Total amount charged (fare + tip + tolls).
     - `color`: Color of the taxi (e.g., yellow, green).
     - `payment`: Payment method used (e.g., cash, credit card).
     - `pickup_zone`: Geographic zone of ride pickup.
     - `dropoff_zone`: Geographic zone of ride dropoff.
     - `pickup_borough`: Borough of ride pickup.
     - `dropoff_borough`: Borough of ride dropoff.

---

## Key Insights
1. **Fares and Distance**:
   - Clear trends between distance and fare.
   - Payment type influences fare distributions.

2. **Ride Trends by Borough**:
   - Taxi rides vary significantly between boroughs and taxi types.

3. **Fare and Tip Comparisons**:
   - Weekday and weekend trends differ in terms of fare and tipping behavior.

4. **Citizen Behavior Analysis**:
   - Time-of-day ride patterns provide insight into the activity levels in New York City.

---

## Future Improvements
- Add filters for boroughs, payment types, and ride distances.
- Include predictive analysis of fares using regression techniques.
- Deploy the app with a scalable backend.

---

## Author
This application was created by **Umar Aftab** as part of the **Programming for AI** course at Bahria University.
