FROM python:3.7
WORKDIR /TicTacToe
COPY . .
RUN apt-get -y update
RUN pip3 install -r requirements.txt
CMD ["python","./Minimax.py"]
