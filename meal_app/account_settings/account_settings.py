from flask import Blueprint, render_template, request, jsonify
import mysql.connector

account_settings = Blueprint('account settings', __name__, template_folder='templates')

mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="rootPass",
    database="MealPlan"
)

@account_settings.route('/', methods=['GET', 'POST'])
def show_accountSettings():  
    return render_template('account_settings.html')


@account_settings.route('/save_personal_info', methods=['POST'])
def save_personal_info():
    if request.method == 'POST':
        age = request.form.get('ageRange')
        gender = request.form.get('gender')
        save_personal_info_to_db(age, gender)
        return jsonify({'status': 'success', 'message': 'Personal information saved successfully'})
    return jsonify({'status': 'error', 'message': 'Invalid request method'})


@account_settings.route('/save_health_info', methods=['POST'])
def save_health_info():
    if request.method == 'POST':
        currentWeight = request.form.get('currentWeight')
        goalWeight = request.form.get('goalWeight')
        height = request.form.get('height')
        mainGoal = request.form.get('mainGoal')
        save_health_info_to_db(currentWeight, goalWeight, height, mainGoal)
        return jsonify({'status': 'success', 'message': 'Health information saved successfully'})
    return jsonify({'status': 'error', 'message': 'Invalid request method'})


@account_settings.route('/save_diet_preferences', methods=['POST'])
def save_diet_preferences():
    if request.method == 'POST':
        diet_preferences = request.form.getlist('dietPreferences')
        save_diet_preferences_to_db(diet_preferences)
        return jsonify({'status': 'success', 'message': 'Diet preferences saved successfully'})
    return jsonify({'status': 'error', 'message': 'Invalid request method'})


def save_personal_info_to_db(age, gender):
    try:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO users (age_range, gender) VALUES (%s, %s)", (age, gender))
        mydb.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def save_health_info_to_db(currentWeight, goalWeight, height, mainGoal):
    try:
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO user_health_info (currentWeight, goalWeight, height, mainGoal) VALUES (%s, %s, %s, %s)",
                       (currentWeight, goalWeight, height, mainGoal))
        mydb.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False


def save_diet_preferences_to_db(diet_preferences):
    try:
        cursor = mydb.cursor()
        for preference in diet_preferences:
            cursor.execute("INSERT INTO user_diet_preferences (diet_preference) VALUES (%s)", (preference,))
        mydb.commit()
        cursor.close()
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False
