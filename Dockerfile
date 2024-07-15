# Official python image
FROM python:3.9-slim-buster

#Working directory in the container
WORKDIR /app

#copy requirements file
COPY requirements.txt .

#install required python packages
RUN pip3 install --no-cache-dir -r requirements.txt

#Copy application code
COPY . .

#Environment variables for the flask app
ENV FLASK_RUN_HOST=0.0.0.0

# Expose the port on which the Flask app will run
EXPOSE 5000

# Start the Flask app when the container is run
CMD ["flask", "run"]