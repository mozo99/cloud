FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed dependencies specified in requirements.txt
RUN pip install nltk

# Download NLTK stopwords
RUN python -m nltk.downloader stopwords

# Run the Python script when the container launches
CMD ["python3", "format.py"]
