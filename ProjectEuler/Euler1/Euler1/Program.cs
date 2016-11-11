using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Euler1
{
    class Program
    {
        static int Main(string[] args)
        {
            int countTo = 0;
            if(args.Length != 1 || !int.TryParse(args[0], out countTo) || countTo < 1)
            {
                Console.WriteLine("Usage: {0} <positive int>", System.Diagnostics.Process.GetCurrentProcess().ProcessName);
                return -1;
            }

            var sum = 0;
            var count = 0;

            var mod3 = new ModEnumerable(3);
            var mod5 = new ModEnumerable(5);

            var result = mod3.Zip(mod5, (m3, m5) =>
            {
                count++;
                if(m3 == 0 || m5 == 0)
                {
                    sum += count;
                }
                return sum;
            }).Skip(countTo - 1).First();

            Console.WriteLine(result);

            return 0;
        }
    }
}
