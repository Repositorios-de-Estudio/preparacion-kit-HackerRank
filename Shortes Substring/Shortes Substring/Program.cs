using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Shortes_Substring
{
    internal class Program
    {

        public static int findShortestSubstring(string s)
        {
            int lonn = 0;

            Dictionary<char, int> dicc = new Dictionary<char, int>(3);

            foreach (char item in s)
            {
                if (!dicc.ContainsKey(item)) 
                {
                    dicc.Add(item, 1);
                    
                }
                else
                {
                    lonn++;
                }
            }

            return lonn;
        }
        static void Main(string[] args)
        {
            string cadena = "abcbbbk";
            Console.WriteLine(findShortestSubstring(cadena));
        }
    }
}
