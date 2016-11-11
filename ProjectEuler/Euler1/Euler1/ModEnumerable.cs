using System;
using System.Collections;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Euler1
{
    /// <summary>
    /// Class to give a series of values mod cycle, without having to calculate mod for each.
    /// Is it faster?  I don't know.
    /// </summary>
    public class ModEnumerable : IEnumerable<int>
    {
        private readonly int _cycle;

        public ModEnumerable(int cycle)
        {
            _cycle = cycle;
        }

        public IEnumerator<int> GetEnumerator()
        {
            return new ModEnumerator(_cycle);
        }

        IEnumerator IEnumerable.GetEnumerator()
        {
            return GetEnumerator();
        }
    }

    public class ModEnumerator : IEnumerator<int>
    {
        private readonly int _cycle;
        private int _current;
        private int _position = -1;

        public ModEnumerator(int cycle)
        {
            _cycle = cycle;
        }

        public int Current
        {
            get
            {
                if(_position < 0)
                {
                    throw new InvalidOperationException();
                }

                return _position;
            }
        }

        object IEnumerator.Current
        {
            get
            {
                return Current;
            }
        }

        public bool MoveNext()
        {
            if (_position < 0)
            {
                _position = 0; //Counting starts at 1 (this 0 will be incremented below)
            }

            _position++;

            if(_position == _cycle)
            {
                _position = 0;
            }

            return true; //Sequence is infinite
        }

        public void Reset()
        {
            _position = -1;
        }

        public void Dispose()
        {
        }
    }
}
