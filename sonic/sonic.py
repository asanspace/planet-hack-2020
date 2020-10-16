from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 4559) # port Sonic Pi is listening on
client.send_message("/trigger/prophet", [1,3,5,8,10,12,15,17,19,22])
