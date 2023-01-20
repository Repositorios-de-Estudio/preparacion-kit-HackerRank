using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FindTheMedian
{
    internal class Program
    {
        static void Main(string[] args)
        {
        }

        /*
         * Complete the 'findMedian' function below.
         *
         * The function is expected to return an INTEGER.
         * The function accepts INTEGER_ARRAY arr as parameter.
         */

        public static int findMedian(List<int> lista)
        {
            lista.Sort();

            int mediana = (lista.Count - 1) / 2;

            return lista[mediana];

        }
    }
}
