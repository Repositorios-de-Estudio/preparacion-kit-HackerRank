using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace MiniMaxSum
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> lista = new List<int>() { 5,9,15,1,0};

            miniMaxSum(lista);
        }

        /*
        * Complete the 'miniMaxSum' function below.
        *
        * The function accepts INTEGER_ARRAY arr as parameter.
        */

        public static void miniMaxSum(List<int> lista)
        {
            lista.Sort();
            
            long sMin = lista[0] + lista[1] + lista[2] + lista[3];
            long sMax = lista[1] + lista[2] + lista[3] + lista[4];

            //StringBuilder mensaje = new StringBuilder(sMin.ToString() + " " + sMax.ToString());

            Console.WriteLine($"{sMin} {sMax}");

        }
    }




}
