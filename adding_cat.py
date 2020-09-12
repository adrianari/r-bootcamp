import pandas as pd
import csv

df = pd.read_csv("2019_verkehrszaehlungen_werte_fussgaenger_velo_bereinigt.csv", sep =";")

#setting the categories of the counting stations
df.loc[df['FK_ZAEHLER'] == "U15G3104443", "KATEGORIE"] = "fussgaenger"
df.loc[df['FK_ZAEHLER'] == "U15G3104446", "KATEGORIE"] = "fussgaenger"
df.loc[df['FK_ZAEHLER'] == "ECO09113499", "KATEGORIE"] = "velo"
df.loc[df['FK_ZAEHLER'] == "ECO07091438", "KATEGORIE"] = "velo"

#copying the values from all columns velo_ and fuss_ into one column per in and out
df.loc[df['KATEGORIE'] == "velo", "IN"] = df["VELO_IN"]
df.loc[df['KATEGORIE'] == "fussgaenger", "IN"] = df["FUSS_IN"]
df.loc[df['KATEGORIE'] == "velo", "OUT"] = df["VELO_OUT"]
df.loc[df['KATEGORIE'] == "fussgaenger", "OUT"] = df["FUSS_OUT"]

#unidirection (movement regardless of the direction one goes)
df["UNIDIR"] = df["IN"]+df["OUT"]

df.to_csv("verkehrszaehlung_after.csv", sep=";", index = False, header = True, encoding = "UTF-8")