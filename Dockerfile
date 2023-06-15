FROM python:3.12.0b2
WORKDIR /TicTacToe
COPY . .
RUN apt-get -y update
RUN pip3 install -r requirements.txt
CMD ["python","TicTacToe-CLI.py"]
