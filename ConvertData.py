import struct


class ConvertData():

    def get_real(self, _bytearray):
        x = _bytearray[0:4]
        real = struct.unpack('>f', struct.pack('4B', *x))[0]
        real = round(real, 2)
        return real

    def set_real(self, real):
        byarray = bytearray('FFFF', 'utf-8')
        real = float(real)
        real = struct.pack('>f', real)
        _bytes = struct.unpack('4B', real)
        for i, b in enumerate(_bytes):
            byarray[i] = b
        return byarray

    def set_dword(self, dword):
        _bytearray = bytearray('FFFF', 'utf-8')
        dword = int(dword)
        _bytes = struct.unpack('4B', struct.pack('>I', dword))
        for i, b in enumerate(_bytes):
            _bytearray[i] = b
        return _bytearray

    def get_dword(self, _bytearray):
        x = _bytearray[0:4]
        real = struct.unpack('>I', struct.pack('4B', *x))[0]
        real = round(real, 2)
        return real

    def set_bool(self, _bytearray, byte_index, bool_index, value):
        assert value in [0, 1, True, False]
        current_value = self.get_bool(_bytearray, byte_index, bool_index)
        index_value = 1 << bool_index
        if current_value == value:
            return
        if value:
            _bytearray[byte_index] += index_value
        else:
            _bytearray[byte_index] -= index_value

    def get_int(self, _bytearray):
        value = int.from_bytes(_bytearray, byteorder='big', signed=False)
        return value

    def get_int_signed(self, _bytearray):
        value = int.from_bytes(_bytearray, byteorder='big', signed=True)
        return value

    def get_bool(self, _bytearray, byte_index=0, bool_index=0):
        index_value = 1 << bool_index
        byte_value = _bytearray[byte_index]
        current_value = byte_value & index_value
        return current_value == index_value

    def bool_write_to(self, client, dbn, by_start, bi_start, bol):
        byte_arr = client.db_read(dbn, by_start, 1)
        self.set_bool(byte_arr, 0, bi_start, bol)
        return client.db_write(dbn, by_start, byte_arr)

    def set_int(self, _int):
        byarray = bytearray('F', 'utf-8')
        _int = int(_int)
        _bytes = bytes([_int])
        byarray[0:1] = _bytes
        return byarray

    def set_word(self, i: int, *, signed: bool = True) -> bytes:
        return i.to_bytes(2, byteorder='big')