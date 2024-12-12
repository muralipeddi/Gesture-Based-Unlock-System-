import serial

def read_serial_data(port, baud_rate, num_data_points):
    """
    Reads data from a serial port.

    Args:
        port (str): The serial port to read from.
        baud_rate (int): The baud rate for the serial communication.
        num_data_points (int): The number of data points to read.

    Returns:
        list: A list of lists containing the read data points.
    """
    ser = serial.Serial(port, baud_rate)
    data = []

    try:
        while len(data) < num_data_points:
            line = ser.readline().decode('utf-8').strip()
            if line:
                values = [float(x) for x in line.split(',')]
                data.append(values)
    finally:
        ser.close()

    return data

def save_data_to_file(data, file_path):
    """
    Saves data to a file.

    Args:
        data (list): The data to save.
        file_path (str): The path to the file where data will be saved.
    """
    with open(file_path, 'w') as f:
        for entry in data:
            f.write("{}, {}, {}\n".format(entry[0], entry[1], entry[2]))

def main():
    port = 'COM4'  # Replace with the appropriate serial port name for your system
    baud_rate = 9600
    num_data_points = 100  # Replace with the desired number of data points
    output_file = 'output.txt'

    data = read_serial_data(port, baud_rate, num_data_points)
    save_data_to_file(data, output_file)

if __name__ == "__main__":
    main()
