FROM python:3.4-alpine

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app
# Install any needed packages specified in requirements.txt
COPY ./requirements.txt /app/.
RUN pip install --trusted-host pypi.python.org -r requirements.txt
#RUN pip install -r requirements.txt

# Define environment variable
ENV NAME World

# Run app.py when the container launches
# In Docker Tool (win7) there is a permissions glitch
# Fix: stackoverflow.com/a/55359108/7409029
RUN chmod 644 app.py
CMD ["python", "app.py"]
