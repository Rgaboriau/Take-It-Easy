# Projet “Take it easy”

Take it easy is a board game. To keep is simple, you have to position a random chosen tile on the board. To mark points the line has to be complete (only the same number). As the end, the point are compute this way;
- Line not complete = 0
- Line complete = number of tile on the line time the number of the line

![Alt text](https://github.com/Rgaboriau/Take-It-Easy/blob/main/Data/photos/take-it-easy-ravensburger-ipad-tablette-enfant-application-la-souris-grise-1%20-%20copie.jpeg?raw=true "View")


Objective : create an application that immediately count the point from photo or with the camera (like a QR code)

4 steps :

- Fill in the results manually in a matrix, then it computes the score : NO AI
- With a picture and an external OCR, the software reconnizes the digit then computes the score : NO AI
- With a picture and an internal OCR, the software reconnizes the digit then computes the score : AI
- With a picture and deep learning algorithm, the software gives the score : AI
