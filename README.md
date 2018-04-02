# EHR-Hyperledger-2018

In order to run the project do the following steps:

1. I assume you have installed Hyperledger fabric and it is running or use ./startFabric.sh to run it

2. You must have composer-cli to run it therefore install it as:
npm install -g compoer-cli

3. Then run this three commands inside the storage-network directory
composer runtime install --c PeerAdmin@hlfv1 --n storage-network
composer network start --a storage-network@0.01.bna --c PeerAdmin@hlfv1 --A admin --S adminpw --f networkadmin.card
composer card import --f networkadmin.card
-------------------In order to check it is working----------
composer network ping --c admin@storage-network

4. Now that we have our hyperledger ready lets create the composer rest API by running:
composer-rest-server
You should see the API ready at localhost/3000

5. To wo run our web application which is a python flask web app, run:
python app.py
If it shows errors it means you have to install the python requirements by doing this
pip install flask requests

