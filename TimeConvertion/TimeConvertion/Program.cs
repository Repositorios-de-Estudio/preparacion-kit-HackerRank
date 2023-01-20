using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using static System.Net.Mime.MediaTypeNames;

namespace TimeConvertion
{
    internal class Program
    {
        static void Main(string[] args)
        {

            string resultado1 = "12:01:00PM";
            string resultado2 = "12:01:45AM";
            string resultado3 = "07:05:45PM";
            string resultado4 = "07:15:45AM";

            Console.WriteLine(timeConversion(resultado1));
            Console.WriteLine(timeConversion(resultado2));
            Console.WriteLine(timeConversion(resultado3));
            Console.WriteLine(timeConversion(resultado4));
        }


        /*
         * Complete the 'timeConversion' function below.
         *
         * The function is expected to return a STRING.
         * The function accepts STRING s as parameter.
         */

        public static string timeConversion(string sss)
        {
            StringBuilder cadena = new StringBuilder(sss);

            string tiempo = "";

            tiempo = cadena[cadena.Length - 2] + "" +cadena[cadena.Length - 1];

            cadena.Remove(cadena.Length - 2, 2);

            string num = cadena[0] + "" + cadena[1];
            cadena.Remove(0, 2);

            if (tiempo.Equals("AM") && num.Equals("12"))
            {
                cadena.Insert(0,"00");
            }
            else if (tiempo.Equals("PM") &&  num.Equals("12"))
            {
                cadena.Insert(0, "12");
            }
            else if (tiempo.Equals("PM"))
            {
                cadena.Insert(0, Convert.ToInt32(num) + 12);
            }
            else
            {
                cadena.Insert(0, num);
            }


            return cadena.ToString();
        }

    }
}
