from onvif import ONVIFCamera


# Replace these values with your DVR's information
ip = '192.168.1.161'
port = 80  # Default ONVIF port is 80
username = 'admin'
password = 'a111111'

mycam = ONVIFCamera(ip, port, username, password)

print(mycam)