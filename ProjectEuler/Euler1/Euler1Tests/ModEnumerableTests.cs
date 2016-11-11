using Microsoft.VisualStudio.TestTools.UnitTesting;
using Euler1;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Euler1.Tests
{
    [TestClass()]
    public class ModEnumerableTests
    {
        [TestMethod()]
        public void ThreesTest()
        {
            var sequence = new ModEnumerable(3).Take(5).ToArray();

            int test5mod3 = sequence.Last();
            int calc5mod3 = 5 % 3;

            Assert.AreEqual(calc5mod3, test5mod3);
        }
    }
}