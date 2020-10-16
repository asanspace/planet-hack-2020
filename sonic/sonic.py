from pythonosc import udp_client

client = udp_client.SimpleUDPClient("127.0.0.1", 4559) # port Sonic Pi is listening on
client.send_message("/trigger/prophet", [35,30,33,32,29,31,29,28,27,28,25,23,24,26,23,22,21,20,18,21,19,18,15,13,12,9,11,10,9,9,8,10,7,4,6,5,4,3,3,2,4,1,0])
