FROM mcr.microsoft.com/devcontainers/python:3.12


# Copy the System V init script for code-server
COPY code-server.sh /etc/init.d/code-server
# Make the init script executable
RUN chmod +x /etc/init.d/code-server

# Install code-server
RUN curl -fsSL https://code-server.dev/install.sh | sh


# Install Pycharm
# Download the file
RUN wget https://download.jetbrains.com/python/pycharm-professional-2024.3.5-aarch64.tar.gz -O /tmp/pycharm-professional.tar.gz
# Create the /opt/pycharm directory
RUN mkdir -p /opt/pycharm
# Extract the downloaded file into the /opt/pycharm directory
RUN tar -xzf /tmp/pycharm-professional.tar.gz -C /opt/pycharm --strip-components=1
# Clean up the downloaded file
RUN rm /tmp/pycharm-professional.tar.gz