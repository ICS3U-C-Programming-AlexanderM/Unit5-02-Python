#!/usr/bin/env python3
# Created By: Alex M
# Date: nov 27, 2023
# 



def calculate_area (base, height):
        area = base * height / 2

        print(f" Area of the triangle is {area} ")

def main():
        base_from_user = int(input("Enter the height in cm "))
        height_from_user = int(input("Enter the base in cm "))
        print("")
        

        calculate_area (base_from_user, height_from_user)




if __name__ == "__main__":
        main()