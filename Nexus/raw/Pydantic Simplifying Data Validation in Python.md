---
title: "Pydantic: Simplifying Data Validation in Python"
source: "https://realpython.com/python-pydantic/?utm_source=chatgpt.com"
author:
  - "[[Real Python]]"
published: 2024-04-10
created: 2026-06-02
description: "Discover the power of Pydantic, Python's most popular data parsing, validation, and serialization library. In this hands-on tutorial, you'll learn how to make your code more robust, trustworthy, and easier to debug with Pydantic."
tags:
  - "clippings"
summary:
---
![Pydantic: Simplifying Data Validation in Python](https://realpython.com/cdn-cgi/image/width=1920,format=auto/https://files.realpython.com/media/Pydantic-Showcase_Watermarked.423b9d2e27c6.jpg)

Pydantic: Simplifying Data Validation in Python

Pydantic is a powerful data validation and settings management library for Python, engineered to enhance the robustness and reliability of your codebase. From basic tasks, such as checking whether a variable is an integer, to more complex tasks, like ensuring highly-nested dictionary keys and values have the correct data types, Pydantic can handle just about any data validation scenario with minimal boilerplate code.

**In this tutorial, you’ll learn how to:**

- Work with **data schemas** with Pydantic’s `BaseModel`
- Write **custom validators** for complex use cases
- **Validate function arguments** with Pydantic’s `@validate_call`
- Manage settings and **configure applications** with `pydantic-settings`

Throughout this tutorial, you’ll get hands-on examples of Pydantic’s functionalities, and by the end you’ll have a solid foundation for your own validation use cases. Before starting this tutorial, you’ll benefit from having an intermediate understanding of Python and [object-oriented programming](https://realpython.com/python3-object-oriented-programming/).

> [!warning] Warning
> **Get Your Code:** [Click here to download the free sample code](https://realpython.com/bonus/pydantic-simplifying-data-validation-in-python/) that you’ll use to help you learn how Pydantic can help you simplify data validation in Python.

==**Take the Quiz:**== Test your knowledge with our interactive “Pydantic: Simplifying Data Validation in Python” quiz. You’ll receive a score upon completion to help you track your learning progress:

---

[![Pydantic: Simplifying Data Validation in Python](https://realpython.com/cdn-cgi/image/width=1920,format=auto/https://files.realpython.com/media/Pydantic-Showcase_Watermarked.423b9d2e27c6.jpg)](https://realpython.com/quizzes/python-pydantic/)

**Interactive Quiz**

[Pydantic: Simplifying Data Validation in Python](https://realpython.com/quizzes/python-pydantic/)

In this quiz, you'll test your understanding of Pydantic, a powerful data validation library for Python. You'll revisit concepts such as working with data schemas, writing custom validators, validating function arguments, and managing settings with pydantic-settings.

## Python’s Pydantic Library

One of Python’s main attractions is that it’s a dynamically typed language. Dynamic typing means that variable types are determined at runtime, unlike statically typed languages where they are explicitly declared at compile time. While dynamic typing is great for rapid development and ease of use, you often need more robust type checking and data validation for real-world applications. This is where Python’s Pydantic library has you covered.

Pydantic has quickly gained popularity, and it’s now the most widely used data validation library for Python. In this first section, you’ll get an overview of Pydantic and a preview of the library’s powerful features. You’ll also learn how to install Pydantic along with the additional dependencies you’ll need for this tutorial.

![](https://img.realpython.net/9dea026bd5e810fee4b4cd33ee0995d8)

[Remove ads](https://realpython.com/account/join/)

### Getting Familiar With Pydantic

Pydantic is a powerful Python library that leverages [type hints](https://realpython.com/python-type-checking/) to help you easily validate and serialize your data schemas. This makes your code more robust, readable, concise, and easier to debug. Pydantic also integrates well with many popular static typing tools and IDEs, which allows you to catch schema issues before running your code.

Some of Pydantic’s distinguishing features include:

- **Customization**: There’s almost no limit to the kinds of data you can validate with Pydantic. From primitive Python types to highly nested data structures, Pydantic lets you validate and serialize nearly any Python object.
- **Flexibility**: Pydantic gives you control over how strict or lax you want to be when validating your data. In some cases, you might want to coerce incoming data to the correct type. For example, you could accept data that’s intended to be a float but is received as an integer. In other cases, you might want to strictly enforce the data types you’re receiving. Pydantic enables you to do either.
- **Serialization**: You can serialize and deserialize Pydantic objects as [dictionaries](https://realpython.com/python-dicts/) and [JSON](https://realpython.com/python-json/) strings. This means that you can seamlessly convert your Pydantic objects to and from JSON. This capability has led to self-documenting APIs and integration with just about any tool that supports JSON schemas.
- **Performance**: Thanks to its core validation logic written in [Rust](https://www.rust-lang.org/), Pydantic is exceptionally fast. This performance advantage gives you swift and reliable data processing, especially in high-throughput applications such as REST APIs that need to scale to a large number of requests.
- **Ecosystem and Industry Adoption**: Pydantic is a dependency of [many popular Python libraries](https://docs.pydantic.dev/2.0/why/#ecosystem) such as [FastAPI](https://realpython.com/fastapi-python-web-apis/), [LangChain](https://realpython.com/build-llm-rag-chatbot-with-langchain/), and [Polars](https://realpython.com/polars-python/). It’s also used by most of the [largest tech companies](https://docs.pydantic.dev/2.0/why/#using-pydantic) and throughout many other industries. This is a testament to Pydantic’s community support, reliability, and resilience.

These are a few key features that make Pydantic an attractive data validation library, and you’ll get to see these in action throughout this tutorial. Up next, you’ll get an overview of how to install Pydantic along with its various dependencies.

### Installing Pydantic

Pydantic is available on [PyPI](https://pypi.org/), and you can install it with [pip](https://realpython.com/what-is-pip/). Open a terminal or command prompt, create a new virtual environment, and then run the following command to install Pydantic:

```
(venv) $ python -m pip install pydantic
```

This command will install the latest version of Pydantic from PyPI onto your machine. To verify that the installation was successful, start a [Python REPL](https://realpython.com/python-repl/) and import Pydantic:

```
>>> import pydantic
```

If the import runs without error, then you’ve successfully installed Pydantic, and you now have the core of Pydantic installed on your system.

### Adding Optional Dependencies

You can install optional dependencies with Pydantic as well. For example, you’ll be working with email validation in this tutorial, and you can include these dependencies in your install:

```
(venv) $ python -m pip install "pydantic[email]"
```

Pydantic has a separate package for [settings management](https://docs.pydantic.dev/latest/concepts/pydantic_settings/), which you’ll also cover in this tutorial. To install this, run the following command:

```
(venv) $ python -m pip install pydantic-settings
```

With that, you’ve installed all the dependencies you’ll need for this tutorial, and you’re ready to start exploring Pydantic. You’ll start by covering models—Pydantic’s primary way of defining data schemas.

## Using Models

Pydantic’s primary way of defining data schemas is through [models](https://docs.pydantic.dev/latest/concepts/models/). A Pydantic model is an object, similar to a Python [dataclass](https://realpython.com/python-data-classes/), that defines and stores data about an entity with [annotated](https://realpython.com/python-type-checking/#annotations) fields. Unlike dataclasses, Pydantic’s focus is centered around automatic data parsing, validation, and serialization.

The best way to understand this is to create your own models, and that’s what you’ll do next.

![](https://img.realpython.net/16bf1efe41b538fae54711c58c701f0e)

[Remove ads](https://realpython.com/account/join/)

### Working With Pydantic BaseModels

Suppose you’re building an application used by a human resources department to manage employee information, and you need a way to verify that new employee information is in the correct form. For example, each employee should have an ID, name, email, date of birth, salary, department, and benefits selection. This is a perfect use case for a Pydantic model!

To define your employee model, you create a [class](https://realpython.com/python-classes/) that [inherits](https://realpython.com/inheritance-composition-python/) from Pydantic’s `BaseModel`:

Python `pydantic_models.py`

```
from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr

class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"

class Employee(BaseModel):
    employee_id: UUID = uuid4()
    name: str
    email: EmailStr
    date_of_birth: date
    salary: float
    department: Department
    elected_benefits: bool
```

First, you import the dependencies you need to define your employee model. You then create an [enum](https://realpython.com/python-enum/) to represent the different departments in your company, and you’ll use this to annotate the `department` field in your employee model.

Then, you define your Pydantic model, `Employee`, which inherits from `BaseModel` and defines the names and expected types of your employee fields via annotations. Here’s a breakdown of each field you’ve defined in `Employee` and how Pydantic validates it when an `Employee` object is instantiated:

- **`employee_id`**: This is the [UUID](https://docs.python.org/3/library/uuid.html) for the employee you want to store information for. By using the `UUID` annotation, Pydantic ensures this field is always a valid UUID. Each instance of `Employee` will be assigned a UUID by default, as you specified by calling `uuid4()`.
- **`name`**: The employee’s name, which Pydantic expects to be a string.
- **`email`**: Pydantic will ensure that each employee `email` is valid by using Python’s [`email-validator`](https://pypi.org/project/email-validator/) library under the hood.
- **`date_of_birth`**: Each employee’s date of birth must be a valid date, as annotated by `date` from Python’s [`datetime`](https://realpython.com/python-datetime/) module. If you pass a string into `date_of_birth`, Pydantic will attempt to parse and convert it to a `date` object.
- **`salary`**: This is the employee’s salary, and it’s expected to be a float.
- **`department`**: Each employee’s department must be one of `HR`, `SALES`, `IT`, or `ENGINEERING`, as defined in your `Department` enum.
- **`elected_benefits`**: This field stores whether the employee has elected benefits, and Pydantic expects it to be a Boolean.

The simplest way to create an `Employee` object is to instantiate it as you would any other Python object. To do this, open a Python [REPL](https://realpython.com/python-repl/) and run the following code:

```
>>> from pydantic_models import Employee

>>> Employee(
...     name="Chris DeTuma",
...     email="cdetuma@example.com",
...     date_of_birth="1998-04-02",
...     salary=123_000.00,
...     department="IT",
...     elected_benefits=True,
... )
Employee(
    employee_id=UUID('73636d47-373b-40cd-a005-4819a84d9ea7'),
    name='Chris DeTuma',
    email='cdetuma@example.com',
    date_of_birth=datetime.date(1998, 4, 2),
    salary=123000.0,
    department=<Department.IT: 'IT'>,
    elected_benefits=True
)
```

In this block, you import `Employee` and create an object with all of the required employee fields. Pydantic successfully validates and coerces the fields you passed in, and it creates a valid `Employee` object. Notice how Pydantic automatically converts your date string into a `date` object and your `IT` string to its respective `Department` enum.

Next, look at how Pydantic responds when you try to pass invalid data to an `Employee` instance:

```
>>> Employee(
...     employee_id="123",
...     name=False,
...     email="cdetumaexamplecom",
...     date_of_birth="1939804-02",
...     salary="high paying",
...     department="PRODUCT",
...     elected_benefits=300,
... )

Traceback (most recent call last):
pydantic_core._pydantic_core.ValidationError: 7 validation errors for
Employee

employee_id
  Input should be a valid UUID, invalid length: expected length 32 for
  simple format, found 3 [type=uuid_parsing, input_value='123',
  input_type=str] For further information visit
  https://errors.pydantic.dev/2.6/v/uuid_parsing

name
  Input should be a valid string [type=string_type, input_value=False,
  input_type=bool] For further information visit
  https://errors.pydantic.dev/2.6/v/string_type

email
  value is not a valid email address: The email address is not valid.
  It must have exactly one @-sign. [type=value_error,
  input_value='cdetumaexamplecom', input_type=str]

date_of_birth
  Input should be a valid date or datetime, invalid date separator,
  expected \`-\` [type=date_from_datetime_parsing,
  input_value='1939804-02', input_type=str] For further information
  visit https://errors.pydantic.dev/2.6/v/date_from_datetime_parsing

salary
  Input should be a valid number, unable to parse string as a number
  [type=float_parsing, input_value='high paying', input_type=str]
  For further information visit
  https://errors.pydantic.dev/2.6/v/float_parsing

department
  Input should be 'HR', 'SALES', 'IT' or 'ENGINEERING'
  [type=enum, input_value='PRODUCT', input_type=str]

elected_benefits
  Input should be a valid boolean, unable to interpret input
  [type=bool_parsing, input_value=300, input_type=int]
  For further information visit
  https://errors.pydantic.dev/2.6/v/bool_parsing
```

In this example, you created an `Employee` object with invalid data fields. Pydantic gives you a detailed error message for each field, telling you what was expected, what was received, and where you can go to learn more about the error.

This detailed validation is powerful because it prevents you from storing invalid data in `Employee`. This also gives you confidence that the `Employee` objects you instantiate without errors contain the data you’re expecting, and you can trust this data downstream in your code or in other applications.

Pydantic’s `BaseModel` is equipped with a suite of methods that make it easy to create models from other objects, such as dictionaries and [JSON](https://realpython.com/python-json/). For example, if you want to instantiate an `Employee` object from a dictionary, you can use the `.model_validate()` [class method](https://realpython.com/instance-class-and-static-methods-demystified/):

```
>>> new_employee_dict = {
...     "name": "Chris DeTuma",
...     "email": "cdetuma@example.com",
...     "date_of_birth": "1998-04-02",
...     "salary": 123_000.00,
...     "department": "IT",
...     "elected_benefits": True,
... }

>>> Employee.model_validate(new_employee_dict)
Employee(
    employee_id=UUID('73636d47-373b-40cd-a005-4819a84d9ea7'),
    name='Chris DeTuma',
    email='cdetuma@example.com',
    date_of_birth=datetime.date(1998, 4, 2),
    salary=123000.0,
    department=<Department.IT: 'IT'>,
    elected_benefits=True
)
```

Here, you create `new_employee_dict`, a dictionary with your employee fields, and pass it into `.model_validate()` to create an `Employee` instance. Under the hood, Pydantic validates each dictionary entry to ensure it conforms with the data you’re expecting. If any of the data is invalid, Pydantic will throw an error in the same way you saw previously. You’ll also be notified if any fields are missing from the dictionary.

You can do the same thing with JSON objects using `.model_validate_json()`:

```
>>> new_employee_json = """
...  {"employee_id":"d2e7b773-926b-49df-939a-5e98cbb9c9eb",
...  "name":"Eric Slogrenta",
...  "email":"eslogrenta@example.com",
...  "date_of_birth":"1990-01-02",
...  "salary":125000.0,
...  "department":"HR",
...  "elected_benefits":false}
...  """

>>> new_employee = Employee.model_validate_json(new_employee_json)
>>> new_employee
Employee(
    employee_id=UUID('d2e7b773-926b-49df-939a-5e98cbb9c9eb'),
    name='Eric Slogrenta',
    email='eslogrenta@example.com',
    date_of_birth=datetime.date(1990, 1, 2),
    salary=125000.0,
    department=<Department.HR: 'HR'>,
    elected_benefits=False
)
```

In this example, `new_employee_json` is a valid JSON string that stores your employee fields, and you use `.model_validate_json()` to validate and create an `Employee` object from `new_employee_json`. While it may seem subtle, the ability to create and validate Pydantic models from JSON is powerful because JSON is one of the most popular ways to transfer data across the web. This is one of the reasons why [FastAPI](https://realpython.com/get-started-with-fastapi/) relies on Pydantic to create REST APIs.

You can also serialize Pydantic models as dictionaries and JSON:

```
>>> new_employee.model_dump()
{
    'employee_id': UUID('d2e7b773-926b-49df-939a-5e98cbb9c9eb'),
    'name': 'Eric Slogrenta',
    'email': 'eslogrenta@example.com',
    'date_of_birth': datetime.date(1990, 1, 2),
    'salary': 125000.0,
    'department': <Department.HR: 'HR'>,
    'elected_benefits': False
}

>>> new_employee.model_dump_json()
'{"employee_id":"d2e7b773-926b-49df-939a-5e98cbb9c9eb",
⮑"name":"Eric Slogrenta",
⮑"email":"eslogrenta@example.com",
⮑"date_of_birth":"1990-01-02",
⮑"salary":125000.0,
⮑"department":"HR",
⮑"elected_benefits":false}'
```

Here, you use `.model_dump()` and `.model_dump_json()` to convert your `new_employee` model to a dictionary and JSON string, respectively. Notice how `.model_dump_json()` returns a JSON object with `date_of_birth` and `department` stored as strings.

While Pydantic already validated these fields and converted your model to JSON, whoever uses this JSON downstream won’t know that `date_of_birth` needs to be a valid `date` and `department` needs to be a category in your `Department` enum. To solve this, you can create a [JSON schema](https://json-schema.org/understanding-json-schema/about) from your `Employee` model.

JSON schemas tell you what fields are expected and what values are represented in a JSON object. You can think of this as the JSON version of your `Employee` class definition. Here’s how you generate a JSON schema for `Employee`:

```
>>> Employee.model_json_schema()
{
    '$defs': {
        'Department': {
            'enum': ['HR', 'SALES', 'IT', 'ENGINEERING'],
            'title': 'Department',
            'type': 'string'
        }
    },
    'properties': {
        'employee_id': {
            'default': '73636d47-373b-40cd-a005-4819a84d9ea7',
            'format': 'uuid',
            'title': 'Employee Id',
            'type': 'string'
        },
        'name': {'title': 'Name', 'type': 'string'},
        'email': {
            'format': 'email',
            'title': 'Email',
            'type': 'string'
        },
        'date_of_birth': {
            'format': 'date',
            'title': 'Date Of Birth',
            'type': 'string'
        },
        'salary': {'title': 'Salary', 'type': 'number'},
        'department': {'$ref': '#/$defs/Department'},
        'elected_benefits': {'title': 'Elected Benefits', 'type': 'boolean'}
    },
    'required': [
        'name',
        'email',
        'date_of_birth',
        'salary',
        'department',
        'elected_benefits'
    ],
    'title': 'Employee',
    'type': 'object'
}
```

When you call `.model_json_schema()`, you get a dictionary representing your model’s JSON schema. The first entry you see shows you the values that `department` can take on. You also see information about how your fields should be formatted. For instance, according to this JSON schema, `employee_id` is expected to be a UUID and `date_of_birth` is expected to be a date.

You can convert your JSON schema to a JSON string using `json.dumps()`, which enables just about [any programming language](https://json-schema.org/implementations) to validate JSON objects produced by your `Employee` model. In other words, not only can Pydantic validate incoming data and serialize it as JSON, but it also provides other programming languages with the information they need to validate your model’s data via JSON schemas.

With that, you now understand how to use Pydantic’s `BaseModel` to validate and serialize your data. Up next, you’ll learn how to use fields to further customize your validation.

![](https://img.realpython.net/c75ad5c06078a2b00c305659dda76f56)

[Remove ads](https://realpython.com/account/join/)

### Using Fields for Customization and Metadata

So far, your `Employee` model validates the data type of each field and ensures some of the fields, such as `email`, `date_of_birth`, and `department`, take on valid formats. However, let’s say you also want to ensure that `salary` is a positive number, `name` isn’t an empty string, and `email` contains your company’s domain name. You can use Pydantic’s [`Field`](https://docs.pydantic.dev/latest/concepts/fields/) class to accomplish this.

The `Field` class allows you to customize and add metadata to your model’s fields. To see how this works, take a look at this example:

Python `pydantic_models.py`

```
from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr, Field

class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"

class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str = Field(min_length=1, frozen=True)
    email: EmailStr = Field(pattern=r".+@example\.com$")
    date_of_birth: date = Field(alias="birth_date", repr=False, frozen=True)
    salary: float = Field(alias="compensation", gt=0, repr=False)
    department: Department
    elected_benefits: bool
```

Here, you import `Field` along with the other dependencies you used previously, and you assign default values to some of the `Employee` fields. Here’s a breakdown of the `Field` parameters you used to add additional validation and metadata to your fields:

- **`default_factory`**: You use this to define a callable that generates default values. In the example above, you set `default_factory` to `uuid4`. This calls `uuid4()` to generate a random UUID for `employee_id` when needed. You can also use a [lambda](https://realpython.com/python-lambda/) function for more flexibility.
- **`frozen`**: This is a Boolean parameter you can set to make your fields immutable. This means, when `frozen` is set to `True`, the corresponding field can’t be changed after your model is instantiated. In this example, `employee_id`, `name`, and `date_of_birth` are made immutable using the `frozen` parameter.
- **`min_length`**: You can control the length of string fields with `min_length` and `max_length`. In the example above, you ensure that `name` is at least one character long.
- **`pattern`**: For string fields, you can set `pattern` to a [regex](https://realpython.com/regex-python/) expression to match whatever pattern you’re expecting for that field. For instance, when you use the regex expression in the example above for `email`, Pydantic will ensure that every email ends with `@example.com`.
- **`alias`**: You can use this parameter when you want to assign an alias to your fields. For example, you can allow `date_of_birth` to be called `birth_date` or `salary` to be called `compensation`. You can use these aliases when instantiating or serializing a model.
- **`gt`**: This parameter, short for “greater than”, is used for numeric fields to set minimum values. In this example, setting `gt=0` ensures `salary` is always a positive number. Pydantic also has other [numeric constraints](https://docs.pydantic.dev/latest/concepts/fields/#numeric-constraints), such as `lt` which is short for “less than”.
- **`repr`**: This Boolean parameter determines whether a field is displayed in the model’s field representation. In this example, you won’t see `date_of_birth` or `salary` when you print an `Employee` instance.

To see this extra validation in action, notice what happens when you try to create an `Employee` model with incorrect data:

```
>>> from pydantic_models import Employee

>>> incorrect_employee_data = {
...     "name": "",
...     "email": "cdetuma@fakedomain.com",
...     "birth_date": "1998-04-02",
...     "salary": -10,
...     "department": "IT",
...     "elected_benefits": True,
... }

>>> Employee.model_validate(incorrect_employee_data)
Traceback (most recent call last):

pydantic_core._pydantic_core.ValidationError: 3 validation errors for
Employee
name
  String should have at least 1 character [type=string_too_short,
   input_value='', input_type=str] For further information visit
    https://errors.pydantic.dev/2.6/v/string_too_short
email
  String should match pattern '.+@example\.com$'
  [type=string_pattern_mismatch,
  input_value='cdetuma@fakedomain.com', input_type=str]
    For further information visit
    https://errors.pydantic.dev/2.6/v/string_pattern_mismatch
salary
  Input should be greater than 0 [type=greater_than, input_value=-10,
  input_type=int] For further information visit
  https://errors.pydantic.dev/2.6/v/greater_than
```

Here, you import your updated `Employee` model and attempt to validate a dictionary with incorrect data. In response, Pydantic gives you three validation errors saying the `name` needs to be at least one character, `email` should match your company’s domain name, and `salary` should be greater than zero.

Now notice the additional features you get when you validate correct `Employee` data:

```
>>> employee_data = {
...     "name": "Clyde Harwell",
...     "email": "charwell@example.com",
...     "birth_date": "2000-06-12",
...     "compensation": 100_000,
...     "department": "ENGINEERING",
...     "elected_benefits": True,
... }

>>> employee = Employee.model_validate(employee_data)
>>> employee
Employee(
    employee_id=UUID('614c6f75-8528-4272-9cfc-365ddfafebd9'),
    name='Clyde Harwell',
    email='charwell@example.com',
    department=<Department.ENGINEERING: 'ENGINEERING'>,
    elected_benefits=True)

>>> employee.salary
100000.0

>>> employee.date_of_birth
datetime.date(2000, 6, 12)
```

In this block, you create a dictionary and an `Employee` model with `.model_validate()`. In `employee_data`, notice how you used `birth_date` instead of `date_of_birth` and `compensation` instead of `salary`. Pydantic recognizes these aliases and assigns their values to the correct field name internally.

Because you set `repr=False`, you can see that `salary` and `date_of_birth` aren’t displayed in the `Employee` representation. You have to explicitly access them as attributes to see their values. Lastly, notice what happens when you try to change a frozen field:

```
>>> employee.department = "HR"
>>> employee.name = "Andrew TuGrendele"
Traceback (most recent call last):

pydantic_core._pydantic_core.ValidationError: 1
validation error for Employee
name
  Field is frozen [type=frozen_field, input_value='Andrew TuGrendele',
  input_type=str]
  For further information visit
  https://errors.pydantic.dev/2.6/v/frozen_field
```

Here, you first change the value of `department` from `IT` to `HR`. This is perfectly acceptable because `department` isn’t a frozen field. However, when you try to change `name`, Pydantic gives you an error saying that `name` is a frozen field.

You now have a solid grasp of Pydantic’s `BaseModel` and `Field` classes. With these alone, you can define many different validation rules and metadata on your data schemas, but sometimes this isn’t enough. Up next, you’ll take your field validation even further with Pydantic validators.

## Working With Validators

Up to this point, you’ve used Pydantic’s `BaseModel` to validate model fields with predefined types, and you incorporated `Field` to further customize your validation. While you can get pretty far with `BaseModel` and `Field` alone, for more complicated validation scenarios that require custom logic, you’ll need to use Pydantic [validators](https://docs.pydantic.dev/latest/concepts/validators/).

With validators, you can execute just about any validation logic that you can express in a function. You’ll see how to do this next.

### Validating Models and Fields

Continuing with the employee example, suppose your company has a policy that they only hire employees who are at least eighteen years old. Any time you create a new `Employee` object, you need to make sure the employee is older than eighteen. To handle this, you could add an `age` field and use the `Field` class to enforce that the employee is at least eighteen. However, this seems redundant since you’ve already stored the employee’s birth date.

A better solution is to use a Pydantic [field validator](https://docs.pydantic.dev/latest/concepts/validators/#field-validators). Field validators allow you to apply custom validation logic to your `BaseModel` fields by adding class methods to your model. To enforce that all employees are at least eighteen, you can add the following `Field` validator to your `Employee` model:

Python `pydantic_models.py`

```
from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import BaseModel, EmailStr, Field, field_validator

class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"

class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str = Field(min_length=1, frozen=True)
    email: EmailStr = Field(pattern=r".+@example\.com$")
    date_of_birth: date = Field(alias="birth_date", repr=False, frozen=True)
    salary: float = Field(alias="compensation", gt=0, repr=False)
    department: Department
    elected_benefits: bool

    @field_validator("date_of_birth")
    @classmethod
    def check_valid_age(cls, date_of_birth: date) -> date:
        today = date.today()
        eighteen_years_ago = date(today.year - 18, today.month, today.day)

        if date_of_birth > eighteen_years_ago:
            raise ValueError("Employees must be at least 18 years old.")

        return date_of_birth
```

In this block, you import `field_validator` and use it to decorate a class method in `Employee` called `.check_valid_age()`. Field validators must be defined a class methods. In `.check_valid_age()`, you calculate today’s date but eighteen years ago. If the employee’s `date_of_birth` is after that date, an error is raised.

To see how this validator works, check out this example:

```
>>> from pydantic_models import Employee
>>> from datetime import date, timedelta

>>> young_employee_data = {
...     "name": "Jake Bar",
...     "email": "jbar@example.com",
...     "birth_date": date.today() - timedelta(days=365 * 17),
...     "compensation": 90_000,
...     "department": "SALES",
...     "elected_benefits": True,
... }

>>> Employee.model_validate(young_employee_data)
Traceback (most recent call last):

pydantic_core._pydantic_core.ValidationError:
1 validation error for Employee
birth_date
  Value error, Employees must be at least 18 years old.
  [type=value_error, input_value=datetime.date(2007, 4, 10),
  input_type=date]
  For further information visit
  https://errors.pydantic.dev/2.6/v/value_error
```

In this example, you specify a `birth_date` that is seventeen years behind the current date. When you call `.model_validate()` to validate `young_employee_data`, you get an error saying employees must be at least eighteen years old.

As you can imagine, Pydantic’s `field_validator()` enables you to arbitrarily customize field validation. However, `field_validator()` won’t work if you want to compare multiple fields to one another or validate your model as a whole. For this, you’ll need to use [model validators](https://docs.pydantic.dev/latest/concepts/validators/#model-validators).

As an example, suppose your company only hires contract workers in the IT department. Because of this, IT workers don’t qualify for benefits and their `elected_benefits` field should be `False`. You can use Pydantic’s `model_validator()` to enforce this constraint:

Python `pydantic_models.py`

```
from typing import Self
from datetime import date
from uuid import UUID, uuid4
from enum import Enum
from pydantic import (
    BaseModel,
    EmailStr,
    Field,
    field_validator,
    model_validator,
)

class Department(Enum):
    HR = "HR"
    SALES = "SALES"
    IT = "IT"
    ENGINEERING = "ENGINEERING"

class Employee(BaseModel):
    employee_id: UUID = Field(default_factory=uuid4, frozen=True)
    name: str = Field(min_length=1, frozen=True)
    email: EmailStr = Field(pattern=r".+@example\.com$")
    date_of_birth: date = Field(alias="birth_date", repr=False, frozen=True)
    salary: float = Field(alias="compensation", gt=0, repr=False)
    department: Department
    elected_benefits: bool

    @field_validator("date_of_birth")
    @classmethod
    def check_valid_age(cls, date_of_birth: date) -> date:
        today = date.today()
        eighteen_years_ago = date(today.year - 18, today.month, today.day)

        if date_of_birth > eighteen_years_ago:
            raise ValueError("Employees must be at least 18 years old.")

        return date_of_birth

    @model_validator(mode="after")
    def check_it_benefits(self) -> Self:
        department = self.department
        elected_benefits = self.elected_benefits

        if department == Department.IT and elected_benefits:
            raise ValueError(
                "IT employees are contractors and don't qualify for benefits"
            )
        return self
```

Here, you add Python’s [`Self` type](https://realpython.com/python-type-self/) and Pydantic’s `model_validator()` to your imports. You then create a method, `.check_it_benefits()`, that raises an error if the employee belongs to the IT department and the `elected_benefits` field is `True`. When you set `mode` to `after` in `@model_validator`, Pydantic waits until after you’ve instantiated your model to run `.check_it_benefits()`.

> [!primary] Primary
> **Note**: You may have noticed that `.check_it_benefits()` is annotated with Python’s `Self` type. This is because `.check_it_benefits()` returns the `Employee` class instance, and the `Self` type is the [preferred annotation](https://realpython.com/python-type-self/#how-to-annotate-a-method-with-the-self-type-in-python) for this. If you’re using a Python version less than 3.11, you’ll have to import the `Self` type from `typing_extensions`.

To see your new model validator in action, check out this example:

```
>>> from pydantic_models import Employee

>>> new_employee = {
...     "name": "Alexis Tau",
...     "email": "ataue@example.com",
...     "birth_date": "2001-04-012",
...     "compensation": 100_000,
...     "department": "IT",
...     "elected_benefits": True,
... }

>>> Employee.model_validate(new_employee)
Traceback (most recent call last):

pydantic_core._pydantic_core.ValidationError: 1 validation error for
Employee
  Value error, IT employees are contractors and don't qualify for
  benefits.
  [type=value_error, input_value={'name': 'Alexis Tau',
  ...elected_benefits': True},
  input_type=dict]
    For further information visit
    https://errors.pydantic.dev/2.6/v/value_error
```

In this example, you try to create an `Employee` model with an `IT` department and `elected_benefits` set to `True`. When you call `.model_validate()`, Pydantic throws an error letting you know that IT employees don’t qualify for benefits because they’re contractors.

With model and field validators, you can implement just about any custom validation you can think of. You should now have a solid foundation to create Pydantic models for your own use cases. Up next, you’ll shift gears and look at how you can use Pydantic to validate arbitrary functions, not just `BaseModel` fields.

![](https://img.realpython.net/e822f46aa4962c3565f257bb0c4679a8)

[Remove ads](https://realpython.com/account/join/)

### Using Validation Decorators to Validate Functions

While `BaseModel` is Pydantic’s bread and butter class for validating data schemas, you can also use Pydantic to validate function arguments using the [`@validate_call`](https://docs.pydantic.dev/latest/concepts/validation_decorator/) decorator. This allows you to create robust functions with informative type errors without having to manually implement validation logic.

To see how this works, suppose you’re writing a function that sends invoices to clients after they’ve made a purchase. Your function takes in the client’s name, email, items purchased, and total billing amount, and it constructs and sends them an email. You need to validate all of these inputs because getting them wrong could result in the email not being sent, being misformatted, or the client being invoiced incorrectly.

To accomplish this, you write the following function:

Python `validate_functions.py`

```
import time
from typing import Annotated
from pydantic import PositiveFloat, Field, EmailStr, validate_call

@validate_call
def send_invoice(
    client_name: Annotated[str, Field(min_length=1)],
    client_email: EmailStr,
    items_purchased: list[str],
    amount_owed: PositiveFloat,
) -> str:

    email_str = f"""
    Dear {client_name}, \n
    Thank you for choosing xyz inc! You
    owe ${amount_owed:,.2f} for the following items: \n
    {items_purchased}
    """

    print(f"Sending email to {client_email}...")
    time.sleep(2)

    return email_str
```

First, you import the dependencies needed to write and annotate `send_invoice()`. You then create `send_invoice()` decorated with `@validate_call`. Before executing `send_invoice()`, `@validate_call` ensures that each input conforms to your annotations. In this case, `@validate_call` checks whether `client_name` has at least one character, `client_email` is properly formatted, `items_purchased` is a list of strings, and `amount_owed` is a positive float.

If one of the inputs doesn’t conform to your annotation, Pydantic will throw an error similar to what you’ve seen already with `BaseModel`. If all the inputs are valid, `send_invoice()` creates a string and simulates sending it to your client with `time.sleep(2)`.

> [!primary] Primary
> **Note**: You might have noticed that `client_name` is annotated with Python’s `Annotated` type. In general, you can use `Annotated` when you want to provide metadata about a function argument. Pydantic [recommends](https://docs.pydantic.dev/latest/concepts/validation_decorator/#using-field-to-describe-function-arguments) using `Annotated` when you need to validate a function argument that has metadata specified by `Field`.
> 
> However, if you use `default_factory` to assign a default value to your function argument, you should assign the argument directly to a `Field` instance. You can see an example of this in [Pydantic’s documentation](https://docs.pydantic.dev/latest/concepts/validation_decorator/#using-field-to-describe-function-arguments).

To see `@validate_call` and `send_invoice()` in action, open a new Python REPL and run the following code:

```
>>> from validate_functions import send_invoice

>>> send_invoice(
...     client_name="",
...     client_email="ajolawsonfakedomain.com",
...     items_purchased=["pie", "cookie", 17],
...     amount_owed=0,
... )
Traceback (most recent call last):
pydantic_core._pydantic_core.ValidationError: 4 validation errors for
send_invoice
client_name
  String should have at least 1 character [type=string_too_short,
  input_value='', input_type=str]
    For further information visit
    https://errors.pydantic.dev/2.6/v/string_too_short
client_email
  value is not a valid email address: The email address is not valid.
  It must have exactly one @-sign. [type=value_error,
  input_value='ajolawsonfakedomain.com', input_type=str]
items_purchased.2
  Input should be a valid string [type=string_type, input_value=17,
  input_type=int]
    For further information visit
    https://errors.pydantic.dev/2.6/v/string_type
amount_owed
  Input should be greater than 0 [type=greater_than, input_value=0,
  input_type=int]
    For further information visit
    https://errors.pydantic.dev/2.6/v/greater_than
```

In this example, you import `send_invoice()` and pass in invalid function arguments. Pydantic’s `@validate_call` recognizes this and throws errors telling you that `client_name` needs at least one character, `client_email` is invalid, `items_purchased` should contain strings, and `amount_owed` should be greater than zero.

When you pass in valid inputs, `send_invoice()` runs as expected:

```
>>> email_str = send_invoice(
...     client_name="Andrew Jolawson",
...     client_email="ajolawson@fakedomain.com",
...     items_purchased=["pie", "cookie", "cake"],
...     amount_owed=20,
... )
Sending email to ajolawson@fakedomain.com...

>>> print(email_str)

    Dear Andrew Jolawson,

    Thank you for choosing xyz inc! You
    owe $20.00 for the following items:

    ['pie', 'cookie', 'cake']
```

While `@validate_call` isn’t as flexible as `BaseModel`, you can still use it to apply powerful validation to your function arguments. This saves you a lot of time and lets you avoid writing boilerplate type checking and validation logic. If you’ve done this before, you know how cumbersome it can be to write [`assert` statements](https://realpython.com/python-assert-statement/) for each of your function arguments. For many use cases, `@validate_call` takes care of this for you.

In the final section of this tutorial, you’ll learn how you can use Pydantic for settings management and configuration.

## Managing Settings

One of the most popular ways to configure Python applications is with environment variables. An environment variable is a variable that lives in the operating system, outside of your Python code, but can be read by your code or other programs. Examples of data you’d want to store as environment variables include secret keys, database credentials, API credentials, server addresses, and access tokens.

Environment variables often change between development and production, and many contain sensitive information. Because of this, you need a robust way to parse, validate, and integrate environment variables in your code. This is a perfect use case of `pydantic-settings`, and that’s what you’ll explore in this section.

### Configuring Applications With BaseSettings

`pydantic-settings` is one of the most powerful ways to manage environment variables in Python, and it has been widely adopted and recommended by popular libraries like [FastAPI](https://fastapi.tiangolo.com/advanced/settings/#pydantic-settings). You can use `pydantic-settings` to create models, similar to `BaseModel`, that parse and validate environment variables.

The main class in `pydantic-settings` is `BaseSettings`, and it has all of the same functionalities as `BaseModel`. However, if you create a model that inherits from `BaseSettings`, the model initializer will try to read any fields not passed as keyword arguments from environment variables.

To see how this works, suppose your application connects to a database and another API service. Your database credentials and API key can change over time and often change depending on which environment you’re deploying in. To handle this, you can create the following `BaseSettings` model:

Python `settings_management.py`

```
from pydantic import HttpUrl, Field
from pydantic_settings import BaseSettings

class AppConfig(BaseSettings):
    database_host: HttpUrl
    database_user: str = Field(min_length=5)
    database_password: str = Field(min_length=10)
    api_key: str = Field(min_length=20)
```

In this script, you import the dependencies needed to create your `BaseSettings` model. Notice that you import `BaseSettings` from `pydantic_settings` with an underscore instead of a dash. You then define a model, `AppConfig`, that inherits from `BaseSettings` and stores fields about your database and API key. In this example, `database_host` has to be a valid HTTP URL, and the remaining fields have a minimum length constraint.

Next, open a terminal and add the following environment variables. If you’re on Linux, macOS, or Windows Bash, you can do this with the `export` command:

```
(venv) $ export DATABASE_HOST="http://somedatabaseprovider.us-east-2.com"
(venv) $ export DATABASE_USER="username"
(venv) $ export DATABASE_PASSWORD="asdfjl348ghl@9fhsl4"
(venv) $ export API_KEY="ajfsdla48fsdal49fj94jf93-f9dsal"
```

You can also [set environment variables in Windows PowerShell](https://realpython.com/python-coding-setup-windows/#setting-and-changing-environment-variables). Then you can open a new Python REPL and instantiate `AppConfig`:

```
>>> from settings_management import AppConfig

>>> AppConfig()
AppConfig(
    database_host=Url('http://somedatabaseprovider.us-east-2.com/'),
    database_user='username',
    database_password='asdfjl348ghl@9fhsl4',
    api_key='ajfsdla48fsdal49fj94jf93-f9dsal'
)
```

Notice how you don’t specify any field names when you instantiate `AppConfig`. Instead, your `BaseSettings` model reads fields from the environment variables you set. Also notice that you exported the environment variables in all capital letters, yet `AppConfig` parsed and stored them successfully. This is because `BaseSettings` is not case-sensitive when matching environment variables to field names.

Next, close your Python REPL and create invalid environment variables:

```
(venv) $ export DATABASE_HOST="somedatabaseprovider.us-east-2"
(venv) $ export DATABASE_USER="usee"
(venv) $ export DATABASE_PASSWORD="asdf"
(venv) $ export API_KEY="ajf"
```

Now open another Python REPL and reinstantiate `AppConfig`:

```
>>> from settings_management import AppConfig

>>> AppConfig()
Traceback (most recent call last):
pydantic_core._pydantic_core.ValidationError: 4 validation errors for
AppConfig
database_host
  Input should be a valid URL, relative URL without a base
  [type=url_parsing, input_value='somedatabaseprovider.us-east-2',
  input_type=str]
    For further information visit
    https://errors.pydantic.dev/2.6/v/url_parsing
database_user
  String should have at least 5 characters [type=string_too_short,
  input_value='usee', input_type=str]
    For further information visit
    https://errors.pydantic.dev/2.6/v/string_too_short
database_password
  String should have at least 10 characters [type=string_too_short,
  input_value='asdf', input_type=str]
    For further information visit
    https://errors.pydantic.dev/2.6/v/string_too_short
api_key
  String should have at least 20 characters [type=string_too_short,
  input_value='ajf', input_type=str]
    For further information visit
    https://errors.pydantic.dev/2.6/v/string_too_short
```

This time, when you try to instantiate `AppConfig`, `pydantic-settings` throws errors saying that the `database_host` is not a valid URL, and the remaining fields don’t meet the minimum length constraint.

While this was a simplified configuration example, you can leverage `BaseSettings` to parse and validate just about anything you need from your environment variables. Any validation you can do with `BaseModel` you can also do with `BaseSettings`, including custom validation with model and field validators.

Lastly, you’ll learn how to further customize the behavior of `BaseSettings` with `SettingsConfigDict`.

![](https://img.realpython.net/655d5b5272a07eaebc6a0885e3bc64ec)

[Remove ads](https://realpython.com/account/join/)

### Customizing Settings With SettingsConfigDict

In the previous example, you saw a barebones example of how to create a `BaseSettings` model that parses and validates environment variables. However, you might want to further customize the behavior of your `BaseSettings` model, and you can accomplish this with `SettingsConfigDict`.

Suppose you can’t manually export each of your environment variables, which is often the case, and you need to read them from a [`.env`](https://pypi.org/project/python-dotenv/) file. You’d want to make sure that `BaseSettings` is case-sensitive when parsing and that there are no additional environment variables in your `.env` file aside from the ones you specify in your model. Here’s how you’d do that with `SettingsConfigDict`:

Python `settings_management.py`

```
from pydantic import HttpUrl, Field
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppConfig(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="forbid",
    )

    database_host: HttpUrl
    database_user: str = Field(min_length=5)
    database_password: str = Field(min_length=10)
    api_key: str = Field(min_length=20)
```

This script is the same as in the previous example, except this time you’ve imported `SettingsConfigDict` and initialized it within `AppConfig`. Within your `SettingsConfigDict`, you specify that environment variables should be read from a `.env` file, case-sensitivity should be enforced, and that extra environment variables are forbidden in the `.env` file.

Next, create a file named `.env` in the same directory as `settings_management.py`, and populate it with the following environment variables:

```
database_host=http://somedatabaseprovider.us-east-2.com/
database_user=username
database_password=asdfjfffffl348ghl@9fhsl4
api_key=ajfsdla48fsdal49fj94jf93-f9dsal
```

Now, you can open a Python REPL and initialize your `AppConfig` model:

```
>>> from settings_management import AppConfig

>>> AppConfig()
AppConfig(
    database_host=Url('http://somedatabaseprovider.us-east-2.com/'),
    database_user='username',
    database_password='asdfjfffffl348ghl@9fhsl4',
    api_key='ajfsdla48fsdal49fj94jf93-f9dsal'
)
```

As you can see, `AppConfig` successfully parsed and validated the environment variables in your `.env` file.

Lastly, add some invalid variables to your `.env` file:

```
DATABASE_HOST=http://somedatabaseprovider.us-east-2.com/
database_user=username
database_password=asdfjfffffl348ghl@9fhsl4
api_key=ajfsdla48fsdal49fj94jf93-f9dsal
extra_var=shouldntbehere
```

Here, you’ve changed `database_host` to `DATABASE_HOST`, violating the case-sensitivity constraint, and you’ve added extra environment variables that shouldn’t be there. Here’s how your model responds when it tries to validate this:

```
>>> from settings_management import AppConfig

>>> AppConfig()
Traceback (most recent call last):
pydantic_core._pydantic_core.ValidationError: 3 validation errors for
AppConfig
database_host
  Field required [type=missing, input_value={'database_user':
  'userna..._var': 'shouldntbehere'}, input_type=dict]
    For further information visit
    https://errors.pydantic.dev/2.6/v/missing
DATABASE_HOST
  Extra inputs are not permitted [type=extra_forbidden,
  input_value='http://somedatabaseprovider.us-east-2.com/', input_type=str]
    For further information visit
    https://errors.pydantic.dev/2.6/v/extra_forbidden
extra_var
  Extra inputs are not permitted [type=extra_forbidden,
  input_value='shouldntbehere', input_type=str]
    For further information visit
    https://errors.pydantic.dev/2.6/v/extra_forbidden
```

You get a nice list of errors saying that `database_host` is missing and that you have extra environment variables in your `.env` file. Notice that because of the case-sensitivity constraint, your model thinks that `DATABASE_HOST` is an extra variable along with `extra_var`.

There’s a lot more you can do with `SettingsConfigDict` and `BaseSettings` more generally, but these examples should give you an idea of how you can use `pydantic-settings` to manage your environment variables for your own use case.

## Conclusion

Pydantic is an easy-to-use, fast, and widely-trusted data validation library in Python. You’ve gotten a broad overview of Pydantic, and now you have the knowledge and resources necessary to start using Pydantic in your own projects.

**In this tutorial, you’ve learned**:

- What **Pydantic** is and why it’s been so widely adopted
- How to **install** Pydantic
- How to parse, validate, and serialize data schemas with **`BaseModel`** and **validators**
- How to write custom validation logic for functions using **@validate\_call**
- How to parse and validate environment variables with **`pydantic-settings`**

Pydantic makes your code more robust and trustworthy, and it partially bridges the gap between Python’s ease of use and the built-in data validation of statically typed languages. For just about any data parsing, validation, and serialization use case you might have, Pydantic has an elegant solution.

> [!warning] Warning
> **Get Your Code:** [Click here to download the free sample code](https://realpython.com/bonus/pydantic-simplifying-data-validation-in-python/) that you’ll use to help you learn how Pydantic can help you simplify data validation in Python.

==**Take the Quiz:**== Test your knowledge with our interactive “Pydantic: Simplifying Data Validation in Python” quiz. You’ll receive a score upon completion to help you track your learning progress:

---

[![Pydantic: Simplifying Data Validation in Python](https://realpython.com/cdn-cgi/image/width=1920,format=auto/https://files.realpython.com/media/Pydantic-Showcase_Watermarked.423b9d2e27c6.jpg)](https://realpython.com/quizzes/python-pydantic/)

**Interactive Quiz**

[Pydantic: Simplifying Data Validation in Python](https://realpython.com/quizzes/python-pydantic/)

In this quiz, you'll test your understanding of Pydantic, a powerful data validation library for Python. You'll revisit concepts such as working with data schemas, writing custom validators, validating function arguments, and managing settings with pydantic-settings.

🐍 Python Tricks 💌

Get a short & sweet **Python Trick** delivered to your inbox every couple of days. No spam ever. Unsubscribe any time. Curated by the Real Python team.

![Python Tricks Dictionary Merge](https://realpython.com/static/pytrick-dict-merge.4201a0125a5e.png)

About **Harrison Hoffman**

Harrison is an avid Pythonista, Data Scientist, and Real Python contributor. He has a background in mathematics, machine learning, and software development. Harrison lives in Texas with his wife, identical twin daughters, and two dogs.

[» More about Harrison](https://realpython.com/team/hhoffman/)

---

*Each tutorial at Real Python is created by a team of developers so that it meets our high quality standards. The team members who worked on this tutorial are:*[Philipp](https://realpython.com/team/pacsany/)

Master Real-World Python Skills With Unlimited Access to Real Python

![Locked learning resources](https://realpython.com/static/videos/lesson-locked.f5105cfd26db.svg)

**Join us and get access to thousands of tutorials, hands-on video courses, and a community of expert Pythonistas:**

Master Real-World Python Skills  
With Unlimited Access to Real Python

![Locked learning resources](https://realpython.com/static/videos/lesson-locked.f5105cfd26db.svg)

**Join us and get access to thousands of tutorials, hands-on video courses, and a community of expert Pythonistas:**

Keep Learning

Related Topics: [intermediate](https://realpython.com/tutorials/intermediate/) [best-practices](https://realpython.com/tutorials/best-practices/) [data-structures](https://realpython.com/tutorials/data-structures/)

Related Courses:

- [Using Pydantic to Simplify Python Data Validation](https://realpython.com/courses/pydantic-simplify-data-validation/?utm_source=realpython&utm_medium=web&utm_campaign=related-course&utm_content=python-pydantic)

Related Tutorials:

- [Build Enumerations of Constants With Python's Enum](https://realpython.com/python-enum/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-pydantic)
- [Python's asyncio: A Hands-On Walkthrough](https://realpython.com/async-io-python/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-pydantic)
- [Data Classes in Python (Guide)](https://realpython.com/python-data-classes/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-pydantic)
- [pytest Tutorial: Effective Python Testing](https://realpython.com/pytest-python-testing/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-pydantic)
- [Managing Python Projects With uv: An All-in-One Solution](https://realpython.com/python-uv/?utm_source=realpython&utm_medium=web&utm_campaign=related-post&utm_content=python-pydantic)