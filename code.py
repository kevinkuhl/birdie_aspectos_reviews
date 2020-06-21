import pandas as pd

column_names = ["retailer", "category_of_product", "client_path", "brand", "url", "SKU", "retailer1", "title", "attributes_simple", "empty1", "attributes_complete", "date1", "code1", "review_title", "review", "stars", "review_date", "review_year", "code2", "code3", "code4", "date3", "country", "boolean", "SKUs"]

df = pd.read_csv("tech_test.tsv", header=0, names=column_names)


df.drop(['category_of_product', 'client_path', "url", "retailer1", "attributes_simple", "empty1", "date1", "code1", "review_date", "review_year", "code2", "code3", "code4", "date3", "boolean"], axis=1, inplace=True)

df["review_title"] = df["review_title"].str.lower()
df["review"] = df["review"].str.lower()


print(df.head(100))