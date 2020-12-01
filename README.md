# What is this image?

This image is a SteamCMD based image setup to download and install an Arma 3 Dedicated Server instance. At this present moment in time, the 'out of the box' features for this image limited but will be worked on. Everytime the container is restarted SteamCMD and the Arma 3 Dedicated Server software is updated, so you will be never out of date even if the image is not updated.

# BEFORE YOU BEGIN
Before you create an container with this image, you will need to have a valid steam account and password with SteamGuard turned off. This is required so your server can contect to Steam servers! I would recommend creating another Steam account for the server, as the account does not need to own the game. 

# How to use this image
To use this image, you can use the template below. 
```console
 docker create \
        --name=Arma3Dedicated \
        -p 2302:2302/udp \
        -p 2303:2303/udp \
        -p 2304:2304/udp \
        -p 2305:2305/udp \
		-p 2306:2306/udp \
        -e STEAM_USER=annoymous \
        -e STEAM_PASSWORD=annoymous \
        themrpuffin/arma3-dedicated
```
You are required to change some lines in this to tailor for your needs. Please change the container name and ensure you have provided valid Steam credentials.

# Required ports
Incoming ports:
| Port     | Description | 
|----------|-------------|
| UDP 2301 | Arma3 rcon port                   |   
| UDP 2302 | Arma3 game port + voice over net  |   
| UDP 2303 | 	Steam query port               |  
| UDP 2304 | Steam port                        |  
| UDP 2305 |                                   |  
| UDP 2306 | BattlEye port                     |  

Outgoing ports:

| Port     | Description | 
|----------|-------------|
| TCP 2345 | BattlEye port        |   
| UDP 2302 | Client traffic       |   
| UDP 2303 | Steam query port     |  
| UDP 2304 | Steam master traffic |  

# Environment Variables

| Variable     | Function | 
|----------|-------------|
| STEAM_USER | Steam account login (required) |   
| STEAM_PASSWORD | Steam password (required)  |   

# Dedicated Server Configurations 
Within the container at location; "/home/steam/Arma3Dedicated/Configs" you will find 'server.cfg', you can edit this before you run the server to change settings for the Arma 3 Server itself. This has very basic configuration which you should edit and add to. 

You should navigate to the volume for the container to make changes to this before you run the container. 

# Planned features
As this image has just been developed, I have many thing I would like to add some of these feature are;
    - Automatic headless client startup
    - Automatic mod detection

This readme is maintained by TheMrPuffin; version 1.0