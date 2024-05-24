# Local Question Server

*Hint: This document can be best read either on Gitlab or using the VS Code Markdown Preview.*

The python code given in this folder implements a simple server application.
The server provides a REST API to get the quiz questions including answers and the total number of available questions.

## Running the server

First you need to install the requirements of the script into your virtual python environment.
Activate your environment and run the following command from the project's root, i.e., `09-modularbeit2-...` folder:

```bash
pip install -r question_server/requirements.txt
```

Then open a terminal in the project root and run the python script using

```bash
python question_server/question_server.py
```

**Note:** You must run the script from the project root, i.e. the folder `09-modularbeit2-...` since the script is looking for the file with the questions in the folder `assets/questions.json`.

Keep the application running as long as you are working on your quiz king application.

## API Key

In order to access the server, an API key is required.
The valid dummy API key's value is 

```text
abcd1234
```

Requests with an invalid API key will result in an error code 403 including the response description "Forbidden: Invalid API Key".

## Getting the total number of questions

<code>GET</code> <code><b>http://127.0.0.1:5000/{api_key}/question_count</b></code> 

##### Parameters

> | name   |  type      | data type      | description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `api_key` |  required  | string         | A valid API key                  |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`        | {"count":85}         |
> | `403`         | `application/json`                | `{"code":"403","message":"Forbidden: Invalid API Key"}`                            |

##### Example

> http://127.0.0.1:5000/abcd1234/question_count

returns 

```json
{
  "count": 85
}
```

## Getting a question

<code>GET</code> <code><b>http://127.0.0.1:5000/{api_key}/question?index={question_number}</b></code> 

##### Parameters

> | name   |  type      | data type      | description                                          |
> |--------|------------|----------------|------------------------------------------------------|
> | `api_key` |  required  | string         | A valid API key                  |

##### Responses

> | http code     | content-type                      | response                                                            |
> |---------------|-----------------------------------|---------------------------------------------------------------------|
> | `200`         | `application/json`        | `{"choices":["Elephant","Blue Whale","Giraffe","Great White Shark"],"correct":"Blue Whale","question":"What is the largest mammal in the world?"}`         |
> | `404`         | `application/json`        | `{"code":"404","message":"Not Found: Question index out of range"}` |
> | `403`         | `application/json`                | `{"code":"403","message":"Forbidden: Invalid API Key"}`                            |

##### Example URLs

Correct Question:

> http://127.0.0.1:5000/abcd1234/question?index=10

returns the 11th question (counting starts at zero) with the following content:

```json
{
  "choices": [
    "Elephant",
    "Blue Whale",
    "Giraffe",
    "Great White Shark"
  ],
  "correct": "Blue Whale",
  "question": "What is the largest mammal in the world?"
}
```
