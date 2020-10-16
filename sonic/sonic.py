from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 4560)
client.send_message("/trigger/prophet", [0,2,4,7,9,11,14,16,18,21,23,25,28,30,32,35])
