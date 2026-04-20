def Display(A,B,C,D):
    print(A,B,C,D)


def main():
    #Display(10,20)   not allowed
    #Display(10,20,30,40,50) not allowed

    Display(10,20,30,40)     #allowed

if __name__ == "__main__":
    main()