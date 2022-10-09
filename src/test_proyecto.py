from proyecto import lee_datos

def main():
    tv_series = lee_datos("./data/TV_SHOWS_0.csv")

    print(tv_series[0]) 
    print(tv_series[1])
    print(tv_series[2]) 
    
    print(tv_series[-1]) 
    print(tv_series[-2])
    print(tv_series[-3])

if __name__ == "__main__":
    main()