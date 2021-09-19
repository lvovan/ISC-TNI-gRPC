# ISC-TNI Travaux Pratiques Remoting multiplateforme avec gRPC

## Objectif du TP
Lors de cette séance de travaux pratiques nous allons explorer gRPC et Protocol Buffers (*protobuf*) pour implémenter des services 

## Pré-requis
1. Installer
    - Python 3.x
    - Créez un [environnement virtuel](https://docs.python.org/3/tutorial/venv.html)
    - Installer le module Python **grpcio-tools**
      `pip install grpcio-tools`
    - [.NET Core 3.1](https://dotnet.microsoft.com/download/dotnet-core)

## Step 1. Exécution de l'exemple de démarrage

Un fichier de définition *protobuf* (.proto) définissant l'interface est disponible dans le dossier **step1/calc.proto**.

Regardez son contenu et notez qu'il ne définit qu'une seule procédure, **Add** qui:
  - Prend en entrée un message **AddRequest** (deux entiers **a** et **b**),
  - et renvoie un message de type **AddResponse** (un entier, **result**).

Exécutons maintenant cet exemple:
  - Ouvrez deux terminaux
  - Dans le premier terminal, lancez le serveur
  
  `python3 calc_server.py`
  - Dans le second terminal lancez le client en lui passant en paramètre deux nombres entiers
  
  `python3 calc_client.py 20 22`

Sous Linux, vous pouvez également "regarder" le contenu du message envoyé en coupant le serveur (CTRL+C), en exécutant la commande ci-dessous puis en relançant le client.

`nc -l localhost 50051`

## Step 2. Modification du .proto et mise à jour du serveur et du client

Nous allons maintenant modifier le fichier .proto ce fichier pour générer automatiquement le code serveur et le code client.

 Générez le client et le serveur:

`python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/calc.proto`

## Step 3. Ajout de structure de données complexes (CalculateArea)

## Step 4. Création d'un client dans un autre langage
