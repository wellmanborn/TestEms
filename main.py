from Temperature import Temperature
from config import TEMPERATURE_DB, TEMPERATURE_DBD

if __name__ == '__main__':
    print(Temperature().test_get_sensor_data(TEMPERATURE_DB,TEMPERATURE_DBD))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
