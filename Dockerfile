# Use the official Python 3.9 slim image as the base
FROM python:3.9-slim

# Set the working directory inside the container to /app
WORKDIR /app

# Copy all files from the current directory on the host to /app in the container
COPY . /app

# Update the package list and install necessary dependencies for Tkinter and X11 support,
# which are needed to run graphical applications
RUN apt-get update && apt-get install -y \
    python3-tk \        # Install Python Tkinter for GUI support
    libtk8.6 \          # Install Tk libraries
    libx11-dev \        # Install X11 libraries for graphical interface
    libxrender-dev \    # Install XRender libraries
    libxext-dev \       # Install X Extensions libraries
    && rm -rf /var/lib/apt/lists/*   # Clean up to reduce the image size

# Install Python dependencies listed in the requirements.txt file
RUN pip install --no-cache-dir -r requirements.txt

# Set the DISPLAY environment variable to :0 for X11 forwarding (used to display GUI applications)
ENV DISPLAY=:0

# Set the default command to run the Python application (todo-app.py)
CMD ["python", "todo-app.py"]
