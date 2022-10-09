from proyecto import lee_datos

def main():
    tv_series = lee_datos("./data/tv_shows.csv")

    print(len(tv_series))
    print(tv_series)

if __name__ == "__main__":
    main()