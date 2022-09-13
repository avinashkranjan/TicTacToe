FROM python:3.11.0rc2
WORKDIR /TicTacToe
COPY . .
RUN apt-get -y update
RUN pip3 install -r requirements.txt
CMD ["python","TicTacToe-CLI.py"]
