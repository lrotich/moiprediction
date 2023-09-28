import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder
import streamlit as st

# Define CSS for colored buttons
colored_button_css = """
<style>
.sidebar .widget-button {
	background-color: #3498db;
	color: white;
	border: none;
	border-radius: 5px;
	padding: 10px 20px;
	cursor: pointer;
}

.sidebar .widget-button:hover {
	background-color: #2980b9;
}
</style>
"""

# Apply the CSS
st.markdown(colored_button_css, unsafe_allow_html=True)
df = pd.read_csv("admission.csv")
# Create a sidebar menu
st.sidebar.title("Menu")

# Add navigation options as colored buttons
if st.sidebar.button("Home", key="home_button"):
	st.empty()
	st.title("Home Page")
	st.write("Welcome to the Home Page.")

if st.sidebar.button("Dashboard", key="dashboard_button"):
	st.empty()
	st.title("Dashboard Page")
	st.write("This is the Dashboard Page.")

if st.sidebar.button("Settings", key="settings_button"):
	st.empty()
	st.title("Settings Page")
	st.write("Configure your settings here.")

# Create a dictionary to map program codes to program names
program_code_to_name = {
    1253101: 'BACHELOR OF ARTS',
    1253107: 'BACHELOR OF SCIENCE (ACTUARIAL SCIENCE)',
    1253112: 'BACHELOR OF SCIENCE (BIOCHEMISTRY)',
    1253115: 'BACHELOR OF SCIENCE (COMPUTER SCIENCE)',
    1253120: 'BACHELOR OF SCIENCE (BSC.)',
    1253123: 'BACHELOR OF SCIENCE (MICROBIOLOGY)',
    1253128: 'BACHELOR OF DENTAL SURGERY',
    1253131: 'BACHELOR OF MEDICINE AND BACHELOR OF SURGERY (MBCHB)',
    1253132: 'BACHELOR OF SCIENCE (NURSING)',
    1253134: 'BACHELOR OF LAWS (LL.B.)',
    1253135: 'BACHELOR OF EDUCATION (ARTS)',
    1253137: 'BACHELOR OF EDUCATION (SCIENCE)',
    1253144: 'BACHELOR OF ARTS (SOCIAL WORK)',
    1253150: 'BACHELOR OF SCIENCE (INFORMATION SCIENCES)',
    1253151: 'BACHELOR OF BUSINESS MANAGEMENT',
    1253157: 'BACHELOR OF TOURISM MANAGEMENT',
    1253161: 'BACHELOR OF ARTS (MUSIC)',
    1253164: 'BACHELOR OF SCIENCE (APPLIED STATISTICS WITH COMPUTING)',
    1253166: 'BACHELOR OF ARTS (FRENCH) - OLD PROGRAMME',
    1253169: 'BACHELOR OF ARTS (GERMAN) - OLD PROGRAMME',
    1253171: 'BACHELOR OF ARTS (COMMUNITY DEVELOPMENT)',
    1253182: 'BACHELOR OF SCIENCE (COMMUNICATION AND JOURNALISM)',
    1253187: 'BACHELOR OF SCIENCE (AGRI BUSINESS MANAGEMENT)',
    1253188: 'BACHELOR OF SCIENCE (ENVIRONMENTAL HEALTH)',
    1253189: 'BACHELOR OF SCIENCE (HUMAN RESOURCE MANAGEMENT)',
    1253194: 'BACHELOR OF SCIENCE (MEDICAL LABORATORY SCIENCE)',
    1253201: 'BACHELOR OF ARTS (WITH EDUCATION)',
    1253215: 'BACHELOR OF SCIENCE (AGRICULTURAL ECONOMICS AND RESOURCE MANAGEMENT)',
    1253222: 'BACHELOR OF HOTELS AND HOSPITALITY MANAGEMENT',
    1253229: 'BACHELOR OF SCIENCE IN ENVIRONMENTAL SCIENCE',
    1253234: 'BACHELOR OF TRAVEL AND TOURS OPERATIONS MANAGEMENT',
    1253237: 'BACHELOR OF ARTS (PSYCHOLOGY)',
    1253260: 'BACHELOR OF SCIENCE IN COMMUNITY HEALTH EDUCATION',
    1253292: 'BACHELOR OF ARTS (GEOGRAPHY)',
    1253293: 'BACHELOR OF SCIENCE (ANIMAL SCIENCE & MANAGEMENT)',
    1253299: 'BACHELOR OF SCIENCE (ENTREPRENEURSHIP STUDIES)',
    1253324: 'BACHELOR OF ARTS (KISWAHILI)',
    1253326: 'BACHELOR OF EDUCATION (GUIDANCE AND COUNSELLING)',
    1253327: 'BACHELOR OF SCIENCE (PROJECT PLANNING AND MANAGEMENT)',
    1253331: 'BACHELOR OF EDUCATION (TECHNOLOGY EDUCATION)',
    1253337: 'BACHELOR OF SCIENCE (COUNSELLING PSYCHOLOGY)',
    1253415: 'BACHELOR OF SCIENCE (AGRICULTURAL EXTENSION EDUCATION)',
    1253418: 'BACHELOR OF SCIENCE WITH EDUCATION',
    1253428: 'BACHELOR OF SCIENCE (INFORMATICS)',
    1253435: 'BACHELOR OF SPORTS MANAGEMENT',
    1253450: 'BACHELOR OF SCIENCE (COMMUNICATION AND PUBLIC RELATIONS)',
    1253490: 'BACHELOR OF BUSINESS MANAGEMENT (CIVIL AVIATION MANAGEMENT)',
    1253491: 'BACHELOR OF SCIENCE (GRAPHIC, COMMUNICATION AND ADVERTISING)',
    1253492: 'BACHELOR OF SCIENCE (MEDIA SCIENCE)',
    1253493: 'BACHELOR OF SCIENCE (STRATEGIC MANAGEMENT)',
    1253494: 'BACHELOR OF EDUCATION (ARTS - BUSINESS STUDIES)',
    1253495: 'BACHELOR OF SCIENCE (MEDICAL PSYCHOLOGY)',
    1253496: 'BACHELOR OF BUSINESS MANAGEMENT (MARINE BUSINESS MANAGEMENT)',
    1253561: 'BACHELOR OF SCIENCE (PHYSICAL THERAPY)',
    1253594: 'BACHELOR OF SCIENCE (AGRICULTURAL BIOTECHNOLOGY)',
    1253598: 'BACHELOR OF ARTS (PENOLOGY, CORRECTION AND ADMINISTRATION)',
    1253599: 'BACHELOR OF ENGINEERING (CHEMICAL AND PROCESS ENGINEERING)',
    1253600: 'BACHELOR OF ENGINEERING (MANUFACTURING, INDUSTRIAL AND TEXTILE ENGINEERING)',
    1253616: 'BACHELOR OF ENGINEERING (CIVIL AND STRUCTURAL ENGINEERING)',
    1253617: 'BACHELOR OF ENGINEERING (ELECTRICAL AND ELECTRONICS ENGINEERING)',
    1253621: 'BACHELOR OF ARTS (LINGUISTICS, MEDIA AND COMMUNICATION)',
    1253646: 'BACHELOR OF ARTS (ECONOMICS)',
    1253656: 'BACHELOR OF EDUCATION (SPECIAL NEEDS EDUCATION - SECONDARY OPTION)',
    1253697: 'BACHELOR OF ENGINEERING (ELECTRICAL AND TELECOMMUNICATION ENGINEERING)',
    1253718: 'BACHELOR OF ENGINEERING (MECHANICAL AND PRODUCTION ENGINEERING)'
}

existing_program_codes = df['Programme Code'].unique()
filtered_program_names = [program_code_to_name[code] for code in existing_program_codes if code in program_code_to_name]

# Dropdown for selecting program name
selected_program_name = st.selectbox("Select Program", filtered_program_names)

# Map selected program name to program code
program_code_input = [code for code, name in program_code_to_name.items() if name == selected_program_name]

# Check if program code is found
if len(program_code_input) > 0:
	program_code_input = program_code_input[0]

# Dropdown for selecting year
year_input = st.selectbox("Select Year", list(range(2015, 2028)))
if st.button("Execute"):
	print(program_code_input)
	X = df[['Year', 'Programme Code']]
	y_total_placed = df['Total Placed']

	encoder = OneHotEncoder(sparse=False)
	program_code_encoded = encoder.fit_transform(X[['Programme Code']])

	X_encoded = pd.concat([X[['Year']], pd.DataFrame(program_code_encoded, columns=encoder.get_feature_names_out(['Programme Code']))], axis=1)
	X_train, X_test, y_total_placed_train, y_total_placed_test = train_test_split(X_encoded, y_total_placed, test_size=0.2, random_state=42, shuffle=True)

	# Choose Linear Regression
	model_total_placed = LinearRegression()
	model_total_placed.fit(X_train, y_total_placed_train)

	# Make Predictions for the selected year and program code
	input_program_code_encoded = encoder.transform([[program_code_input]])
	input_data_with_year = [[year_input] + input_program_code_encoded[0].tolist()]

	predicted_total_placed = int(model_total_placed.predict(input_data_with_year)[0])

	# Display the prediction
	st.write(f"Predicted Total Placed: {predicted_total_placed}")
