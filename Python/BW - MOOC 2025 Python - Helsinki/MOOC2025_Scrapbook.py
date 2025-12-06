# https://programming-25.mooc.fi/part-3
# WIP | Need to get the columns to alternate between result output. 

def chessboard(length):
    row = length
    column = length
    row_results = ""
    index = 0
    column_index = 0

    while column_index < length: 
               
        while index < length:
            
            if index % 2 == 0:
                row_results += "1"
                index += 1
            else:
                row_results += "0"
                index += 1
        
        print(f"{row_results}")
        column_index += 1

            
if __name__ == "__main__":
    chessboard(6)
