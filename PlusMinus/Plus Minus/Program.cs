using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Plus_Minus
{
    internal class Program
    {
        static void Main(string[] args)
        {
            List<int> lista = new List<int>() { 1, 1, 0, -1, -1 };

            plusMinus(lista);
            
        }

        /*
         * Complete the 'plusMinus' function below.
         *
         * The function accepts INTEGER_ARRAY arr as parameter.
         */

        //positivos / n, negativos/n, ceros/n
        public static void plusMinus(List<int> lista)
        {
            decimal rPos = 0.000000m;
            decimal rNeg = 0.000000m;
            decimal rCer = 0.000000m;

            decimal tamano = lista.Count;

            decimal nPos = 0;
            decimal nNeg = 0;
            decimal nCer = 0;

            foreach (int item in lista)
            {
                if (item > 0) { nPos++; }
                else if (item < 0) { nNeg++; }
                else { nCer++; }
            }

            rPos = nPos / tamano;
            rNeg = nNeg / tamano;
            rCer = nCer / tamano;

            Console.WriteLine(string.Format("{0:0.000000}",rPos));
            Console.WriteLine(string.Format("{0:0.000000}", rNeg));
            Console.WriteLine(string.Format("{0:0.000000}", rCer));
        }

    }
}

