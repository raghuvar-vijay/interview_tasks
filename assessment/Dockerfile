FROM ubuntu:16.04
#Installing dependencies
RUN apt-get update && apt-get upgrade -y 

RUN apt-get install -y \
    build-essential \
    curl

RUN apt-get update

RUN apt-get install python3.9 -y

RUN curl https://sh.rustup.rs -sSf | bash -s -- -y

ENV PATH="/root/.cargo/bin:${PATH}"


RUN rustup component add rustfmt

RUN apt-get update && apt-get upgrade -y 

RUN apt install libclang-3.9-dev -y


RUN cargo install cargo-contract --vers ^0.12 --force --locked 

RUN curl https://getsubstrate.io -sSf | bash -s -- --fast-y

RUN rustup component add rust-src --toolchain nightly

RUN rustup target add wasm32-unknown-unknown --toolchain nightly

RUN mkdir /project

COPY gs /project/gs_1

RUN cargo install canvas-node --git https://github.com/paritytech/canvas-node.git --tag v0.1.8 --force --locked

RUN apt-get update

RUN apt-get install python3-pip -y

RUN apt-get update && apt-get upgrade

RUN apt-get update && apt-get upgrade

RUN git clone https://github.com/polkascan/py-substrate-interface.git 

WORKDIR /project/gs_1


CMD ["ls"]
