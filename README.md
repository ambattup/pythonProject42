

A. To request data from the microservice you can go about that by sending a POST request to an URL using "requests.post". The URL should be to the endpoint which is the function named generate_password and in my case the URL is 'http://127.0.0.1:5000/generate_password'. An example of a line of code that requests data from the microservice is: response =
requests.post(url, headers=headers, data=json.dumps(data)).

B. The line of code from part 1 will send a POST request to the URL and store the response from that URL in the response variable. The data held in the response variable will be the randomly generated password that was created with the specified length, number of uppercase letters, and number of numbers.

![image](https://github.com/ambattup/pythonProject42/assets/122513977/a2418c0a-5a43-4a63-931d-40aca33d9fb4)



