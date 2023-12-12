# ctenarsky-denik
# ==============

Web scraper, který najde veřejně dostupné rozbory maturitní četby a přepíše je podle formátu pomocí OpenAI.

## Instalace
- poté, co si naklonujete repozitář, spusťte `pip install -r requirements.txt`
- když spustíte soubor `main.py`, vytvoří se vám .env soubor, do kterého je třeba doplinit API klíč na server, který vám poskytne OpenAI klíč.
- rozbory se vám uloží do složky `output`

## Použití
- spusťte soubor `main.py`. všechny parametry fungují jako filter, takže například: "python3 main.py karel" najde pouze rozbory knih, které mají v názvu jebo jménu autora "karel". filtrů může být libovolný počet.

legal:
používaní ai blablabla plagiát vole blablabla
to ai sucks ass, stejně to budete muset upravit. jestli to někomu odevzdáte takhle a zjistí, že je to ai, neni to muj problém.