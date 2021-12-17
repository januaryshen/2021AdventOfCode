import numpy as np


class BITS:
    def __init__(self, hex_string):
        self.hex_string = hex_string
        self.hex_size = len(self.hex_string) * 4
        self.binary_string = bin(int(hex_string, 16))[2:].zfill(self.hex_size)
        self.version_sum = 0
        self.literal_value = 0
        self.subpacket_defined_bit = []
        self.subpacket_current_bit = 0
        self.typeID = 0
        self.literal_value_subpacket = []
        self.ultimate_sum = 0
        self.count_bit_mode_on = 0

    def add_subpacket_bit(self, value):
        if self.count_bit_mode_on == 1:
            self.subpacket_current_bit += value

    def get_literal_value(self, binary_string):
        max_group = len(binary_string) // 5
        value = ""
        for i in range(max_group):
            target = binary_string[i*5: (i+1)*5]
            value = value + target[1:]
            if target[0] == "0":
                self.literal_value += int(value, 2)
                self.literal_value_subpacket.append(int(value, 2))
                self.binary_string = binary_string[(i+1)*5:]
                self.get_version_and_type(self.binary_string)
                self.add_subpacket_bit((i + 1) * 5)
                break

    def get_version_decimal(self, binary_string):
        self.version_sum += int(binary_string, 2)

    def num_of_packet_mode(self, binary_string):
        # next 11 bits contains the number of packet
        num_of_packet = int(binary_string[0: 11], 2)
        self.binary_string = binary_string[11:]
        self.add_subpacket_bit(7+11)
        for i in range(num_of_packet):
            self.get_version_and_type(self.binary_string)

    def length_in_bit_mode(self, binary_string):
        # next 15 bits contains the bit usage of subpacket
        self.subpacket_defined_bit.append(int(binary_string[0: 15], 2))
        self.binary_string = binary_string[15:]
        self.add_subpacket_bit(7+15)
        self.count_bit_mode_on = 1
        while self.subpacket_current_bit < self.subpacket_defined_bit[-1]:
            self.get_version_and_type(self.binary_string)
        self.subpacket_defined_bit.pop()
        self.count_bit_mode_on = 0

    def part_2_count(self):
        if self.literal_value_subpacket:
            if self.typeID == 0 or self.typeID == 4:
                self.ultimate_sum += np.sum(self.literal_value_subpacket)
            elif self.typeID == 1:
                if len(self.literal_value_subpacket) == 1:
                    self.ultimate_sum += np.sum(self.literal_value_subpacket)
                else:
                    self.ultimate_sum += np.prod(self.literal_value_subpacket)
            elif self.typeID == 2:
                self.ultimate_sum += np.min(self.literal_value_subpacket)
            elif self.typeID == 3:
                self.ultimate_sum += np.max(self.literal_value_subpacket)
            elif self.typeID == 5:
                self.ultimate_sum += 1 if self.literal_value_subpacket[0] > self.literal_value_subpacket[1] else 0
            elif self.typeID == 6:
                self.ultimate_sum += 1 if self.literal_value_subpacket[0] < self.literal_value_subpacket[1] else 0
            elif self.typeID == 7:
                self.ultimate_sum += 1 if self.literal_value_subpacket[0] == self.literal_value_subpacket[1] else 0
        self.literal_value_subpacket = []

    def get_version_and_type(self, binary_string):
        self.part_2_count()
        if len(self.binary_string) >= 11:
            self.get_version_decimal(binary_string[0:3])
            self.typeID = int(binary_string[3:6], 2)
            if self.typeID == 4:
                self.add_subpacket_bit(6)
                self.get_literal_value(binary_string[6:])
            else:  # operator mode
                if binary_string[6] == '1':
                    self.num_of_packet_mode(binary_string[7:])
                else:
                    self.length_in_bit_mode(binary_string[7:])


def part1(inputData):
    packet = BITS(open(inputData, 'r').read().rstrip())
    packet.get_version_and_type(packet.binary_string)
    print("literal value: ", packet.literal_value)
    print("version sum: ", packet.version_sum)


def part2(inputData):
    packet = BITS(open(inputData, 'r').read().rstrip())
    packet.get_version_and_type(packet.binary_string)
    print("literal value: ", packet.literal_value)
    print("version sum: ", packet.version_sum)
    print("ultimate sum: ", packet.ultimate_sum)


if __name__ == "__main__":
    input_data = "./data.txt"
    # part1(input_data)
    part2(input_data)

    # source: Zealousideal-Pen9091 from https://www.reddit.com/r/adventofcode/comments/rgqzt5/2021_day_15_solutions/
