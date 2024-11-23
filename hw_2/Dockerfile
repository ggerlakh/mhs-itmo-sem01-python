FROM ubuntu:latest
ENV DEBIAN_FRONTEND=noninteractive
RUN apt update && \
    apt install -y software-properties-common && \
    add-apt-repository -y ppa:deadsnakes/ppa && \
    apt install python3.12 python3-pip texlive-latex-base -y && \
    pip install --break-system-packages -i https://test.pypi.org/simple/ latex-gen-ggerlakh