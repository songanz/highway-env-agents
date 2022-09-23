### Base image: official nvidia docker with cuda and cudnn
ARG BASE_IMAGE=nvidia/cuda:11.0.3-cudnn8-devel-ubuntu20.04

FROM $BASE_IMAGE AS builder
LABEL maintainer="Songan Zhang <szhan117@ford.com>"

ARG DEBIAN_FRONTEND=noninteractive

# RUN rm /etc/apt/sources.list.d/cuda.list
# RUN rm /etc/apt/sources.list.d/nvidia-ml.list
RUN apt-get update \
      && apt-get install --no-install-recommends --no-install-suggests -y gnupg2 ca-certificates python3-tk ffmpeg\
            git build-essential dirmngr nano libopenmpi-dev gcc swig dialog python-opengl python3-pip python3-dev\
      && rm -rf /var/lib/apt/lists/*

RUN echo "export PATH="/root/.local/bin:$PATH"" >> ~/.bashrc

#
# Install Git LFS
#
RUN apt-get update && \
    apt-get install -y curl && \
    curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | bash && \
    apt-get install -y git git-lfs && \
    git lfs install && \
    rm -rf /var/lib/apt/lists/* && \
    apt-get -y autoclean && \
    apt-get -y clean

# nvidia
ENV NVIDIA_VISIBLE_DEVICES \
    ${NVIDIA_VISIBLE_DEVICES:-all}
ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}graphics

### Install Pytorch 1.7.0
RUN pip3 install --no-warn-script-location torch==1.7.0+cu110 torchvision==0.8.1+cu110 torchaudio==0.7.0 -f https://download.pytorch.org/whl/torch_stable.html

### Install Openai gym
# Install Python packages - Step 1
# including whatever newest tensorflow
COPY requirements_1.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements_1.txt
# Install Python packages - Step 2 (OpenAI Gym)
COPY requirements_2.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements_2.txt

### Install other packages
RUN pip3 install --no-warn-script-location numpy scipy matplotlib ipython jupyter pandas sympy nose

### Final cleanup
RUN apt-get clean
RUN rm -rf /var/lib/apt/lists/*

### for display
RUN echo "export QT_QPA_PLATFORM=xcb" >> ~/.bashrc

SHELL ["/bin/bash", "-c"]
RUN source ~/.bashrc
