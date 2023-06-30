# scalable-automated-tests-service

This project is a distributed test automation system developed in Python. It allows you to execute tests in a scalable and distributed manner. The system includes an API that can be consumed by HTTP requests, a queue for task management, and multiple test execution agents to parallelize test execution.

## Features

- Execute tests in a distributed and scalable manner.
- API for managing test runs, configurations, and retrieving test results.
- Test execution agents that listen to a queue for task distribution.
- Parallel test execution to improve efficiency.
- Centralized storage of test results.

## Installation

To set up the project, follow these steps:

1. Clone the repository:

   ```shell
   git clone https://github.com/your-username/distributed-test-automation.git
   cd distributed-test-automation
1. Install the dependencies:

   ```shell
   pip install -r requirements.txt
