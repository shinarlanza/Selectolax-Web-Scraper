import httpx
from selectolax.parser import HTMLParser
import pandas as pd
import tabulate


def get_data(url, book, price):

    response = httpx.get(url, headers={"User-Agent": "Mozilla/5.0 (...)"})

    parser = HTMLParser(response.text)

    book_name = parser.css_first(book).text().strip()
    item_number = parser.css_first(price).text().strip()

    return {
        "Book": book_name,
        "Price": item_number
    }


def main():
    data = []

    
    data.append(get_data("https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html", "h1","p.price_color"))
    data.append(get_data("https://books.toscrape.com/catalogue/tipping-the-velvet_999/index.html", "h1","p.price_color"))
    data.append(get_data("https://books.toscrape.com/catalogue/soumission_998/index.html", "h1","p.price_color"))
    data.append(get_data("https://books.toscrape.com/catalogue/sharp-objects_997/index.html", "h1","p.price_color"))
    data.append(get_data("https://books.toscrape.com/catalogue/sapiens-a-brief-history-of-humankind_996/index.html", "h1","p.price_color"))
    data.append(get_data("https://books.toscrape.com/catalogue/the-requiem-red_995/index.html", "h1","p.price_color"))
    data.append(get_data("https://books.toscrape.com/catalogue/the-dirty-little-secrets-of-getting-your-dream-job_994/index.html", "h1","p.price_color"))
    data.append(get_data("https://books.toscrape.com/catalogue/the-coming-woman-a-novel-based-on-the-life-of-the-infamous-feminist-victoria-woodhull_993/index.html", "h1","p.price_color"))
    data.append(get_data("https://books.toscrape.com/catalogue/the-boys-in-the-boat-nine-americans-and-their-epic-quest-for-gold-at-the-1936-berlin-olympics_992/index.html", "h1","p.price_color"))
    data.append(get_data("https://books.toscrape.com/catalogue/the-black-maria_991/index.html", "h1","p.price_color"))
    
    
    print(data)
    print(tabulate.tabulate(data))


    df = pd.DataFrame(data)
    df.to_excel("Books.xlsx", index=False)


if __name__ == "__main__":
    main()
