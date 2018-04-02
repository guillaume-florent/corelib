FROM continuumio/miniconda3:4.4.10

MAINTAINER Guillaume Florent <florentsailing@gmail.com>

RUN conda update -n base conda
RUN conda install -y numpy scipy matplotlib pytest

# corelib
WORKDIR /opt
ADD https://api.github.com/repos/guillaume-florent/corelib/git/refs/heads/master version.json
RUN git clone --depth=1 https://github.com/guillaume-florent/corelib
RUN cp -r /opt/corelib/corelib /opt/conda/lib/python3.6/site-packages