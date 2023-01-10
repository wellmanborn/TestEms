import snap7
import logging

from config import DEVICE_ADDRESS

logger = logging.getLogger('django')

class SingletonMeta(type):
    """
    The Singleton class can be implemented in different ways in Python. Some
    possible methods include: base class, decorator, metaclass. We will use the
    metaclass because it is best suited for this purpose.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Possible changes to the value of the `__init__` argument do not affect
        the returned instance.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class Device(metaclass=SingletonMeta):
    client = False
    status = ""

    def connect_to_plc(self):
        attempts = 0
        while attempts < 3:
            try:
                logger.info("connecting to DEVICE")
                self.client = snap7.client.Client()
                self.client.connect(DEVICE_ADDRESS, 0, 1)
                logger.info("DEVICE connected")
                return self.client
            except Exception as e:
                self.client = False
                logger.error("Device is not connected, please be sure the device is ready and accessible")
                logger.error(e.__str__())
                print("Device is not connected, please be sure the device is ready and accessible")
                attempts += 1
        return self.client

    def get_client(self):
        if self.client:
            return self.client
        else:
            return self.connect_to_plc()

    def refresh_client(self):
        return self.connect_to_plc()

    def get_status(self):
        return self.status

    def set_status(self, status):
        self.status = status
        pass
