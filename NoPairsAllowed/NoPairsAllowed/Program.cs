using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace NoPairsAllowed
{

    internal class Program
    {
        static void Main(string[] args)
        {

            List<string> sss = new List<string>() { "add", "boook", "break" };

            List<int> aaa = minimalOperations(sss);

            foreach (var item in aaa)
            {
                Console.WriteLine(item);
            }

        }

        public static List<int> minimalOperations(List<string> sss)
        {
            List<int> contt = new List<int>();
            int temp = 0;

            foreach (string word in sss)
            {
                StringBuilder cadena = new StringBuilder(word);

                for (int i = 0; i < cadena.Length - 1; i++)
                {
                    if (cadena[i] == cadena[i + 1])
                    {
                        cadena.Remove(i,i + 1);
                        cadena.Append('!',i+1);
                        temp++;
                        break;
                    }
                }

                contt.Add(temp);

            }

            return contt;


        }
    }
}
