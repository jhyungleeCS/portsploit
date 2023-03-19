# PortSploit

**PortSploit** is a web application that allows users to recieve information about a network's vulnerabilities including open ports in a network. 
Ports are endpoints used for communication in a network that allows data to be sent and recieved. 

Open ports are a risk to a network because this gives a potential access point for attackers to gain unauthorized access. 
Having open ports on a network can leave attackers to deploy an array of attacks including Port/Packet sniffing, a DoS (Denial of Service) attack, 
and even exploiting known vulnerabilities that the port has. 

This application will allow you to see which ports are open in a organization as well as any known vulnerabilities that are currently 
associated with that port. The web application is pulling in information from the following websites: 

shodan.io </br>
speedguide.net </br>

How to run in your local machine: 

- Run the file in command line to open up a connection with python3 flask_shodan.py
- Copy any address that the connection is running on
