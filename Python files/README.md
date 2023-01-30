To use the trained model, run the file [main.py](https://github.com/cagutierrezgu/My_Portfolio/blob/bcf56de444780898cbdbc2dfdad1a190e5d1f6c5/Stars%20classification%20and%20prediction/Python%20files/main.py), and in the terminal window of your machine, write:

curl -d "{"Data":[['Temperature','Luminosity','Radio','Absolute magnitude']]}" -H "Content-Type: application/json" -X POST http://127.0.0.1:5000/run
