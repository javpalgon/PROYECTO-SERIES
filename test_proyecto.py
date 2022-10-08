from proyecto import lee_datos

def main():
    TV_SERIES = lee_datos("./data/tv_shows.csv")
    print(TV_SERIES)

    if __name__ == "__main__":
        main()