import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams["font.sans-serif"] = ["DejaVu Sans"]
plt.rcParams["font.family"] = "sans-serif"
plt.style.use("seaborn-v0_8-whitegrid")
df = pd.read_csv("GLOBAL_FIREPOWER.CSV")
print(df.head())
print(df.columns)
print(df.info())
print(df.describe())
print(df.isnull().sum())

cols_to_convert = ["Coastline (km)", "Waterways (km)"]

for col in cols_to_convert:
    df[col] = pd.to_numeric(df[col], errors="coerce")
    df[col] = df[col].fillna(0)


df["Defense Budget (Billion USD)"] = df["Defense Budget"] / 1000
df["Total Military Personnel (Million People)"] = (
    df["Total Military Personnel"] / 1000000
)
df["PPP (Trillion USD)"] = df["Purchasing Power Parity"] / 1000000

print("Veri temizliği ve yeni metrik oluşturma tamamlandı.")

# --- 2. Görselleştirme ve Analizler ---
df_budget = (
    df.sort_values(by="Defense Budget (Billion USD)", ascending=False).head(10).copy()
)
df_personnel = (
    df.sort_values(by="Total Military Personnel (Million People)", ascending=False)
    .head(10)
    .copy()
)

plt.figure(figsize=(14, 7))

# Plot 1: Top 10 Savunma Bütçesi
plt.subplot(1, 2, 1)
sns.barplot(
    data=df_budget, x="Country", y="Defense Budget (Billion USD)", palette="viridis"
)
plt.title("Top 10 Savunma Bütçesi", font="DejaVu Sans", fontsize=16)
plt.xticks(rotation=45)
plt.ylabel("Savunma Bütçesi (Milyar USD)")
plt.xlabel("Ülke")
# plt.show()

# Plot 2: Top 10 Toplam Askeri Personel
plt.subplot(1, 2, 2)
sns.barplot(
    data=df_personnel,
    x="Country",
    y="Total Military Personnel (Million People)",
    palette="mako",
)
plt.title("Top 10 Toplam Askeri Personel", font="DejaVu Sans", fontsize=16)
plt.xticks(rotation=45)
plt.ylabel("Toplam Askeri Personel (Milyon Kişi)")
plt.xlabel("Ülke")
plt.savefig("military_analysis.png", bbox_inches="tight")
# plt.show()
plt.suptitle("Temel Askeri Güç Göstergeleri")
plt.tight_layout()
plt.savefig("military_analysis.png", bbox_inches="tight")

# Korelasyon Heatmap (Askeri Varlıklar)
correlation_cols_military = [
    "Defense Budget (Billion USD)",
    "Total Military Personnel (Million People)",
    "Total Aircraft Strength",
    "Combat Tanks",
    "Total Naval Assets",
]
correlation_matrix_military = df[correlation_cols_military].corr(method="pearson")
plt.figure(figsize=(8, 6))

sns.heatmap(
    correlation_matrix_military,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    linecolor="black",
    cbar_kws={"label": "Korelasyon Katsayısı"},
)
plt.title("Seçili Askeri Varlıklar Arası Korelasyon", fontsize=14)
plt.xticks(rotation=45, ha="right")
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()


# Askeri Sıralama (Rank) vs. Ekonomik Güç (PPP) - Scatter Plot
plt.figure(figsize=(10, 6))
sns.regplot(
    x="PPP (Trillion USD)",
    y="Rank",
    data=df,
    scatter_kws={"alpha": 0.6, "color": "#0070c0"},
    line_kws={"color": "#c00000", "lw": 2},
)
plt.title(
    "Askeri Sıralama (Rank) ile Satın Alma Gücü Paritesi (PPP) İlişkisi", fontsize=14
)
plt.xlabel("Satın Alma Gücü Paritesi (Trilyon USD)", fontsize=12)
plt.ylabel("Askeri Sıralama (Düşük = Daha Güçlü)", fontsize=12)
plt.grid(True)
plt.show()
