# smartexecutorlib

Smart command executor.

---

[![GitHub release (latest by date)](https://img.shields.io/github/v/release/smartlegionlab/smartexecutorlib)](https://github.com/smartlegionlab/smartexecutorlib/)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/smartexecutorlib?label=pypi%20downloads)](https://pypi.org/project/smartexecutorlib/)
![GitHub top language](https://img.shields.io/github/languages/top/smartlegionlab/smartexecutorlib)
[![PyPI](https://img.shields.io/pypi/v/smartexecutorlib)](https://pypi.org/project/smartexecutorlib)
[![GitHub](https://img.shields.io/github/license/smartlegionlab/smartexecutorlib)](https://github.com/smartlegionlab/smartexecutorlib/blob/master/LICENSE)
[![PyPI - Format](https://img.shields.io/pypi/format/smartexecutorlib)](https://pypi.org/project/smartexecutorlib)

***

Author and developer: ___A.A. Suvorov.___

***

## Help:

`pip install smartexecutorlib`

```python
from smartexecutorlib.executors import SmartExecutor

smart_executor = SmartExecutor()

smart_executor.os.execute('pip list')
smart_executor.sub.execute('pip list')

```

***

## Disclaimer of liability:

    THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
    AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
    IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
    DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
    FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
    DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
    SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
    CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
    OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
    OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

***

## Copyright:
    --------------------------------------------------------
    Licensed under the terms of the BSD 3-Clause License
    (see LICENSE for details).
    Copyright © 2018-2024, A.A. Suvorov
    All rights reserved.
    --------------------------------------------------------
