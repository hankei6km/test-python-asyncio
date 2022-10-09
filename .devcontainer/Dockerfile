FROM ghcr.io/hankei6km/h6-dev-containers:2022-10-08-main-python


ARG USERNAME=vscode

# Install iotop
USER root
RUN apt-get update \
  && apt-get -y install --no-install-recommends iotop \
  # Clean up
  && apt-get autoremove -y \
  && apt-get clean -y \
  && rm -rf /var/lib/apt/lists/*

WORKDIR "/home/${USERNAME}"
USER ${USERNAME}

# Make temp dir in home
RUN mkdir -p "/home/${USERNAME}/tmp"