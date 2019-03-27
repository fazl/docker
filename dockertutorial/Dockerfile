# To create the docker image use this command inside the
# docker toolbox:
#   docker build --tag=friendlyhello .
# TIP: if the downloading of parts hangs, just 
# hit CTRL+C and rerun the build command, it 
# seems to carry on where it left off 
# For me the third or fourth attempt completed.
# 
# Once the build completes you can see the results:
#  $ docker image ls
#  REPOSITORY    TAG       IMAGE ID       CREATED       SIZE
#  friendlyhello latest    a529933179e8   9 minutes ago 131MB
#  ubuntu        latest    94e814e2efa8   2 weeks ago   88.9MB
#  python        2.7-slim  8559620b5b0d   3 weeks ago   120MB
#  hello-world   latest    fce289e99eb9   2 months ago  1.84kB

# Use an official Python runtime as a parent image
FROM python:2.7-slim

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
