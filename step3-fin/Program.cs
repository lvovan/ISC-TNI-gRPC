using System;
using System.Net.Http;
using System.Threading.Tasks;
using Grpc.Net.Client;

namespace Calc
{
    class Program
    {
        static void  Main(string[] args)
        {
            var x = int.Parse(args[0]);
            var y = int.Parse(args[1]);

            // Création du client (nous devons accepter )
            AppContext.SetSwitch("System.Net.Http.SocketsHttpHandler.Http2UnencryptedSupport", true);
            using var channel = GrpcChannel.ForAddress("http://localhost:50051");
            var client =  new Calc.CalcClient(channel);

            // Appels au serveur
            var replyAdd = client.Add(new ArithmeticRequest { A = x, B = y });
            var replyMultiply = client.Multiply(new ArithmeticRequest { A = x, B = y });
            
            // Affichage des résultats
            Console.WriteLine($"Client .NET pour Calc");
            Console.WriteLine($"{x} + {y} = {replyAdd.Result}");
            Console.WriteLine($"{x} * {y} = {replyMultiply.Result}");
        }
    }
}