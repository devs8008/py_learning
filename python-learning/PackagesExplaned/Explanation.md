# Python Packages Explained

## 1. What is a Python Package?

A **package** is a directory that contains Python modules and other packages.

A module is usually a `.py` file:

```text
math_util.py
string_util.py
```

A package groups related modules together:

```text
package/
├── __init__.py
├── general.py
├── a_utils/
│   ├── __init__.py
│   └── math_util.py
└── b_utils/
    ├── __init__.py
    └── string_util.py
```

Packages help us organize large Python projects into smaller, manageable parts.

---

# 2. What is `__init__.py`?

`__init__.py` is a special Python file commonly placed inside a package.

Example:

```text
package/
├── __init__.py
├── general.py
└── a_utils/
    ├── __init__.py
    └── math_util.py
```

When a package is imported, Python can execute the code inside its `__init__.py`.

For example:

```python
# package/__init__.py

print("Importing the package")
```

If we run:

```python
import package
```

we will get:

```text
Importing the package
```

because Python executes the code in `__init__.py` when the package is imported.

---

# 3. `__init__.py` Can Control What Gets Imported

Suppose we have:

```text
package/
├── __init__.py
├── general.py
├── a_utils/
│   └── math_util.py
└── b_utils/
    └── string_util.py
```

Our `__init__.py` contains:

```python
from .a_utils.math_util import add_util
from .b_utils.string_util import String_util
from .general import general_util

print("Importing the package")
```

Now the package imports these objects when it is imported.

Instead of:

```python
from package.a_utils.math_util import add_util
```

we can potentially use:

```python
from package import add_util
```

because `add_util` was imported inside `package/__init__.py`.

---

# 4. What Does `.` Mean in an Import?

Consider:

```python
from .general import general_util
```

The `.` means:

> Start from the current package.

So if we are inside:

```text
package/__init__.py
```

Python understands:

```text
package/general.py
```

Similarly:

```python
from .a_utils.math_util import add_util
```

means:

```text
current package
    ↓
a_utils
    ↓
math_util.py
    ↓
add_util
```

This is called a **relative import**.

---

# 5. Absolute Import vs Relative Import

### Absolute import

```python
from package.a_utils.math_util import add_util
```

This starts from the package name.

### Relative import

```python
from .a_utils.math_util import add_util
```

This starts from the current package.

The `.` tells Python to look relative to the current package.

---

# 6. Why Use Packages?

Packages become especially useful when a project becomes large.

Without packages:

```text
project/
├── math.py
├── string.py
├── database.py
├── users.py
├── authentication.py
├── payments.py
└── ...
```

This can become difficult to manage.

With packages:

```text
project/
├── users/
│   ├── models.py
│   ├── authentication.py
│   └── views.py
│
├── payments/
│   ├── models.py
│   └── services.py
│
└── utils/
    ├── math.py
    └── string.py
```

Related functionality is grouped together.

---

# 7. Important Terms

### Module

A Python file containing Python code.

Example:

```text
math_util.py
```

### Package

A directory used to organize Python modules and subpackages.

Example:

```text
a_utils/
```

### `__init__.py`

A special file that can initialize a package and expose/import objects from the package.

### Import

Used to bring code from another module or package into the current Python file.

Example:

```python
from package import add_util
```

### Relative import

An import that uses `.` or `..` to refer to the current package or its parent package.

Example:

```python
from .general import general_util
```

---

# 8. Example Used in This Project

The package has this structure:

```text
package/
├── __init__.py
├── general.py
├── a_utils/
│   ├── __init__.py
│   └── math_util.py
└── b_utils/
    ├── __init__.py
    └── string_util.py
```

Inside `__init__.py`:

```python
from .a_utils.math_util import add_util
from .b_utils.string_util import String_util
from .general import general_util

print("Importing the package")
```

When we execute:

```python
import package
```

Python loads the package and executes `__init__.py`.

Therefore:

```text
import package
      ↓
package/__init__.py
      ↓
imports add_util
      ↓
imports String_util
      ↓
imports general_util
      ↓
prints "Importing the package"
```

---

# 9. One Important Note

Modern versions of Python can recognize some directories as packages even without `__init__.py`, through **namespace packages**.

However, `__init__.py` is still extremely common and useful in real Python projects.

For learning Python, Django, and backend development, it is important to understand what it does rather than simply memorizing that it "makes a folder a package."

---

# Key Takeaway

The relationship is:

```text
Module
  ↓
.py file

Package
  ↓
directory containing related Python modules

__init__.py
  ↓
package initialization and package-level imports

Relative import
  ↓
. means current package
.. means parent package
```

The main concept to remember is:

> **Packages organize Python code, and `__init__.py` can control what happens when that package is imported.**