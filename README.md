# ISC-TNI Travaux Pratiques Remoting multiplateforme avec gRPC

## Objectif du TP
Lors de cette séance de travaux pratiques nous allons explorer gRPC et Protocol Buffers (*protobuf*) pour implémenter des services 

## Pré-requis
Ce TP requiert un certain nombre de prérequis techniques sur votre machine:
  - Python 3.x
  - Créez un [environnement virtuel](https://docs.python.org/3/tutorial/venv.html)
  - Installer le module Python **grpcio-tools** avec `pip install grpcio-tools`
  - [.NET Core 3.1](https://dotnet.microsoft.com/download/dotnet-core)

## Step 1. Exécution de l'exemple de démarrage
Regardez le contenu du fichier **protos/calc.proto** qui spécifie l'interface dans l'IDL gRPC et notez qu'il ne définit qu'une seule procédure, **Add** qui:
  - Prend en entrée un message **AddRequest** (deux entiers **a** et **b**),
  - Renvoie un message de type **AddResponse** (un entier, **result**).

Exécutons maintenant cet exemple:
  1. Allez dans le dossier `step1`
  2. Dans un premier terminal, lancez le serveur avec la commande `python calc_server.py`
  3. Dans un second terminal, lancez le client en lui passant en paramètre deux nombres entiers `python calc_client.py 20 22`
  4. Vous observerez que le serveur a répondu à la requête en renvoyons le résultat de l'addition

Sous Linux, vous pouvez également "regarder" le contenu du message tel qu'il est envoyé sur le réseau en coupant le serveur (CTRL+C) puis en exécutant `nc -l localhost 50051` (qui lancera une écoute sur le port **localhost:50051**) puis en relançant le client.

## Step 2. Modification du .proto et mise à jour du serveur et du client
Modifiez maintenant le fichier **protos/calc.proto** afin d'y ajouter une procédure **Multiply**:
  - Ajoutez la procédure **rpc** adéquate
  - Trouvez une manière élégante de déclarer les types de message qui seront utilisés dans votre serveur
  - Générez les fichiers Python liés à ce nouveau .proto, ce qui écrasera les fichiers générés avec la version originale: `python -m grpc_tools.protoc -I./protos --python_out=. --grpc_python_out=. ./protos/calc.proto`

  - Implémenter la nouvelle procédure dans une fonction dédiée de **calc_server.py**
  - Modifier le client **calc_client.py** afin qu'il appelle **Add** et **Multiply**, avec les mêmes paramètres d'entrée
  - Testez votre implémentation

## Step 3. Création d'un client dans un autre langage (.NET Core)
Comme vu en cours, l'intérêt majeur des IDL tels que le permet gRPC via Protobuf est la capacité de rendre interopérables des technologies différentes. Dans ce dernier exercice nous allons conserver notre serveur, mais allons l'appeler depuis un client écrit en .NET et plutôt qu'en Python.

  1. Depuis le dossier **step3**
  2. Créez un nouveau programme console avec la commande `dotnet new console`
  3. Ajoutez les dépendances gRPC:

          dotnet add package Grpc.Net.Client
          dotnet add package Google.Protobuf
          dotnet add package Grpc.Tools`

  4. Ajoutez les lignes suivantes au fichier **step3.csproj** comme enfant de la section `<project>`, qui permettent de référencer le fichier .proto dans le projet .NET, qui génèrera automatiquement l'implémentation nécessaire

          <ItemGroup>
              <Protobuf Include="protos\calc.proto" GrpcServices="Client" />
          </ItemGroup>

  5. Remplacez le contenu de votre fichier **Program.cs** par [celui-ci](step3/Program_reference.cs). Si nécessaire, modifiez les noms de type pour correspondre à ceux de votre fichier .proto.
  Notez que la casse des noms des objets et de leurs propriétés ont été ajustés aux nommages standards de .NET (majuscules)
  6. Lancez le serveur de step 2 dans un nouveau terminal
  7. Compilez le programme: `dotnet build`
  8. Exécutez le client tout juste compilé: `bin/Debug/netcoreapp3.1/step3 20 22`
  
Vous pouvez maintenant observer que grâce à l'utilisation d'un IDL, le fichier .proto est suffisant pour que votre code .NET communique parfaitement avec votre code serveur en Python. Si nécessaire, la solution complète est disponible dans le dossier [step3-fin](step3-fin).
