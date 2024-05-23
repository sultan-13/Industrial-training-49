"""
Author: Kalim Amzad Chy
Email: kalim.amzad.chy@gmail.com
Version: 1.0

This module demonstrates the usage of the `requests` library in Python for making HTTP requests.
It covers various real-world examples including GET and POST requests, handling response data,
and working with headers and parameters. This script is designed as an educational tool for
understanding web scraping and API interaction using Python.
"""

import requests

def get_example():
    """
    Demonstrates a simple GET request using the `requests` library.
    Fetches data from a public API and prints the titles of all posts.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    response = requests.get(url)

    # My Assignment modificaion

    try:
        if response.status_code == 200:
            print("GET request successful!")
            posts = response.json()


            for itr in range(min(70, len(posts))):
                print(f"Title {itr + 1} - {posts[itr]['title']}")
        else:
            print("Failed to retrieve data")

    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unknown Error: {e}")


def post_example():
    """
    Demonstrates a simple POST request using the `requests` library.
    Sends JSON data to a public API and prints the response.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 10
    }
    
    try:
        response = requests.post(url, json=data)
        response.raise_for_status()  
        
        print("POST request successful!")
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unknown Error: {e}")


def main():
    """
    Main function to execute the examples.
    """
    print("Executing GET example...")
    get_example()
    # print("\nExecuting POST example...")
    # post_example()

if __name__ == "__main__":
    # main()
    pass



# Assignments
# 1. Modify the GET Example: Change the get_example function to fetch a list of posts instead of just one. Analyze the JSON structure and print out the titles of all posts.
    
# 2. Error Handling: Add error handling to both functions to manage exceptions like connection errors or timeouts.
     # both Done above

# Advanced requests
"""
This module discuss advanced features like custom headers, user agents, and error handling.


Custom Headers and User Agents: These are used to provide additional information to the server about the request being made. For example, the 
`User-Agent` header can be used to simulate requests from different browsers.

Error Handling: The `try-except` blocks are used to catch and handle different types of exceptions that might occur during the request, such as network problems or invalid responses.
"""

import requests

def get_with_headers():
    """
    Demonstrates a GET request with custom headers and a user agent.
    Fetches data from a public API and prints the JSON response.
    """
    url = 'https://jsonplaceholder.typicode.com/posts/1'
    headers = {
        'User-Agent': 'My User Agent 1.0',
        'Accept': 'application/json'
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        print("GET request with custom headers successful!")
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unknown Error: {e}")

def post_with_authentication():
    """
    Demonstrates a POST request using basic authentication.
    Sends JSON data to a public API and prints the response.
    """
    url = 'https://jsonplaceholder.typicode.com/posts'
    data = {
        'title': 'foo',
        'body': 'bar',
        'userId': 1
    }
    headers = {
        'User-Agent': 'My User Agent 1.0'
    }
    auth = ('root', 'root')  
    
    try:
        response = requests.post(url, json=data, headers=headers, auth=auth)
        response.raise_for_status()
        print("POST request with authentication successful!")
        print(response.json())
    except requests.exceptions.HTTPError as errh:
        print(f"HTTP Error: {errh}")
    except requests.exceptions.ConnectionError as errc:
        print(f"Connection Error: {errc}")
    except requests.exceptions.Timeout as errt:
        print(f"Timeout Error: {errt}")
    except requests.exceptions.RequestException as err:
        print(f"Error: {err}")
    except Exception as e:
        print(f"Unknown Error: {e}")

def main():
    """
    Main function to execute advanced examples.
    """
    print("Executing GET example...")
    get_example()
    print("\nExecuting POST example...")
    post_example()

    # Advanced usages
    # print("Executing GET request with custom headers...")
    # get_with_headers()
    # print("\nExecuting POST request with authentication...")
    # post_with_authentication()

if __name__ == "__main__":
    main()

