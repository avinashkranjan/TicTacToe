FROM python:3.10.0b4
WORKDIR /TicTacToe
COPY . .
RUN apt-get -y update
RUN pip3 install -r requirements.txt
CMD ["python","TicTacToe-CLI.py"]
