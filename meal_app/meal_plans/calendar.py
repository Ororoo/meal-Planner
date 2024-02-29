from flask import Blueprint, render_template
import mysql.connector
import random

calendar = Blueprint('calendar', __name__, template_folder='templates')


def get_random_vegan_meal():
    mydb = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="rootPass",
        database="MealPlan"
    )

    try:
        cursor = mydb.cursor()

        # Get the total number of vegan meals
        cursor.execute("SELECT COUNT(*) FROM all_diets WHERE Diet_type = 'vegan'")
        total_vegan_meals = cursor.fetchone()[0]

        if total_vegan_meals == 0:
            return None
        
        random_index = random.randint(1, total_vegan_meals)

        cursor.execute("SELECT Recipe_name FROM all_diets WHERE Diet_type = 'vegan' LIMIT %s, 1", (random_index,))
        random_vegan_meal = cursor.fetchone()

        return random_vegan_meal[0]

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

    finally:
        if cursor:
            cursor.close()
        if mydb.is_connected():
            mydb.close()

@calendar.route('/', methods=['GET', 'POST'])
def show_calendar():
    # Get random vegan meals for each day
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    meals = {day.lower() + '_meal': get_random_vegan_meal() for day in days}

    return render_template('calendar.html', meals=meals)
