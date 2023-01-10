from SensorABC import SensorABC


class Temperature(SensorABC):

    sensor_type = "temperature"
    config = {
        "very_high": 30,
        "high": 27,
        "low": 12,
        "very_low": 10,
        "offset": 0
    }

    def test_get_sensor_data(self, db, dbd):
        self.value = self.get_real(self.client.db_read(int(db), dbd, 4))
        return self.value

    def get_sensor_data(self):
        self.value = self.get_real(self.client.db_read(int(self.db_id), 52, 4))
        self.alarm = self.get_int(self.client.db_read(int(self.db_id), 60, 2))
        return self.send_response_data()

    def get_sensor_config(self):
        self.config["very_high"] = int(self.get_real(self.client.db_read(self.db_id, 4, 4)))
        self.config["high"] = int(self.get_real(self.client.db_read(self.db_id, 8, 4)))
        self.config["low"] = int(self.get_real(self.client.db_read(self.db_id, 12, 4)))
        self.config["very_low"] = int(self.get_real(self.client.db_read(self.db_id, 16, 4)))
        self.config["offset"] = int(self.get_real(self.client.db_read(self.db_id, 24, 4)))
        return self.config

    def set_sensor_data(self):
        self.client.db_write(int(self.db_id), 4, self.set_real(int(self.config['very_high'])))
        self.client.db_write(int(self.db_id), 8, self.set_real(int(self.config['high'])))
        self.client.db_write(int(self.db_id), 12, self.set_real(int(self.config['low'])))
        self.client.db_write(int(self.db_id), 16, self.set_real(int(self.config['very_low'])))
        self.client.db_write(int(self.db_id), 24, self.set_real(int(self.config['offset'])))
        return self.config